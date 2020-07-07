
import pygame, sys, random
import cv2
from copy import deepcopy
from pygame.locals import *

img_path=  "1.jpg"

# 一些常量
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
BACKGROUNDCOLOR = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 40

VHNUMS = 3
CELLNUMS = VHNUMS * VHNUMS
MAXRANDTIME = 100

img = cv2.imread(img_path)
b,g,r = cv2.split(img)
img = cv2.merge([r, g, b])


# 退出
def terminate():
    pygame.quit()
    sys.exit()

# 随机生成游戏盘面
def newGameBoard():
    board = []
    for i in range(CELLNUMS):
        board.append(i)
    blackCell = CELLNUMS - 1
    board[blackCell] = -1
    success_board = deepcopy(board)

    for i in range(MAXRANDTIME):
        direction = random.randint(0, 3)
        if (direction == 0):
            blackCell = moveLeft(board, blackCell)
        elif (direction == 1):
            blackCell = moveRight(board, blackCell)
        elif (direction == 2):
            blackCell = moveUp(board, blackCell)
        elif (direction == 3):
            blackCell = moveDown(board, blackCell)
    return success_board,board, blackCell


# 若空白图像块不在最左边，则将空白块左边的块移动到空白块位置
def moveRight(board, blackCell):
    if blackCell % VHNUMS == 0:
        return blackCell
    board[blackCell - 1], board[blackCell] = board[blackCell], board[blackCell - 1]
    return blackCell - 1


# 若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
def moveLeft(board, blackCell):
    if blackCell % VHNUMS == VHNUMS - 1:
        return blackCell
    board[blackCell + 1], board[blackCell] = board[blackCell], board[blackCell + 1]
    return blackCell + 1


# 若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
def moveDown(board, blackCell):
    if blackCell < VHNUMS:
        return blackCell
    board[blackCell - VHNUMS], board[blackCell] = board[blackCell], board[blackCell - VHNUMS]
    return blackCell - VHNUMS


# 若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
def moveUp(board, blackCell):
    if blackCell >= CELLNUMS - VHNUMS:
        return blackCell
    board[blackCell + VHNUMS], board[blackCell] = board[blackCell], board[blackCell + VHNUMS]
    return blackCell + VHNUMS


# 是否完成
def isFinished(board, success_board):
    if board == success_board:
        return True
    return False


def commodity(windowSurface,text,fx,fy,color=(0,0,255)):
    # 获取系统字体并定义字体大小
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 30)
    # 定义字体颜色及文本内容
    text_surface = font.render(text, True, color)
    # 获取字体所在的矩形区域
    textRectObj = text_surface.get_rect()
    # 设置矩形区域的中心
    textRectObj.center = (fx,fy)
    # 绑定主窗口 显示文本
    windowSurface.blit(text_surface, textRectObj)


def start():
    # 步数计算
    step = 0
    success_text=  ""
    # 初始化
    pygame.init()
    mainClock = pygame.time.Clock()

    # 加载图片
    gameImage = pygame.image.load(img_path)
    gameRect = gameImage.get_rect()

    # 设置窗口
    windowSurface = pygame.display.set_mode((gameRect.width+300, gameRect.height))
    pygame.display.set_caption('拼图')

    cellWidth = int(gameRect.width / VHNUMS)
    cellHeight = int(gameRect.height / VHNUMS)

    finish = False

    success_board,gameBoard, blackCell = newGameBoard()


    # 游戏主循环
    while True:
        # 获取键盘输入
        for event in pygame.event.get():

            # 如果是退出按钮 ESC  则退出游戏
            if event.type == QUIT:
                terminate()
            # 如果游戏结束 则继续
            if finish:
                continue

            # 捕获键盘按键
            if event.type == KEYDOWN:
                # 增加步长
                step+=1

                # a键 左移
                if event.key == K_LEFT or event.key == ord('a'):
                    blackCell = moveLeft(gameBoard, blackCell)
                # d 键 右移
                if event.key == K_RIGHT or event.key == ord('d'):
                    blackCell = moveRight(gameBoard, blackCell)
                # w键 上移
                if event.key == K_UP or event.key == ord('w'):
                    blackCell = moveUp(gameBoard, blackCell)
                # s键 下移
                if event.key == K_DOWN or event.key == ord('s'):
                    blackCell = moveDown(gameBoard, blackCell)

            # 鼠标点击
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                step+=1
                x, y = pygame.mouse.get_pos()


                if gameRect.width+100 -40<=x<=gameRect.width + 100+40 and gameRect.height/3-20<y<gameRect.height /3+20:
                    print("重新开始")
                    start()

                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * VHNUMS
                if (index == blackCell - 1 or index == blackCell + 1 or index == blackCell - VHNUMS or index == blackCell + VHNUMS):
                    gameBoard[blackCell], gameBoard[index] = gameBoard[index], gameBoard[blackCell]
                    blackCell = index

            if (isFinished(gameBoard, success_board)):
                print("游戏结束 恭喜过关")
                gameBoard[blackCell] = CELLNUMS - 1
                # finish = True
                success_text="游戏结束 恭喜通过"

        windowSurface.fill(BACKGROUNDCOLOR)

        for i in range(CELLNUMS):
            rowDst = int(i / VHNUMS)
            colDst = int(i % VHNUMS)
            rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

            if gameBoard[i] == -1:
                continue

            rowArea = int(gameBoard[i] / VHNUMS)
            colArea = int(gameBoard[i] % VHNUMS)
            rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
            windowSurface.blit(gameImage, rectDst, rectArea)

        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
        for i in range(VHNUMS + 1):
            pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))
        commodity(windowSurface,"step:"+str(step), gameRect.width+100, gameRect.height/5)
        commodity(windowSurface,"重新开始", gameRect.width + 100, gameRect.height /3)
        commodity(windowSurface, success_text, gameRect.width + 130, gameRect.height / 3 + 100, (255, 0, 0))

        pygame.display.update()
        mainClock.tick(FPS)


if __name__ == '__main__':
    start()
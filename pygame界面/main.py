import pygame, sys

def pygame_test():
    # 初始化
    pygame.init()
    # 创建一个窗口
    screen = pygame.display.set_mode((500, 500))
    # 设置窗口标题
    pygame.display.set_caption('这是一个窗口标题')

    # 通过不断循环来侦听事件
    while True:
        # 给屏幕填充淡蓝色
        screen.fill((135, 206, 250))

        # get():获取事件的返回值
        for event in pygame.event.get():
            # 判断事件是否是退出事件，是则退出
            if event.type == pygame.QUIT:
                # 先退出pygame窗口，再退出程序
                pygame.quit()
                sys.exit()
            # 单击鼠标窗口颜色变为粉红色
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill((255, 192, 203))

            # 更新整个待显示的 Surface 对象到屏幕上
            pygame.display.flip()

pygame_test()
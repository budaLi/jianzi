# -*- coding: utf-8 -*-
import pygame
import sys
import time
from random import randint
from pygame.locals import *
from pygame import Rect


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 255)

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("积分商店！")

# color = (255, 255, 255)
# font_height = font.get_linesize()
event_text = []
display_width = 640
display_height = 480
gameDisplay = pygame.display.set_mode( (display_width,display_height) )

def game_loop():
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button (msg, x, y, w, h, ic, ac):
    mouse =pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    smallText = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 24)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def message_diaplay(text):
    largeText = pygame.font.Font('C:/Windows/Fonts/simsun.ttc', 16)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def commodity(text,fx,fy,color=(0,0,0)):
    text_surface = font.render(text, True, color)
    textRectObj = text_surface.get_rect()
    textRectObj.center = (fx,fy)
    screen.blit(text_surface, textRectObj)

s1 = (0,0,0)
s2 = (0,0,0)
s3 = (0,0,0)
s4 = (0,0,0)
score = 100000
cost = 0
    # posx = 200
    # posy = 200
while True:  # 死循环确保窗口一直显示
    screen.fill((204, 178, 178))

    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            print(mx,my)
            if 200<=mx<=400 and 180<my<220:
                s1 = (0,0,255)
                cost = 5000
            else:
                s1 = (0, 0, 0)

            if 200<=mx<=400 and 220<my<260:
                s2 = (0,0,255)
                cost=8000
            else:
                s2 = (0, 0, 0)

            if 200<=mx<=400 and 260<my<300:
                s3 = (0,0,255)
                cost=10000
            else:
                s3 = (0, 0, 0)

            if 200<=mx<=400 and 300<my<340:
                s4 = (0,0,255)
                cost=2000
            else:
                s4 = (0, 0, 0)

            if 500 <= mx <= 600 and 400 <= my <= 450:
                # print("购买成功")
                message_diaplay('购买成功')
                score-=cost

    button("购买", 500, 400, 100, 50, green, bright_green)
    font = pygame.font.Font("C:/Windows/Fonts/simsun.ttc", 24)
    commodity("Store", 200, 80)
    commodity("现有积分:{}分".format(score), 400, 80)
    commodity("商品", 200, 150)
    commodity("价格", 400, 150)

    commodity("1.额外的生命值", 200, 200,s1)
    commodity("5000分/次", 400, 200,s1)

    commodity("2.更厚的装甲  ",200,240,s2)
    commodity("8000分/次", 400, 240,s2)

    commodity("3.连发子弹    ", 200, 280,s3)
    commodity("10000分/次", 400, 280,s3)

    commodity("4.一次性武器  ", 200, 320,s4)
    commodity("2000分/个", 400, 320,s4)




    pygame.display.flip()



    # pygame.quit()  # 退出pygame





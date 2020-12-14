# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

from turtle import *
from time import sleep

class DrawHeart():
    def go_to(self,x, y):
        up()
        goto(x, y)
        down()


    def big_Circle(self,size):  # 函数用于绘制心的大圆
        speed(5)
        for i in range(150):
            forward(size)
            right(0.3)


    def small_Circle(self,size):  # 函数用于绘制心的小圆
        speed(10)
        for i in range(210):
            forward(size)
            right(0.786)


    def line(self,size):
        speed(5)
        forward(51 * size)


    def heart(self,x, y, size):
        self.go_to(x, y)
        left(150)
        begin_fill()
        self.line(size)
        self.big_Circle(size)
        self.small_Circle(size)
        left(120)
        self.small_Circle(size)
        self.big_Circle(size)
        self.line(size)
        end_fill()


    def arrow(self):
        pensize(10)
        setheading(0)
        self.go_to(-400, 0)
        left(15)
        forward(150)
        self.go_to(339, 178)
        forward(150)


    def arrowHead(self):
        pensize(1)
        speed(5)
        color('red', 'red')
        begin_fill()
        left(120)
        forward(20)
        right(150)
        forward(35)
        right(120)
        forward(35)
        right(150)
        forward(20)
        end_fill()


    def main(self):
        pensize(4)
        color('red', 'pink')
        # getscreen().tracer(30, 0) #取消注释后，快速显示图案
        self.heart(200, 0, 1)  # 画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
        setheading(0)  # 使画笔的方向朝向x轴正方向
        self.heart(-80, -100, 1.5)  # 画出第二颗心
        self.arrow()  # 画出穿过两颗心的直线
        self.arrowHead()  # 画出箭的箭头
        self.go_to(400, -300)
        done()

if __name__ == '__main__':
    drawheart = DrawHeart()
    drawheart.main()
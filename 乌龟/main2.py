# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""


import turtle


class DrawTaichi():
    def __init__(self):
        turtle.speed(1)
        turtle.pensize(4)

    def draw_mid_circle(self):
        turtle.color('black', 'black')
        turtle.begin_fill()
        #右中圆
        turtle.circle(50,180)
        #左大圆
        turtle.circle(100,180)
        #左中圆
        turtle.left(180)
        turtle.circle(-50,180)
        turtle.end_fill()

    def draw_up_circle(self):
        turtle.color('white', 'white')
        turtle.begin_fill()
        #上小圆
        turtle.left(90)
        turtle.penup()
        turtle.forward(35)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(15)
        turtle.end_fill()

    def draw_lower_circle(self):
        turtle.color('black', 'black')
        turtle.begin_fill()
        #下小圆
        turtle.left(90)
        turtle.penup()
        turtle.backward(70)
        turtle.pendown()
        turtle.left(90)
        turtle.circle(15)
        turtle.end_fill()
    def draw_right_circle(self):
        #右大圆
        turtle.right(90)
        turtle.up()
        turtle.backward(65)
        turtle.right(90)
        turtle.down()
        turtle.circle(100, 180)

        turtle.done()

    def main_draw(self):
        self.draw_mid_circle()
        self.draw_up_circle()
        self.draw_lower_circle()
        self.draw_right_circle()


if __name__ == '__main__':
    draw_taichi = DrawTaichi()
    draw_taichi.main_draw()
# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

import turtle
class Drawhuan():

    def __init__(self):
        turtle.title("五环")
        self.pen=turtle.Pen()

    def draw_first(self):

        self.pen.width(8)
        self.pen.color("#307CB9")
        self.pen.circle(40)

    def draw_second(self):
        self.pen.penup()
        self.pen.forward(90)
        self.pen.pendown()
        self.pen.pencolor("black")
        self.pen.circle(40)

    def draw_third(self):
        self.pen.penup()
        self.pen.forward(90)
        self.pen.pendown()
        self.pen.pencolor("red")
        self.pen.circle(40)

    def draw_four(self):
        self.pen.penup()
        self.pen.right(180)
        self.pen.forward(100)
        self.pen.right(90)
        self.pen.pendown()
        self.pen.pencolor("orange")
        self.pen.circle(40)

    def draw_five(self):
        self.pen.penup()
        self.pen.right(90)
        self.pen.forward(15)
        self.pen.right(90)
        self.pen.forward(5)
        # self.pen.right(90)
        self.pen.pendown()
        self.pen.pencolor("green")
        self.pen.circle(40)
        turtle.done()

    def draw(self):
        self.draw_first()
        self.draw_second()
        self.draw_third()
        self.draw_four()
        self.draw_five()

if __name__ == '__main__':
    drawhuan = Drawhuan()
    drawhuan.draw()
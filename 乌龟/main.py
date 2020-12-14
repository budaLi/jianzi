# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import turtle

class DrawTortoise:
    def __init__(self):
        self.t = turtle.Turtle()

    def setpen(self,x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.setheading(0)

    def circle(self,x, y, r, color):
        n = 36
        angle = 360 / n
        pi = 3.1415926
        c = 2 * pi * r
        l = c / n
        start_x = x - l / 2
        start_y = y + r
        self.setpen(start_x, start_y)
        self.t.pencolor(color)
        self.t.fillcolor(color)
        self.t.begin_fill()
        for i in range(n):
            self.t.forward(l)
            self.t.right(angle)
        self.t.end_fill()


    def five_star(self,l):
        self.setpen(0, 0)
        self.t.setheading(162)
        self.t.forward(150)
        self.t.setheading(0)
        self.t.fillcolor('WhiteSmoke')
        self.t.begin_fill()
        self.t.hideturtle()
        self.t.penup()
        for i in range(5):
            self.t.forward(l)
            self.t.right(144)
        self.t.end_fill()


    def sheild(self):
        self.circle(0, 0, 300, 'red')
        self.circle(0, 0, 250, 'white')
        self.circle(0, 0, 200, 'red')
        self.circle(0, 0, 150, 'blue')
        self.five_star(284)
        turtle.done()

if __name__ == '__main__':
    draw_tortoise = DrawTortoise()
    draw_tortoise.sheild()


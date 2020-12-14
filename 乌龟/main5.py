# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

from turtle import *
from time import *
import turtle
class Draw():
    def __init__(self):

        self.t = Turtle()
        self.t.pensize(2)
        turtle.bgcolor("black")
        self.colors = ["red", "yellow", 'purple', 'blue']
        self.t._tracer(False)
    def draw(self):
        for x in range(400):
            self.t.forward(2*x)
            self.t.color(self.colors[x % 4])
            self.t.left(91)
        self.t._tracer(True)
        done()


if __name__ == '__main__':
    draw = Draw()
    draw.draw()
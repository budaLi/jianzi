#!/usr/bin/env python
# -*- coding: utf-8 –*-
''' Use the turtle class to draw a five-star red flag. '''
__author__ = 'xu xinjian'

import turtle
import math

'''Define a class of coordinate points'''


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y


'''Define a class to get the distance between two points'''


class Getlen:
    def __init__(self, p1, p2):
        self.x = p1.getx() - p2.getx()
        self.y = p1.gety() - p2.gety()
        # Use math.sqrt() to find the square root
        self.len = math.sqrt((self.x ** 2) + (self.y ** 2))
        # Define the function to get the length of the line

    def getlen(self):
        return self.len


'''Initialize window and canvas size'''

turtle.setup(width=240 * 2, height=160 * 2, startx=350, starty=250)
turtle.bgcolor("red")
turtle.shape("turtle")
turtle.color("yellow", "yellow")

'''
 Draw a big five-pointed star
'''
turtle.penup()
turtle.goto(-160, 108)
turtle.right(72)
turtle.pendown()

length1 = 2 * 48 * math.cos(18)  # Calculate the side length of the five-pointed star
# print(length1)
turtle.begin_fill()  # Start filling
# Repeat drawing five sides
for i in range(5):
    turtle.forward(length1)
    turtle.right(144)
turtle.end_fill()

'''Back to the center of the big five-pointed star'''
turtle.penup()
turtle.goto(-160, 80)
turtle.setheading(0)  # To the right

'''
 Draw the first small five-pointed star
'''
p0 = Point(-160, 80)
p1 = Point(-80, 124)
d1 = Getlen(p0, p1).getlen()  #

angle1 = math.degrees(math.atan(3 / 5))
print("angle1:", angle1)
turtle.left(angle1)
turtle.penup()
turtle.forward(d1 - 16)
turtle.pendown()
turtle.left(18)
length2 = 2 * 16 * math.cos(18)
turtle.begin_fill()
for i in range(5):
    turtle.forward(length2)
    turtle.right(144)
turtle.end_fill()

'''Back to the center of the big five-pointed star'''
turtle.penup()
turtle.goto(-160, 80)
turtle.setheading(0)
'''
 Draw the second small five-pointed star
'''
p0 = Point(-160, 80)
p1 = Point(-48, 96)
d1 = Getlen(p0, p1).getlen()

angle1 = math.degrees(math.atan(1 / 7))
print("angle1:", angle1)
turtle.left(angle1)
turtle.penup()
turtle.forward(d1 - 16)
turtle.pendown()
turtle.left(18)
length2 = 2 * 16 * math.cos(18)
turtle.begin_fill()
for i in range(5):
    turtle.forward(length2)
    turtle.right(144)
turtle.end_fill()

'''Back to the center of the big five-pointed star'''
turtle.penup()
turtle.goto(-160, 80)
turtle.setheading(0)
'''
 Draw the third small five-pointed star
'''
p0 = Point(-160, 80)
p1 = Point(-48, 48)
d1 = Getlen(p0, p1).getlen()

angle1 = math.degrees(math.atan(2 / 7))
print("angle1:", angle1)
turtle.right(angle1)
turtle.penup()
turtle.forward(d1 - 16)
turtle.pendown()
turtle.left(18)
length2 = 2 * 16 * math.cos(18)
turtle.begin_fill()
for i in range(5):
    turtle.forward(length2)
    turtle.right(144)
turtle.end_fill()

'''Back to the center of the big five-pointed star'''
turtle.penup()
turtle.goto(-160, 80)
turtle.setheading(0)
'''
 Draw the fourth small five-pointed star
'''
p0 = Point(-160, 80)
p1 = Point(-80, 16)
d1 = Getlen(p0, p1).getlen()

angle1 = math.degrees(math.atan(4 / 5))
print("angle1:", angle1)
turtle.right(angle1)
turtle.penup()
turtle.forward(d1 - 16)
turtle.pendown()
turtle.left(18)
length2 = 2 * 16 * math.cos(18)
turtle.begin_fill()
for i in range(5):
    turtle.forward(length2)
    turtle.right(144)
turtle.end_fill()

turtle.hideturtle()
turtle.mainloop()
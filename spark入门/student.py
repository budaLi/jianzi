# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def __gt__(self, other):
        if self.score> other.score:
            return True
        elif self.score == other.score and self.age >other.age :
            return True
        else:
            return False
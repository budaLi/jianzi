# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
class Person(object):
    def __init__(self):

        # 私有属性
        self.__name = "libuda"

        # 非公有属性
        self._age = 18

        # 公有属性 不与保留字冲突
        self.skill = "code"
        # 公有属性 与保留字冲突
        self.print_ = "play"
    def _print(self,name):

        return None
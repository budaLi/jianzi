# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import threading

def thread_1(number):
    for i in range(number):
        thread_1 = threading.Thread(target=eval("lis.append('A')"))
        thread_1.start()
        thread_2()
        thread_3()
        thread_4()

def thread_2():
    thread_2 = threading.Thread(target=eval("lis.append('B')"))
    thread_2.start()

def thread_3():
    thread_3 = threading.Thread(target=eval("lis.append('C')"))
    thread_3.start()

def thread_4():
    thread_4 = threading.Thread(target=eval("lis.append('D')"))
    thread_4.start()

while 1:
    lis = []
    n = int(input())
    thread_1(n)
    print("".join(lis))
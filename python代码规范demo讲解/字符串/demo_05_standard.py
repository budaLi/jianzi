"""
    字符串
"""
# @Time    : 2020/10/27 11:02
# @Author  : Libuda
# @FileName: demo_05_old.py
# @Software: PyCharm


#1. python中字符串为常量，每次执行 + 操作都需要申请内存，重新创建一个新字符串，性能很差。
# 2. %占位符格式化字符串，来自于C语言，在有多个占位符填充时可读性很差。

STR_2 = "{} from {}".format("Hello World", "Python")

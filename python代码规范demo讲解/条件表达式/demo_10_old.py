"""
    条件表达式
"""
# @Time    : 2020/10/27 10:49
# @Author  : Libuda
# @FileName: demo_10_old.py
# @Software: PyCharm


t = 10
unit = "seconds" if t < 60 else "minutes" if t < 3600 else "hours"

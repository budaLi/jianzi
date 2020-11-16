"""
    2.10条件表达式
"""
# @Time    : 2020/10/27 10:49
# @Author  : Libuda
# @FileName: demo_10_old.py
# @Software: PyCharm

# 条件表达式仅用于一行之内，禁止嵌套使用
# 语法略小众，其它语言背景开发者(如C++)看起来比较困惑。写复杂了难以阅读维护
T = 10
if T < 60:
    UNIT = "seconds"
elif T < 3600:
    UNIT = "minutes"
else:
    UNIT = "hours"

"""
    生成器和迭代器
"""
# @Time    : 2020/10/27 10:42
# @Author  : Libuda
# @FileName: demo_08_old.py
# @Software: PyCharm


def odds(n):
    ret = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            ret.append(i)
    return ret


for i in odds(1000):
    print(i)

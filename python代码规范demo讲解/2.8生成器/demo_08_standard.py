"""
    生成器和迭代器
"""
# @Time    : 2020/10/27 10:42
# @Author  : Libuda
# @FileName: demo_08_old.py
# @Software: PyCharm

# 生成器函数可以避免返回大列表，占用过多内存、影响性能；同时还可以保持代码的优雅易读。
# 缺点：执行速度变慢。


def odds(num):
    """
       求小于等于数字num的奇数
    :param num:
    :return:奇数列表
    """
    for num_i in range(1, num + 1):
        if num_i % 2 == 1:
            yield num_i


for i in odds(1000):
    print(i)

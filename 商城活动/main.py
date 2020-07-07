# @Time    : 2020/6/27 16:27
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm

#做一个1000次的循环，每一次循环都要生成100个随机数，
# 然后筛选1到10，10到30，30到100的个数a，
# b，c，然后就有1000个abc，再取平均值
import random

def shoujiang():
    """抽奖程序"""
    # 一二三等奖
    the_first_prize = 0
    the_secont_prize = 0
    the_third_prize = 0

    # 模拟100个人随机抽奖 放回抽样
    for i in range(100):
        number = random.randint(1, 100)  # a <= n <= b
        if number < 10:
            the_first_prize += 1
        elif number >= 10 and number < 30:
            the_secont_prize += 1
        else:
            the_third_prize += 1
    return the_first_prize, the_secont_prize, the_third_prize

def solution():
    # 循环多少次
    all_count = 1000

    totle_first = 0
    totle_secoud = 0
    totle_third = 0

    for i in range(all_count):
        res_first,res_secoud,res_third = shoujiang()
        totle_first+=res_first
        totle_secoud+=res_secoud
        totle_third+=res_third

    average_first_prize_number = totle_first/all_count
    average_second_prize_number = totle_secoud/all_count
    average_third_prize_number = totle_third/all_count
    print("经{}次求平均，一等奖需准备{}个，二等奖{}个，三等奖{}个".format(all_count,average_first_prize_number,average_second_prize_number,average_third_prize_number))


if __name__ == '__main__':
    solution()
# @Time    : 2020/7/7 10:48
# @Author  : Libuda
# @FileName: question1.py
# @Software: PyCharm
import random

def q1():
    """
    产生随机数 并输出
    :return:
    """
    res_lis = []
    for i in range(40):
        number = random.randint(100,999)
        res_lis.append(number)

    for i in range(len(res_lis)):
        if i!=0 and i%8==0:
            print("\n")
        print("\t"*3+str(res_lis[i]),end="\t")
    print("\n")
    return res_lis

def q2(rel_lis):
    """
    统计最大值 最小值 平均值
    :return:
    """
    print("最大值：{}，最小值：{}，平均值：{}".format(max(rel_lis),min(rel_lis),sum(rel_lis)/len(rel_lis)))

def q3(res_lis):
    """
    统计水仙花数
    :param res_lis:
    :return:
    """
    res = []
    for one in res_lis:
        # 必须是三位数
        if one>=100 and one<1000:
            tmp = str(one)
            if int(tmp[0])**3 +int(tmp[1])**3+int(tmp[2])**3 ==one:
                res.append(one)

    if len(res)==0:
        print("该列表中无水仙花数")
    else:
        print("水仙花数有:")
        for one in res:
            print(one)


if __name__ == '__main__':
    res_lis = q1()
    q2(res_lis)
    q3(res_lis)
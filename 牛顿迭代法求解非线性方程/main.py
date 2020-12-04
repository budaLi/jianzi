# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""


from numpy import *
import numpy as np

def Fun(x,num):                       #方程组在这里，两个变量分别是x的两个分量，num是未知数个数，这里是2，f是2个方程组
    i = num
    f = np.zeros((i),dtype=float)
    f[0] = x[0]+2*x[1]-3
    f[1] = 2*x[0]**2 + x[1]**2-5

    return f

def dfun(x,num):                         #计算雅可比矩阵的逆矩阵
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001                           #
    x1 = np.copy(x)
    for i in range(0,num):              # 求导数，i是列，j是行
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx           #x+dx
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx   #f(x+dx)-f（x）/dx
    df_1 = np.linalg.inv(df)                              #计算逆矩阵
    return df_1

def Newton(x,num):
    x1 = np.copy(x)
    i = 0
    delta = np.copy(x)

    while(np.sum(abs(delta)) > 1.e-3):  #控制循环次数  10-3
        x1 = x-dot(dfun(x,num),Fun(x,num))  #公式
        delta = x1-x                     #比较x的变化
        x = x1
        i = i+1

    return x

def main():
    # 方程未知数的个数
    num =2

    x = np.ones((num),dtype=float)

    #初始值
    x[0]=1.5
    x[1]=1.0
    a = Newton(x,num)
    print(a)

if __name__ == '__main__':
    main()
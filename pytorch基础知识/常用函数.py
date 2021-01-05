# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import torch
import numpy as np

# 判断一个对象是否是tensor(pytoch张量)
data = np.zeros((2,2))
print(data)
print(torch.is_tensor(data))
data = torch.tensor(data)
print(torch.is_tensor(data))

# 创建一个张量  对角线为1 其他位置为0
# n：行数
# m：列数 默认为n
print(torch.eye(2))

# 返回tensor中元素的个数
print(torch.numel(torch.randn([1,2,3,4]))) #24

# 将ndarrary的数据转换为tensor
print(torch.from_numpy(np.array([1,2,3])))

# 输出一维张量 包含区间在 start 和 end 之间的均匀间隔step个数据
print(torch.linspace(1,200,50))

# 输出一维张量 为torch.pow(10,start)和torch.pow(10,end)之前的step个数据
print(torch.logspace(10,20,10))

print(torch.rand(4))
print(torch.rand(2,3))
print(torch.rand([2,3]))

# 返回一个从0到n-1的随机整数排列
print(torch.randperm(10))

# tensor连接
x = torch.rand(2,3)
# 在行上 默认dim为0
print(torch.cat((x,x,x),dim=0))
# 列上
print(torch.cat((x,x,x),dim=1))

# 分块 将tensor按指定方向切分成指定块数
x2 = torch.rand(4,4)
print(torch.chunk(x2,2,dim=0))
print(torch.chunk(x2,2,dim=1))

# torch.squeeze
# torch.squeeze(input, dim=None, out=None)
# 将输入张量形状中的1 去除并返回。 如果输入是形如(A×1×B×1×C×1×D)，那么输出形状就为： (A×B×C×D)
# 当给定dim时，那么挤压操作只在给定维度上。例如，输入形状为: (A×1×B), squeeze(input, 0) 将会保持张量不变，只有用 squeeze(input, 1)，形状会变成 (A×B)。
#
# 注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。
#
# 参数:
#
# input (Tensor) – 输入张量
# dim (int, optional) – 如果给定，则input只会在给定维度挤压
# out (Tensor, optional) – 输出张量
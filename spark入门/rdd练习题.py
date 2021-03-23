# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
from pyspark.context import SparkContext


sc = SparkContext("local","test")
# -----------------------求平均数
# data = [1,5,7,10,23,20,6,5,10,7,10]
# # reduce后除以数量
# rdd = sc.parallelize(data)
#
# totle_sum = rdd.reduce(lambda x,y:x+y+0.0)
# totle_cnt = rdd.count()
# avg = totle_sum/totle_cnt

##------------------------求data中出现次数最多的数，若有多个，求这些数的平均值
data =  [1,5,7,10,23,20,7,5,10,7,10]
rdd = sc.parallelize(data)
# 计算每个数出现的次数
totle_dict = rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
print(totle_dict.collect())
# 出现次数最多的数 不能用max 因为出现次数最多的数可能有好几个
max_count = totle_dict.max(lambda x:x[1])
# 我们可以得出出现最多的次数为n次  找出这些数 求平均
mode = totle_dict.filter(lambda x:x[1]==max_count[1])
print(mode.collect())
mode = mode.reduce(lambda x,y:x[0]+y[0]+0.0)/mode.count()
print(mode)


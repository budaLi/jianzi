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
# data =  [1,5,7,10,23,20,7,5,10,7,10]
# rdd = sc.parallelize(data)
# # 计算每个数出现的次数
# totle_dict = rdd.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
# print(totle_dict.collect())
# # 出现次数最多的数 不能用max 因为出现次数最多的数可能有好几个
# max_count = totle_dict.max(lambda x:x[1])
# # 我们可以得出出现最多的次数为n次  找出这些数 求平均
# mode = totle_dict.filter(lambda x:x[1]==max_count[1])
# print(mode.collect())
# mode = mode.reduce(lambda x,y:x[0]+y[0]+0.0)/mode.count()
# print(mode)


# -----------------------求TopN 任务：有一批学生信息表格，包括name,age,score, 找出score排名前3的学生, score相同可以任取
# students = [("LiLei",18,87),("HanMeiMei",16,77),("DaChui",16,66),("Jim",18,77),("RuHua",18,50)]
# n = 3
# rdd = sc.parallelize(students)
# # 第一种
# # top3= rdd.top(n,key=lambda x:x[2])
# # print(top3)
# # 第二种
# rdd = rdd.sortBy(lambda x:x[2],ascending=False)
# top3 = rdd.take(3)
# print(top3)



# ------------------- 排序并返回序号
#任务：排序并返回序号, 大小相同的序号可以不同
# data = [1,7,8,5,3,18,34,9,0,12,8]
# rdd = sc.parallelize(data)
# res =rdd.sortBy(lambda x:x,ascending=True).zipWithIndex()
# print(res.collect())


# ------------------- 二次排序
#任务：有一批学生信息表格，包括name,age,score
#首先根据学生的score从大到小排序，如果score相同，根据age从大到小
# students = [("LiLei",18,87),("HanMeiMei",16,77),("DaChui",16,66),("Jim",18,77),("RuHua",18,50)]
# rdd_students = sc.parallelize(students)
# # 只能从另外一个文件导入 否则会序列化报错
# from student import Student
# # 重写student的__gt__方法可用于比较
# rdd_sorted = rdd_students.map(lambda t:Student(t[0],t[1],t[2])).\
#     sortBy(lambda x:x,ascending=True).\
#     map(lambda student:(student.name,student.score,student.age))
# print(rdd_sorted.collect())


#---------------------任务：已知班级信息表和成绩表，找出班级平均分在75分以上的班级
#班级信息表包括class,name,成绩表包括name,score
# classes = [("class1","LiLei"), ("class1","HanMeiMei"),("class2","DaChui"),("class2","RuHua")]
# scores = [("LiLei",76),("HanMeiMei",80),("DaChui",70),("RuHua",60)]
#
# def avg(info):
#     class_name = info[0]
#     score = info[1]
#     avg_score = sum(score)/len(score)
#     return class_name,avg_score
#
# # 要注意join时 需要第一位元素相同
# rdd_1 = sc.parallelize(classes).map(lambda x:(x[1],x[0]))
# rdd_2 = sc.parallelize(scores)
# totle_data = rdd_1.join(rdd_2).map(lambda x:(x[1][0],x[1][1])).groupByKey().map(lambda x:avg(x)).filter(lambda x:x[1]>75)
# print(totle_data.collect())


# -------------分组求众数
#任务：有一批学生信息表格，包括class和age。求每个班级学生年龄的众数。
students = [("class1",15),("class1",15),("class2",16),("class2",16),("class1",17),("class2",19)]
rdd_students = sc.parallelize(students)

def get_zhongshu(info):
    class_name = info[0]
    scores = info[1]
    scores_count = {}
    for score in scores:
        if score not in scores_count:
            scores_count[score] =1
        else:
            scores_count[score]+=1

    max_score_cnt = 0
    max_score = 0
    for score_key,score_cnt in scores_count.items():
        if score_cnt>max_score_cnt:
            max_score_cnt = score_cnt
            max_score = score_key

    return class_name,max_score

rdd_students = rdd_students.groupByKey().map(lambda info:get_zhongshu(info))
print(rdd_students.collect())
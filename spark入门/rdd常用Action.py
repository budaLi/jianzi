# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
from pyspark.context import SparkContext



sc = SparkContext("local","rdd操作")
#numSlices为并行集合的数量  他指定了将数据集切分为几份
# 在集群模式中 Spark会为每一份slice起一个task，一般来说，spark会默认指定
rdd = sc.parallelize(range(10),numSlices=1)
print(rdd.collect())

# 随机取若干个数 withReplacement 为是否放回抽样 放回的话有几率重复
sample_data = rdd.takeSample(withReplacement=True,num=10,seed=0)
print(sample_data)

#first取第一个数据
rdd = sc.parallelize(range(10),5)
first_data = rdd.first()
print(first_data)

#count查看RDD元素数量
rdd = sc.parallelize(range(10),5)
data_count = rdd.count()
print(data_count)

#reduce利用二元函数对数据进行规约
rdd = sc.parallelize(range(10),5)
rdd.reduce(lambda x,y:x+y)

#foreach对每一个元素执行某种操作，不生成新的RDD
#累加器用法详见共享变量
rdd = sc.parallelize(range(10),5)
accum = sc.accumulator(0)
rdd.foreach(lambda x:accum.add(x))
print(accum.value)


#countByKey对Pair RDD按key统计数量
pairRdd = sc.parallelize([(1,1),(1,4),(3,9),(2,16)])
pairRdd.countByKey()

#saveAsTextFile保存rdd成text文件到本地
text_file = "./data/rdd.txt"
rdd = sc.parallelize(range(5))
rdd.saveAsTextFile(text_file)

#filter应用过滤条件过滤掉一些数据
rdd = sc.parallelize(range(10),3)
rdd.filter(lambda x:x>5).collect()

#flatMap操作执行将每个元素生成一个Array后压平
rdd = sc.parallelize(["hello world","hello China"])
rdd.map(lambda x:x.split(" ")).collect()


#distinct去重
rdd = sc.parallelize([1,1,2,2,3,3,4,5])
rdd.distinct().collect()

#subtract找到属于前一个rdd而不属于后一个rdd的元素
a = sc.parallelize(range(10))
b = sc.parallelize(range(5,15))
a.subtract(b).collect()

#union合并数据
a = sc.parallelize(range(5))
b = sc.parallelize(range(3,8))
a.union(b).collect()

#intersection求交集
a = sc.parallelize(range(1,6))
b = sc.parallelize(range(3,9))
a.intersection(b).collect()

#cartesian笛卡尔积
boys = sc.parallelize(["LiLei","Tom"])
girls = sc.parallelize(["HanMeiMei","Lily"])
boys.cartesian(girls).collect()

#按照某种方式进行排序
#指定按照第3个元素大小进行排序
rdd = sc.parallelize([(1,2,3),(3,2,2),(4,1,1)])
rdd.sortBy(lambda x:x[2]).collect()


#按照拉链方式连接两个RDD，效果类似python的zip函数
#需要两个RDD具有相同的分区，每个分区元素数量相同

rdd_name = sc.parallelize(["LiLei","Hanmeimei","Lily"])
rdd_age = sc.parallelize([19,18,20])

rdd_zip = rdd_name.zip(rdd_age)
print(rdd_zip.collect())

#将RDD和一个从0开始的递增序列按照拉链方式连接。
rdd_name =  sc.parallelize(["LiLei","Hanmeimei","Lily","Lucy","Ann","Dachui","RuHua"])
rdd_index = rdd_name.zipWithIndex()
print(rdd_index.collect())

# PairRDD指的是数据为长度为2的tuple类似(k,v)结构的数据类型的RDD,其每个数据的第一个元素被当做key，第二个元素被当做value.
#reduceByKey对相同的key对应的values应用二元归并操作
rdd = sc.parallelize([("hello",1),("world",2),
                               ("hello",3),("world",5)])
rdd.reduceByKey(lambda x,y:x+y).collect()

#groupByKey将相同的key对应的values收集成一个Iterator
rdd = sc.parallelize([("hello",1),("world",2),("hello",3),("world",5)])
rdd.groupByKey().collect()

#sortByKey按照key排序,可以指定是否降序
rdd = sc.parallelize([("hello",1),("world",2),
                               ("China",3),("Beijing",5)])
rdd.sortByKey(False).collect()


#join相当于根据key进行内连接
age = sc.parallelize([("LiLei",18),
                        ("HanMeiMei",16),("Jim",20)])
gender = sc.parallelize([("LiLei","male"),
                        ("HanMeiMei","female"),("Lucy","female")])
age.join(gender).collect()

#leftOuterJoin相当于关系表的左连接
age = sc.parallelize([("LiLei",18),
                        ("HanMeiMei",16)])
gender = sc.parallelize([("LiLei","male"),
                        ("HanMeiMei","female"),("Lucy","female")])
age.leftOuterJoin(gender).collect()

#cogroup相当于对两个输入分别goupByKey然后再对结果进行groupByKey
x = sc.parallelize([("a",1),("b",2),("a",3)])
y = sc.parallelize([("a",2),("b",3),("b",5)])
result = x.cogroup(y).collect()
print(result)
print(list(result[0][1][0]))

#foldByKey的操作和reduceByKey类似，但是要提供一个初始值
x = sc.parallelize([("a",1),("b",2),("a",3),("b",5)],1)
x.foldByKey(1,lambda x,y:x*y).collect()
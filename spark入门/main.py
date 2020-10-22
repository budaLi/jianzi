# @Time    : 2020/10/22 14:45
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# 从pyspark.context模块导入SparkContext
from pyspark.context import SparkContext
import jieba

# 实例化一个SparkContext，用于连接Spark集群
# 第一个参数“local”表示以本地模式加载集群
# 第二个参数“WordCount”表示appName，不能有空格
spark = SparkContext("local", "WordCount")

# 读取数据，创建弹性式分布数据集（RDD）
data = spark.textFile(r"C:\Users\lenovo\PycharmProjects\兼\spark入门\news.txt")

# 读取中文停用词
with open(r'C:\Users\lenovo\PycharmProjects\兼\spark入门\stopwords-zh.txt', 'r', encoding='utf-8') as f:
    s = f.readline()
stop = [i.replace('\n','') for i in s]

# 分词并统计词频
data = data.flatMap(lambda line: jieba.cut(line,cut_all=False)).\
    filter(lambda w: w not in stop).\
    map(lambda w: (w,1)).\
    reduceByKey(lambda w0, w1: w0 + w1).\
    sortBy(lambda x: x[1], ascending=False)

# 输出前100个高频词汇
print(data.take(100))
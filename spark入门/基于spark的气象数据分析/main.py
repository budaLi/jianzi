# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
#导入所需要的库
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 关于spark sql的字段类型 https://blog.csdn.net/An1090239782/article/details/102541024#11_11
# 主要有ByteType ShortType IntegerType LongTyple FloatType DecimalType BooleanType及时间 TimestampType DateType
from pyspark.sql.types import DecimalType,TimestampType
import os



# 计算各个城市过去24小时的累计雨量
def compute_rained_24h():
    # 选择所需要的列 并把下雨的数据转换数据类型为任意精度 scale表示取小数点后几位
    # agg 在指定的轴上(默认为0) 使用一个或多个函数聚合 aggregate
    df_rain = df.select(df["province"],df["city_name"],df["city_code"],df["rain1h"].cast(DecimalType(scale=2)))\
                .filter(df["rain1h"]<1000)\
                .groupby("province","city_name","city_code")\
                .agg(F.sum("rain1h").alias("rain24h"))\
                .sort(F.desc("rain24h"))  # 分组聚合排序
    df_rain.show()


# 计算各个城市当日平均气温  以2,8,12,20时的平均气温计算
def compute_avg_temperature():
    df_temperature = df.select(df["province"],df["city_name"],df["city_code"],
                               df["temperature"].cast(DecimalType(scale=2)),
                                F.date_format(df["time"],"yyyy-MM-dd").alias("date"),
                                F.hour(df["time"]).alias("hour"))
    # 只需要4个时间的数据
    df_4_point_temperature = df_temperature.filter(df_temperature["hour"].isin(2,8,12,20))

    df_avg_temperature = df_4_point_temperature.groupby("province","city_name","city_code","date").\
                        agg(F.count("temperature"),F.avg("temperature").alias("avg_temperature")).\
                        filter("count(temperature)=4").\
                        sort(F.asc("avg_temperature")).select("province", "city_name", "city_code", "date",
                                     F.format_number('avg_temperature', 2).alias("avg_temperature"))
    df_avg_temperature.show()


if __name__ == '__main__':
    filename = "./data/weather_noall.csv"
    # spark session对象  .getOrCreate())如果不存在则创建
    spark = SparkSession.builder.master('local').appName("compute_rained").getOrCreate()
    # 从指定文件中读取数据 指定格式和表头
    df = spark.read.load(filename, format="csv", header="true")
    # df.show()

    # compute_rained_24h()
    compute_avg_temperature()

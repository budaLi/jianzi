# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import random
from pyspark.context import  SparkContext
from pyspark import SparkConf

def mock_data(number):
    """
    mock 数据
    :return:
    """
    date = []
    base_date = "2021-3-{}"
    for i in range(30):
        date.append(base_date.format(i))

    ip = []
    base_ip = "192.168.{}.{}"
    for i in range(255):
        ip.append(base_ip.format(i,i))

    url = []
    base_url = "www.{}.com"
    name = ["baidu","360","aiqiyi"]
    for one in name:
        url.append(base_url.format(one))

    uid = []
    for i in range(10000):
        uid.append("uid_{}".format(i))

    area = ["shanghai","beijing","shengzhen","guangzhou","taiyuan"]

    action = ["login","view","buy","register","comment"]

    totle_data = []
    for i in range(number):
        data = "{} {} {} {} {} {}".format(
            random.choice(date),
            random.choice(ip),
            random.choice(url),
            random.choice(uid),
            random.choice(area),
            random.choice(action),
        )
        totle_data.append(data)

    with open("data.txt","w") as f:
        for one in totle_data:
            print(one)
            f.write(one+"\n")

def get_top3_uid_and_cnt(info):
    """ info 为某site 对应的用户访问个数 """

    # site = info[0]
    # uid_cnt = info[1]
    #
    # top_res = ["","",""]
    # for one in uid_cnt:
    #     uid = one[0]
    #     cnt = one[1]
    #     if top_res[2]=="":
    #         top_res[2] = cnt
    #     elif cnt>top_res[2]:
    #         top_res[2] = cnt
    #         top_res[0] = site
    #         top_res[1] = uid
    # top_res = tuple(top_res)
    return {"1":123}

# 统计每个网站每个用户访问的次数
def get_site_uid_cnt(info):
    site = info[0]
    uids = info[1]

    # 统计每个用户访问次数
    info_cnt = {}
    for uid in uids:
        if uid not in info_cnt:
            info_cnt[uid] = 1
        else:
            info_cnt[uid] += 1
    # 统计当前site 每个用户出现的次数
    res = []
    for uid, cnt in info_cnt.items():
        tem = (site, uid, cnt)
        res.append(tem)
    # res = tuple(res)
    return res

def get_top_3():
    """
    统计每个网址访问的uid的前三个人及他访问的次数
    :return:
    """

    spark = SparkContext("local","get_top3")
    data = spark.textFile("data.txt")

    data.map(lambda line:(line.split(" ")[2],line.split(" ")[3])).\
        groupByKey()\
        .flatMap(lambda info:get_site_uid_cnt(info))\
        .groupByKey()\
        .map(lambda x:get_top3_uid_and_cnt(x))\
        .foreach(print)



if __name__ == '__main__':
    # 生成数据
    # number = 10000
    # mock_data(number)
    #
    get_top_3()
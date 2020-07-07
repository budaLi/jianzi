# @Time    : 2020/6/25 18:00
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm

import pandas as pd

from pylab import *
import matplotlib.pyplot as plt


def show():
    # 图像上显示中文
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    data = pd.read_csv(r"Find-Job (1).csv",encoding="gbk")

    # 察看表格信息
    # print(data.head())
    # 表格shape
    print(data.shape)

    # 统计缺失值信息
    print(data.isnull().sum())

    # 提取有用数据
    useful_data = data.iloc[:,3]
    # # print(useful_data.shape)

    # # 去除空值
    useful_data = useful_data.dropna(how="any")
    print(useful_data.shape)

    # 只要月的数据
    useful_data = useful_data[useful_data.str.contains("月")]
    # 最高薪资
    useful_data_max = useful_data.str.replace("/月","").str.split("-").str[1].map(lambda x: float(x.strip('千'))/10 if ('千' in x) else float(x.strip('万')))
    useful_data_max.value_counts().plot(kind='barh',rot=0)
    plt.title("最高薪资/万")
    plt.show()

    # 最低薪资
    useful_data_min = useful_data.str.replace("/月","").str.split("-").str[0].map(lambda x: float(x)/10 if float(x)>3 else float(x))
    useful_data_min.value_counts().plot(kind='barh',rot=0)
    plt.title("最低薪资/万")


    plt.show()


    print(useful_data_min)


if __name__ == '__main__':
    show()
# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import os
import pandas as pd
import xlrd
from xlutils.copy import copy as xl_copy

totle_res_dic = {}  # 记录总的出入次数  example:  {(123,234):3,(456,567):1......}

class OperationExcel():
    """
    操作Excel
    """

    def __init__(self, file_name=None, sheet_id=None):
        """
        初始化OperationExcel对象
        :param file_name:
        :param sheet_id: vv
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            raise Exception("请指定filename")
        self.tables = self.get_tables()

    def get_tables(self):
        """
        返回tables对象
        :return:
        """
        ecel = xlrd.open_workbook(self.file_name)
        tables = ecel.sheet_by_index(self.sheet_id)
        return tables

    def get_nrows(self):
        """
        获取表格行数
        :return:
        """
        return self.tables.nrows

    def get_ncols(self):
        """
        获取表格列数
        :return:
        """
        return self.tables.ncols


    def get_cel_value(self, row, col):
        """
        获取某个指定单元格的内容
        :param row:
        :param col:
        :return:
        """
        data = self.tables.cell_value(row, col)
        return data

    def write_to_excel(self, file_path, sheet_id, row, col, value):
        """
        写入excel
        """
        work_book = xlrd.open_workbook(file_path, formatting_info=False)
        # 先通过xlutils.copy下copy复制Excel
        write_to_work = xl_copy(work_book)
        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(sheet_id)
        sheet_data.write(row, col, str(value))
        # 这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(file_path)


def read_data(file_path):
    """
    读取数据
    """
    dataframe = pd.read_csv(file_path)
    for index, row in dataframe.iterrows():
        # 入站
        start_station = row["ENTRYSTATIONID"]
        # 出站
        end_station = row["STATIONID"]

        # 统计次数
        if (start_station,end_station) not in totle_res_dic:
            totle_res_dic[(start_station,end_station)] = 1
        else:
            totle_res_dic[(start_station, end_station)]+=1



def map_station(bianhao_file):
    """
    将车站编号和车站名称对应成字典
    :return:
    """
    map_dic = {}
    map_dataframe = pd.read_excel(bianhao_file)

    for index, row in map_dataframe.iterrows():
        number = row['车站编号']
        name = row['车站名称']
        map_dic[number] = name

    return map_dic


def main():


    bianhao_file = "站点编号说明.xlsx"
    root_dir = "./test"
    res_file_path = "res.xls"


    res_operation_excel = OperationExcel(res_file_path, 0)
    map_dic = map_station(bianhao_file)
    new_totle_res_dic = {}
    for root,dir,files in os.walk(root_dir):
        for file in files:
            f = os.path.join(root,file)
            print("读取数据：{}".format(file))
            read_data(f)

        for key,value in totle_res_dic.items():
            new_totle_res_dic[(map_dic[key[0]],map_dic[key[1]])] = value

    # 表头
    for index,key in enumerate(map_dic):
        res_operation_excel.write_to_excel(res_file_path, 0, 0, index+1, map_dic[key])
    for index, key in enumerate(map_dic):
        res_operation_excel.write_to_excel(res_file_path, 0, index+1, 0, map_dic[key])


    row = 1
    col = 1
    for _,start_ in map_dic.items():
        for _,end_ in map_dic.items():
            value = 0
            if (start_,end_) not in new_totle_res_dic:
                res_operation_excel.write_to_excel(res_file_path,0,row,col,value)
            else:
                value = new_totle_res_dic[(start_,end_)]
                res_operation_excel.write_to_excel(res_file_path, 0, row, col, value)
            print("{} {} {} {} {}".format(row,col,start_,end_,value))
            col += 1
        col = 1
        row += 1



if __name__ == '__main__':

    main()
    # map_station()
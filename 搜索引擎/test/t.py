# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import re
import urllib.request
import urllib.request
from configparser import ConfigParser
from queue import Queue
from urllib.error import HTTPError, URLError
import threading
import time
from termcolor import colored
import xlrd
from fake_useragent import UserAgent
from googlesearch import search
from socket import timeout
from xlutils.copy import copy as xl_copy

import subprocess

def toUTF8():
    process = subprocess.Popen(['chcp', '65001'], shell=True)
    process.communicate()
toUTF8()
imageExt = ["jpeg", "exif", "tiff", "gif", "bmp", "png", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif", "bat",
            "bpg", "cgm", "svg", "jpg","css",".js",".io"]
ua = UserAgent()

def green(text):
    return colored(text, 'green', attrs=['bold'])

def red(text):
    return colored(text, 'red', attrs=['bold'])

def logger(msg,color=""):
    """
    日志信息
    """
    timeArray = time.localtime(time.time())
    now = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # now = time.strftime("",time.time())
    txt = "{}:{}".format(now, msg)
    if color=="red":
        txt = red(txt)
    elif color=="green":
        txt = green(txt)
    print(txt)


class OperationExcel():
    """
    #以面向对象的方式操作Excel
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
            self.file_name = r"C:\Users\lenovo\PycharmProjects\Spider\biying_data.xls"
            self.sheet_id = 0
        self.tables = self.get_tables()

    def create_sheet(self, sheet_name):
        ecel = xlrd.open_workbook(self.file_name)
        wb = xl_copy(ecel)
        wb.add_sheet(sheet_name)
        wb.save(self.file_name)

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

    def get_data_by_row(self, row):
        """
        根据行号获取某一行的内容
        :param row:
        :return:
        """
        if row < 0:
            row = 0
        if row > self.get_nrows():
            row = self.get_nrows()
        data = self.tables.row_values(row)
        return data

    def get_data_by_col(self, col):
        """
        根据列号返回某一列的内容
        :param col:
        :return:
        """
        if col < 0:
            col = 0
        if col > self.get_ncols():
            col = self.get_ncols()
        data = self.tables.col_values(col)
        return data

    def get_cel_value(self, row, col):
        """
        获取某个指定单元格的内容
        :param row:
        :param col:
        :return:
        """
        data = self.tables.cell_value(row, col)

        # ecxel中读取数据时默认将数字类型读取为浮点型
        if isinstance(data, float):
            data = int(data)
        return data


class Spider:
    def __init__(self):
        global url_count
        global email_count

        # 关键词excel
        self.opExcel = OperationExcel(config['keywords_excel_path'], 0)
        # 存放url的excel
        self.dataExcel = OperationExcel(file_path, 0)
        # 存放email的excel
        self.emailExcel = OperationExcel(email_path, 0)
        # 关键词队列
        self.keyword_queue = Queue()

        # url及email初始索引
        self.url_count = self.dataExcel.tables.nrows
        self.email_count = self.emailExcel.tables.nrows
        url_count = self.url_count
        email_count = self.email_count

        self.keyword_index = 0

        # 去重url和email
        self.totlc_url_res = set()
        self.totlc_email_res = set()

    def get_keywords_data(self, row):
        """
        获取关键词中某一行的值
        :param row:
        :return:
        """
        actual_data = OperationExcel(config['keywords_excel_path'], 0).get_cel_value(row, 0)
        return actual_data

    def generate_keywords_queue(self):
        """
        生成关键词队列  太大会比较慢
        :return:
        """
        key_len = self.opExcel.get_nrows()
        xx = 100 if key_len > 100 else key_len
        logger("生成关键点队列中......请稍候")
        for index in range(xx):
            key = self.get_keywords_data(index)
            key += " email"
            self.keyword_queue.put(key)

    def write_to_excel(self, file_path, sheet_id, row, col, value):
        work_book = xlrd.open_workbook(file_path, formatting_info=False)
        # 先通过xlutils.copy下copy复制Excel
        write_to_work = xl_copy(work_book)
        # 通过sheet_by_index没有write方法 而get_sheet有write方法
        sheet_data = write_to_work.get_sheet(sheet_id)
        sheet_data.write(row, col, str(value))
        # 这里要注意保存 可是会将原来的Excel覆盖 样式消失
        write_to_work.save(file_path)

    def extractOnlyUrl(self, url):
        global email_count
        try:
            listUrl = []
            req = urllib.request.Request(url,data=None,headers={ 'User-Agent': ua.random })
            try:
                conn = urllib.request.urlopen(req, timeout=10)
            except timeout:
                raise ValueError('Timeout ERROR')

            except (HTTPError, URLError):
                raise ValueError('Bad Url...')

            status = conn.getcode()
            contentType = conn.info().get_content_type()

            if (status != 200 or contentType == "audio/mpeg"):
                raise ValueError('Bad Url...')

            html = conn.read().decode('utf-8')

            # 邮箱正则匹配
            emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)

            for email in emails:
                if (email not in self.totlc_email_res and email[-3:] not in imageExt):
                    self.totlc_email_res.add(email)
                    listUrl.append(email)
            if len(listUrl) > 0:
                for email in listUrl:
                    try:
                        self.write_to_excel(email_path, 0, email_count, 0, email)
                        email_count += 1
                        logger("Email:【{}】-{}".format(email_count, email),color="red")
                    except Exception as e:
                        logger("异常信息：{}".format(e))

            return listUrl
        except Exception as e:
            pass
            # logger("获取邮箱异常：{}".format(e))

    def spider(self, key_queue):
        global url_count
        try:
            while not key_queue.empty():
                key = key_queue.get()

                logger("当前爬取第{}个关键词：{}".format(self.keyword_index, key))
                self.keyword_index += 1
                response = search(key,user_agent= ua.random)

                for index, result in enumerate(response):

                    #  休眠1s目前  暂时稳定
                    time.sleep(1)
                    # 每个url解析email
                    self.extractOnlyUrl(result)

                    url = result.split("/")
                    try:
                        tmp = url[0] + "//" + url[2]
                    except Exception as e:
                        tmp = url[0] + "//" + url[2]
                    if tmp not in self.totlc_url_res:
                        try:
                            logger("Url:【{}】:{}".format(url_count, tmp),color="green")
                            self.totlc_url_res.add(tmp)
                            self.write_to_excel(file_path, 0, url_count, 0, tmp)
                            url_count += 1
                            if url_count != 0 and url_count % 50 == 0:
                                pass
                                # logger("休眠60s中")
                                # time.sleep(60)
                        except Exception as e:
                            logger("异常信息：{}".format(e))
        except Exception as e:
            logger("异常信息：{}".format(e))

    def main(self):
        global start_index, res_set

        logger("当前已有url数量：{}".format(self.url_count))
        logger("当前已有email数量：{}".format(self.email_count))

        key_len = self.opExcel.get_nrows()
        logger("关键词总数：{}".format(key_len))
        self.generate_keywords_queue()


        threads = []
        thread_num = 5
        for i in range(thread_num):
            thread = threading.Thread(target=self.spider, args=(self.keyword_queue,))
            threads.append(thread)

        for one in threads:
            one.start()
        for one in threads:
            one.join()





def main():
    spider = Spider()
    spider.main()


if __name__ == '__main__':
    start_index = 0

    config_parser = ConfigParser()
    config_parser.read('config.cfg')
    config = config_parser['default']
    file_path = config['google_datas']
    email_path = config['google_email']
    logger(time.ctime())
    main()

# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import encodings.idna # Unknown encoding: idna in Python Requests
import smtplib  # 发送邮件 连接邮件服务器
from email.mime.text import MIMEText  # 构建邮件格式
import re
import urllib.request
import urllib.request
from configparser import ConfigParser
from os import devnull
from queue import Queue
from urllib.error import HTTPError, URLError

import threading
import time
import xlrd
from fake_useragent import UserAgent
from googlesearch import search
from socket import timeout
from termcolor import colored
from xlutils.copy import copy as xl_copy


# def to_utf8():
#     process = subprocess.Popen(['chcp', '65001'], shell=True)
#     process.communicate()
# to_utf8()

imageExt = ["jpeg", "exif", "tiff", "gif", "bmp", "png", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif", "bat",
            "bpg", "cgm", "svg", "jpg", "css", ".js", ".io", "ebp"]
ua = UserAgent()


def green(text):
    return colored(text, 'green', attrs=['bold'])


def red(text):
    return colored(text, 'red', attrs=['bold'])

class SendEmail:
    def __init__(self):
        # 发件人
        self.send_user = "李晋军" + "<1364826576@qq.com>"
        # 登录名
        self.login_user = '1364826576@qq.com'
        # 这里要注意 不是qq密码 而是在邮箱里设置的发送邮箱的授权码
        self.password = 'btfixrcdeguejfja'
        # 发送邮件的服务器地址 qq为smtp.qq.com  163邮箱为smtp.163.com
        self.email_host = 'smtp.qq.com'

    def _send(self, userlist, message):
        # 实例化邮件发送服务器
        server = smtplib.SMTP()
        # 连接qq邮箱服务器
        server.connect(self.email_host)
        # 登录服务器
        server.login(self.login_user, self.password)
        # 发送邮件  注意此处消息的格式应该用as_string()函数
        server.sendmail(self.send_user, userlist, message.as_string())
        # 关闭邮箱
        server.close()

    def send_text(self, userlist, subject, content):
        """
        发送文本邮件
        :param userlist: 接收人  列表形式
        :param subject: 主题
        :param content:  内容
        :return:
        """
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = subject
        message['From'] = self.send_user
        message['To'] = ';'.join(userlist)  # 收件人列表以分号隔开
        self._send(userlist, message)

def logger(msg, color=""):
    """
    日志信息
    """
    timeArray = time.localtime(time.time())
    # now = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    now = time.strftime("%m-%d %H:%M:%S", timeArray)
    # now = time.strftime("",time.time())
    txt = "{}:{}".format(now, msg)
    if color == "red":
        txt = red(txt)
    elif color == "green":
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
            raise Exception("请指定filename")
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
        global key_count

        key_count = 0
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

        self.keyword_index = 1
        key_index = self.keyword_index

        # 去重url和email
        self.totlc_url_res = set()
        self.totlc_email_res = set()

        # 过滤规则
        self.fillter = config['fillter'].split(",")

    def filter_email(self,data):
        for one in self.fillter:
            if one in data:
                return None
        return data

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
        xx = target_spider_keyword_number if key_len > target_spider_keyword_number else key_len
        logger("生成关键点队列中......请稍候")

        for index in range(start_keyword_index,xx):
            key = self.get_keywords_data(index)
            key += " "+default_add_keyword
            self.keyword_queue.put(key)

    def write_to_excel(self, file_path, sheet_id, row, col, value):
        """
        写入excel  #TODO 异常处理
        :param file_path:
        :param sheet_id:
        :param row:
        :param col:
        :param value:
        :return:
        """
        try:
            work_book = xlrd.open_workbook(file_path, formatting_info=False, logfile=open(devnull, 'w'))
            # 先通过xlutils.copy下copy复制Excel
            write_to_work = xl_copy(work_book)
            # 通过sheet_by_index没有write方法 而get_sheet有write方法
            sheet_data = write_to_work.get_sheet(sheet_id)
            sheet_data.write(row, col, str(value))
            # 这里要注意保存 可是会将原来的Excel覆盖 样式消失
            write_to_work.save(file_path)
        except:
            pass

    def extractOnlyUrl(self, url,key_index,key,thread_number):
        global email_count
        try:
            time.sleep(pre_url_or_email_sleep)
            listUrl = []
            req = urllib.request.Request(url, data=None, headers={'User-Agent': ua.random})
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
                    email = self.filter_email(email)
                    if email:
                        self.totlc_email_res.add(email)
                        listUrl.append(email)
            if len(listUrl) > 0:
                for email in listUrl:
                    try:
                        self.write_to_excel(email_path, 0, email_count, 0, email)
                        email_count += 1
                        logger("线程：{}：正采集第{}词：{},Email为:【{}】:{}".format(thread_number,key_index, key,email_count, email), color="")
                    except Exception as e:
                        logger("邮箱异常信息：{}".format(e))

            return listUrl
        except Exception as e:
            # logger("获取邮箱异常：{}".format(e))
            pass

    def spider(self, key_queue,thread_number):
        global url_count
        global key_count
        key_index=thread_number
        try:
            while not key_queue.empty():
                key = key_queue.get()

                logger("线程：{}：当前爬取第{}个关键词：{}".format(thread_number,key_index, key))
                key_count+=1
                response = search(key, user_agent=ua.random)
                current_url_count = url_count

                for index, result in enumerate(response):

                    #  休眠1s目前  暂时稳定
                    time.sleep(pre_url_or_email_sleep)
                    # 每个url解析email
                    self.extractOnlyUrl(result,key_index,key,thread_number)

                    url = result.split("/")
                    try:
                        tmp = url[0] + "//" + url[2]
                    except Exception as e:
                        tmp = url[0] + "//" + url[2]
                    if tmp not in self.totlc_url_res:
                        tmp = self.filter_email(tmp)
                        if tmp:
                            try:
                                logger("线程：{}：正采集第{}词：{},Url为:【{}】:{}".format(thread_number,key_index, key,url_count, tmp), color="")
                                self.totlc_url_res.add(tmp)
                                self.write_to_excel(file_path, 0, url_count, 0, tmp)
                                url_count += 1
                                if url_count != 0 and url_count % number_of_url_will_sleep == 0:
                                    # logger("休眠60s中")
                                    time.sleep(10)
                            except Exception as e:
                                logger("异常信息：{}".format(e))
                if current_url_count==url_count:
                    logger("线程：{}：爬取第{}个关键词：{},未获取到信息，已重新爬取！！".format(thread_number, key_index, key))
                    key_queue.put(key)
                    continue
                logger("线程：{}：爬取第{}个关键词：{},爬取完毕！！".format(thread_number,key_index, key))
                logger("线程：{}:sleep:{}".format(thread_number,time_wait))
                config_parser.set("default", "start_keyword_index", str(key_index))
                config_parser.write(open("config.cfg", 'w'))
                time.sleep(time_wait)
                # key_count+=1
                key_index = key_count

        except BaseException as e:
            logger("url异常信息：{}".format(e))
            logger("线程：{}：爬取速度过快，休眠中.....休眠时间为:{}".format(thread_number,time_sleep_on_sealing_ip))
            try:
                send = SendEmail()
                content = "线程{}:当前爬取第{}个关键词遇到异常：{}，正在休眠等待重启".format(thread_number,key_index,e)
                send.send_text(user_list,"爬虫封ip警告",content)
            except Exception as e :
                logger("发邮件失败;{}".format(e))
            time.sleep(time_sleep_on_sealing_ip)
            self.spider(key_queue,key_index)

    def main(self):
        global start_keyword_index, res_set
        logger("当前已爬关键词数量：{}".format(start_keyword_index))
        logger("当前已有url数量：{}".format(self.url_count))
        logger("当前已有email数量：{}".format(self.email_count))

        key_len = self.opExcel.get_nrows()
        logger("关键词总数：{}".format(key_len))
        self.generate_keywords_queue()

        threads = []
        for i in range(thread_num):
            thread = threading.Thread(target=self.spider, args=(self.keyword_queue,i))
            threads.append(thread)

        for one in threads:
            one.start()
        for one in threads:
            one.join()


def main():
    spider = Spider()
    spider.main()


if __name__ == '__main__':
    config_parser = ConfigParser()
    config_parser.read('config.cfg')
    config = config_parser['default']
    file_path = config['google_datas']
    email_path = config['google_email']
    time_wait = int(config['time_wait'])
    thread_num = int(config["thread_num"])
    default_add_keyword = config["default_add_keyword"]
    pre_url_or_email_sleep = int(config["pre_url_or_email_sleep"])
    time_sleep_on_sealing_ip = int(config["time_sleep_on_sealing_ip"])
    start_keyword_index = int(config["start_keyword_index"])
    target_spider_keyword_number = int(config["target_spider_keyword_number"])
    send_userlist = config["send_userlist"]

    number_of_url_will_sleep = 50
    user_list = send_userlist.split(",")
    print(user_list)
    logger(time.ctime())
    main()

    # 避免窗口退出
    logger("采集完毕")
    while 1:
        pass

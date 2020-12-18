# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

import poplib, email, telnetlib
import datetime, time, sys, traceback
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import imaplib


def logger(msg):
    """
    日志信息
    """
    now = time.ctime()
    print("[%s] %s" % (now, msg))


class down_email():

    def __init__(self, user, password, eamil_server):
        # 输入邮件地址, 口令和POP3服务器地址:
        self.user = user
        # 此处密码是授权码,用于登录第三方邮件客户端
        self.password = password
        self.pop3_server = eamil_server
        self.count = 0
        self.totle_set = None  # 邮件去重

    # 获得msg的编码
    def guess_charset(self, msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    # 获取邮件内容
    def get_content(self, msg):
        content = ""
        content_type = msg.get_content_type()
        # print('content_type:',content_type)
        if content_type == 'text/plain':  # or content_type == 'text/html'

            content = msg.get_payload(decode=True)
            # print("这是未解析正文", content)
            charset = self.guess_charset(msg)
            if charset:
                # print("编码格式",charset)
                # print("这是正文", content)
                content = content.decode(charset)
            else:
                content = content.decode("unicode-escape")
        elif content_type == 'multipart/alternative':
            pass
        else:
            filename = msg.get_filename()  # 得到附件的文件名
            if filename:
                print("file", filename)
                # 将附件下载（写入）本地磁盘文件
                with open(filename, 'wb') as f:
                    f.write(msg.get_payload(decode=True))
        return content

    # 字符编码转换
    # @staticmethod
    def decode_str(self, str_in):
        value, charset = decode_header(str_in)[0]
        if charset:
            value = value.decode(charset)
        return value

    # 解析邮件,获取内容
    def get_att(self, msg_in):
        result = []
        for part in msg_in.walk():
            # 是文本内容
            content = self.get_content(part)

            if content:
                content.replace("\n"," ")
                result.append(content)
        return ",".join(result)

    def run_ing(self, users, second):
        try:
            # telnetlib.Telnet(self.pop3_server, 995)
            self.server = poplib.POP3(self.pop3_server, 110, timeout=10)
        except:

            self.server = poplib.POP3(self.pop3_server, 110, timeout=10)

        # 打印POP3服务器的欢迎文字:
        print("身份验证成功，下面为测试输出：{}".format(self.server.getwelcome().decode('utf-8')))
        # 身份认证:
        self.server.user(self.user)
        self.server.pass_(self.password)
        # 返回邮件数量和占用空间:
        logger('邮件总数: %s. 大小: %s' % self.server.stat())

        # list()返回所有邮件的编号:
        resp, mails, octets = self.server.list()
        # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]


        index = [i for i in range(self.count + 1, len(mails) + 1)]
        self.count = len(mails)

        for i in index:  # 倒序遍历邮件

            # for i in range(1, index + 1):# 顺序遍历邮件
            resp, lines, octets = self.server.retr(i)
            # lines存储了邮件的原始文本的每一行,
            # 邮件的原始文本:
            try:
                msg_content = b'\r\n'.join(lines).decode('gb2312')
            except Exception as  e:
                msg_content = b'\r\n'.join(lines).decode('utf-8')

            msg = Parser().parsestr(msg_content)
            try:
                From = parseaddr(msg.get('From'))[1]
                To = parseaddr(msg.get('To'))[1]
                Cc = parseaddr(msg.get_all('Cc'))[1]  # 抄送人
                Subject = self.decode_str(msg.get('Subject'))


                # 邮件时间格式转换
                d = msg.get("Date")
                if not d:
                    continue
                date1 = time.strptime(d[0:24], '%a, %d %b %Y %H:%M:%S')
                now_date = datetime.datetime(date1.tm_year, date1.tm_mon, date1.tm_mday)

                # 获取指定日期内的邮件
                if start_date<=now_date<=end_date:
                    content = self.get_att(msg)
                    if len(users)>0:
                        if From in users:
                            with open(txt,"a+") as f:
                                f.write("发送时间：{}\n".format(now_date))
                                f.write("发件人:{}\n".format(From))
                                f.write("收件人:{}\n".format(To))
                                f.write("抄送人:{}\n".format(Cc))
                                f.write("主题:{}\n".format(Subject))
                                f.write("内容：{}\n".format(content))
                                f.write("-"*20+"\n")
                                f.write("\n")

                            print('发件人:%s,收件人:%s,抄送人:%s,主题:%s' % (From, To, Cc, Subject))
                    else:
                        with open(txt, "a+") as f:
                            f.write("发送时间：{}\n".format(now_date))
                            f.write("发件人:{}\n".format(From))
                            f.write("收件人:{}\n".format(To))
                            f.write("抄送人:{}\n".format(Cc))
                            f.write("主题:{}\n".format(Subject))
                            f.write("内容：{}\n".format(content))
                            f.write("-" * 20 + "\n")
                            f.write("\n")

                        print('发件人:%s,收件人:%s,抄送人:%s,主题:%s' % (From, To, Cc, Subject))

            except Exception as e:
                print(e, "解析错误")
                return None

        # 可以根据邮件索引号直接从服务器删除邮件:
        # self.server.dele(7)

        # 退出 不然会锁死
        self.server.quit()


if __name__ == '__main__':
    # 邮件保存的路径
    txt = "email.txt"


    user = '1456543127@qq.com'
    password = 'zyvjsnovvqiyiggc'

    start_date = datetime.datetime(2020, 3, 18)  # 起始时间
    end_date = datetime.datetime(2020, 12, 19)  # 结束时间

    # 设置只收取指定发件人的邮件  为空时默认接收所有邮件
    # users = []
    users = ['1364826576@qq.com']
    # 刷新时间间隔
    time_s = 1

    eamil_server = 'pop.qq.com'
    email_class = down_email(user=user, password=password, eamil_server=eamil_server)


    content = email_class.run_ing(users, time_s)
    time.sleep(time_s)

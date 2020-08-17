# @Time    : 2020/8/17 8:59
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm

import cv2
import os
from tqdm import tqdm
import time
import datetime
import smtplib  # 发送邮件 连接邮件服务器
from email.mime.text import MIMEText  # 构建邮件格式
from email.mime.multipart import MIMEMultipart  # 发送多个部分
from email.mime.application import MIMEApplication  # 发送附件


def logger(msg):
    print("{}:---{}".format(time.ctime(),msg))


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
def main(times,send_dict):

    while True:
        # 判断是周几
        today=int(time.strftime("%w"))

        # 周六日不发送
        if today==6 or today==7:
            logger("当前是周：{}".format(today))
            continue
        # 小时
        hour = str(time.strftime("%H"))
        # 分钟
        minte = str(time.strftime("%M"))
        for one in times:
            need_hour = one[0]
            need_mintus = one[1]
            if hour==need_hour and minte==need_mintus:
                logger("{}：{}发送邮件".format(hour,minte))
                send = SendEmail()

                for userlist,files in send_dict.items():
                    for file in files:
                        with open(file,encoding="utf-8") as f:
                            data = f.readlines()
                            data = "".join(data)
                            send.send_text(userlist,data,data)
                            logger("发送给{}：{}成功".format(userlist,data))
                time.sleep(60)
            else:
                logger("{}:{} 不在发送时间".format(need_hour,need_mintus))
                time.sleep(5)

if __name__ == '__main__':
    root_dir = "./txt"  # 不用管  往里面放txt就行
    times = [["01","20"],["02","10"],["09","39"],["18","34"]]  # 意思是1点20发一次  2点10分发一次  自己按格式往后加
    send_dict= {
            "1364826576@qq.com":["./txt/1.txt","./txt/2.txt"],
            "1410000000@qq.com": ["./txt/1.txt"],
            } #指定收件人

    main(times,send_dict)
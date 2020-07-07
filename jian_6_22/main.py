# @Time    : 2020/6/22
# @Author  : Libuda
# @FileName: test.py
# @Software: PyCharm
from PyQt5 import  QtCore,QtGui,QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.append("./")
from report import SecondWindow

# 布局加部件 部件设置布局

current_user=""
current_pwd = ""
class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        global current_user,current_pwd
        super(Mywindow, self).__init__()
        self.setFixedSize(400,200)
        # 定义主布局 主窗口部件 并设置为网格布局
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.title = QtWidgets.QLabel("程序设计基础-python")
        self.username = QtWidgets.QLabel("用户名：")
        self.password = QtWidgets.QLabel("密码：")
        self.input_user =  QtWidgets.QTextEdit()
        self.input_password =  QtWidgets.QTextEdit()
        self.register_btn = QtWidgets.QPushButton("注册")
        self.login_btn = QtWidgets.QPushButton("登录")
        self.cancy_btn = QtWidgets.QPushButton("取消")


        self.main_layout.addWidget(self.title,0,1,1,4)
        self.main_layout.addWidget(self.username,1,1,1,1)
        self.main_layout.addWidget(self.password,2,1,1,3)
        self.main_layout.addWidget(self.input_user,1,2,1,5)
        self.main_layout.addWidget(self.input_password,2,2,1,5)
        self.main_layout.addWidget(self.register_btn,6,1,1,1)
        self.main_layout.addWidget(self.login_btn,6,3,1,1)
        self.main_layout.addWidget(self.cancy_btn,6,6,1,1)

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.register_btn.clicked.connect(self.register)
        self.login_btn.clicked.connect(self.login)

        self.cancy_btn.clicked.connect(self.cancy)

    def register(self):
        user_name = self.input_user.toPlainText()
        password = self.input_password.toPlainText()
        if user_name=="" or password=="":
            QMessageBox.information(self, "错误提示", "请输入用户名和密码")
        else:
            with open("user.txt") as f:
                lines = f.readlines()

            for line in lines:
                data = line.split()
                usr = data[0]
                if user_name==usr:
                    QMessageBox.information(self, "错误提示", "用户名已存在！",)
                    return
                else:
                    continue
            with open("user.txt","a+") as f:
                f.write(user_name+"\t"+password+"\n")
            QMessageBox.information(self, "注册成功", "注册成功！")

    def login(self):
        flag = False
        user_name = self.input_user.toPlainText()
        password = self.input_password.toPlainText()
        if user_name=="" or password=="":
            QMessageBox.information(self, "错误提示", "请输入用户名和密码")
        else:
            with open("user.txt") as f:
                lines = f.readlines()
            for line in lines:
                data = line.split()
                usr = data[0]
                pwd = data[1]
                if user_name==usr:
                    if  pwd==password:
                        QMessageBox.information(self, "登录成功", "登录成功！")
                        flag = True

                        with open("current_user.txt","w") as f:
                            f.write(user_name+"\t"+password)
                        # print(current_user,current_pwd)
                        self.close()
                        self.w2 = SecondWindow()
                        self.w2.show()


                    else:
                        QMessageBox.information(self, "登录错误", "密码错误！")
                        flag = True

            if not flag:
                QMessageBox.information(self, "登录错误", "用户名不存在！")


    def cancy(self):
        self.input_user.setText("")
        self.input_password.setText("")





def report_show():
    global current_user,current_pwd
    print(current_pwd)

    w2 = SecondWindow()
    w2.show()
    w2.exec_()


if __name__ == '__main__':
    # 定义Qapplication应用程序
    app = QtWidgets.QApplication(sys.argv)
    w = Mywindow()
    w.show()
    sys.exit(app.exec_())



from PyQt5 import  QtCore,QtGui,QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        with open("current_user.txt") as f:
            lines = f.readlines()
        line = lines[-1].split()
        self.username= line[0]
        self.pwd = line[1]

        self.setFixedSize(800,500)
        # 定义主布局 主窗口部件 并设置为网格布局
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.title = QtWidgets.QLabel("个人一寸照片展示")
        self.info = QtWidgets.QLabel(self.username+"+"+self.pwd)
        self.label = QtWidgets.QLabel("学习报告")
        self.text =  QtWidgets.QTextEdit("")

        self.img = QtWidgets.QLabel()

        pixmap =  QPixmap('1.png')  # 按指定路径找到图片
        self.img.setPixmap (pixmap)  # 在label上显示图片
        self.img.setScaledContents(True)  # 让图片自适应label大小

        self.main_layout.addWidget(self.title,0,1,1,1)
        self.main_layout.addWidget(self.info,1,1,1,1)
        self.main_layout.addWidget(self.label,2,1,1,1)
        self.main_layout.addWidget(self.img,0,5,3,3)
        self.main_layout.addWidget(self.text,3,1,10,10)


        self.setCentralWidget(self.main_widget)  # 设置窗口主部件



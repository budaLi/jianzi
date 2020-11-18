# @Time    : 2020/11/18 14:33
# @Author  : Libuda
# @FileName: filter.py
# @Software: PyCharm

from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import sys
import os
import numpy as np



class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):

        super(DisplayImageWidget, self).__init__(parent)

        # 禁止最大化
        self.setWindowFlag(
            QtCore.Qt.WindowMinimizeButtonHint
            # QtCore.Qt.WindowCloseButtonHint)
        )
        self.setWindowTitle("谷歌 Email url 采集工具 V1.0  -by  李不搭")
        self.main_title = QtWidgets.QLabel("谷歌数据采集系统")
        self.search_bth  = QtWidgets.QPushButton("搜索")
        self.config_info_label = QtWidgets.QLabel("配置信息")
        self.url_label = QtWidgets.QLabel("url")
        self.email_label = QtWidgets.QLabel("email")
        self.keyword_import_btn = QtWidgets.QPushButton("导入关键词")

        self.thread_number_label = QtWidgets.QLabel("线程数：")
        self.thread_number_text = QtWidgets.QTextEdit("5")

        self.sleep_time_label = QtWidgets.QLabel("休眠时间(s)：")
        self.sleep_time_text = QtWidgets.QTextEdit("5")

        self.sleep_time_when_f_label = QtWidgets.QLabel("反爬时线程休眠时间(s)：")
        self.sleep_time__when_f_text = QtWidgets.QTextEdit("5")

        self.url_table = QtWidgets.QTableWidget(4,3)
        data = QtWidgets.QTableWidgetItem()
        data.setText("11111")
        self.url_table.setItem(1,1,data)

        self.email_table = QtWidgets.QTableWidget(4,3)
        data = QtWidgets.QTableWidgetItem("sss")
        self.email_table.setItem(1,1,data)


        self.layout = QtWidgets.QGridLayout()

        self.layout.addWidget(self.main_title,0,1,1,1)
        self.layout.addWidget(self.search_bth,0,2,1,1)
        self.layout.addWidget(self.config_info_label,1,1,1,1)
        self.layout.addWidget(self.url_label,1,2,1,1)
        self.layout.addWidget(self.email_label,1,3,1,1)

        self.layout.addWidget(self.url_table,2,2,1,1)
        self.layout.addWidget(self.email_table,2,3,1,1)
        # self.layout.addWidget(self.next_btn,2,2,1,1)
        # self.layout.addWidget(self.pose_pitch,3,1,1,1)
        # self.layout.addWidget(self.pose_yaw,4,1,1,1)
        # self.layout.addWidget(self.pose_roll,5,1,1,1)
        # self.layout.addWidget(self.text, 6, 2, 1, 1)
        # self.layout.addWidget(self.tips,6,1,1,1)
        self.setLayout(self.layout)

        # self.image_frame.setFixedSize(self.img_size,self.img_size)
        # self.image_frame.setStyleSheet('border-width: 1px;border-style: solid; border - color: rgb(255, 170, 0);background - color: rgb(100, 149, 237);')
        # self.pic_btn.clicked.connect(self.click_choice_dir)
        # self.previous_btn.clicked.connect(self.previous_img)
        # self.next_btn.clicked.connect(self.next_img)
        # self.save_btn.clicked.connect(self.save)

    def click_choice_dir(self):
        # dir_path = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "")
        txt_path = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)") #('E:/桌面/facepp-python-sdk-master/out/list.txt', 'All Files (*)')
        # print(txt_path)
        self.landmark_txt_to_array(txt_path[0])
        self.show_image()





if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)

        display_image_widget = DisplayImageWidget()
        # 全屏
        # display_image_widget.showFullScreen()

        display_image_widget.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
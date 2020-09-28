# @Time    : 2020/9/19 13:33
# @Author  : Libuda
# @FileName: filter.py
# @Software: PyCharm
import requests
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, pyqtSignal
import cv2
import sys
import os
import numpy as np
import json
import urllib
from queue import Queue
import  shutil




class Spider:
    """
    妹子图爬虫   http://mzitu.icu/
    """
    def __init__(self):
        self.url = "http://mapi.ibayeux.com/v1/airticle/?offset={}"
        self.user_agent = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"

    def download(self):
        response =  requests.get(self.url).json()
        result = response["results"]
        for one in result:
            title = one["title"]
            imgs_content = eval(one["content"])
            path = one["path"]
            for _img in imgs_content:
                img_url = path+"/"+_img
                img = requests.get(img_url)
                p = "./img/"+_img
                with open(p, 'wb') as file:
                    file.write(img.content)

class ShowGirl(QtWidgets.QWidget):
    def __init__(self,parent=None):

        super(ShowGirl, self).__init__(parent)

        # s = Spider()
        # s.download()
        self.img_queue = Queue()

        files = os.listdir("./img")
        for file in files:
            p = "./img/"+file
            self.img_queue.put(p)

        self.img_index = 0
        # 禁止最大化
        self.setWindowFlag(
            QtCore.Qt.WindowMinimizeButtonHint
            # QtCore.Qt.WindowCloseButtonHint)
        )
        self.setWindowTitle("宅男福利-V1.0")
        self.img_size = 224


        self.origin_imgs_paths = []  # 原图列表


        self.before_score = []
        self.after_score = []


        self.origin_frame = QtWidgets.QLabel()
        self.origin_frame_label = QtWidgets.QLabel("")

        # self.previous_btn = QtWidgets.QPushButton("上一张")
        # self.next_btn = QtWidgets.QPushButton("下一张")


        self.layout = QtWidgets.QGridLayout()

        self.layout.addWidget(self.origin_frame,0,0,1,1)
        # self.layout.addWidget(self.origin_frame_label,1,0,1,1)
        # self.layout.addWidget(self.previous_btn,1,0,1,1)
        # self.layout.addWidget(self.next_btn,2,0,1,1)


        self.setLayout(self.layout)

        self.origin_frame.setFixedSize(self.img_size,self.img_size)
        self.origin_frame.setStyleSheet('border-width: 1px;border-style: solid; border - color: rgb(255, 170, 0);background - color: rgb(100, 149, 237);')

        # self.previous_btn.clicked.connect(self.previous_img)
        # self.next_btn.clicked.connect(self.next_img)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.show_image)
        self.timer1.start(2000)
        # self.show()

    ## 读取图像，解决imread不能读取中文路径的问题
    def _cv_imread(self,file_path):
        try:
            cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        except Exception as e:
            print(e)

    def previous_img(self):
        """
        前一张图片
        :return:
        """
        if self.img_index>0:
            self.img_index -=1
            self.tips.setText("")
        else:
            self.img_index =0
            self.tips.setText("已是第一张图片")

        self.show_image()

    def next_img(self):
        """
        下一张图片
        :return:
        """
        if self.img_index<len(self.origin_imgs_paths)-1:
            self.img_index+=1
            self.tips.setText("")
        else:
            self.img_index=len(self.origin_imgs_paths)-1
            self.tips.setText("已是最后一张图片")

        self.show_image()


    def show_image(self):
        if not self.img_queue.empty():
            path = self.img_queue.get()
            self.origin_image =self._cv_imread(path)
            self.origin_image = cv2.resize(self.origin_image,(self.img_size,self.img_size))


            self.origin_image = QtGui.QImage(self.origin_image.data.tobytes(), self.origin_image.shape[1], self.origin_image.shape[0],self.origin_image.shape[1]*3, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.origin_frame.setPixmap(QtGui.QPixmap.fromImage(self.origin_image))

            # shutil.rmtree(path)



if __name__ == '__main__':

    try:
        app = QtWidgets.QApplication(sys.argv)

        display_image_widget = ShowGirl()
        # 全屏
        # display_image_widget.showFullScreen()

        display_image_widget.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


# @Time    : 2020/6/11 17:45
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Mywindow(QWidget):
    def __init__(self,parent=None,**kwargs):
        super(Mywindow, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle("结课报告-admin")
        self.setWindowIcon(QIcon("./icon.jpg"))
        self.label1 = QLabel("个人一寸照片展示")
        self.label2 = QLabel("学号+姓名")
        self.image = QImage("./1.jpg")
        self.grid = QGridLayout()
        self.grid.addWidget(self.label1,1,2)
        self.grid.addWidget(self.label2,2,2)
        # self.grid.addWidget(self.image,3,1)

        self.setLayout(self.grid)
        self.resize(400,200)

if __name__ == '__main__':
    window = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    sys.exit(window.exec_())
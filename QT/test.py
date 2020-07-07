# @Time    : 2020/6/12 9:51
# @Author  : Libuda
# @FileName: test.py
# @Software: PyCharm
from PyQt5 import  QtCore,QtGui,QtWidgets
import sys


# 布局加部件 部件设置布局


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setFixedSize(800,400)
        # 定义主布局 主窗口部件 并设置为网格布局
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # 左侧部件 网格布局
        self.left_widget = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        # 退出按钮
        self.exit_btn = QtWidgets.QPushButton()
        self.left_label_1 = QtWidgets.QPushButton("每日推荐")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')


        self.left_layout.addWidget(self.exit_btn,0,1,1,1)
        self.left_layout.addWidget(self.left_label_1,1,1,1,1)
        self.left_layout.addWidget(self.left_label_2,2,1,1,1)
        self.left_layout.addWidget(self.left_label_3,3,1,1,1)


        # 右侧部件 网格布局
        self.right_widget =QtWidgets.QWidget()
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("可馨HANM")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('./r1.jpg'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.right_layout.addWidget(self.recommend_button_1,1,2,1,5)

        # 布局添加部件
        self.main_layout.addWidget(self.left_widget,0,0,1,5)
        self.main_layout.addWidget(self.right_widget,0,1,1,10)

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件






if __name__ == '__main__':
    # 定义Qapplication应用程序
    app = QtWidgets.QApplication(sys.argv)
    w = Mywindow()
    w.show()
    sys.exit(app.exec_())



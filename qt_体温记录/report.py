# @Time    : 2020/6/22 19:54
# @Author  : Libuda
# @FileName: report.py
# @Software: PyCharm
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.main_widget =  QtWidgets.QWidget()
        self.main_widget.setFixedSize(800,500)
        self.layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.layout)
        self.querry_user_label = QLabel("请输入用户名")
        self.querry_user = QLineEdit()
        self.querry_tiwen_label = QLabel("请输入体温")
        self.querry_tiwen = QLineEdit()
        self.querry_btn = QPushButton("查询")
        self.table =QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(6)
        self.layout.addWidget(self.querry_user_label, 0, 0,1,1)
        self.layout.addWidget(self.querry_user, 0,1,1,1)
        self.layout.addWidget(self.querry_tiwen_label,0,2,1,1)
        self.layout.addWidget(self.querry_tiwen,0,3,1,1)
        self.layout.addWidget(self.querry_btn,0,4,1,1)
        self.layout.addWidget(self.table, 1, 0,5,5)
        self.table.setHorizontalHeaderLabels(['姓名', '性别', '年龄', '联系方式',"体温","是否有城际移动"])

        # self.table.setItem(0, 0, QTableWidgetItem(self.led.text()))

        self.table.itemChanged.connect(self.table_update)
        self.setCentralWidget(self.main_widget)

    def table_update(self):
        row_select = self.table.selectedItems()
        if len(row_select)==0:
            return
        print("选择长度",len(row_select))
        col  = self.table.currentColumn()
        row = self.table.currentRow()
        # comBox = QComboBox()
        # if col==0:
        #     comBox.addItems(['男', '女'])
        #     comBox.addItem('未知')
        #     comBox.setStyleSheet('QComboBox{margin:3px}')
        #     self.table.setCellWidget(row, col+1, comBox)
        # print(comBox.currentText())
        print(row,col)
        data = row_select[0].text()
        print(data)

    def querry(self):
        user = self.querry_user.text()
        tiwen = self.querry_tiwen.text()
        if user=="" and tiwen=="":
            QMessageBox.information(self,"查询","请输入用户名或体温查询")
        elif user!="" and tiwen!="":
            # 查询
            pass
        elif user=="":
            # 查体温
            pass
        else:
            pass


if __name__ == '__main__':
    # 定义Qapplication应用程序
    app = QtWidgets.QApplication(sys.argv)
    w = SecondWindow()
    w.show()
    sys.exit(app.exec_())



# @Time    : 2020/8/19 13:33
# @Author  : Libuda
# @FileName: filter.py
# @Software: PyCharm

from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import sys
import os
import numpy as np


res_txt_path = "res.txt"
api_txt_paht  = "api.txt"
age_map = { "幼儿":[1,0,0,0,0],"青少年":[0,1,0,0,0], "青年":[0,0,1,0,0],"中年":[0,0,0,1,0], "老年":[0,0,0,0,1],}
sex_map = { "男性":0, "女性":1}
hat_map = { "无帽":0, "有帽":1}
mask_map = { "无口罩": 0, "戴口罩": 1,"不确定": 2,}
glass_map = { "戴眼镜": 1,"无眼镜": 0,"不确定": 2}
bag_map= { "无背包": 0, "有包": 1,"不确定": 2}
viewpoints_map = {"正面":[1,0,0,0],"背面":[0,1,0,0],"左面":[0,0,1,0],"右面":[0,0,0,1]}
#需求中 黑、白、灰、红、蓝、黄、橙、棕、绿、紫、粉、银、花色
up_color_map = {"红":3,"橙":6,"黄":5,"绿":8,"蓝":4,"紫":9,"粉":10,"黑":0,"白":1,"灰":2,"棕":7,"未知":12}
lower_color_map = {"红":3,"橙":6,"黄":5,"绿":8,"蓝":4,"紫":9,"粉":10,"黑":0,"白":1,"灰":2,"棕":7,"不确定":12}

def trans_dict(dict):
    new_dict={}
    for key,value in dict.items():
        if isinstance(value,list):
            value = tuple(list(map(str,value)))
        else:
            value = str(value)
        new_dict[value]= key
    return new_dict

def trans_color(color_map,color_list):

    res=""
    color_map = trans_dict(color_map)

    for index,one in enumerate(color_list):
        if one=="1":
            res+=color_map[str(index)]+" "

    return res

age_map = trans_dict(age_map)
sex_map = trans_dict(sex_map)
hat_map = trans_dict(hat_map)
mask_map = trans_dict(mask_map)
glass_map = trans_dict(glass_map)
bag_map = trans_dict(bag_map)
viewpoints_map = trans_dict(viewpoints_map)


class DisplayImageWidget(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(DisplayImageWidget, self).__init__(parent)

        # 禁止最大化
        self.setWindowFlag(
            QtCore.Qt.WindowMinimizeButtonHint
            # QtCore.Qt.WindowCloseButtonHint)
        )
        self.setWindowTitle("行人属性过滤工具-V1.0")
        self.img_size = 500
        self.img_path_list= []  # 图片路径
        self.gt_attr= []  # RAP
        self.pre_attr= []  # 百度api
        self.img_index = 0
        self.pic_btn = QtWidgets.QPushButton('Start')
        self.image_frame = QtWidgets.QLabel()

        self.img_name_label =  QtWidgets.QLabel("当前图片：{}")
        self.previous_btn = QtWidgets.QPushButton("上一张")
        self.next_btn = QtWidgets.QPushButton("下一张")
        self.tips = QtWidgets.QLabel("RAPv2  vs API")
        self.text = QtWidgets.QLabel("0/0")
        self.age = QtWidgets.QLabel("年龄：{}/{}")
        self.sex = QtWidgets.QLabel("性别：{}/{}")
        self.hat = QtWidgets.QLabel("帽子：{}/{}")
        self.mask = QtWidgets.QLabel("口罩：{}/{}")
        self.glass = QtWidgets.QLabel("眼镜：{}/{}")
        self.bag = QtWidgets.QLabel("背包：{}/{}")
        self.up_color = QtWidgets.QLabel("上衣颜色：{}/{}")
        self.low_color = QtWidgets.QLabel("下衣颜色：{}/{}")
        self.viewpoint = QtWidgets.QLabel("角度：{}/{}")

        self.layout = QtWidgets.QGridLayout()

        self.layout.addWidget(self.pic_btn,0,0,1,1)
        self.layout.addWidget(self.image_frame,1,0,10,1)

        self.layout.addWidget(self.img_name_label,1,1,1,1)
        self.layout.addWidget(self.tips,0,1,1,1)
        self.layout.addWidget(self.previous_btn,2,1,1,1)
        self.layout.addWidget(self.next_btn,2,2,1,1)

        self.layout.addWidget(self.age,3,1,1,1)
        self.layout.addWidget(self.sex,4,1,1,1)
        self.layout.addWidget(self.hat,5,1,1,1)
        self.layout.addWidget(self.mask, 6, 1, 1, 1)
        self.layout.addWidget(self.glass, 7, 1, 1, 1)
        self.layout.addWidget(self.bag,8,1,1,1)
        self.layout.addWidget(self.up_color,9,1,1,1)
        self.layout.addWidget(self.low_color,10,1,1,1)
        self.layout.addWidget(self.viewpoint,11,1,1,1)
        self.setLayout(self.layout)

        self.image_frame.setFixedSize(self.img_size,self.img_size)
        self.image_frame.setStyleSheet('border-width: 1px;border-style: solid; border - color: rgb(255, 170, 0);background - color: rgb(100, 149, 237);')
        self.pic_btn.clicked.connect(self.click_choice_dir)
        self.previous_btn.clicked.connect(self.previous_img)
        self.next_btn.clicked.connect(self.next_img)


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
        if self.img_index<len(self.img_path_list)-1:
            self.img_index+=1
            self.tips.setText("")
        else:
            self.img_index=len(self.img_path_list)-1
            self.tips.setText("已是最后一张图片")

        self.show_image()


    def click_choice_dir(self):
        gt_file_lines = []
        gt_imgs = []
        with open(res_txt_path) as res_file:
            res_file_lines = res_file.readlines()
            for idx,line in enumerate(res_file_lines):
                line = line.strip().split(" ")
                gt_imgs.append(line[0])
                gt_file_lines.append(line[1:])

        with open(api_txt_paht) as api_file:
            lines = api_file.readlines()
            for idx,line in enumerate(lines):
                line = line.strip().split(" ")
                if line[0]!=gt_imgs[idx]:
                    continue
                img = r"E:\桌面\工作算法\rap2.0\RAP_dataset\{}".format(line[0])
                if "1" not in gt_file_lines[idx][29]:
                    continue
                self.img_path_list.append(img)
                self.pre_attr.append(line[1:])
                self.gt_attr.append(gt_file_lines[idx])
        self.show_image()



    def show_image(self):
        self.image =self._cv_imread(self.img_path_list[self.img_index])

        # 适当放大看的更清楚
        self.image = cv2.resize(self.image,(self.img_size,self.img_size))
        # print(self.image.shape[1], self.image.shape[0])
        try:
            gt_age = age_map[tuple(self.gt_attr[self.img_index][:5])]
            pre_age = age_map[tuple(self.pre_attr[self.img_index][:5])]
            # if pre_age!="幼儿":
            #     self.img_index+=1
            #     self.show_image()

            self.tips.setText("RAPv2  vs API")
            self.image = QtGui.QImage(self.image.data.tobytes(), self.image.shape[1], self.image.shape[0],self.image.shape[1]*3, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
            self.text.setText("标注数据：{}/{}".format(self.img_index + 1, len(self.img_path_list)))

            self.img_name_label.setText("当前图片：{}".format(self.img_path_list[self.img_index].split("/")[-1]))


            self.age.setText("年龄：{}/{}".format(gt_age,pre_age))

            gt_sex = sex_map[self.gt_attr[self.img_index][5]]
            pre_sex= sex_map[self.pre_attr[self.img_index][5]]
            self.sex.setText("性别：{}/{}".format(gt_sex,pre_sex))

            gt_hat = hat_map[self.gt_attr[self.img_index][6]]
            pre_hat= hat_map[self.pre_attr[self.img_index][6]]
            self.hat.setText("帽子：{}/{}".format(gt_hat,pre_hat))

            gt_mask = mask_map[self.gt_attr[self.img_index][7]]
            pre_mask = mask_map[self.pre_attr[self.img_index][7]]
            self.mask.setText("口罩：{}/{}".format(gt_mask,pre_mask))

            gt_glass = glass_map[self.gt_attr[self.img_index][8]]
            pre_glass = glass_map[self.pre_attr[self.img_index][8]]
            self.glass.setText("眼镜：{}/{}".format(gt_glass,pre_glass))

            gt_bag = bag_map[self.gt_attr[self.img_index][9]]
            pre_bag= bag_map[self.pre_attr[self.img_index][9]]
            self.bag.setText("背包：{}/{}".format(gt_bag,pre_bag))

            gt_upcolor = trans_color(up_color_map,self.gt_attr[self.img_index][10:23])
            pre_upcolor = trans_color(up_color_map,self.pre_attr[self.img_index][10:23])
            self.up_color.setText("上衣颜色：{}/{}".format(gt_upcolor,pre_upcolor))

            gt_lower_color = trans_color(lower_color_map,self.gt_attr[self.img_index][23:36])
            pre_lower_color = trans_color(lower_color_map,self.pre_attr[self.img_index][23:36])


            self.low_color.setText("下衣颜色：{}/{}".format(gt_lower_color,pre_lower_color))

            gt_viewpoint = viewpoints_map[tuple(self.gt_attr[self.img_index][36:40])]
            pre_viewpoint = viewpoints_map[tuple(self.pre_attr[self.img_index][36:40])]
            self.viewpoint.setText("角度：{}/{}".format(gt_viewpoint,pre_viewpoint))

        except Exception as e:
            print(e)



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
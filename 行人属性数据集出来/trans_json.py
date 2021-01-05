# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
import json
import os


age_map = { "幼儿":[1,0,0,0,0],"青少年":[0,1,0,0,0], "青年":[0,0,1,0,0],"中年":[0,0,0,1,0], "老年":[0,0,0,0,1],}
sex_map = { "男性":0, "女性":1}
hat_map = { "无帽":0, "普通帽":1, "安全帽":1,}
mask_map = { "无口罩": 0, "戴口罩": 1,"不确定": 2,}
glass_map = { "戴眼镜": 1, "戴墨镜": 1,"无眼镜": 0,"不确定": 2}
bag_map= { "无背包": 0, "单肩包": 1,"双肩包": 1,"不确定": 2}
color_map = {}
viewpoints_map = {"正面":[1,0,0,0],"背面":[0,1,0,0],"左侧面":[0,0,1,0],"右侧面":[0,0,0,1]}

#需求中 黑、白、灰、红、蓝、黄、橙、棕、绿、紫、粉、银、花色
up_color_map = {"红":3,"橙":6,"黄":5,"绿":8,"蓝":4,"紫":9,"粉":10,"黑":0,"白":1,"灰":2,"棕":7}
lower_color_map = {"红":3,"橙":6,"黄":5,"绿":8,"蓝":4,"紫":9,"粉":10,"黑":0,"白":1,"灰":2,"棕":7,"不确定":12}

for key,value in up_color_map.items():
    new_value= [0 for i in range(13)]
    new_value[value]=1
    up_color_map[key] = new_value
for key,value in lower_color_map.items():
    new_value= [0 for i in range(13)]
    new_value[value]=1
    lower_color_map[key] = new_value

new_data = []

def check_equal(target,pre):
    if isinstance(pre,list):
        pre = list(map(str,pre))
    elif isinstance(pre,int):
        pre = str(pre)
    if  target==pre:
        return 1
    return 0
error_couynt =0
totle_res = []
with open("rapv2_12_25.txt") as f:
    lines = f.readlines()
    for index,line in enumerate(lines):

        line = line.split()
        img = line[0].split(".")[0]
        gt_age = line[1:6]
        gt_sex = line[6]
        gt_hs_hat = line[7]
        gt_hs_mask = line[8]
        gt_hs_glass = line[9]
        gt_hs_bag = line[10]
        gt_up_color_str = line[11:24]
        gt_lower_color_str = line[24:37]
        gt_viewpoints_str = line[37:41]
        res_json_file = r"D:\行人属性数据\res_json_file\{}.json".format(img)
        if os.path.isfile(res_json_file):
            with open(res_json_file,'r') as load_f:
                res = json.load(load_f)[0]["attributes"]
                if res=="":
                    continue
                is_human = res["is_human"]["name"]
                if is_human=="非正常人体":
                    error_couynt+=1
                    continue
                upper_cut = res["upper_cut"]["name"]
                if upper_cut=="有上方截断":
                    error_couynt+=1
                    continue
                pre_age = age_map[res["age"]["name"]]
                pre_sex = sex_map[res["gender"]['name']]
                pre_hs_hat = hat_map[res["headwear"]['name']]
                pre_hs_mask = mask_map[res["face_mask"]['name']]
                pre_hs_glass = glass_map[res["glasses"]['name']]
                pre_hs_bag = bag_map[res["bag"]['name']]
                pre_up_color_str = up_color_map[res["upper_color"]['name']]
                pre_lower_color_str = lower_color_map[res["lower_color"]['name']]
                pre_viewpoints_str = viewpoints_map[res["orientation"]['name']]
                res = [check_equal(gt_age,pre_age),check_equal(gt_sex,pre_sex),
                                                    check_equal(gt_hs_hat,pre_hs_hat),check_equal(gt_hs_mask,pre_hs_mask),
                                                    check_equal(gt_hs_glass,pre_hs_glass),check_equal(gt_hs_bag,pre_hs_bag),
                                                        check_equal(gt_viewpoints_str,pre_viewpoints_str),
                                                        check_equal(gt_up_color_str,pre_up_color_str),
                                                        check_equal(gt_lower_color_str,pre_lower_color_str)]

                pre_age = " ".join(list(map(str, pre_age)))
                pre_up_color_str = " ".join(list(map(str, pre_up_color_str)))
                pre_lower_color_str = " ".join(list(map(str, pre_lower_color_str)))
                pre_viewpoints_str = " ".join(list(map(str, pre_viewpoints_str)))

                # 共 41 列
                res_str = "{} {} {} {} {} {} {} {} {} {}\n".format(line[0], pre_age, pre_sex, pre_hs_hat, pre_hs_mask, pre_hs_glass, pre_hs_bag,
                                                                   pre_up_color_str, pre_lower_color_str, pre_viewpoints_str)
                totle_res.append(res_str)

print("异常数据",error_couynt)
with open("api.txt", "w") as res_file:
    for res_str in totle_res:
        print(res_str)
        res_file.write(res_str)
# 统计每个属性标签与百度APi的预测情况
# totle_res = list(map(list, zip(*totle_res)))
# print("当前图片数：{}".format(len(totle_res[0])))
# for one in totle_res:
#     print(one.count(1))
# print("完全可用:{}".format(len(totle_res)))
# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""

import os,json

age_map = { "幼儿":[1,0,0,0,0],"青少年":[0,1,0,0,0], "青年":[0,0,1,0,0],"中年":[0,0,0,1,0], "老年":[0,0,0,0,1],}
sex_map = { "男性":0, "女性":1}
hat_map = { "无帽":0, "普通帽":1, "安全帽":1,}
mask_map = { "无口罩": [0,1,0], "戴口罩": [1,0,0],"不确定": [0,0,1],}
glass_map = { "戴眼镜": [1,0,0], "戴墨镜": [1,0,0],"无眼镜": [0,1,0],"不确定": [0,0,1]}
bag_map= { "无背包": 0, "单肩包": 1,"双肩包": 1,"不确定": 0}
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
count = 0

totole_res = []
# peta
keyword = "peta"
lines = [f"{i+1:05}" for i in range(19000)]
# pa-100k
# lines = [f"{i+1:06}" for i in range(100000)]
for index,line in enumerate(lines):

    # res_json_file = r"D:\行人属性数据\peta\{}.json".format(line)
    res_json_file = r"D:\行人属性数据\{}\{}.json".format(keyword,line)
    if os.path.isfile(res_json_file):
        with open(res_json_file, 'r') as load_f:
            res = json.load(load_f)[0]["attributes"]
            if res == "":
                continue
            is_human = res["is_human"]["name"]
            if is_human=="非正常人体":
                continue
            upper_cut = res["upper_cut"]["name"]
            if upper_cut=="有上方截断":
                continue
            pre_age = age_map[res["age"]["name"]]
            pre_sex = sex_map[res["gender"]['name']]
            pre_hs_hat = hat_map[res["headwear"]['name']]
            pre_hs_mask = mask_map[res["face_mask"]['name']]
            pre_hs_glass = glass_map[res["glasses"]['name']]
            pre_hs_bag = bag_map[res["bag"]['name']]
            pre_up_color_str = up_color_map[res["upper_color"]['name']]
            pre_lower_color_str = lower_color_map[res["lower_color"]['name']]
            need_index = [6,9,10,11]
            if  any([pre_lower_color_str[int(i)] for i in need_index]) or pre_age==[1,0,0,0,0] or pre_age==[0,0,0,0,1] or pre_hs_hat==1 or pre_hs_mask==[1,0,0] or pre_hs_bag==1:
                print(index)
                pre_age = " ".join(list(map(str, pre_age)))
                pre_up_color_str = " ".join(list(map(str, pre_up_color_str)))
                pre_lower_color_str = " ".join(list(map(str, pre_lower_color_str)))
                # pre_viewpoints_str = " ".join(list(map(str, pre_viewpoints_str)))
                pre_hs_mask = " ".join(list(map(str, pre_hs_mask)))
                pre_hs_glass = " ".join(list(map(str, pre_hs_glass)))

                # 共 41 列
                res_str = "{} {} {} {} {} {} {} {} {}\n".format("{}_".format(keyword)+line+".png", pre_age, pre_sex, pre_hs_hat, pre_hs_mask,
                                                                   pre_hs_glass, pre_hs_bag,
                                                                   pre_up_color_str, pre_lower_color_str)
                totole_res.append(res_str)

with open("{}_final_data.txt".format(keyword), "w") as res_file:
    for one in totole_res:
        # print(res_str)
        res_file.write(one)
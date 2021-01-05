# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
RAPv2 和百度API数据集提取策略
1.年龄 百度API
2.性别 RAPv2
3.眼镜 如果百度API标注不确定 就认为其为"不确定" 否则使用RAPv2
4.口罩 同3
5.帽子 RAPv2
6.背包 RAPv2
7.上下装颜色 百度
8.朝向  暂不考虑
Authors: lijinjun1351@ichinae.com
"""
def get():
    img_path_list = []  # 图片路径
    gt_attr = []  # RAP
    pre_attr = []  # 百度api
    res_txt_path = "rapv2_12_25.txt"
    api_txt_paht = "api.txt"
    gt_file_lines = []
    totle_res =[]
    gt_imgs = []
    with open(res_txt_path) as res_file:
        res_file_lines = res_file.readlines()
        for idx, line in enumerate(res_file_lines):
            line = line.strip().split(" ")
            gt_imgs.append(line[0])
            gt_file_lines.append(line[1:])

    with open(api_txt_paht) as api_file:
        lines = api_file.readlines()
        gt_index = 0
        for idx, line in enumerate(lines):
            line = line.strip().split(" ")
            if line[0] != gt_imgs[gt_index]:
                gt_index += 1
                while line[0] != gt_imgs[gt_index]:
                    gt_index+=1

            # img = r"E:\桌面\工作算法\rap2.0\RAP_dataset\{}".format(line[0])
            img =line[0]
            img_path_list.append(img)
            pre_attr.append(line[1:])
            gt_attr.append(gt_file_lines[gt_index])
            gt_index+=1

        assert len(img_path_list)==len(lines),"{} {} ".format(len(img_path_list),len(lines))

    for img_index in range(len(img_path_list)):
        cur_img = img_path_list[img_index]
        # 年龄
        pre_age = pre_attr[img_index][:5]
        # if pre_age ==['1', '0', '0', '0', '0']:
        #     print(1)
        cur_age = " ".join(pre_age)
        assert cur_age.count("1")==1

        # 性别
        gt_sex = gt_attr[img_index][5]
        pre_sex =pre_attr[img_index][5]
        cur_sex = gt_sex

        # 帽子
        gt_hat = gt_attr[img_index][6]
        pre_hat = pre_attr[img_index][6]
        cur_hat = gt_hat

        # 口罩  戴 不戴 不确定
        gt_mask =gt_attr[img_index][7]
        pre_mask = pre_attr[img_index][7]
        cur_mask = " ".join(["0","0","0"])
        if pre_mask=="2":
            cur_mask = " ".join(["0","0","1"])
        elif gt_mask=="1":
            cur_mask = " ".join(["1","0","0"])
        elif gt_mask == "0":
            cur_mask = " ".join(["0", "1", "0"])
        assert cur_mask.count("1")==1

        # 眼镜 同口罩
        gt_glass = gt_attr[img_index][8]
        pre_glass =pre_attr[img_index][8]
        cur_glass = " ".join(["0","0","0"])
        if pre_glass=="2":
            cur_glass = " ".join(["0","0","1"])
        elif gt_glass=="1":
            cur_glass = " ".join(["1","0","0"])
        elif gt_glass == "0":
            cur_glass = " ".join(["0", "1", "0"])
        assert cur_glass.count("1")==1

        gt_bag = gt_attr[img_index][9]
        pre_bag = pre_attr[img_index][9]
        cur_bag = gt_bag

        # 上装颜色 #需求中 黑、白、灰、红、蓝、黄、橙、棕、绿、紫、粉、银、花色
        gt_upcolor = gt_attr[img_index][10:23]
        pre_upcolor =pre_attr[img_index][10:23]
        cur_up_color = pre_upcolor
        if gt_upcolor[-1]=="1":  # 如果RAP未知 则为未知
            cur_up_color[:] = ["0" for i in range(13)]
            cur_up_color[-1]="1"
            assert cur_up_color.count("1")==1
        elif gt_upcolor[11]=="1":  # 如果 银色
            cur_up_color[:] = ["0" for i in range(13)]
            cur_up_color[11]="1"
            assert cur_up_color.count("1")==1
        else:
            need_index = [5,6,9,10,11]
            for one in need_index:
                if gt_upcolor[one]=="1":
                    cur_up_color[:] = ["0" for i in range(13)]
                    cur_up_color[one] = "1"
                    assert cur_up_color.count("1")==1
        cur_up_color = " ".join(cur_up_color)


        gt_lower_color = gt_attr[img_index][23:36]
        pre_lower_color = pre_attr[img_index][23:36]
        cur_lower_color = pre_lower_color
        if gt_lower_color[-1]=="1":  # 如果RAP未知 则为未知
            cur_lower_color[:] = ["0" for i in range(13)]
            cur_lower_color[-1]="1"
            assert cur_lower_color.count("1")==1
        elif gt_lower_color[11]=="1":  # 如果银色
            cur_lower_color[:] = ["0" for i in range(13)]
            cur_lower_color[11]="1"
            assert cur_lower_color.count("1")==1
        else:
            need_index = [5,6, 9, 10, 11]
            for one in need_index:
                if gt_lower_color[one] == "1":
                    cur_lower_color[:] = ["0" for i in range(13)]
                    cur_lower_color[one] = "1"
                    assert cur_lower_color.count("1")==1
        cur_lower_color = " ".join(cur_lower_color)

        # if gt_lower_color[6]==1 or gt_lower_color[9]==1 or gt_lower_color[10]==1 or  gt_lower_color[11]==1:
        # # if gt_lower_color[6]==1:
        #     print(cur_img,gt_lower_color)
        assert cur_lower_color.count("1")==1

        res_str = "{} {} {} {} {} {} {} {} {}\n".format(cur_img, cur_age, cur_sex, cur_hat, cur_mask, cur_glass, cur_bag,
                                                           cur_up_color, cur_lower_color)
        totle_res.append(res_str)

    with open("rapv2_final_data.txt","w") as res_file:
        for one in totle_res:
            res_file.write(one)
    print("final")
if __name__ == '__main__':
    # get()
    lines = []
    peta = "peta_final_data.txt"
    pa_100k = "PA-100k_final_data.txt"
    rapv2= "rapv2_final_data.txt"
    sliver_lower = "silver_kuzi.txt"
    sliver_up = "silver_up.txt"
    with open(sliver_lower) as f:
        x = f.readlines()
        lines.extend(x)
    with open(sliver_up) as f:
        x = f.readlines()
        lines.extend(x)
    # with open(peta) as f:
    #     x = f.readlines()
    #     lines.extend(x)
    # with open(pa_100k) as f:
    #     x = f.readlines()
    #     lines.extend(x)
    with open(rapv2,"a") as f:
        for line in lines:
            f.write(line)
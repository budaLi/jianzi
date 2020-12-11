# coding=utf-8
# Copyright (c) 2020 ichinae.com, Inc. All Rights Reserved
"""
Module Summary Here.
Authors: lijinjun1351@ichinae.com
"""
from scipy.io import loadmat
import base64
import random
import requests
import json
import os

'''
人体检测和属性识别
 
 # 上：红、橙、黄、绿、蓝、紫、粉、黑、白、灰、棕
 # 下：红、橙、黄、绿、蓝、紫、粉、黑、白、灰、棕、不确定
'''
class BaiDuDetectionApi(object):
    def __init__(self,key_file_path):
        self.key_file_path = key_file_path
        self.access_token = self._generate_access_token()

    def _gengerate_key(self):
        """
        生成请求秘钥
        :return:
        """
        with open(self.key_file_path) as f:
            data = f.readlines()
        key_lis = []
        for line in data[2:]:
            line = line.split()
            API_KEY, API_SECRET = line[0], line[1]
            key_lis.append((API_KEY,API_SECRET))
        return key_lis

    def _generate_access_token(self):
        # 初始化对象，进行api的调用工作
        key_lis = self._gengerate_key()
        API_KEY,API_SECRET = random.choice(key_lis)
        print(API_KEY,API_SECRET)
        access_token = self.get_acces_token(API_KEY, API_SECRET)
        return access_token

    def get_acces_token(self,api_key, secret_key):
        """
        获取 access_token # https://console.bce.baidu.com/ai/?_=1606380550492#/ai/body/app/detail~appId=2063251
        """
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            api_key, secret_key)
        response = requests.get(host).json()
        print(response)
        if not response.get("error"):
            return response["access_token"]

    def trans_json(self,response_json):
        try:
            person_info = response_json["person_info"][0]
            return person_info
        except Exception:
            return None

    def get_attribute(self,index,file_path):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
        # 二进制方式打开图片文件
        new_file_path = img_root_path.format(file_path)
        f = open(new_file_path, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        request_url = request_url + "?access_token=" + self.access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            person_info = self.trans_json(response.json())
            print(index,person_info)
            if person_info:
                json_file_name = file_path.split(".")[0]+".json"
                with open(res_json_file.format(json_file_name),"w") as f:
                    json.dump([person_info],f,indent=2,ensure_ascii=False)



    def main(self):
        data = loadmat(mat_path)
        images = []
        atts = []
        att_name = []

        # 数据集总数
        for idx in range(84928):
            img_pt = data['RAP_annotation'][0][0][0][idx][0][0]
            img = img_pt.split(".")[0]
            res_json_file = "./res_json_file/{}.json".format(img)
            if not os.path.isfile(res_json_file):
                images.append(img_pt)
            atts.append(data['RAP_annotation'][0][0][1][idx, :].tolist())
        print("totle:{}".format(len(images)))
        for index,img in enumerate(images[::-1]):
            self.get_attribute(index,img)

if __name__ == '__main__':
    mat_path = r"E:\桌面\工作算法\rap2.0\RAP_annotation\RAP_annotation.mat"
    img_root_path = r"E:\桌面\工作算法\rap2.0\RAP_dataset\{}"
    res_json_file = "./res_json_file/{}"
    baidu = BaiDuDetectionApi("KEY.txt")
    baidu.main()


    # with open( res_json_file.format("CAM31-2014-03-18-20140318124418-20140318125002-tarid8-frame482-line1.json"),'r') as load_f:
    #     res = json.load(load_f)
    #     print(res)
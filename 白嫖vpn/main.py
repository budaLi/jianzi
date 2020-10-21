# @Time    : 2020/10/20 18:02
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
# 16位随机数字和字母组成订阅链接

from itertools import chain
import requests
from queue import Queue
from tqdm import tqdm
import string
import hashlib
import random
import threading

# urls= "https://sub.52dog.cloud/link/YiotLqs9YjEk5aCz?sub=3"
# url = "https://sub.52dog.cloud/link/47o6gGe3scYEGIFz?sub=3"
# 可用的两个订阅  16位随机字母加数字构成
# 原理：可用订阅正常访问时会下载文件  不可用订阅无内容




base_url = "https://sub.52dog.cloud/link/{}?sub=3"
res_file  = "res.txt"
count =0
total_dic= {}


def generute_url():

    url_quque = Queue()
    total_count = 10000
    for i in range(total_count):

        # 选取16个随机字符串加密
        pwd = "".join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 16))
        if pwd not in total_dic:
            url_quque.put(base_url.format(pwd))
            total_dic[pwd]=1

    return url_quque


def get(url):
    print(url)
    response = requests.get(url)
    if response.text!="":
        with open(res_file,"a") as f:
            f.write(url+"\n")
        return 1
    return None

def main(url_quque):
    global count

    while not url_quque.empty():
        url = url_quque.get()
        res = get(url)
        if res:
            print("订阅成功获取个数为：{}".format(count))
            count+=1

if __name__ == '__main__':
    thread_num = 5
    url_quque = generute_url()
    thread_lis = []
    for i in range(thread_num):
        th = threading.Thread(target=main,args=(url_quque,))
        thread_lis.append(th)
    for one in thread_lis:
        one.start()
    for one in thread_lis:
        one.join()

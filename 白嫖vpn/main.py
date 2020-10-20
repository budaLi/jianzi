# @Time    : 2020/10/20 18:02
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
# 16位随机数字和字母组成订阅链接

from itertools import chain
import requests
from queue import Queue
from tqdm import tqdm

# urls= "https://sub.52dog.cloud/link/YiotLqs9YjEk5aCz?sub=3"
# url = "https://sub.52dog.cloud/link/47o6gGe3scYEGIFz?sub=3"
base_url = "https://sub.52dog.cloud/link/{}?sub=3"
res_file  = "res.txt"


# chr(97) -> 'a' 这个变量保存了密码包含的字符集
dictionaries = [chr(i) for i in
                chain(
                    range(48, 58), # 0 - 9
                    range(97, 123),  # a - z
                      range(65, 91))  ] # A - Z


def all_passwd(dictionaries, maxlen: int):
    # 返回由 dictionaries 中字符组成的所有长度为 maxlen 的字符串
    def helper(temp: list, start: int, n: int):
        # 辅助函数，是个生成器
        if start == n:  # 达到递归出口
            yield ''.join(temp)
            return
        for t in dictionaries:
            temp[start] = t  # 在每个位置
            yield from helper(temp, start + 1, n)

    yield from helper([0] * maxlen, 0, maxlen)



def generute_url():
    lengths = [16]  # 密码长度
    total = sum(len(dictionaries) ** k for k in lengths)  # 密码总数
    url_quque = Queue()

    total_count = 10

    for pwd in tqdm(chain.from_iterable(all_passwd(dictionaries, maxlen) for maxlen in lengths), total=total):
        if total_count<=0:
            break
        url_quque.put(base_url.format(pwd))
        total_count -= 1
    return url_quque


def get(url):
    print(url)
    response = requests.get(url)
    if response.text!="":
        with open(res_file,"a") as f:
            f.write(url+"\n")
        return 1
    return None

def main():
    count =0
    url_quque = generute_url()
    while not url_quque.empty():
        url = url_quque.get()
        res = get(url)
        if res:
            print("订阅成功获取个数为：{}".format(count))
            count+=1

main()

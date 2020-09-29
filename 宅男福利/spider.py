# @Time    : 2020/9/29 10:33
# @Author  : Libuda
# @FileName: spider.py
# @Software: PyCharm
import requests
import os
from tqdm import tqdm

class Spider:
    """
    妹子图爬虫   http://mzitu.icu/
    """
    def __init__(self):
        self.save_path = "./img/"
        self.url = "http://mapi.ibayeux.com/v1/airticle/?offset={}"
        self.headers = {
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        }
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def download(self):
        while 1:
            start_offset = 0
            url = self.url.format(start_offset)
            response =  requests.get(url).json()
            result = response["results"]
            for one in result:
                title = one["title"]
                imgs_content = eval(one["content"])
                path = one["path"]
                for _img in tqdm(imgs_content):
                    img_url = path+"/"+_img
                    img = requests.get(img_url)
                    p = self.save_path+_img
                    with open(p, 'wb') as file:
                        file.write(img.content)
            start_offset+=20


if __name__ == '__main__':

    s =Spider()
    s.download()
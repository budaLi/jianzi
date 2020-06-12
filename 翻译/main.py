# @Time    : 2020/6/12 16:02
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
import xlrd
from xlutils.copy import copy
import hashlib
import time
import random
import requests


def get_keywords_data(tables, row, col):
    actual_data = tables.cell_value(row, col)
    return actual_data

def write_to_excel(file_path, row, col, value):
    work_book = xlrd.open_workbook(file_path, formatting_info=False)
    write_to_work = copy(work_book)
    sheet_data = write_to_work.get_sheet(0)
    sheet_data.write(row, col, str(value))
    write_to_work.save(file_path)


class youdao():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Referer': 'http://fanyi.youdao.com/',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-481680322@10.169.0.83;'
        }
        self.data = {
            'i': None,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': None,
            'sign': None,
            'ts': None,
            'bv': None,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def translate(self, word):
        ts = str(int(time.time() * 10000))
        salt = ts + str(int(random.random() * 10))
        sign = 'fanyideskweb' + word + salt + '97_3(jkMYg@T[KZQmqjTK'
        sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
        bv = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        bv = hashlib.md5(bv.encode('utf-8')).hexdigest()
        self.data['i'] = word
        self.data['salt'] = salt
        self.data['sign'] = sign
        self.data['ts'] = ts
        self.data['bv'] = bv
        res = requests.post(self.url, headers=self.headers, data=self.data)

        try:
            return [res.json()['translateResult'][0][0].get('tgt')]
        except Exception:
            return word


def main():
    link_file_path = "test.xls"
    link_ecel = xlrd.open_workbook(link_file_path)
    link_tables = link_ecel.sheet_by_index(0)
    link_get_col = 0
    link_datas = [get_keywords_data(link_tables, i, link_get_col) for i in range(1, link_tables.nrows)]
    y = youdao()

    index = 0
    for data in link_datas:
        res = y.translate(data)
        print("index:{},data:{},transdata:{}".format(index,data,res))
        write_to_excel(link_file_path,index,link_get_col,data)
        write_to_excel(link_file_path,index+1,link_get_col,res)
        index+=2

    print("end")


if __name__ == '__main__':
    main()
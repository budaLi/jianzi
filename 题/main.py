# @Time    : 2020/6/29 15:18
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm


# def main(st):
#     dic={}
#     for one in st:
#         if one not in dic:
#             dic[one]=1
#         else:
#             dic[one]+=1
#     return dic
#
#
# res= main("sassafasfsaf")
# print(res)


def main():
    import random
    def ranstr(num):
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        salt = ''
        for i in range(num):
            salt += random.choice(H)
        return salt

    dic = {}
    for i in range(100):
        st = ranstr(3)  # 3位的随机字符串
        for one in st:
            if one not in dic:
                dic[one]=1
            else:
                dic[one]+=1

    dic = sorted(dic.items())
    print(dic[:20])


main()
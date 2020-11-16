"""
    这是demo 02
"""
# @Time    : 2020/10/27 10:24
# @Author  : Libuda
# @FileName: demo_02_old.py
# @Software: PyCharm

# 菜鸟教程 异常处理 https://www.runoob.com/python/python-exceptions.html
import os


# 1.用户自定义异常类型
class TooLongExceptin(Exception):
    "this is user's Exception for check the length of name "

    def __init__(self, leng):
        self.leng = leng

    def __str__(self):
        msg = "姓名长度是" + str(self.leng) + "，超过长度了"
        return msg

# 2.手动抛出用户自定义类型异常
def name_test():
    try:
        name = input("enter your naem:")
        if len(name)>4:
            raise TooLongExceptin(len(name))
        else :
            print(name)

    except TooLongExceptin as e_result:
        print("捕捉到异常了")
        print("打印异常信息：",e_result)

if __name__ == '__main__':
    name_test()
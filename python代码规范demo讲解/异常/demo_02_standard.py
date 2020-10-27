"""
    这是demo 02
"""
# @Time    : 2020/10/27 10:24
# @Author  : Libuda
# @FileName: demo_02_old.py
# @Software: PyCharm


try:
    FILE = open("1.txt")
except FileNotFoundError as print_exception:
    print(print_exception)
finally:
    FILE.close()

# @Time    : 2020/6/24 11:52
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
import time
import random
import sys
sys.path.append("./")
from bubble_sort import BubbleSortMethod
from insert_sort import InsertSortMethod
from select_sort import select_sort
from shell_sort import shell_sort
from merge_sort import merge_sort

testlist = [i for i in  range(1,1000)]
random.shuffle(testlist)
with open("testlist.txt","w") as f:
    for one in testlist:
        f.write(str(one)+"\t")



print("待排序数据 共1000个数字",testlist)
print("\n")
start_time = time.time()
bubble = BubbleSortMethod(testlist)  # new object of BubbleSortMethod class
sortlist = bubble.bubble_sort1()
print("冒泡排序：",sortlist)
print("冒泡排序用时：",time.time()-start_time)
print("\n")
start_time = time.time()
insert = InsertSortMethod(testlist)  # new object of InsertSortMethod class
sortlist = insert.insert_sort1()
print("直接插入排序：",sortlist)
print("直接插入排序用时：",time.time()-start_time)
print("\n")
start_time = time.time()
sortlist = select_sort(testlist)
print("直接选择排序：",sortlist)
print("直接选择排序用时：",time.time()-start_time)
print("\n")
start_time = time.time()
sortlist = shell_sort(testlist)
print("希尔排序：",sortlist)
print("希尔排序用时：",time.time()-start_time)
print("\n")
start_time = time.time()
sortlist = merge_sort(testlist,0,len(testlist)-1)
print("归并排序：",sortlist)
print("归并排序用时：",time.time()-start_time)

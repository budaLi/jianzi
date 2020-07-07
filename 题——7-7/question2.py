
def search(a,key):
    """
    非递归函数
    :param a:
    :param key:
    :return:
    """
    for i in range(len(a)):
        if a[i]==key:
            return i
    return -1

def reserach(a,key,left,right):
    """
    递归实现顺序查找
    :param a:
    :param key:
    :param left:
    :param right:
    :return:
    """
    # 如果左边界大于右边界 查找不到 为-1
    if left>right:
        return -1

    for i in range(left,len(a)):
        if a[i]!=key:
            return reserach(a,key,left+1,right)
        else:
            return i
    return -1

def question3(number):
    lis = [34,56,78,87,88,90,101,112,520,888]
    res1 = search(lis,number)
    if res1!=-1:
        print("顺序查找结果为：{}".format(res1))
    else:
        print("顺序查找结果为：not found")

    res2 = reserach(lis,number,0,len(lis))
    if res2!=-1:
        print("递归查找结果为：{}".format(res2))
    else:
        print("递归查找结果为：not found")

if __name__ == '__main__':
    number = input("请输入一个数字:")
    question3(int(number))
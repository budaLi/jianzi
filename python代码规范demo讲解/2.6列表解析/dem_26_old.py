"""
    2.6列表解析
"""
# @Time    : 2020/10/29 9:23
# @Author  : Libuda
# @FileName: dem_26_old.py
# @Software: PyCharm

# 代码格式并不影响得分


def fun():
    """
        xxxx
    :return:
    """
    # result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

    return (
        (x, y, z)
        for x in range(5)
        for y in range(5)
        if x != y
        for z in range(5)
        if y != z
    )

"""
    这是demo 03
"""
# @Time    : 2020/10/27 10:33
# @Author  : Libuda
# @FileName: demo_03_old.py
# @Software: PyCharm


def get_person_info():
    """
        获取个人信息
    :return:
    """
    person_info = {}
    person_info["name"] = "jjp"
    person_info["sex"] = "MALE"
    person_info["age"] = 30
    person_info["weight"] = 130

    return person_info


PERSON_INFO = get_person_info()

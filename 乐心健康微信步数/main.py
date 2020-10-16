# @Time    : 2020/10/12 9:35
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
import requests
import hashlib
import json
import time
import random


def md5(code):
    res = hashlib.md5()
    res.update(code.encode("utf8"))
    return res.hexdigest()


def get_information(mobile, password):
    header = {
        'Content-Type': 'application/json; charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    url = "http://sports.lifesense.com/sessions_service/login?systemType=2&version=4.6.7"
    datas = {
        "appType": 6,
        "clientId": md5("5454"),
        "loginName": str(mobile),
        "password": md5(str(password)),
        "roleType": 0
    }
    response = requests.post(url, headers=header, data=json.dumps(datas))
    return response.text


def update_step(step, information):
    step = int(step)
    url = "http://sports.lifesense.com/sport_service/sport/sport/uploadMobileStepV2?version=4.5&systemType=2"
    accessToken = json.loads(information)["data"]["accessToken"]
    userId = json.loads(information)["data"]["userId"]
    # print(accessToken)
    # print(userId)
    # 获取当前时间和日期
    timeStamp = time.time()
    localTime = time.localtime(timeStamp)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
    print(strTime)
    measureTime = strTime + "," + str(int(timeStamp))

    header = {
        'Cookie': 'accessToken=' + accessToken,
        'Content-Type': 'application/json; charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    sport_datas = {
        "list": [
            {
                "DataSource": 2,
                "active": 1,
                "calories": str(int(step / 4)),
                "dataSource": 2,
                "deviceId": "M_NULL",
                "distance": str(int(step / 3)),
                "exerciseTime": 0,
                "isUpload": 0,
                "measurementTime": measureTime,
                "priority": 0,
                "step": str(step),
                "type": 2,
                "updated": str(int(time.time() * 1000)),
                "userId": str(userId)
            }]
    }
    result = requests.post(url, headers=header, data=json.dumps(sport_datas))
    return result.text


def server_send(msg):
    if sckey == '':
        return
    server_url = "https://sc.ftqq.com/" + str(sckey) + ".send"
    data = {
        'text': msg,
        'desp': msg
    }
    requests.post(server_url, data=data)


def kt_send(msg):
    if ktkey == '':
        return
    kt_url = 'https://push.xuthus.cc/send/' + str(ktkey)
    data = ('步数刷取完成，请查看详细信息~\n' + str(msg)).encode("utf-8")
    requests.post(kt_url, data=data)


def execute_walk(phone, password, step):
    information = get_information(phone, password)
    update_result = update_step(step, information)
    result = json.loads(update_result)["msg"]
    if result == '成功':
        msg = "刷新步数成功！此次刷取" + str(step) + "步。"
        print(msg)
        server_send(msg)
        kt_send(msg)
    else:
        msg = "刷新步数失败！请查看云函数日志。"
        print(msg)
        server_send(msg)
        kt_send(msg)


def main(phone,password,step):
    execute_walk(phone, password, step)



# 江西
# phone = '18779089018'  # 登陆账号
# password = 'z19970927'  # 密码




if __name__ == '__main__':
    info = [
        ['15735656005','123456',69999],  # 李不搭
        ['17600180818','123456',69999],  # 张航
        ['18832676386','123456',16888],  # 张老师
    ]
    for one in info:
        phone = one[0]
        password = one[1]
        step = one[2]
        main(phone, password, step)
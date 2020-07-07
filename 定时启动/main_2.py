# coding:utf-8
# @Time    : 2020/6/24 21:11
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
import time
import os
import time

log_path = "./"+str(time.gmtime().tm_mday)+"_"+str(time.gmtime().tm_hour+8)+"_"+str(time.gmtime().tm_min)+"_log.txt"
if not os.path.exists(log_path):
    with open(log_path,"w") as f:
        f.write("{}：启动程序".format(time.ctime()))

def logging(msg):
    log = "{}:{}".format(time.ctime(),msg)
    with open(log_path, "a") as f:
        f.write(log+"\n")
    print(log)


# 启动时间
start_time_hour = 21
# 结束时间
end_time_hour =  23

# 检查程序
check_process ="ps -ef | grep -v grep | grep vdsd | wc -l"
# 停止程序
stop_process = "vds-cli stop"
# 启动程序
start_process = "vdsd -daemon"
# 删除文件
rm_file = "rm /vds_data/mncache.dat"
# 获取assetid
get_id = "vds-cli mnsync status"
# 卡块高度 # 查看：区块高度返回值（打印日志"
get_height = "vds-cli getblockcount"
# 卡块删除文件
ca_rm_file = "rm -rf /vds_data/mncache.dat mnpayments.dat"
# 卡块命令A
reconsiderblock = "vds-cli reconsiderblock {}"
#vds-cli mnsync next
next = "vds-cli mnsync next"


# 检测时间间隔
check_time = 300

# 最多高度重复次数 判断卡块
dic = {}
car_count = 5  #  5次高度一致则认为卡块

def is_ca():
    """
    判断是否卡块  卡块返回true
    :return:
    """
    logging("执行：{}".format(get_height))
    res =  os.popen(get_height).read().strip()
    logging("返回结果：{}".format(res))
    if res not in dic:
        dic[res] = 1
    else:
        if dic[res]>=car_count:
            logging("高度{}次不再变化，卡块！".format(dic[res]))
            return True
        else:
            dic[res]+=1
    return False

def restart():
    """
    卡块重启
    :return:
    """
    logging("执行：{}".format(get_height))
    res =  os.popen(get_height).read().strip()
    logging("当前卡块高度：{}".format(res))
    #停止节点运行
    stop()

    # 保证程序已结束
    flag = True
    while flag:
        if not check():
            flag=False

    # 删除卡块文件
    logging("执行：{}".format(ca_rm_file))
    res1 =  os.popen(ca_rm_file).read().strip()
    logging("返回结果：{}".format(res1))

    # 重启
    logging("执行：{}启动节点".format(start_process))
    os.system(start_process)
    # 等待60秒
    time.sleep(60)

    #res为上次卡块高度
    logging("执行：{}".format(reconsiderblock.format(res)))
    os.system(reconsiderblock)

    # 等待15s
    time.sleep(15)
    logging("执行：{}".format(get_height))
    new_res =  os.popen(get_height).read().strip()
    logging("返回结果：{}".format(new_res))

    #如果还等于卡块高度，再等待15秒后，重复执行一次命令A，直到区块高度大于卡块高度，，
    while new_res<=res:
        # 等待15s
        time.sleep(15)
        logging("执行：{}".format(reconsiderblock.format(res)))
        os.system(reconsiderblock)
        logging("执行：{}".format(get_height))
        new_res = os.popen(get_height).read().strip()
        logging("返回结果：{}".format(new_res))

    start_time = time.time()
    ok = False
    #大于后，执行 vds-cli mnsync status，等待返回值【"AssetID"】，
    res = os.popen(get_id).read().strip()
    res = eval(res)
    asserid = res["AssetID"]
    if asserid=="999":
        pass
    else:
        flag = True

        while flag:
            time.sleep(10)
            res = os.popen(get_id).read().strip()
            res = eval(res)
            asserid = res["AssetID"]
            if asserid=="999":
                flag = False
                ok = True
            # 如果 6 分钟后，还没有返回 999  退出循环
            elif time.time() -start_time>=300:
                flag = False

    if not ok:
        logging("执行：{}".format(new_res))
        next_res = os.popen(new_res).read().strip()
        logging("返回结果：{}".format(next_res))
        res = eval(next_res)
        asserid = res["AssetID"]
        if asserid=="999":
            pass
        else:
            # 如果不是999休眠15s再执行 直到其为999
            flag = True
            time.sleep(15)
            while flag:
                time.sleep(10)
                res = os.popen(next_res).read().strip()
                res = eval(res)
                asserid = res["AssetID"]
                if asserid == "999":
                    flag = False



def check():
    """
    检测程序是否正常运行
    :return:
    """
    res =  os.popen(check_process).read().strip()
    logging("执行：{}".format(check_process))
    logging("返回结果：{}".format(res))
    if res!="0" and not is_ca():  #不是0就正常
        logging("节点正在运行，继续监测!")
        return True

    logging("程序已结束")
    return False

def stop():
    """
    保证程序退出
    :return:
    """
    logging("执行：{}，停止节点运行".format(stop_process))
    os.system(stop_process)
    exit_flag = True
    while exit_flag:
        logging("等待30秒")
        time.sleep(30)

        # 如果已结束
        if not check():
            exit_flag = False
        else:
            logging("正在执行：{}".format(stop_process))
            os.system(stop_process)

def edit_file_first():
    """
    节点异常编辑文件
    :return:
    """
    logging("正在删除并编辑文件")
    logging("正在执行：{}".format(rm_file))
    os.system(rm_file)
    file = "/root/.vds/vds.conf"

    with open(file,"w") as f:
        lines = f.readlines()
    for line in lines:
        if "masternode=1" in line or "masternodeprivkey" in line:
            line = "# "+line
        f.write(line+"\n")


def start():
    """
    保证程序启动
    :return:
    """
    logging("执行：{}启动节点".format(start_process))
    os.system(start_process)
    # 检测代码是否正常运行
    if check():
        logging("程序已启动")
        return True
    else:
        logging("程序未启动，等待重新启动中")
        # 异常  编辑文件
        edit_file_first()
        # 启动
        start()
        res = os.popen(get_id).read().strip()
        res = eval(res)
        asserid = res["AssetID"]
        if asserid=="999":
            pass
        else:
            flag = True
            while flag:
                time.sleep(120)
                res = os.popen(get_id).read().strip()
                res = eval(res)
                asserid = res["AssetID"]
                if asserid=="999":
                    flag = False
        stop()
        #等待20秒后，执行：ps -ef | grep -v grep | grep vdsd | wc -l，等待返回值为“0”
        time.sleep(20)
        if not check():
            logging("正在编辑文件:/root/.vds/vds.conf")
            file = "/root/.vds/vds.conf"
            with open(file, "w") as f:
                lines = f.readlines()
            for line in lines:
                if "#masternode=1" in line:
                    line = line.replace("#masternode=1","masternode=1")
                elif "masternodeprivkey" in line:
                    line = line.replace("#masternodeprivkey","masternodeprivkey")
                f.write(line + "\n")

            # 启动
            start()

def main():
    # 是否是第一次运行
    is_first = True
    flag = True
    while flag:
        try:
            now_time_hour = time.gmtime().tm_hour+8

            # 如果是第一次运行时间
            if now_time_hour==start_time_hour and is_first:
                stop()
                start()
                is_first =False
            # 如果在时间范围内
            elif now_time_hour== 24:
                is_first  = True
            else:
                logging("节点守护中")
                if not check():
                    start()

            time.sleep(check_time)
        except Exception as e :
            logging("程序异常：{}".format(e))
            time.sleep(check_time)
            # flag = False
if __name__ == '__main__':
    main()

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
start_time_hour = 8
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


check_time = 300

def check():
    """
    检测程序是否正常运行
    :return:
    """
    res =  os.popen(check_process).read().strip()
    logging("正在执行：{}".format(check_process))
    logging("执行结果：{}".format(res))
    if res!="0":  #不是0就正常
        logging("程序正在运行!")
        return True
    logging("程序已结束")
    return False

def stop():
    """
    保证程序退出
    :return:
    """
    logging("正在执行：{}".format(stop_process))
    os.system(stop_process)
    exit_flag = True
    while exit_flag:
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
    logging("正在执行：{}".format(start_process))
    os.system(start_process)
    # 检测代码是否正常运行  #TODO
    if check():
        logging("程序已启动")
        return True
    else:
        logging("程序启动失败，等待重新启动中")
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
                logging("检测程序运行中")
                if not check():
                    start()

            time.sleep(check_time)
        except Exception as e :
            logging("程序异常：{}".format(e))
            time.sleep(check_time)
            # flag = False
if __name__ == '__main__':
    main()
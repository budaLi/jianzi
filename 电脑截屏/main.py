# @Time    : 2020/6/11 17:34
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
import time

import numpy as np
from PIL import ImageGrab
import time
import win32gui, win32ui, win32con, win32api

def draw():
    """
    屏幕截图
    :return:
    """
    # 每抓取一次屏幕需要的时间约为1s,如果图像尺寸小一些效率就会高一些
    beg = time.time()
    debug = False
    for i in range(10):
        img = ImageGrab.grab()
        # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
        # img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
        img.save("1.png")
    end = time.time()
    print(end - beg)


def draw2():
    """
    速度快
    :return:
    """
    def window_capture(filename):
        hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        # print w,h　　　#图片大小
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, filename)

    beg = time.time()
    for i in range(10):
        window_capture("haha.jpg")
    end = time.time()
    print(end - beg)

if __name__ == '__main__':
    draw2()
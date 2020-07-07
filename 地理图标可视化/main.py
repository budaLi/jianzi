# @Time    : 2020/6/27 16:56
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm
from pyecharts import Map


# 定义省份
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9,
                         '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7,
                         '内蒙古': 3, '重庆': 3,'云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1,
                         '天津': 1,'其他': 1}


def draw():
    # 获取省份
    provice = list(province_distribution.keys())
    # 每个省份队对应的值
    values = list(province_distribution.values())

    #设置地图的大小
    map = Map("中国地图",width=1200, height=600)

    # 添加地图
    map.add("", provice, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
      visual_text_color='#000',is_label_show=True)

    #生成html
    map.render(path="中国地图.html")
    print("中国地图生成完毕")


def draw2():
    map2 = Map("贵州地图", '贵州', width=1200, height=600)
    city = ['贵阳市', '六盘水市', '遵义市', '安顺市', '毕节市', '铜仁市', '黔西南布依族苗族自治州', '黔东南苗族侗族自治州', '黔南布依族苗族自治州']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]
    map2.add('贵州', city, values2, visual_range=[1, 10], maptype='贵州', is_visualmap=True, visual_text_color='#000')

    map2.render(path="贵州地图.html")
    print("贵州地图生成完毕")


def draw3():
    from pyecharts import Map

    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ["China", "Canada", "Brazil", "Russia", "United States"]
    map0 = Map("世界地图示例", width=1200, height=600)
    map0.add("世界地图", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    map0.render(path="世界地图.html")
    print("世界地图生成完毕")


if __name__ == '__main__':

    draw()# 中国地图
    draw2() # 贵州地图
    draw3() # 世界地图
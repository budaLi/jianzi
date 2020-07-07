#导入自动化框架模块
from selenium import webdriver
import time
import csv
#导入拼音库
from pypinyin import pinyin
#提供字符数据库的访问
import unicodedata

# 定义一个类
class FindJob:
    #类的初始化/爬取哪个职位、哪个城市、爬取多少页
     def __init__(self,keyword,city,page):
         self.keyword=keyword
         self.city=city
         self.page=page
#
     #设计一个爬取内容的主方法
     def run(self):
        #启动Chrome浏览器,由于没有把浏览器驱动目录加入环境变量Path中，所以需要指明浏览器安装位置
         input(f'启动Chrome浏览器前，请您确保程序中已正确填入浏览器路径，已填入请按回车继续查询，否则填入正确路径后在查询')
         print(f'正在启动浏览器查询...')
         time.sleep(2)
         driver=webdriver.Chrome(r'chromedriver.exe')
         #设置一个全局的隐式的等待时间，0.5秒刷新一次，最长等待10秒
         driver.implicitly_wait(10)
         #打开51job网址
         print(f'您将要查询{self.city}的{self.keyword}岗位')
         print(f'正在打开网站.....')
         time.sleep(2)
         driver.get('http://www.51job.com')
         # 根据id选择元素，返回的就是该元素对应的WebElement对象,
         # 通过该 WebElement对象send_key，就可以对页面元素进行字符串输入操作了,比如输入Python
         #输入关键字
         driver.find_element_by_id('kwdselectid').send_keys(self.keyword)
         #点击查询按钮
         driver.find_element_by_id('work_position_input').click()
         #等待1秒确保页面稳定
         time.sleep(1)
         #去掉之前可能点击过的城市,返回值是一个列表
         needClearCityElements=driver.find_elements_by_css_selector('#work_position_click_multiple_selected > span')
         #通过循环方式获取列表的每一个元素并点击（点击一下就是清除一个元素）
         for element in needClearCityElements:
             element.click()
         #清除完获取的元素以后，获取所有可以查询的热门城市
         canChoiceCityElements=driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
         #首先设置目标城市为空，循环获取最终目标城市就是要去查询的城市，
         # 如果获取的城市和我们想要查询的城市相等，就把获取的城市赋给目标城市，退出循环
        #循环获取可以查询的每一个城市，当查询的这个城市等与我们传参数的城市时，
        # 把参数城市赋值给一开始为空的目标城市
         targetCityElement=None
         for targetCity in canChoiceCityElements:
             if targetCity.text==self.city:
                 targetCityElement=targetCity
                 break

         #如果目标城市不为空说明热门城市可以查询到，就点击确定按钮，否则不再热门。
         if targetCityElement is not None:
             print(f'{self.city}在热门城市列表，正在查询目标城市，请稍候.....')
             targetCityElement.click()
         else:
             print(f'{self.city}不在热门城市列表，正在查询目标城市，请稍候.....')
             #获取想要查询的城市的拼音
             unpopularTargetCityElement = pinyin(self.city)
             #循环只获取第一个拼音就break跳出循环
             for unpopularTargetCityFirstChinese in unpopularTargetCityElement:
                 #将城市名字的第一个拼音转化为字符串
                 unpopularTargetCityFirstLetter = ''.join(unpopularTargetCityFirstChinese)
                 break
            #截取字符串的第一个字母，并变大写
             unpopularTargetCityUpperLetterFirst= unpopularTargetCityFirstLetter[0:1].upper()
            #字母去声调
             res=unicodedata.normalize('NFKD',unpopularTargetCityUpperLetterFirst).encode('ascii','ignore')
             unpopularTargetCityUpperLetterLatter=res.decode()

             if unpopularTargetCityUpperLetterLatter in 'ABC':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_092200').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_092200 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'DEFG':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_091700').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_091700 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'HI':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_220200').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_220200 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'JK':
                 driver.find_element_by_css_selector('#work_position_click_center_left>#work_position_click_center_left_each_220900').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector('#work_position_click_center_right_list_220900 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                        targetCityElement = targetCity
                        break
             elif unpopularTargetCityUpperLetterLatter in 'LMN':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_300200').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_300200 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'OPQR':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_091000').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_091000 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'STU':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_171800').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_171800 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'VWX':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_100700').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_100700 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             elif unpopularTargetCityUpperLetterLatter in 'YZ':
                 driver.find_element_by_css_selector(
                     '#work_position_click_center_left>#work_position_click_center_left_each_102000').click()
                 canChoiceCityElements1 = driver.find_elements_by_css_selector(
                     '#work_position_click_center_right_list_102000 em')
                 for targetCity in canChoiceCityElements1:
                     if targetCity.text == self.city:
                         targetCityElement = targetCity
                         break

             #确定好目标城市，点击它
             targetCityElement.click()
         #选好目标城市后点击确定按钮
         driver.find_element_by_id('work_position_click_bottom_save').click()
         #点击搜索按钮
         driver.find_element_by_css_selector('div.ush > button').click()

         #打开文件
         with open("Find-Job.csv", 'w',newline='',encoding='gbk') as excelFile:
             #写标题行
             f_csv=csv.DictWriter(excelFile,
                                  ['职位名称',
                                   '公司名称',
                                   '工作地点',
                                   '薪资',
                                   '发布时间',
                                   ])
             f_csv.writeheader()
             #循环读取所有页
             for wantToReadPage in range(1,self.page+1):
                #获取页码位置
                 currentPageLocation=driver.find_element_by_id('jump_page')
                 #清空当前到第几页的数字
                 currentPageLocation.clear();
                 #设置页数为当前想要去读取的页
                 currentPageLocation.send_keys(str(wantToReadPage))
                 #获取确定按钮位置并点击确定
                 driver.find_element_by_css_selector('span.og_but').click()
                 time.sleep(1)
                 # 调用处理每一页数据的方法，处理每一页信息
                 onePageAllRows=self.handelOnePageInformations(driver)
                 #将每一页列表写入文件中
                 f_csv.writerows(onePageAllRows)
                 print(f'查询第{wantToReadPage}页完毕')
                 #判断是否是最后一页，因为有可能想要获取信息的页数多余了真正存在的页数，如果是最后一页就break
                 if self.isLastPage(driver):
                   break
         print(f'{self.city}所有{self.keyword}岗位已查询完，正往Find-Job文件中写入，稍候可在Find-Job中查看。')
         time.sleep(3)
         print(f'{self.city}所有{self.keyword}岗位已写入Find-Job文件中。')


     # 判断是否是最后一页的方法，如果是最后一页那“下一页”是灰色的，点不了，发现里面和有“下一页”时是不同的
     #下一页如果还有页面，那里面是有a链接到目标地址的
     def isLastPage(self,driver):
         #获取“下一页”按钮
         nextPageButton=driver.find_element_by_css_selector('div.dw_page li:last-child')
         #设置一个隐式的等待时间，0.5秒刷新一次，最长等待2秒
         driver.implicitly_wait(2)
         #判断“下一页”里面是否有a链接标签
         isHasALabel=nextPageButton.find_elements_by_tag_name('a')
         # 在设置为最初的10秒
         driver.implicitly_wait(10)
         if isHasALabel:#不是最后一页
             return False
         else:#是最后一页
             return True

     #处理每一页数据的方法/返回的是一个列表，列表的每一行是一个字典
     def handelOnePageInformations(self,driver):
         #定义一个空列表用来返回每一页数据，每一行是一个字典
         onePageAllRows=[ ]
        #获取每一页的全部信息
         eachPageWorkInformations=driver.find_elements_by_css_selector('#resultList div[class=el]')
         #循环获取每一行
         for eachCompanyWorkInformation in eachPageWorkInformations:
             #获取每一行中的所有属性
             eachCompanyAllAttributes=eachCompanyWorkInformation.find_elements_by_tag_name('span')
             #获取每一行属性的每一个属性值，返回值是列表
             stringeEachCompanyEachAttributes=[eachCompanyEachAttribute.text for eachCompanyEachAttribute in eachCompanyAllAttributes]
             print(stringeEachCompanyEachAttributes)
             for eachCompanyEachAttribute in eachCompanyAllAttributes:
                 eachCompanyEachAttributeUrl=eachCompanyEachAttribute
             #字典
             data={
                 "职位名称":stringeEachCompanyEachAttributes[0],
                  "公司名称":stringeEachCompanyEachAttributes[1],
                  "工作地点":stringeEachCompanyEachAttributes[2],
                  "薪资":stringeEachCompanyEachAttributes[3],
                  "发布时间":stringeEachCompanyEachAttributes[4],
             }
             onePageAllRows.append(data)
         return onePageAllRows


import pandas as pd

from pylab import *
import matplotlib.pyplot as plt

# 分析数据
def show():
    # 图像上显示中文
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    data = pd.read_csv(r"Find-Job.csv", encoding="gbk")

    # 察看表格信息
    # print(data.head())
    # 表格shape
    print(data.shape)

    # 统计缺失值信息
    print(data.isnull().sum())

    # 提取有用数据
    useful_data = data.iloc[:, 3]
    # # print(useful_data.shape)

    # # 去除空值
    useful_data = useful_data.dropna(how="any")
    print(useful_data.shape)

    # 只要月的数据
    useful_data = useful_data[useful_data.str.contains("月")]
    # 最高薪资
    useful_data_max = useful_data.str.replace("/月", "").str.split("-").str[1].map(
        lambda x: float(x.strip('千')) / 10 if ('千' in x) else float(x.strip('万')))
    useful_data_max.value_counts().plot(kind='barh', rot=0)
    plt.title("最高薪资/万")
    plt.show()

    # 最低薪资
    useful_data_min = useful_data.str.replace("/月", "").str.split("-").str[0].map(
        lambda x: float(x) / 10 if float(x) > 1 else float(x))
    useful_data_min.value_counts().plot(kind='barh', rot=0)
    plt.title("最低薪资/万")

    plt.show()

    print(useful_data)



keyword=(input("请您输入查询职位："))
city=(input("请您输入查询城市："))
page=(eval(input("请您输入查询页数：")))
FindJob(keyword,city,page).run()

show()
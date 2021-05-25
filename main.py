# coding: utf-8
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"


def open_br():
    """打开浏览器"""
    chromeOptions = webdriver.ChromeOptions()  # 设置代理
    chromeOptions.binary_location = 'Application/chrome.exe'
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
    # chromeOptions.add_argument('--incognito')
    br = webdriver.Chrome(executable_path='Application/chromedriver.exe', chrome_options=chromeOptions)
    br.maximize_window()
    return br


def wiat_tag(br, t, by, name):
    """封装webdriverwait"""
    tag = False
    try:
        tag = WebDriverWait(br, t).until(EC.presence_of_element_located((by, name)))
        return tag
    except Exception as e:
        return tag


def read_urls():
    """
    读取urls
    :return:
    """
    with open(r'urls.txt', 'r', encoding='utf-8') as f:
        urls = [str(i).strip() for i in f.readlines()]
        return urls


def main(main_url):
    id_rz = re.compile(r'id=(\d+)')
    br = open_br()
    urls = read_urls()
    br.get(main_url)
    input('请登录，按回车继续：')

    for index,url in enumerate(urls):
        print("index:{},url:{}".format(index,url))
        pid = id_rz.findall(url)
        if pid:
            pid = pid[0]
            while True:
                try:
                    br.get(url)
                    close_btn = wiat_tag(br, 8, By.CSS_SELECTOR, 'div[class="sufei-dialog-close"]')
                    video = wiat_tag(br, 8, By.CSS_SELECTOR, 'div[id="detail"]')
                    ztbtn = wiat_tag(br, 8, By.CSS_SELECTOR, 'ul[id="J_UlThumb"]')
                    if ztbtn:
                        try:
                            br.find_element_by_css_selector('ul[id="J_UlThumb"]').find_element_by_tag_name('li').click()
                            time.sleep(2)
                        except Exception as e:
                            print('点主图错误', e)

                    if close_btn and video:
                        time.sleep(2)
                        br.execute_script("""(function () {
                                                var btn1 = document.getElementsByClassName('sufei-dialog-close');
                                                var btn2 = document.getElementsByClassName('baxia-dialog-close');
                                                if (btn1.length > 0) {
                                                    btn1[0].click();
                                                } else if (btn2.length > 0) {
                                                    btn2[0].click();
                                                };
                                            
                                            })()""")
                        break
                    elif video and not close_btn:
                        break
                    else:
                        print('重试中...')
                except TimeoutException as e:
                    print(e)
            wiat_tag(br, 5, By.CSS_SELECTOR, 'span[class="tm-price"]')
            img_path = f'./img/{pid}.png'
            br.save_screenshot(img_path)
            print("save to {} ".format(img_path))

    br.quit()
    input('抓取完成')


if __name__ == '__main__':
    main_url = 'https://login.tmall.com/?spm=875.7931836/B.a2226mz.1.27bd4265t0mzp6&redirectURL=https%3A%2F%2Fwww.tmall.com%2F%3Fspm%3Da220o.1000855.0.0.187c14ccgEuMte'
    main(main_url)
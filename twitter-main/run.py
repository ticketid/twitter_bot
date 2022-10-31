import time
from selenium import webdriver
#在chrome浏览器目录输入chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"启动代理命令
from selenium.webdriver.common.by import By
from lxml import etree
import os
import sys
import setting
path = os.getcwd() +'/setting.py'
sys.path.append('/setting.py')


def xiala(path):
    all_list = []
    temp_height = 0
    # while True:
    for i in range(2):
        # 循环将滚动条下拉
        driver.execute_script("window.scrollBy(0,1000)")
        # sleep一下让滚动条反应一下
        time.sleep(0.8)
        # 获取当前滚动条距离顶部的距离
        check_height = driver.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        # 如果两者相等说明到底了
        # filters()

        tree = etree.HTML(driver.page_source, parser=etree.HTMLParser(encoding='utf-8'))
        lists = tree.xpath('//*[@data-testid="cellInnerDiv"]')
        with open(f'数据/{path}.txt', 'r', encoding='utf-8')as f:
            content = f.readlines()
            content = [i.replace('\n', '') for i in content]
        for i in lists:
            name = ''.join(i.xpath('./div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span/text()'))

            name = ''.join(i.xpath('./div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span/text()'))
            if name == '':
                continue
            if name not in content:
                with open(f'数据/{path}.txt', 'a', encoding='utf-8')as f:
                    f.write('\n' + u)
                    f.write('\n' + name)
                print('以下为新增关注', name, u)
                with open(f'数据/{path}新增关注.txt', 'a', encoding='utf-8')as f:
                    f.write('\n' + u)
                    f.write('\n' + name)
                print('保存成功')
        # print(all_list)
        if check_height == temp_height:
            # all_list = [i.replace('\n', '') for i in all_list]
            # return all_list
            return
        temp_height = check_height
    # all_list = [i.replace('\n', '') for i in all_list]
    # return all_list

option = webdriver.ChromeOptions()
option.add_experimental_option('debuggerAddress','127.0.0.1:9222')
driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)
url = setting.url

while 1:
    for u in url:
        print(u)
        path = u.split('/')[-2]
        if not os.path.exists(f'数据/{path}.txt'):
            open(f'数据/{path}.txt', 'w', encoding='utf-8')
        if not os.path.exists(f'数据/{path}新增关注.txt'):
            open(f'数据/{path}新增关注.txt', 'w', encoding='utf-8')
        try:
            driver.get(u)
            while 1:
                try:
                    if driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span'):
                        all_list = xiala(path)
                        break
                        # with open(f'数据/{path}.txt','r',encoding='utf-8')as f:
                        #     content = f.readlines()
                        #     content = [i.replace('\n', '') for i in content]
                        #     for name in all_list:
                        #         if name not in content:
                        #             if name != '':
                        #                 with open(f'数据/{path}.txt', 'a', encoding='utf-8')as f:
                        #                     f.write('\n' + u)
                        #                     f.write('\n' + name)
                        #             # if name not in content:
                        #                 print('以下为新增关注',name,u)
                        #                 with open(f'数据/{path}新增关注.txt', 'a', encoding='utf-8')as f:
                        #                     f.write('\n' + u)
                        #                     f.write('\n' + name)
                        #                 print('保存成功')
                        #
                        #     break
                except Exception as e:
                    # print(e)
                    continue
        except Exception as e:
            # print(e)
            continue


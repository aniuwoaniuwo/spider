#-*-coding:utf-8-*-
import time
from selenium import webdriver
import urllib.request
import re


driver=webdriver.Firefox()#获取驱动
driver.maximize_window()#窗口最大化
driver.get('http://jandan.net/ooxx/page-1')#模拟登陆网页
time.sleep(5)#给个两秒的延迟
x=1
print(driver.page_source)


for i in range(11):
    selector = driver.page_source  # 获取网页文本
    pattern = re.compile(r'<div class="text">.*?<p>.*?<img src="(.*?)".*?</p>', re.S)
    items = re.findall(pattern, selector)
    for item in items:
        print(item)
        print(x)
        urllib.request.urlretrieve(item,'c:\\pachong\\meizitu\\'+'%s.jpg' % x)
        x += 1
    #driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/a[3]').click()#点击下一页

    driver.find_element_by_xpath('//*[@id="comments"]/div[2]/div/a[1]').click()  #
    time.sleep(5)#5秒延迟



#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
import time
from selenium import webdriver
import urllib.request
from lxml import etree

import re

user="18813295794"
password="18898604973it"
driver=webdriver.Firefox()#获取驱动
driver.maximize_window()#窗口最大化
driver.get('http://radar.itjuzi.com//investevent')#模拟登陆网页
time.sleep(5)#给个两秒的延迟
driver.find_element_by_id('create_account_email').send_keys(user)
driver.find_element_by_id('create_account_password').send_keys(password)
driver.find_element_by_xpath('//*[@id="login_btn"]').click()
time.sleep(10)#给个两秒的延迟
selector = etree.HTML(driver.page_source)
for i in range(1):

    items = selector.xpath('/html/body/div[4]/div[2]/ul/li[2]/a/text()')
    #selector = driver.page_source  # 获取网页文本
    #pattern = re.compile(r'<span class="title"><a href=.*? target="_blank">(.*?)</a>.*?</span>', re.S)
    #items = re.findall(pattern, selector)
    for item in items:
        print(item)
    time.sleep(10)#5秒延迟



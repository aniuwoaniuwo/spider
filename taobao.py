#-*-coding:utf-8-*-
'''注意：模拟鼠标点击有错误！！！
运用selenium爬取淘宝吉他的评价
记得加一些反爬虫措施，否则爬取不到数据
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re
import xlrd
import xlwt
from lxml import etree
import time
class taobao():
    def __init__(self):
        self.tbjt=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.tbjt.add_sheet(u'淘宝',cell_overwrite_ok=True)
        sheetcount=(u'编号',u'时间','评价')
        for i in range(len(sheetcount)):
            self.sheet.write(0,i,sheetcount[i])
        self.tbjt.save('tbjt.xlsx')
    def spider(self):
        driver=webdriver.Firefox()
        driver.maximize_window()  # 窗口最大化
        driver.get('https://uland.taobao.com/sem/tbsearch?refpid=mm_15891853_2192459_8654707&keyword=%E5%A5%B3%E8%A3%85&clk1=315358d81a06b080c93ddffd4a756ba9&upsid=315358d81a06b080c93ddffd4a756ba9')
        driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()#点击登录按钮
        driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()  # 点击密码登录
        driver.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys("18813295794")  # 输入账号
        driver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys("18898604973tb")  # 输入密码
        driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()#点击登录
        time.sleep(10)
        driver.switch_to.default_content()#让wabdriver操纵当前页
        driver.find_element_by_xpath('//*[@id="q"]').click()

        driver.find_element_by_xpath('//*[@id="q"]').clear()#清空输入框
        driver.find_element_by_xpath('//*[@id="q"]').send_keys("Farida法丽达D10 D-10k R10")#搜索法丽达吉他

        driver.find_element_by_xpath('//*[@id="J_searchForm"]/input[4]').click()#点击搜索
        time.sleep(3)#给个延迟，不然加载不了，出错

        for handle in driver.window_handles:
            driver.switch_to_window(handle)#最后一个窗口才是我们要操作的窗口
        driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div[1]/a/div[2]/span').click()#点击第一个链接


        for handle in driver.window_handles:
            driver.switch_to_window(handle)
        time.sleep(10)  # 给足时间加载页面

        selector = etree.HTML(driver.page_source)
        action=driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div/div[1]/div/div[1]/ul/li[2]/a/em')
        ActionChains(driver).click_and_hold(action).perform()#模拟鼠标点击
        print(selector)
        pingluns=selector.xpath('/html/body/div[5]/div/div[4]/div/div[1]/div/div[5]/div/ul/li[1]/text()')
        print(2)
        for pinglun in pingluns:
                print(1,pinglun)


ff=taobao()
ff.spider()

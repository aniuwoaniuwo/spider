#-*-coding:utf-8-*-
#在售产品名称，类别，价格，过往价格（部分有），地理位置，词云
#利用selenium+requests请求，正则表达式+lxml来解析网页，csv保存，带有headers，暂时不需要cookies，代理，
#sleep太久也会报错，8秒容易报错，5秒不会

import time,csv
from selenium import webdriver
import urllib.request
import re,requests
from lxml import etree
import xlwt,xlrd,pymysql
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from lxml import etree
import xlwt,xlrd,re,json
from selenium.webdriver.common.proxy import Proxy, ProxyType

class Spider(object):
    def __init__(self):
        self.k=1
        self.n=1
        self.classifications = ['手机', '数码', '租房', '服装', '居家', '美妆', '运动', '家电', '玩具乐器']
        #第几页
        self.page=1
    def get_ip(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:
            return None

    def spider(self,url, time=time):
        m=0
        ip='61.161.46.179'
        port=8118
        proxies = self.get_ip()
        if proxies:
            items = re.findall('(.*?):(.*)', proxies)
            ip=items[0][0]
            port=items[0][1]
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", ip)
        ff_profile.set_preference("network.proxy.http_port", int(port))
        ff_profile.set_preference("network.proxy.ssl", ip)
        ff_profile.set_preference("network.proxy.ssl_port", int(port))
        ff_profile.set_preference("network.proxy.ftp", ip)
        ff_profile.set_preference("network.proxy.ftp_port", int(port))
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox()
        wait=WebDriverWait(driver,15)
        try:
            driver.maximize_window()#窗口最大
            driver.get(url)

            time.sleep(5)#给个五秒延迟,必须先定义，不能在函数中直接用
            for i in range(10,13):#九个类别
                self.n = i - 4
                submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.main > div.tabbar-wrap > div:nth-of-type({}) > p'.format(i))))#直到此元素可以点击
                print('开始爬取:{}'.format(self.classifications[self.n]))
                submit.click()#点击这个类别
                for j in range(100):
                    self.page=j+1
                    for g in range(1, 2):
                        height = 20000 * g  # 每次滑动20000像素
                        strWord = "window.scrollBy(0," + str(height) + ")"
                        driver.execute_script(strWord)
                        time.sleep(2)
                    s=driver.page_source
                    yield s
                    e=self.exit(driver,'//*[@id="tyc_banner_close"]')
                    if e==True:
                        print('有小弹窗')
                        driver.find_element_by_xpath('//*[@id="tyc_banner_close"]').click()
                    else:
                        print('无弹窗')
                    #点击下一页，延时5秒
                    driver.find_element_by_css_selector('body > div.main > div.pagination > div > button.btn-next > i').click()

                    time.sleep(5)
        except Exception as e:
            print(e)

    def exit(self,driver,css):#判断是否有小弹窗
        try:
            driver.find_element_by_xpath(css)
            return True
        except:
            return False

    def jiexi(self, response):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            pattern = re.compile(
                '<a.*?data-v-eab80fd8.*?href="(//2.*?)".*?_blank.*?>',
                re.S)
            items = re.findall(pattern, response)
            for item in items:
                item='http:'+item
                print('*****',self.classifications[self.n],'第{}页'.format(self.page),'*****')
                print(item)
                yield item
        else:
            return None

    def csv(self, item):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('xianyu.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([item,self.classifications[self.n]])

    def main(self):
        '''
        进程启动入口
        :return:
        '''
        start = time.time()
        urls = ['https://2.taobao.com/']
        for url in urls:
            for response in self.spider(url):
                for item in self.jiexi(response):
                    self.csv(item)
        end = time.time()
        data = end-start
        h = data // 3600
        yushu = data % 3600
        m = yushu // 60
        yushu = yushu % 60
        s = yushu
        print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))

if __name__=='__main__':
    f=Spider()
    f.main()
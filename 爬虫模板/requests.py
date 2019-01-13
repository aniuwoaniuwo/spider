#-*-coding:utf-8-*-
#requests+etree爬虫模板，带有headers，cookies，代理，数据库保存，txt保存，excel保存
import requests
import time
import re,os,pymysql,random
from lxml import etree
class Spider(object):
    def __init__(self):
        iplist = ['http://61.135.217.7:80']
        proxies = random.choice(iplist)
        proxies = {'http': proxies}
        print(proxies)
        self.proxies = proxies
        referer=''
        cookie=''
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
        self.headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}


    def spider(self,url):
        response=requests.get(url,headers=self.headers,proxies=self.proxies).text
        s=etree.HTML(response)
        members=s.xpath('')
        print(members)
    def txt(self):

    def excel(self):

    def base(self):
        

if __name__=='__main__':
    start=time.time()
    f=Spider()
    f.spider(url)
    end=time.time()
    print('总共花费的时间：',(end-start))
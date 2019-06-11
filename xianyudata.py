#-*-coding:utf-8-*-
#在售产品名称，类别，价格，过往价格（部分有），成色，地理位置，词云
#利用selenium+requests请求，正则表达式+lxml来解析网页，csv保存，带有headers，暂时不需要cookies，代理，
#sleep太久也会报错，8秒容易报错，5秒不会
#抓包不能爬取数据，因为ssl证书原因导致请求不了
#不能直接从notepad++复制到pycharm，会导致缩进的错误和未知的错误
#全局变量在多进程里面，每一个新进程都会等于重新调用整个函数（类），且是迭代完进去一个进程池里再运行每个进程
import re,csv
from lxml import etree
import time
import os,pymysql,random
import xlrd,xlwt
import requests,json
from multiprocessing import Pool

class Spider(object):
    def __init__(self):#这个适用非excel储存
        iplist = ['61.135.217.7:80']
        proxies = random.choice(iplist)
        self.user_agent_list = [
            'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
            'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
            'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
            'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
            'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
            'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
            'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
            'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
        ]
        proxies = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
        print(proxies)
        self.proxies = proxies
        self.referer = 'https://2.taobao.com/'

        #储存指数，使标题只能保存一次
        self.k=1
        #访问失败计数器
        self.n=0
        #访问成功计数器
        self.N=0
        #网页访问指数，达到4则放弃
        self.cu = 0
        #访问网址的总个数
        self.num=0
        #类别
        self.classification=2

    def get_ip(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:
            return None

    def spider(self,url):
        '''
        获取响应，返回响应
        :param url:
        :return:
        '''
        try:
            proxies = self.get_ip()
            if proxies:
                self.proxies = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
            user_agent = random.choice(self.user_agent_list)
            # print(user_agent)
            headers = {'User-Agent': user_agent}
            response = requests.get(url, headers=headers)
            # print(response.text)
            if response.status_code==200:
                self.cu = 0
                self.N+=1
                return response.text
            else:
                if self.cu<4:
                    self.cu+=1
                    print('出错了，重试第{}次'.format(self.cu))
                    self.spider(url)
                else:
                    self.cu = 0
                    self.n+=1
                    print('被封了，或者网页不存在,跳过')
                    return None
        except Exception as e:
            print(e)
            print('ip无效')
            print('出错了，重试第{}次'.format(self.cu))
            time.sleep(5)
            if self.cu < 4:
                self.cu += 1
                self.spider(url)
            else:
                self.n+=1
                print('被封了，或者网页不存在')

    def jiexi(self, response,classification,url):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            pattern = re.compile(
                '<div.*?main-wrap.*?title.*?>(.*?)</h1>.*?price big.*?<em>(.*?)</em>.*?para.*?<em>(.*?)</em>.*?para.*?<em>(.*?)</em>',
                re.S)
            items = re.findall(pattern, response)
            x=etree.HTML(response).xpath('//*[@id="J_Property"]/ul[1]/li[2]/span[2]/text()')[0]
            data=x if x else "无数据"
            items.append(data)
            items.append(classification)
            items.append(url)
            print(items)
            yield items
        else:
            return None

    def csv(self, items):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('xianyudata.csv', 'a', encoding='utf-8') as f:
            names = ['name','classification','nowprice','originalprice','colour','address','url']
            writer = csv.writer(f)
            if items[3]=='http://2.taobao.com/item.htm?id=592838761902':
                writer.writerow(names)
            print(items[0][0],items[2],items[0][1],items[1],items[0][2],items[0][3],items[3])
            writer.writerow([items[0][0],items[2],items[0][1],items[1],items[0][2],items[0][3],items[3]])

    def main(self,url,classification):
        '''
        进程启动入口
        :return:
        '''
        response=self.spider(url)
        # print('正在访问第{}个网址：'.format(self.num))
        # print('访问成功网址个数：{}'.format(self.N))
        # print('访问失败网址个数：{}'.format(self.n))
        # self.classification = row[1]
        if response:
            for items in self.jiexi(response,classification,url):
                #正在保存
                self.csv(items)

if __name__=='__main__':
    f=Spider()
    start = time.time()
    pool = Pool(processes=6)
    with open('xianyu.csv', 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        for row in reader:
            if row:
                pool.apply_async(f.main,(row[0],row[1],) )
        pool.close()  # 关闭进程池，不再接受新的进程
        pool.join()  # 主进程阻塞等待子进程的退出
    end = time.time()
    data = end - start
    h = data // 3600
    yushu = data % 3600
    m = yushu // 60
    yushu = yushu % 60
    s = yushu
    print('用时：{}时{}分{}秒'.format(h, m, s))
#-*-coding:utf-8-*-
#爬取珍爱网的数据，姓名，地址，年龄，身高，学历，简介，图片，网址
#响应的网址包含json这些格式，用正则会匹配不了甚至死机，没有代理先不多进程爬取，怕被封
#每个地方只有6页的人物上首页,反爬能力很弱，见过最弱的
#设定了一个阀值，请求超过4次就不再请求

import time,re,csv
from multiprocessing import Pool
import requests
from lxml import etree
class zhenaiwang(object):
    def __init__(self):
        self.cookies='sid=7d3dfec9-9f62-498d-813d-74ba203b4af8; token=1927645435.1553167936794.6b87b76c0bd3263e0ec65c4c9e2548ef; p=%5E%7Eworkcity%3D10101021%5E%7Esex%3D0%5E%7Emt%3D1%5E%7Enickname%3D%E4%BC%9A%E5%91%981927645435%5E%7Edby%3Da6818b805da69686%5E%7Elh%3D1927645435%5E%7Eage%3D28%5E%7E; isSignOut=%5E%7ElastLoginActionTime%3D1553167936794%5E%7E; mid=%5E%7Emid%3D1927645435%5E%7E; loginactiontime=%5E%7Eloginactiontime%3D1553167936794%5E%7E; live800=%5E%7EinfoValue%3DuserId%253D1927645435%2526name%253D1927645435%2526memo%253D%5E%7E; preLG_1927645435=2019-03-21+19%3A32%3A17; _pc_myzhenai_showdialog_=1; _pc_myzhenai_memberid_=%22%2C1927645435%22; Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2=1553168781; Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2=1553170198'
        self.user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
        self.headers={'User-Agent':self.user_agent,'Cookies':self.cookies}
        self.k=1
        #重试阀值
        self.cu=0
        self.urls=[]

    def geturl(self,url):
        '''
        每个城市都会有6页的推荐，先把每个城市的网址爬取出来，返回网址
        :param url:
        :return:
        '''
        response=requests.get(url,headers=self.headers).text
        for i in range(2,24):
            items=etree.HTML(response).xpath('//div[@class="cityList"]/dl')[i]
            items = items.xpath('./dd/a/@href')
            for item in items:
                self.urls.append(item)
        return self.urls

    def spider(self,url):
        '''
        获取响应，返回响应
        :param url:
        :return:
        '''
        try:
            response=requests.get(url,headers=self.headers)
            if response.status_code==200:
                self.cu = 0
                return response.text
            else:
                if self.cu<4:
                    self.cu+=1
                    print('出错了，重试')
                    self.spider(url)
                else:
                    self.cu = 0
                    print('被封了，或者网页不存在,跳过')
                    return None
        except Exception as e:
            print(e)
            print('太频繁了，等待5s')
            time.sleep(5)
            if self.cu < 4:
                self.cu += 1
                self.spider(url)
            else:
                print('被封了，或者网页不存在')

    def jiexi(self,response):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            pattern1 = re.compile('</head><body(.*?)珍爱首页', re.S)
            HTML = re.findall(pattern1, response)[0]
            pattern = re.compile(
                '<div.*?f-item.*?>.*?href="(.*?)".*?src="(.*?)".*?f-nickname.*?>(.*?)<span.*?t-info.*?>(.*?)\|(.*?)\|(.*?)</pre.*?c-tag.*?tag.*?>(.*?)</div.*?tag.*?>(.*?)</div.*?t-introduce.*?>(.*?)</div>',
                re.S)
            items = re.findall(pattern,HTML)
            for item in items:
                yield item
        else:
            return None

    def save(self,item):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('zhenai.csv','a',encoding='utf-8') as f:
            names=['名字','头像','地址','年龄','身高','婚姻状况','学历','简介','主页']
            writer=csv.writer(f)
            if self.k==1:
                writer.writerow(names)
                self.k+=1
            writer.writerow([item[2],item[1],item[4],item[3],item[5],item[6],item[7],item[8],item[0]])

    def main(self,url,j):
        '''
        进程启动入口
        :return:
        '''
        print('爬取第{}个城市'.format(j))
        urls=['/nv/{}'.format(i) for i in range(1,7)]
        for url1 in urls:
            response=self.spider(url+url1)
            for item in self.jiexi(response):
                self.save(item)
            time.sleep(4)
if __name__=='__main__':
    f=zhenaiwang()
    urls=f.geturl('http://m.zhenai.com/zhenghun/')
    print('总共{}城市'.format(len(urls)))
    print(urls)
    pool=Pool(processes=4)
    for i in range(len(urls)):
        pool.apply_async(f.main,(urls[i],i,))
    pool.close()
    pool.join()
# -*-coding:utf-8-*-
# 利用requests请求,采用了异步的方法加快爬取速度，因为异步还是不是非常了解，所以只是用了函数没有采用类的方法，正则表达式来解析网页，TXT、excel、数据库保存，其中的excel还是采用类的方法，带有headers，cookies，代理，

import time
import re
import asyncio
import aiohttp
import random
import requests
import os
import itchat
import pymysql
import xlrd, xlwt, json, csv
from lxml import etree
import csv, json
class Spider(object):
    def __init__(self):#这个适用非excel储存
        '''
        类的变量
        '''
        self.referer = ' '
        self.cookie = ' '
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
        #响应池
        self.res_list=[]
        self.headers = {}

    async def creat_joke(self,url, semaphore):
        '''
        获取响应，返回响应
        :param url:
        :return:
        '''
        async with semaphore:
            global proxies
            try:
                user_agent = random.choice(self.user_agent_list)
                self.headers = {'User-Agent': user_agent, 'Referer': self.referer, 'Cookie': self.cookie}
                async with aiohttp.ClientSession() as session:
                    #get无proxies代理可以设置
                    async with session.get(url, headers=self.headers) as res:
                        # assert res.status == 200
                        # self.res_list.append(await res.text)
                        if res.status == 200:
                            self.res_list.append(await res.text())
            except Exception as e:
                # print(e)
                print('ip出错了')
            # proxies转为全局变量
            # global proxies
            # try:
            #     if len(self.iplist):
            #         proxies = random.choice(self.iplist)
            #     else:
            #         proxies = self.get_ip()
            #         self.iplist.append(proxies)
            #     if proxies:
            #         self.ip = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
            #     user_agent = random.choice(self.user_agent_list)
            #     self.headers = {'User-Agent': user_agent, 'Referer': self.referer, 'Cookie': self.cookie}
            #     async with aiohttp.ClientSession() as session:
            #         async with session.get(url, headers=self.headers, proxies=self.ip) as res:
            #                 # assert res.status == 200
            #                 # self.res_list.append(await res.text)
            #                 if res.status == 200:
            #                     self.urlerror = 0
            #                     self.iperror = 0
            #                     self.iplist.append(proxies)
            #                     self.res_list.append(await res.text())
            #                 else:
            #                     if self.urlerror < 3:
            #                         self.urlerror += 1
            #                         print('出错了，重试第{}次'.format(self.urlerror))
            #                         self.spider(url)
            #                     else:
            #                         self.urlerror = 0
            #                         self.iperror = 0
            #                         print('网页不存在,跳过')
            # except Exception as e:
            #     # print(e)
            #     print('ip出错了，重试第{}次'.format(self.iperror))
            #     # time.sleep(5)
            #     if self.iperror < 4:
            #         self.iperror += 1
            #         self.spider(url)
            #     else:
            #         # self.iplist.pop(0)
            #         self.iplist.remove(proxies)
            #         print('ip被封了,或者ip无效,应该移除')
            #         self.urlerror = 0
            #         self.iperror = 0
            #         self.spider(url)


    def get_ip(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:
            return None

    def jiexi(self,response):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            s = etree.HTML(response)
            td = s.xpath('//*[@id="main"]/div[5]/ul/li')
            for p in td:
                title = p.xpath('./div[2]/h3/a/text()')
                author = p.xpath('.div[2]/div/a/text()')
                time = p.xpath('.div[2]/div/span/text()')
                content = p.xpath('.div[2]/p/text()')
                address = p.xpath('./div[2]/h3/a/@data-share')
                title = title[0] if len(title) > 0 else 'null'
                author = author[0] if len(author) > 0 else 'null'
                time = time[0] if len(time) > 0 else 'null'
                content = content[0] if len(content) > 0 else 'null'
                address = address[0] if len(address) > 0 else 'null'
                yield [title, author, time, content, address]
        else:
            return None


    def txt(self,item):
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            f.write(item[0])
            f.write(item[1])


    def csv(self,item, k):
        '''
        保存数据到csv
        :param item:
        :param k:
        :param items:
        :return:
        '''
        with open('zhenai.csv', 'a', encoding='utf-8') as f:
            names = ['title', 'author', 'time', 'content', 'address']
            writer = csv.writer(f)
            if k == 1:
                writer.writerow(names)
                k += 1
            writer.writerow([item[0], item[1], item[2], item[3], item[4]])


    def json(self,item):
        '''
        保存数据
        :param response:
        :return:
        '''
        item = {'item0': item[0], 'item1': item[1]}
        with open('sfd.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, indent=2, ensure_ascii=False))
            f.write(',')


    def base(self,item):
        if item:
            db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')  # db选择相应的数据库名称
            cursor = db.cursor()
            data = {
                'name': item[0],
                'score': item[1],
                'good': 0
            }
            table = 'musics'
            keys = ','.join(data.keys())
            values = ','.join(['%s'] * len(data))
            update = ','.join([" {key}=%s".format(key=key) for key in data])  # 注意空格
            sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                                values=values)
            sql = sql + update
            try:
                if cursor.execute(sql, tuple(data.values()) * 2):  # 这是格式，第二个参数要有
                    # if cursor.execute(sql,(title[i],score[i],renshu[i])):
                    print('成功')
                    db.commit()  # 执行保存
            except:
                db.rollback()
                print('失败！')
        pass


    def main(self):
        start = time.time()
        url_list = ['http://www.qiushibaike.com/hot/page/{}/'.format(str(k)) for k in range(1, 31)]  # format放在引号外面
        loop = asyncio.get_event_loop()
        semaphore = asyncio.Semaphore(500)  # 限制并发量为500,默认509，linux默认1024，避免并发太多报错或者系统负担太大
        tasks = [self.creat_joke(host, semaphore) for host in url_list]
        loop.run_until_complete(asyncio.wait(tasks))
        for response in res_list:
            for item in jiexi(response):
                txt(item)
        print("joke爬取完成")
        end = time.time()
        data = end - start
        h = data // 3600
        yushu = data % 3600
        m = yushu // 60
        yushu = yushu % 60
        s = yushu
        print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))


if __name__ == '__main__':
    f=Spider()
    f.main()
    # creat_joke()26.849535703659058
    # 2.0631182193756104异步的速度真的快，比多进程快多了，哈哈哈
    # send_news()

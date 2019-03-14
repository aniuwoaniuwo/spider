#-*-coding:utf-8-*-
#利用requests请求,采用了异步的方法加快爬取速度，因为异步还是不是非常了解，所以只是用了函数没有采用类的方法，正则表达式来解析网页，TXT、excel、数据库保存，其中的excel还是采用类的方法，带有headers，cookies，代理，

import time
import re
import asyncio
import aiohttp
import random
import requests
import os
import itchat
import pymysql
import xlrd,xlwt
async def creat_joke(url,res_list):
    print("开始爬取joke")
    iplist = ['61.135.217.7:80']
    proxies = random.choice(iplist)
    # proxies = {'http': proxies}
    proxies = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
    print(proxies)
    referer = ' '
    cookie = ' '
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
    headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers,proxies=proxies) as res:
            assert res.status==200
            res_list.append(await res.text())
def txt(response):
    pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
    items = re.findall(pattern, response)
    for i in range(0, len(items)):
        a = items[i].replace('<br/>', '')
        with open("yibuqiushi.txt", "a", encoding='utf-8') as f:  # a是追加,要加上第三个参数，否则读取不了
            f.write(a + "\n")
    #time.sleep(3)

def base(response):
    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')  # db选择相应的数据库名称
    cursor = db.cursor()

    pattern = re.compile(r'<a href="(/chapter/.*?)"', re.S)
    titles = re.findall(pattern, response)
    pattern1 = re.compile(r'<title>(.*?)</title>')
    scores = re.findall(pattern1, response)
    pattern2 = re.compile(r'<title>(.*?)</title>')
    renshus = re.findall(pattern2, response)
    pattern3 = re.compile(r'<title>(.*?)</title>')
    qitas = re.findall(pattern3, response)
    pattern4 = re.compile(r'<title>(.*?)</title>')
    tupians = re.findall(pattern4, response)

    for i in range(0, len(titles)):

        title = titles[i]
        score = scores[i]
        renshu = renshus[i]
        qita = qitas[i]
        tupian = tupians[i]

        data = {}
        data = {
            'name': title,
            'score': score,
            'good': renshu
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


class Spider(object):
    def __init__(self):  # 这个是适用excel储存
        self.shuju = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.shuju.add_sheet(u'列表', cell_overwrite_ok=True)
        sheetcount = (u'编号', u'地址', u'标题', u'价格')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.shuju.save('xlsx.xlsx')

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style

    def excel(self,response):
        pattern = re.compile(r'<a href="(/chapter/.*?)"', re.S)
        dizhis = re.findall(pattern, response)
        pattern1 = re.compile(r'<title>(.*?)</title>')
        biaotis = re.findall(pattern1, response)
        pattern2 = re.compile(r'<title>(.*?)</title>')
        jiages = re.findall(pattern2, response)
        for i in range(0, len(dizhis)):
            data = []  # 建立空的list
            dizhi = dizhis[i]
            biaoti = biaotis[i]
            jiage = jiages[i]
            data.append(m + 1)
            data.append(dizhi)
            data.append(biaoti)
            data.append(jiage)
            for j in range(0, len(data)):
                self.sheet.write(m + 1, j, data[j])
            m = m + 1
            print(m)
            self.shuju.save('58tongcheng.xlsx')



def main():
    start=time.time()
    url_list = ['http://www.qiushibaike.com/hot/page/{}/'.format(str(k)) for k in range(1, 31)]  # format放在引号外面
    loop=asyncio.get_event_loop()
    res_list=[]
    tasks=[creat_joke(host,res_list) for host in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    for response in res_list:
        txt(response)
        #base(response)
    print("joke爬取完成")
    print((time.time() - start))
main()
#creat_joke()26.849535703659058
#2.0631182193756104异步的速度真的快，比多进程快多了，哈哈哈
#send_news()
#-*-coding:utf-8-*-
#利用requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，cookies，代理，
import re
import time
import os,pymysql,random
import xlrd,xlwt
import requests

class Spider(object):
    def __init__(self):#这个适用非excel储存
        iplist = ['61.135.217.7:80']
        proxies = random.choice(iplist)
        # proxies = {'http': proxies}
        proxies = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
        print(proxies)
        self.proxies = proxies
        referer=' '
        cookie=' '
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
        self.headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}


    '''def __init__(self):#这个是适用excel储存
		self.m=0
        iplist = ['61.135.217.7:80']
        proxies = random.choice(iplist)
        # proxies = {'http': proxies}
        proxies = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
        print(proxies)
        self.proxies = proxies
        referer=' '
        cookie=' '
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
        self.headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}
        self.shuju = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.shuju.add_sheet(u'列表', cell_overwrite_ok=True)
        sheetcount = (u'编号', u'地址', u'标题', u'价格')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.shuju.save('xlsx.xlsx')'''

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style
    def spider(self,url):
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
        pattern = re.compile(r'<a href="(/chapter/.*?)"', re.S)
        shuju = re.findall(pattern, response)[0]
        pattern1 = re.compile(r'<title>(.*?)</title>')
        shujus = re.findall(pattern1, response)
        for shuju in shujus:
            print(shuju)

    def txt(self,url):
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
        pattern = re.compile(r'<a href="(/chapter/.*?)"', re.S)
        shuju = re.findall(pattern, response)[0]
        pattern1 = re.compile(r'<title>(.*?)</title>')
        shujus = re.findall(pattern1, response)
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            for content in range(0,len(shujus)):
                print(content)
                f.write(content)
    def excel(self):
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
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
            data.append(self.m + 1)
            data.append(dizhi)
            data.append(biaoti)
            data.append(jiage)
            for j in range(0, len(data)):
                self.sheet.write(self.m + 1, j, data[j])
            self.m = self.m + 1
            print(self.m)
            self.shuju.save('58tongcheng.xlsx')
    def base(self,url):
        db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')  # db选择相应的数据库名称
        cursor = db.cursor()
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
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

        for i in range(0,len(titles)):

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
if __name__=='__main__':
    start=time.time()
    urls = ['https://music.douban.com/top250?start={}'.format(i * 25) for i in range(1, 20)]
    for url in urls:
        f=Spider()
        f.spider(url)
    end=time.time()
    print('总共花费的时间：',(end-start))
#-*-coding:utf-8-*-
#requests+etree爬虫模板，带有headers，cookies，代理，数据库保存，txt保存，excel保存
import requests
import time
import re,os,pymysql,random
from lxml import etree
import xlrd,xlwt
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
        response=requests.get(url,headers=self.headers,proxies=self.proxies).text
        s=etree.HTML(response)
        members=s.xpath('')
        print(members)

    def txt(self,url):
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
        s = etree.HTML(response)
        contents = s.xpath('')
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            for content in range(0,len(contents)):
                print(content)

                f.write(content)


    def excel(self):
        m=0
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
        s = etree.HTML(response)

        dizhis = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/p[2]/a[2]/text()')  # li地址
        biaotis = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/h2/a/text()')  # 标题的内容
        jiages = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[3]/div[2]/b/text()')  # 租房价格
        # print(dizhis,biaotis,jiages)
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
    def base(self):
        db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')#db选择相应的数据库名称
        cursor = db.cursor()
        response = requests.get(url, headers=self.headers, proxies=self.proxies).text
        s = etree.HTML(response)
        td = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')

        for p in td:

            title = p.xpath('./td[2]/div/a/text()')
            score = p.xpath('./td[2]/div/div/span[2]/text()')
            renshu = p.xpath('./td[2]/div/div/span[3]/text()')
            qita = p.xpath('./td[2]/div/p/text()')
            tupian = p.xpath('./td[1]/a/img/@src')

            title = title[0] if len(title) > 0 else ''
            score = score[0] if len(score) > 0 else ''
            renshu = renshu[0] if len(renshu) > 0 else ''
            qita = qita[0] if len(qita) > 0 else ''
            tupian = tupian[0] if len(tupian) > 0 else ''
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
        url=' '
        f=Spider()
        f.spider(url)
    end=time.time()
    print('总共花费的时间：',(end-start))
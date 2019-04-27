#-*-coding:utf-8-*-
#利用requests请求,采用了多进程的方法加快爬取速度，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，cookies，代理，
import re
import time,json,csv
import re,os,pymysql,random
import xlrd,xlwt
import requests
from multiprocessing import Pool,Process

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
        self.k=1
        self.n=0
        self.cu = 0

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
            response = requests.get(url, headers=self.headers, proxies=self.proxies)
            if response.status_code==200:
                self.cu = 0
                return response.text
            else:
                if self.cu<4:
                    self.cu+=1
                    print('出错了，重试第{}次'.format(self.cu))
                    self.spider(url)
                else:
                    self.cu = 0
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
                print('被封了，或者网页不存在')

    def jiexi(self, response):
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
            items = re.findall(pattern, HTML)
            for item in items:
                yield item
        else:
            return None

    def txt(self,item):
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            f.write(item[0])
            f.write(item[1])

    def csv(self, item):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('wxouguan.csv', 'a', encoding='utf-8') as f:
            names = ['title', 'author','time','content','address']
            writer = csv.writer(f)
            if self.k == 1:
                writer.writerow(names)
                self.k += 1
            writer.writerow([item[0],item[1],item[2],item[3],item[4]])

    def json(self,item):
        '''
        保存数据
        :param response:
        :return:
        '''
        item={'item0':item[0],'item1':item[1]}
        with open('sfd.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, indent=2, ensure_ascii=False))
            f.write(',')

    def excel(self,item):
        for j in range(0, len(item)):
            self.sheet.write(self.n + 1, j, item[j])
            self.n+=1
            print(self.n)
            self.shuju.save('58tongcheng.xlsx')

    def base(self,item):
        if item:
            db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')#db选择相应的数据库名称
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
            sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values)
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

    def main(self,url):
        '''
        进程启动入口
        :return:
        '''
        response = self.spider(url)
        for item in self.jiexi(response):
            self.txt(item)
        time.sleep(4)

if __name__=='__main__':
    start = time.time()
    f = Spider()
    urls=[]
    pool = Pool(processes=4)
    for i in range(len(urls)):
        pool.apply_async(f.main, (urls[i],))
    pool.close()#关闭进程池，不再接受新的进程
    pool.join()#主进程阻塞等待子进程的退出
    end = time.time()
    print('总共花费的时间：', (end - start))

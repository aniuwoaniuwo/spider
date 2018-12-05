#-*-coding:utf-8-*-
import requests
import time
import pymysql
from lxml import etree
from multiprocessing import Pool, Lock, Process
import os


'''多进程的时间缩短了，可是存在xlsx这里会出错，因为各个进程基本同时进行，同时打开了xlsx，不能同时操作xlsx来保存数据，只保存了一个进程的数据，不过ide上打印出了所有的数据，考虑txt保存或者存入数据库或者加Lock就可以解决当前问题!!!经过验证，用TXT也不能解决，同样的原因。'''
'''经过验证，多进程存到数据库可以缩短时间'''



def geturl(i):

    #print('now running process:%s' % os.getpid())

    url = 'https://music.douban.com/top250?start={}'.format(i * 25)
    #re = i * 25
    getxpath(url)


def getxpath(url):
    if url is None:
        return None

    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')
    cursor = db.cursor()

    proxies = {
        'http': 'http://124.72.109.183:8118'

    }
    cookie = 'll = "118288";bid = CFXSFuC2 - o8;ps = y;ap_v = 0, 6.0;dbcl2 = "167986306:/8RFXuXSZKo";ck = xdv3;_vwo_uuid_v2 = DCF442F5C0A235FB578E77DBF12FFED3A | 9b84a1e7866efa3ab0debcf4546f59f9;push_noty_num = 0;push_doumail_num = 0'
    referer = 'https: // www.douban.com / accounts / login?source = music'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
    headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}
    html = requests.get(url, headers=headers, timeout=3, proxies=proxies).text
    td = etree.HTML(html).xpath('//*[@id="content"]/div/div[1]/div/table/tr')

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
            'name':title,
            'score':score,
            'good':renshu
        }
        table = 'musics'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        update = ','.join([" {key}=%s".format(key=key) for key in data])  # 注意空格
        sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
        sql=sql + update
        try:
            if cursor.execute(sql, tuple(data.values()) * 2):  # 这是格式，第二个参数要有
                # if cursor.execute(sql,(title[i],score[i],renshu[i])):
                print('成功')
                db.commit()  # 执行保存
        except:
            db.rollback()
            print('失败！')

if __name__ == '__main__':
    start = time.time()
    #db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306,db='douban')
    #cursor=db.cursor()#不能再这里链接数据库，这是主进程，子进程里面并没有连接，所以不能执行数据库操作

    #lock = Lock()
    #print('now running process:%s' % os.getpid())

    p=Pool(4)

    for f in range(1,11):
        p.apply_async(geturl, args=( f,))

        #p.start()
    #p.join()
    p.close()
    p.join()
    end = time.time()
    print((end - start))  # 用了19.56002712249756秒，现在对比多进程爬虫










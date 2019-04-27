#-*-coding:utf-8-*-
from multiprocessing import Pool,Lock,Process
import time
import requests
import re
import json
import pymysql
def spider(i):
    proxies = {'http': 'http://115.46.66.18:8123'}
    headers = {
    'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=580000998253&userNumId=2529466216&currentPageNum={}&_ksTS=1545448307516_2832&callback=jsonp_tbcrate_reviews_list'.format(i)
    response=requests.get(url,headers=headers).text
    print(requests.get(url,headers=headers).text)
    k=20*i
    save(response,k)
def save(res,k):
    print(res)
    db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306,database='spider')
    cursor=db.cursor()
    jsons = re.findall(r'{.*}', res)[0]  # 除去json格式外的东西，匹配出来是list
    json1 = json.loads(jsons)  # 这是一个字典模式，把字典变成json格式然后 可以用json的函数
    print(json1)
    comment2 = json1.get('comments')
    print(comment2)
    data = {}
    for comment in comment2:
        comment1 = comment.get('content')
        if comment1:
            print(comment1)
            data['id'] = k  # 储存到mysql数据库
            k+=1
            data['comment'] = comment1
            table = 'tbcomment'
            keys = ','.join(data.keys())
            values = ','.join(['%$'] * len(data))
            sql = 'INSERT INTO {table}({keys}) values({values}) on duplicate key update'.format(table=table, keys=keys,
                                                                                                values=values)
            update = ','.join([" {key}=%$".format(key=key) for key in data])
            sql = sql + update
            try:
                if cursor.execute(sql, tuple(data.values()) * 2):
                    print('successful')
                    db.commit()
            except:
                print('failed')
                db.rollback()
        else:
            print('wrong')
if __name__=='__main__':
    start=time.time()
    #lock=Lock()
    for i in range(1,5):
        print('正在爬取第{}页的评论'.format(i))
        p=Process(target=spider,args=(i,))
        p.start()
    p.join()#不能放在循环里面，这样会导致子进程执行完才能运行主进程，就形成了加锁的功效一个进程完再做另外一个进程
    end=time.time()
    print('总共花费的时间为')
    print((end-start))
    
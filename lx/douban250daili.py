'''BeautifulSoup爬取豆瓣音乐前250的专辑名称、评分、点赞人数,保存到mysql数据库，还有生成ip的方法'''
from bs4 import BeautifulSoup
import requests
import random
from lxml import etree
import pymysql



def createbase():
    db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306)
    cursor=db.cursor()
    cursor.execute("CREATE  DATABASE douban DEFAULT CHARACTER SET utf8")
    cursor.close()
def createtable():
    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306,db='douban')
    cursor = db.cursor()
    #not null表示不能留空
    cursor.execute("CREATE TABLE IF NOT EXISTS musics (name VARCHAR(255) NOT NULL,score VARCHAR(255) NOT NULL,good VARCHAR(255) NOT NULL,PRIMARY KEY (name) )")
    cursor.close()

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def main():
    url='https://music.douban.com/top250'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'

    headers = {'User-Agent': user_agent}
    html = requests.get(url, headers=headers, timeout=3).text

    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306,db='douban')#连接豆瓣这个数据库
    cursor = db.cursor()#连接游标


    s=etree.HTML(html)
    title=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')
    score=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')
    renshu=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')
    for i in range(25) :
        data={}
        print(title[i],score[i],renshu[i])
        data={
            'name':title[i],
            'score':score[i],
            'good':renshu[i]
        }
        table='musics'
        keys=','.join(data.keys())
        values=','.join(['%s']*len(data))
        update=','.join([" {key}=%s".format(key=key) for key in data])#注意空格
        sql='INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
        #sql = 'INSERT INTO musics(name,score,good) VALUES(%s,%s,%s)'
        sql=sql+update
        try:
            if cursor.execute(sql,tuple(data.values())*2):#这是格式，第二个参数要有
            #if cursor.execute(sql,(title[i],score[i],renshu[i])):
                print('成功')
                db.commit()#执行保存
        except:
            db.rollback()
            print('失败！')
if __name__ == '__main__':
    #createbase()
    #createtable()
    main()
    '''url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    print(proxies)

proxies = {
            'http': 'http://124.72.109.183:8118',
            'http': 'http://49.85.1.79:31666'

}'''


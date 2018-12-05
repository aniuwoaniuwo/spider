#-*-coding:utf-8-*-
import time
import urllib.request
import re
import requests
from lxml import etree

def geturl(url,referers,x):
    #url='http://jandan.net/ooxx/page-33#comments'
    user_agent='Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 58.0.3029.110Safari / 537.36SE2.XMetaSr1.0'
    #referer='http://jandan.net/ooxx/page-33'
    referer=referers

    accept='text/html,application/xhtml+xml,application/xml;q = 0.9,image/webp,*/*;q =0.8'
    accept_encoding='gzip, deflate, sdch'
    accept_language='zh-CN,zh;q=0.8'
    connection='keep-alive'
    host='jandan.net'
    proxies = {
        'http': 'http://124.72.109.183:8118'

    }
    headers={'User-Agent':user_agent,'Referer':referer,'Accept':accept,'Accept-Encoding':accept_encoding,'Accept-Language':accept_language,'Connection':connection,'Host':host}
    response=requests.get(url,headers=headers,timeout=3).text
    #print(response)
    #s=etree.HTML(response)
    #items=s.xpath('//*[@id="comment-3973150"]/div/div/div[2]/p/img/@src')
    pattern=re.compile(r'<div class="text">.*?<p>.*?<img src="(.*?)".*?</p>',re.S)
    items=re.findall(pattern,response)

    for item in items:
        print(item)
        #urllib.request.urlretrieve(item,'c:\\pachong\\meizitu\\'+'%s.jpg' % x)
        x+=1
        print(x)
def getpage():
    for i in range(31,32):
        print(i)
        url='http://jandan.net/ooxx/page-{}#comments'.format(i)
        referer='http://jandan.net/ooxx/page-{}'.format(i)
        x=1
        geturl(url,referer,x)
        time.sleep(5)
if __name__=='__main__':
    start=time.time()
    getpage()
    end=time.time()
    print('总共用时：',(end-start))
    #http://wx3.sinaimg.cn/mw600/0076BSS51v1fvjkoazy6fj311v1jk1kx.jpg
    '''更新referer的函数
    def update_header(referer):
           header['Referer'] = '{}'.format(referer)

....
            pic_src = soup.find('div', 'main-image').find('img')['src']
            pic_name = pic_src.split('/')[-1]
            update_header(pic_src)
            f = open(pic_name, 'wb')
            f.write(requests.get(pic_src, headers=header).content)
            f.close()'''


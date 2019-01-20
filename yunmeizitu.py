#-*-coding:utf-8-*-
#这是一个爬取煎蛋妹子图的程序，可以挂在云服务器一直运行，每晚10点爬取最新一天的上传的美女图
#用到了requests、lxml、正则、bs4抓取，同时设置定时，图片的链接加了密，首先需要解密，这里参考了别人的方法
import requests
from bs4 import BeautifulSoup
import hashlib
import base64
import requests
import time
import re,random
from lxml import etree
import urllib.request
class Spider(object):
    def __init__(self):
        self.g=0#运行第一天爬取的图片是否为最近一天上传的参数
        self.k=0#运行到第二天爬取的图片是否为最近一天上传的参数，为1则说明已经爬取过了
        self.x = 1
        self.urllist=[]#保存图片链接
        iplist = ['http://61.135.217.7:80']#这个适用非excel储存
        proxies = random.choice(iplist)
        proxies = {'http': proxies}
        print(proxies)
        self.proxies = proxies
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Referer': 'http://jandan.net/ooxx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Cookie': '__cfduid=d0f8f8aef303ad3b55cd071a426e7a59c1504854664; _ga=GA1.2.986719823.1501079288; _gid=GA1.2.1585289570.1506061387',
        }
        self.url1=''#spider的url参数
    def spider(self, url):
        response = requests.get(url, headers=self.headers).text
        #print(response)
        s = etree.HTML(response)
        pattern=re.compile(r'<a title="Older Comments" href="(.*?)" class="previous-comment-page">下一页</a>',re.S)
        hrefs=re.findall(pattern,response)#下一页的网址
        print(hrefs[1])
        self.url1 = 'http:' + hrefs[1]
        pattern = re.compile(r'&lt;/a&gt;: &#39;">(.*?)</a></span></small>', re.S)
        times = re.findall(pattern, response)#时间节点
        if self.g==0:#只执行第一天
            self.get_urls(response)
            for j in range(0,len(times)):
                print('---------时间节点------------')
                print(times[j][-5])
                print(times[j][-6])
                if times[j][-5]=='y' or times[j][-6]=='y':#当页有前一天的就不再执行spider了
                    self.g = 1#指示是否继续循环spider的标志
                    break#结束这个循环也就是结束这个while，continue是跳出这个循环，接着下一个循环也就是接着这个while的下一个循环
        else:
            self.get_urls(response)

    def _md5(self,value):
        '''md5加密'''
        m = hashlib.md5()
        m.update(value.encode('utf-8'))
        return m.hexdigest()

    def _base64_decode(self,data):
        '''bash64解码，要注意原字符串长度报错问题'''
        missing_padding = 4 - len(data) % 4
        if missing_padding:
            data += '=' * missing_padding
        return base64.b64decode(data)

    def get_imgurl(self,m, r='', d=0):
        '''解密获取图片链接'''
        e = "DECODE"
        q = 4
        r = self._md5(r)
        o = self._md5(r[0:0 + 16])
        n = self._md5(r[16:16 + 16])
        l = m[0:q]
        c = o + self._md5(o + l)
        m = m[q:]
        k = self._base64_decode(m)
        url = ''
        url = k.decode('utf-8', errors='ignore')
        url = '//w' + url
        #h = list(range(256))
        #b = [ord(c[g % len(c)]) for g in range(256)]

        #f = 0
        '''for g in range(0, 256):
            f = (f + h[g] + b[g]) % 256
            tmp = h[g]
            h[g] = h[f]
            h[f] = tmp'''

        t = ""
        #p, f = 0, 0
        '''for g in range(0, len(k)):
            p = (p + 1) % 256
            f = (f + h[p]) % 256
            tmp = h[p]
            h[p] = h[f]
            h[f] = tmp
            t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))'''
        #t = t[26:]
        t = url
        return t

    def get_r(self,js_url):
        '''获取关键字符串'''
        js = requests.get(js_url).text
        _r = re.findall('c=[\w\d]+\(e,"(.*?)"\)', js)[0]
        return _r

    def get_urls(self,response):
        '''获取一个页面的所有图片的链接'''
        js_url = 'http:' + re.findall('<script src="(//cdn.jandan.net/static/min/[\w\d]+\.\d+\.js)"></script>', response)[-1]
        _r = self.get_r(js_url)
        soup = BeautifulSoup(response, 'lxml')
        tags = soup.select('.img-hash')
        for tag in tags:
            img_hash = tag.text
            img_url = self.get_imgurl(img_hash, _r)
            print(img_url)
            img_url='http:'+img_url
            if img_url in self.urllist:
                self.k=1
                break
            else:
                self.urllist.append(img_url)
                self.download(img_url)
    def download(self,img_url):
        urllib.request.urlretrieve(img_url, '/myfolder/meizitu/' + '美女图%s.jpg' % self.x)
        self. x += 1

if __name__=='__main__':
    f = Spider()
    url = 'http://jandan.net/ooxx/'
    while 1:
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        love_time = curr_time.split(" ")[1]
        love_time = love_time[0:2]
        print('当前的小时数：',love_time)
        if love_time == "22":#一直挂着就是每天这个点发送，如果想每个小时都发送，可以考虑在条件那里用到‘或’条件，不过不美观，建议提取时与分出来，直接切除前面几个字符love_time[3:8]就可以了
            while 1:
                if f.k==1 or f.g==1:#当前页面有一天前上传的图片，跳出循环
                    break
                f.spider(url)
                print('k:',f.k)
                url=f.url1
                print('下个页面的网址是：',url)
                time.sleep(30)#给个延时，不然会被封，反正时间不急
            print('今天的图已经下载完了，明天再来')
        else:
            print('还没到10点，耐心等待一个小时再检测')
            print('祝你生活愉快！')
        time.sleep(3600)#一个小时监测一次

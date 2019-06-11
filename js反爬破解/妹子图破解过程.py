#-*-coding:utf-8-*-
#这是一个爬取煎蛋妹子图的程序，可以挂在云服务器一直运行，每晚10点爬取最新一天的上传的美女图
#用到了requests、lxml、正则、bs4抓取，同时设置定时，图片的链接加了密都变成了gif格式，首先需要解密，这里参考了别人的方法
#妹子图的解密需要一个hash值还有一个js文件的参数，前者在imgurl后面接着，后者在一个js文件中，
#hash值正则取到，js参数先正则拿到js文件url，再请求，正则获取js参数，然后两个参数放到jandan_load_img(this)函数才能得到图片的url，
#具体参考http://tendcode.com/article/jiandan-meizi-spider/，里面是用c写的，作者了改成python，里面运用了md5加密和bash解码



#此前的妹子图网址，还是存在js加密的，图片的网址被js解密了，需要js解密才可以获取网址，或者selenium也可以轻松获取
#此前的妹子图，相对应的html为：
#1.<p><img src="//img.jandan.net/img/blank.gif" onload="jandan_load_img(this)" /><span class="img-hash">ece8ozWUT/VGGxW1hlbITPgE0XMZ9Y/yWpCi5Rz5F/h2uSWgxwV6IQl6DAeuFiT9mH2ep3CETLlpwyD+kU0YHpsHPLnY6LMHyIQo6sTu9/UdY5k+Vjt3EQ</span></p>
#2.首先onload函数就是在页面加载完后再加载；所以这个就是函数即使一个典型的ajax，或者js加密函数
#3.仔细看src，这是不正确的网址，真正的网址包含在jandan_load_img(this)这个函数里面以及后面的一串字符串，仔细看这串字符串，只有大小写字母和/+等符号，初步判断是base64加密后的数据
#4.接着在各个js文件中搜索jandan_load_img这个函数，接着会在http://cdn.jandan.net/static/min/1d694f08895d377af4835a24f06090d0.29100001.js文件搜索到
#5.js文件中的代码如下：

# function jandan_load_img(b) {
#     var d = $(b);
#     var f = d.next("span.img-hash");
#     var e = f.text();
#     f.remove();
#     var c = f_Qa8je29JONvWCrmeT1AJocgAtaiNWkcN(e, "agC37Is2vpAYzkFI9WVObFDN5bcFn1Px");
#6.仔细分析，e就是哈希值，也就是刚刚的一段字符串，f_Qa8je29JONvWCrmeT1AJocgAtaiNWkcN函数有两个函数，一个是e，一个就是一段字符串，这个是固定在这里的，加密用的
#7.继续查找f_Qa8je29JONvWCrmeT1AJocgAtaiNWkcN这个函数，最后在js文件找到原型如下：

# var f_Qa8je29JONvWCrmeT1AJocgAtaiNWkcN = function(m, r, d) {
#     var e = "DECODE";----给定的值
#     var r = r ? r : "";
#     var d = d ? d : 0;
#     var q = 4;        ---q=4
#     r = md5(r);       ---md5加密哈希值
#     var o = md5(r.substr(0, 16)); ----substr函数第一个参数指代截取子串开始下标，第二个是长度，也就是切片函数
#     var n = md5(r.substr(16, 16));
#     if (q) { if (e == "DECODE") { var l = m.substr(0, q) } } else { var l = "" }---q存在，e对，换成python其实就是l=m[0,q]
#     var c = o + md5(o + l);   --一样
#     var k;
#     if (e == "DECODE") {
#         m = m.substr(q);         ----q开始切片
#         k = base64_decode(m)      ---重写base64解码函数
#     }
#     var h = new Array(256);           ----数组
#     for (var g = 0; g < 256; g++) { h[g] = g } ----就是一个0-255的list，
#     var b = new Array();
#     for (var g = 0; g < 256; g++) { b[g] = c.charCodeAt(g % c.length) }   ---charCodeAt() 方法可返回指定位置的字符的 Unicode 编码。这个返回值是 0 - 65535 之间的整数。python中是ord函数，ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值，
#     for (var f = g = 0; g < 256; g++) {
#         f = (f + h[g] + b[g]) % 256;
#         tmp = h[g];
#         h[g] = h[f];
#         h[f] = tmp
#     }         ----这一段一样，不过应该在前面先定义f=0
#     var t = "";
#     k = k.split("");
#     for (var p = f = g = 0; g < k.length; g++) {  ----python就是for in 循环
#         p = (p + 1) % 256;
#         f = (f + h[p]) % 256;
#         tmp = h[p];
#         h[p] = h[f];
#         h[f] = tmp;
#         t += chr(ord(k[g]) ^ (h[(h[p] + h[f]) % 256]))
#     }             ---一样python
#     if (e == "DECODE") { if ((t.substr(0, 10) == 0 || t.substr(0, 10) - time() > 0) && t.substr(10, 16) == md5(t.substr(26) + n).substr(0, 16)) { t = t.substr(26) } else { t = "" } }            ----前面的条件应该是对的，切片26以后的字符串
#     return t      -----这就是破解后的网址
# };


#8.这个就是破解js加密的整一个函数，所以我们只需要模仿着改成python函数就可以破解，
# 上面有个md5函数，应该是md5加密，base64_decode函数是base64解码函数，都需要重写，总共三个参数，第一个是哈希值，第二个是给定的参数，第三个无效
#9.重写的python函数：
def get_imgurl(m, r='', d=0):
    '''解密获取图片链接'''
    e = "DECODE"
    q = 4
    r = _md5(r)
    o = _md5(r[0:0 + 16])
    n = _md5(r[16:16 + 16])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    h = list(range(256))
    b = [ord(c[g % len(c)]) for g in range(256)]

    f = 0
    for g in range(0, 256):
        f = (f + h[g] + b[g]) % 256
        tmp = h[g]
        h[g] = h[f]
        h[f] = tmp

    t = ""
    p, f = 0, 0
    for g in range(0, len(k)):
        p = (p + 1) % 256
        f = (f + h[p]) % 256
        tmp = h[p]
        h[p] = h[f]
        h[f] = tmp
        t += chr(k[g] ^ (h[(h[p] + h[f]) % 256]))
    t = t[26:]
    return t
#10.md5函数：
def _md5(value):
    '''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
#11.base64解密函数
def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    missing_padding = 4 - len(data) % 4  #一般情况下经base64加密后的字符串是4的倍数，如果不是的可能其本身自动去除了“=”，所以不是4的倍数就补齐“=”
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)       #解码
#整个解密就是上述的过程，网站多段时间有可能就会改变一下加密的函数，比如现在就没有加密了，所以按照实际情况分析


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
                    self.k = 1#指示是否继续循环spider的标志
                    self.g = 1
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
        #这里判断是否是4的倍数，差多少个是4的倍数就加上多少个“=”，这个是base64加密的规则
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
        #base64解码
        k = self._base64_decode(m)
        url = ''
        #utf-8解码，可读性高
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
    while 1:
        url = 'http://jandan.net/ooxx/'
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        love_time = curr_time.split(" ")[1]
        love_time = love_time[0:2]
        print('当前的小时数：',love_time)
        if love_time == "20":#一直挂着就是每天这个点发送，如果想每个小时都发送，可以考虑在条件那里用到‘或’条件，不过不美观，建议提取时与分出来，直接切除前面几个字符love_time[3:8]就可以了
            f.k=0
            while 1:
                if f.k==1:#当前页面有一天前上传的图片，跳出循环
                    break
                f.spider(url)
                print('k:',f.k)
                url=f.url1
                print('下个页面的网址是：',url)
                time.sleep(30)#给个延时，不然会被封，反正时间不急
            print('今天的图已经下载完了，明天再来')
        else:
            print('还没到8点，耐心等待一个小时再检测')
            print('祝你生活愉快！')
        time.sleep(3600)#一个小时监测一次

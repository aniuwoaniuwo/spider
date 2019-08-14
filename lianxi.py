# -*-coding:utf-8-*-
import requests
import requests, json

'''s = requests.Session()
s.get('http://www.baidu.com/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)'''

'''url='http://httpbin.org/post'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
data={'value1':'1','value2':'2'}
r=requests.get(url,params=data,headers=header)
print(r.text,r.cookies,r.encoding,r.url)'''
'''data=[{
    'ranking': '无数据',
    'pictrue':'无数据'
}]
with open('maoyan55.json', 'a', encoding='utf-8') as f:
    f.write(str(data))
print(json.dumps(data))
print(requests.get('https://hotel.qunar.com/city/guangzhou/').status_code,requests.get('https://hotel.qunar.com/city/guangzhou/').text)'''
'''str=[]
s=" "
print('s0:',s[0])
if s[0] not in str:
    str.append(s[0])
print(len(s))
print(len(str))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str=[]
        max=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in str:
                    str.append(s[j])
                else:
                    break
            f = len(str)
            str = []
            if max < f:
                max = f
        return max
if __name__=='__main__':
    f=Solution()
    s=" "
    print(f.lengthOfLongestSubstring(s))'''
'''from multiprocessing import Pool,Process
def jj(i):
    list=[]
    f=10+i
    for h in range(i,f)
        list.append(h)
    return list
def printg():
    print(list)
if __name__=='__main__':#暂时写到txt储存的，excel和数据库用到再改善

    for i in range(10):
        pi=Process(target=jj,args=(i,))
        pi.start()

    pi.join()#最后一个要结束才可以继续下面的进程'''
'''import re
r='ni'
print(r)
print('fff')
patterns=re.compile('title=\"(.*?)\">',re.S)'''
'''try:
    print('try...')
    r = 10 / 0
    print('result:', r)
#except ZeroDivisionError as e:#知道具体的错误类型，除数是0的错误，打印
    #print('except:', e)
except Exception as e:#不知道错误类型，直接打出错误信息
    print(e)
except:#出错就打印一个特定的字符串
    print("exception")'''
'''from selenium import webdriver

proxy='110.52.235.184:9999'
options=webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + proxy)
driver=webdriver.Chrome(chrome_options=options)
driver.get('http://httpbin.org/get')
'''

'''firefox_options = webdriver.FirefoxOptions()
ff_profile = webdriver.FirefoxProfile()
ff_profile.set_preference("network.proxy.type", 1)
ff_profile.set_preference("network.proxy.http", '110.52.235.184')
ff_profile.set_preference("network.proxy.http_port", int(9999))
ff_profile.set_preference("network.proxy.ssl", '110.52.235.184')
ff_profile.set_preference("network.proxy.ssl_port", int(9999))
ff_profile.set_preference("network.proxy.ftp", '110.52.235.184')
ff_profile.set_preference("network.proxy.ftp_port", int(9999))
ff_profile.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
ff_profile.update_preferences()
driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
driver.get('http://httpbin.org/get')'''
'''import requests
print(requests.get('http://www.zhenai.com/zhenghun/guangzhou/nv/2').text)'''
'''import csv
with open('lianxi.csv', 'a', encoding='utf-8') as f:
    names = ['name', 'head', 'address', 'age', 'height', 'marriage', 'schooling', 'introduction', 'url']
    writer = csv.writer(f)

    writer.writerow(['jttt','hgff','gff'])
    writer.writerow('jttt', 'hgff', 'gff')'''
'''import re

items=re.findall('(.*?):(.*)','135.26.565.666:56894')
print(items[0][0],items[0][1])
print(int('2318'),int(2318))'''
'''from  selenium import webdriver  # 引入网页驱动包

driver = webdriver.PhantomJS(
    executable_path=r'D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')  # 使用webkit无界面浏览器，如果路径为EXE启动程序的路径 那么该路径需要加一个r

driver.get('http://news.sohu.com/scroll/')  # 获取指定网页的数据

print(driver.find_element_by_class_name('title').text)'''
'''import os
file='C:\spider\lx'
file1='C:\\spider\\lx\\os\\'#双斜线是比单好点，单的话后面必须跟文件夹名，而双可以不跟
if os.path.exists(file1):#判断是否存在
    print('存在此文件夹')
else:
    print('不存在此文件夹')
    os.makedirs(file1)#创建文件夹
if os.path.exists(file1):
    print('存在此文件夹')
else:
    print('不存在此文件夹')
f=open(file1+'os'+'.txt','a')
print(os.getcwd())#获取当前文件路径
print(os.path.abspath('eason.py'))#获取绝对路径，包括文件名
print(os.path.abspath(''))
print(os.path.dirname('eason.py'))'''
# import csv
# with open('xianyu.csv','r',encoding='utf-8') as f:
#     reader=list(csv.reader(f))
#     print(reader[0])
#     # for row in reader:
#     #     if row:
#     #         print(row[0])
#
#     # for i in range(20):
#     #     print(reader[i][0],reader[i][1])
'''data=3670
h=data//3600
yushu=data%3600
m=yushu//60
yushu=yushu%60
s=yushu
print('用时：{}时{}分{}秒'.format(h,m,s))'''
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('unicode_escape'))
# import requests
# print(requests.get('https://2.taobao.com/').text)
# from multiprocessing import Pool
# class Spider(object):
#     def __init__(self):
#         self.num=0
#     def main(self,num):
#         num+=1
#         print(num)
#     def make(self):
#         pool = Pool(processes=4)
#         num=0
#         for i in range(60):
#             print(88)
#             pool.apply_async(f.main,(i,))
#             print(99)
#         pool.close()  # 关闭进程池，不再接受新的进程
#         pool.join()  # 主进程阻塞等待子进程的退出
# if __name__=='__main__':
#     f=Spider()
#     f.make()
# import time
# import re
# import asyncio
# import aiohttp
# import random
# import requests
# import os
# import itchat
# import pymysql
# import xlrd, xlwt, json, csv
# from lxml import etree

#
# async def creat_joke(url, res_list,num):
#     print("开始爬取joke")
#     num+=1
#     print(num)
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
#     headers = {'User-Agent': user_agent}
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url, headers=headers) as res:
#             assert res.status == 200
#             num+=1
#             print(num)
#             res_list.append(await res.text())
# def main(num):
#     url_list = ['https://music.douban.com/top250?start={}'.format(str(5*k)) for k in range(1, 20)]  # format放在引号外面
#     loop = asyncio.get_event_loop()
#     res_list = []
#     tasks = [creat_joke(host, res_list,num) for host in url_list]
#     loop.run_until_complete(asyncio.wait(tasks))
#
#     print("joke爬取完成")
# if __name__ == '__main__':
#     k = 1
#     num=0
#     main(num)
# import requests
# print(len('ece8ozWUT/VGGxW1hlbITPgE0XMZ9Y/yWpCi5Rz5F/h2uSWgxwV6IQl6DAeuFiT9mH2ep3CETLlpwyD+kU0YHpsHPLnY6LMHyIQo6sTu9/UdY5k+Vjt3EQ'))
# proxy_url='http://localhost:5555/random'
# y=0
# n=0
# def get_ip(url):
#     try:
#         response=requests.get(url)
#         if response.status_code==200:
#             return response.text
#         else:
#             return None
#     except:
#         return None
# while 1:
#     try:
#         proxy_ip = get_ip(proxy_url)
#         print(proxy_ip)
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
#         }
#         proxies = {'http': 'http://' + proxy_ip, 'https': 'https://' + proxy_ip, }
#         res=requests.get('http://2.taobao.com/item.htm?id=592843024804',headers=headers,proxies=proxies)
#         print(res.text)
#         if res.status_code==200:
#             y += 1
#             print('有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n))
#             print('这是有效的ip:',proxies)
#         else:
#             n += 1
#             print('有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n))
#     except Exception as e:
#         n += 1
#         print('有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n))
#         print('继续测试')
# #         print(e)
# import requests
# while 1:
#     response=requests.get('http://weixin.sogou.com/weixin?query=%E6%AC%A7%E5%86%A0&_sug_type_=&sut=6545&lkt=1%2C1553941706038%2C1553941706038&s_from=input&_sug_=y&type=2&sst0=1553941706143&page=1&ie=utf8&w=01019900&dr=1')
#     print(response.status_code)
# import requests
# cookies='__jsluid=3aaad7d16be6fb73e66bf6dde66a85ff; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1559041585; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1559045128; __jsl_clearance=1559045146.02|0|rejf%2Fa%2FAL0i46QE0lguPr46K4O0%3D'
# headers={'Cookies':cookies,'Upgrade-Insecure-Requests':'1','Referer':'http://www.66ip.cn/1.html','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
# ,'Accept-Encoding':'gzip, deflate, sdch',
# 'Accept-Language':'zh-CN,zh;q=0.8','Host':'www.66ip.cn','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'}
# response=requests.get('http://www.66ip.cn/1.html',headers=headers)
# print(response.text,response.status_code)
# response=requests.get('http://localhost:6666/test').text
# import re
# pattern=re.compile('ip:(.*?)<br/>score:(.*)',re.S)
# items=re.findall(pattern,response)
# print(items,'\n',items[0][0],items[0][1],len(items[0][0]))
# i
# url='https://2.taobao.com/item.htm?id=592838761902'
# url1='http://2.taobao.com/item.htm?id=592844024166'
# proxy_ip='94.180.249.187:38051'
# proxies = {'http': 'http://' + proxy_ip, 'https': 'https://' + proxy_ip, }
# response = requests.get(url1,proxies=proxies)
# print('11111111')
# print(response.status_code,response.text)
# response1 = requests.get(url1)
# # print(response1.status_code,response1.text)
# #
# ip=666
# iplist=[15]
# global ip
# try:
#
#     ip=777
#     iplist.append(ip)
#     print(iplist)
#     if iplist[5]:
#         pass
# except:
#     iplist.remove(ip)
#     print(iplist)
# import time
# import re
# import asyncio
# import aiohttp
# import random
# import requests
# import os
# import itchat
# import pymysql
# import xlrd, xlwt, json, csv
# from lxml import etree
# import csv, json
#
#
# class Spider(object):
#     def __init__(self):  # 这个适用非excel储存
#         '''
#         类的变量
#         '''
#         self.referer = ' '
#         self.cookie = ' '
#         self.user_agent_list = [
#             'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
#             'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
#             'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
#             'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
#             'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
#             'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
#             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
#             'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
#             'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
#         ]
#         # 重试阀值
#         # ip错误指数
#         self.iperror = 0
#         # 网页错误指数
#         self.urlerror = 0
#         # ip池
#         self.iplist = []
#         self.ip = {}
#         self.res_list = []
#
#     async def creat_joke(self, url,  semaphore):
#         async with semaphore:
#             global proxies
#             try:
#                 if len(self.iplist):
#                     proxies = random.choice(self.iplist)
#                 else:
#                     proxies = self.get_ip()
#                     self.iplist.append(proxies)
#                 if proxies:
#                     self.ip = {'http': 'http://' + proxies, 'https': 'https://' + proxies, }
#                 user_agent = random.choice(self.user_agent_list)
#                 self.headers = {'User-Agent': user_agent}
#                 async with aiohttp.ClientSession() as session:
#                     async with session.get(url, headers=self.headers) as res:
#                         # assert res.status == 200
#                         # self.res_list.append(await res.text())
#                         if res.status == 200:
#                             self.urlerror = 0
#                             self.iperror = 0
#                             self.iplist.append(proxies)
#                             print(await res.text())
#                             self.res_list.append(await res.text())
#                         else:
#                             if self.urlerror < 3:
#                                 self.urlerror += 1
#                                 print('出错了，重试第{}次'.format(self.urlerror))
#                                 self.creat_joke(url,semaphore)
#                             else:
#                                 self.urlerror = 0
#                                 self.iperror = 0
#                                 await time.sleep(0.01)
#                                 print('网页不存在,跳过')
#             except Exception as e:
#                 # print(e)
#                 print('ip出错了，重试第{}次'.format(self.iperror))
#                 # time.sleep(5)
#                 if self.iperror < 4:
#                     self.iperror += 1
#                     await time.sleep(0.01)
#                     self.creat_joke(url, semaphore)
#                 else:
#                     # self.iplist.pop(0)
#                     self.iplist.remove(proxies)
#                     print('ip被封了,或者ip无效,应该移除')
#                     self.urlerror = 0
#                     self.iperror = 0
#                     await time.sleep(0.01)
#                     self.creat_joke(url, semaphore)
#
#     def get_ip(self):
#         try:
#             response = requests.get('http://localhost:6666/random')
#             if response.status_code == 200:
#                 return response.text
#             else:
#                 return None
#         except:
#             return None
#
#     def main(self):
#         start = time.time()
#         url_list = ['http://httpbin.org/get'  for k in range(1, 31)]  # format放在引号外面
#         loop = asyncio.get_event_loop()
#         semaphore = asyncio.Semaphore(500)  # 限制并发量为500,默认509，linux默认1024，避免并发太多报错或者系统负担太大
#         tasks = [self.creat_joke(host,  semaphore) for host in url_list]
#         loop.run_until_complete(asyncio.wait(tasks))
#         # print(self.res_list)
#         # for response in res_list:
#         #     for item in jiexi(response):
#         #         txt(item)
#         print("joke爬取完成")
#         end = time.time()
#         data = end - start
#         h = data // 3600
#         yushu = data % 3600
#         m = yushu // 60
#         yushu = yushu % 60
#         s = yushu
# #         print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))
# #
# # if __name__ == '__main__':
# #     f = Spider()
# #     f.main()
# #     # creat_joke()26.849535703659058
# #     # print(requests.get('https://www.qiushibaike.com/hot/page/30/').status_code)
# #-*-coding:utf-8-*-
# #利用selenium+requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，暂时不需要cookies，代理，
# import time,csv
# from selenium import webdriver
# import urllib.request
# import re,requests
# from lxml import etree
# import xlwt,xlrd,pymysql
# from selenium.webdriver.support.wait import  WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# from lxml import etree
# import xlwt,xlrd,re,json
# from selenium.webdriver.common.proxy import Proxy, ProxyType
# from multiprocessing import Pool
#
# class Spider(object):
#     def __init__(self):
#         self.k=1
#
#
#     def get_ip(self):
#         try:
#             response = requests.get('http://localhost:6666/random')
#             if response.status_code == 200:
#                 return response.text
#             else:
#                 return None
#         except:
#             return None
#
#     def spider(self,url, time=time):
#         for i in range(3):
#             m=0
#             #f=xlrd.open_workbook('tianyancha.xlsx')
#             ip='61.161.46.179'
#             port=8118
#             proxies = self.get_ip()
#             if proxies:
#                 items = re.findall('(.*?):(.*)', proxies)
#                 ip=items[0][0]
#                 port=items[0][1]
#             firefox_options = webdriver.FirefoxOptions()
#             ff_profile = webdriver.FirefoxProfile()
#             ff_profile.set_preference("network.proxy.type", 1)
#             ff_profile.set_preference("network.proxy.http", ip)
#             ff_profile.set_preference("network.proxy.http_port", int(port))
#             ff_profile.set_preference("network.proxy.ssl", ip)
#             ff_profile.set_preference("network.proxy.ssl_port", int(port))
#             ff_profile.set_preference("network.proxy.ftp", ip)
#             ff_profile.set_preference("network.proxy.ftp_port", int(port))
#             ff_profile.set_preference("general.useragent.override",
#                                       "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
#             ff_profile.update_preferences()
#             driver = webdriver.Firefox()
#             driver.get('http://httpbin.org/get')
#             driver.execute_script('window.open()')
#
#             driver.switch_to_window(driver.window_handles[1])
#             driver.get('http://httpbin.org/get')
#             time.sleep(1)
#
#             for i in range(10):
#                 driver.execute_script('window.open()')
#
#                 driver.switch_to_window(driver.window_handles[i+2])
#                 driver.get('http://www.douban.com/')
#                 time.sleep(1)
            # wait=WebDriverWait(driver,15)
            # try:
            #     driver.maximize_window()#窗口最大
            #     driver.get(url)#天眼查制造业企业的信息
            #     time.sleep(5)#给个五秒延迟,必须先定义，不能在函数中直接用
            #     submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#searchHotelPanel > div.b_tool.clr_after > div.pager.js_pager > div > ul > li.item.next > a > span:nth-of-type(1)')))#直到此元素可以点击
            #     for i in range(1):
            #         '''for j in range(1, 3):
            #             height = 20000 * j  # 每次滑动20000像素
            #             strWord = "window.scrollBy(0," + str(height) + ")"
            #             driver.execute_script(strWord)
            #             time.sleep(2)'''
            #         selector=driver.page_source
            #         yield selector
            #
            # except Exception as e:
            #     print(e)

#
#
#     def main(self,url):
#         '''
#         进程启动入口
#         :return:
#         '''
#         start = time.time()
#         self.spider(url)
#             # time.sleep(2)
#         end = time.time()
#         data = end - start
#         h = data // 3600
#         yushu = data % 3600
#         m = yushu // 60
#         yushu = yushu % 60
#         s = yushu
#         print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))
#
# if __name__=='__main__':
#     f=Spider()
#     # urls = ['https://music.douban.com/top250?start={}'.format(i * 25) for i in range(1, 3)]
#     # pool = Pool(processes=4)
#     # for i in range(len(urls)):
#     #     pool.apply_async(f.main, (urls[i],))
#     # pool.close()  # 关闭进程池，不再接受新的进程
#     # pool.join()  # 主进程阻塞等待子进程的退出
#     # # f.main()
# m=0
# while 1:
#     m+=1
#     if m==5:
#         break
# urls=['https://music.douban.com/top250?start={}'.format(i*25) for i in range(10)]
# print(urls)
# import requests

# print(requests.get('https://www.tianyancha.com/').status_code)
# import queue,time,random
# import threading
#
# q = queue.Queue()
# def put():
#     for i in range(100):
#         q.put(i)
#
# def get():
#     while 1:
#         number=random.choice([5,10])
#         time.sleep(number)
#         print(q.get())
# put()
# for j in range(5):
#     t=threading.Thread(target=get)
#     t.start()
#
# import time,requests
# for i in range(3):
#     print(i)
#     testnum=0
#     while 1:
#         try:
#             print(testnum)
#             if testnum == 3:
#                 break
#             time.sleep(1)
#             requests.get('shsisi')
#
#         except:
#             print('ip无效')
#             testnum += 1
# import queue,time,random
# import threading
#
# def get(i):
#     print(i)
#     time.sleep(random.choice([1,4,7]))
#     print(i+i)
#
# for j in range(5):
#     t=threading.Thread(target=get,args=(j,))
#     t.start()
data={'ssj':55,'nsi':8}
print(tuple(data.values())*2)
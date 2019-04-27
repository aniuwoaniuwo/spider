#-*-coding:utf-8-*-
import requests
import requests,json

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
import csv
with open('xianyu.csv','r',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        if row:
            print(row[0])








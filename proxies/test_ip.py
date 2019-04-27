#-*-coding:utf-8-*-
#首先本来就有ip池，然后测试这些给出的ip是否可用。
#代理的时候，被访问的网址是http，代理也要对应http，https对应https
from bs4 import BeautifulSoup
import requests
import random

def get_random_ip(ip_list):#构造ip
    proxy_ip = random.choice(ip_list)
    proxies = {'http': 'http://'+proxy_ip,'https': 'https://'+proxy_ip,}#最好这样构造，这样http，https都可以访问
    #proxies = {'http': 'http://' + proxy_ip }
    return proxies

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    ip_list = ['110.52.235.184:9999']
    proxies = get_random_ip(ip_list)
    print(proxies)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    res=requests.get(url,headers=headers,proxies=proxies)
    print(res.text)
    if res.status_code==200:
        print('这是有效的ip:',proxies)
    else:
        print('这不是有效的ip！',proxies)


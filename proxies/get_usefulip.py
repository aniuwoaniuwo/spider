#-*-coding:utf-8-*-
'''爬取了西刺前面5页的ip，然后逐个尝试访问网址，成功访问的则选出来打印出来，这些都是有用的ip
作为临时去爬虫的代理ip'''
from bs4 import BeautifulSoup
import requests
import random
from urllib import error

def get_ip_list(url, headers):#爬取ip的函数
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip):#构造代理ip
    proxies = {'http': 'http://'+ip}
    print(proxies)
    return proxies

def errors(ip):#试验代理ip是否可用
    url1 = 'http://httpbin.org/get'
    try:
        proxies = get_random_ip(ip)
        print('正在进行ip代理尝试')
        res = requests.get(url1, headers=headers, proxies=proxies)
        if res.status_code == 200:
            print(res.text)
            print('有用的ip:' + ip)
            return ip
        return None
    except:
        print('尝试下一个ip')
        return None

if __name__ == '__main__':
    for i in range(1,6):
        url = 'http://www.xicidaili.com/nn/{}'.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        ip_list = get_ip_list(url, headers=headers)
        iplist=[]
        print('总共爬爬取的ip数：',len(ip_list))
        for i in range(len(ip_list)):
            try:
                ip=errors(ip_list[i])
                if ip:
                    iplist.append(ip)
                print('ip池',iplist)
            except:
                print('有错了')
    print('done')







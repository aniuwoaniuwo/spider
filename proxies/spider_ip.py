#-*-coding:utf-8-*-
'''这个只是单纯地爬取西刺代理整页的ip，然后随机选了一个试一下百度的，很多是没用的，不常用'''
from bs4 import BeautifulSoup
import requests
import random

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
    print('未筛选过的ip池：',proxy_list)
    #print(proxy_ip)
    proxies = {'http': proxy_ip}
    #print(proxies)
    return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    ip_list = get_ip_list(url, headers=headers)

    proxies = get_random_ip(ip_list)
    print(proxies)
    url1='http://httpbin.org/get'
    res=requests.get(url1,headers=headers,proxies=proxies)
    print(res.text,res.status_code)

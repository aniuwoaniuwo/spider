from bs4 import BeautifulSoup
import requests
import random
from lxml import etree 

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

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    print(proxies)

proxies = {
            'http': 'http://124.72.109.183:8118',
            'http': 'http://49.85.1.79:31666'

}
url='https://music.douban.com/top250'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'

headers = {'User-Agent': user_agent}
html = requests.get(url, headers=headers, timeout=3).text


s=etree.HTML(html)
title=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')
score=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')
renshu=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')
for i in range(25) :
    print(title[i],score[i],renshu[i])
#-*-coding:utf-8-*-
import requests
proxies = {'http': 'http://115.46.66.18:8123'}
headers = {
    'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
    }
url='https://rate.taobao.com/feedRateList.htm?auctionNumId=580000998253&userNumId=2529466216&currentPageNum=1&_ksTS=1545448307516_2832&callback=jsonp_tbcrate_reviews_list'
response=requests.get(url,headers=headers,proxies=proxies).text
print(requests.get(url,headers=headers,proxies=proxies).text)
from lxml import etree
import requests
url=('https://music.douban.com/top250')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'

headers={'User-Agent':user_agent}

htmltext=requests.get(url,headers=headers).text

s=etree.HTML(htmltext)
title=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')
for i in range(25):
    print(title[i])




from lxml import etree 
import requests
url='https://music.douban.com/top250'
html=requests.get(url).text
#print(html)
s=etree.HTML(html)
title=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/a/text()')
score=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[2]/text()')
renshu=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div/div/span[3]/text()')
for i in range(25) :
    print(title[i],score[i],renshu[i])

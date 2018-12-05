#-*-coding:utf-8-*-
import scrapy
from lxml import etree
from scrapy.crawler import CrawlerProcess
'''import sys
import os
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)'''
from tongczf.items import TongczfItem

class tongczf(scrapy.Spider):
    name="tongcheng"
    allowed_domains=['zhanjiang.58.com']
    start_urls=['https://zhanjiang.58.com/xiashan/chuzu/pn{}/?PGTID=0d3090a7-0031-93e0-2a41-133d2ee2c850&ClickID=2'.format(i) for i in range(10,12)]

    def parse(self, response):
        s=etree.HTML(response.text)
        print('开始爬虫')
        print(s)
        print(response.request.headers['User-Agent'])
        datas=s.xpath('./html/body/div[5]/div/div[5]/div[2]/ul/li')
        #/html/body/div[5]/div/div[5]/div[2]/ul/li[4]/div[2]/h2/a
        #/html/body/div[5]/div/div[5]/div[2]/ul/li[4]/div[3]/div[2]/b
        #/html/body/div[5]/div/div[5]/div[2]/ul/li[4]/div[2]/p[2]/text()
        #/html/body/div[5]/div/div[5]/div[2]/ul/li[4]/div[2]/p[1]
        print(datas)
        for data in datas:
            print('可以爬取')
            name=data.xpath('./div[2]/h2/a/text()')[0]
            price = data.xpath('./div[3]/div[2]/b/text()')[0]
            community = data.xpath('./div[2]/p[2]/text()')[0]
            decorate = data.xpath('./div[2]/p[1]/text()')[0]
            print(name,price,community,decorate)
            item=TongczfItem(name=name,price=price,community=community,decorate=decorate)
            yield item
        pass

if __name__ == '__main__':
    process = CrawlerProcess({
        })
    process.crawl(tongczf)
    process.start()
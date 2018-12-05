#-*-coding:utf-8-*-

import scrapy
from lxml import etree
from scrapy.crawler import CrawlerProcess
import sys
import os
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)
from tongcheng.items import TongchengItem

class tongcheng(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["jandan.net"]
    start_urls = ["https://jandan.net/ooxx/page-1"]

    def parse(self, response):
        print('开始爬虫')
        print(response.text)
        '''/ html / body / div[5] / div / div[5] / div[2] / ul / li[1] / div[2] / h2 / a
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / h2 / a
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[3] / div[2] / b
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / p[2] / text()
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / p[1]'''
        '''s=etree.HTML(response.text)
        datas=s.xpath('/ html / body / div[5] / div / div[5] / div[2] / ul / li')
        for data in datas:
            name=data.xpath('./ div[2] / h2 / a/text()')
            price = data.xpath('./ div[3] / div[2] / b/text()')
            community = data.xpath('./ div[2] / p[2] / text()')
            decorate = data.xpath('./ div[2] / p[1]/text()')
            print(name,price,community,decorate)
            item=TongchengItem(name=name,price=price,community=community,decorate=decorate)
            yield item'''
        pass

if __name__ == '__main__':
    process = CrawlerProcess({'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'
        })
    process.crawl(tongcheng)
    process.start()
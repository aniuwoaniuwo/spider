#-*-coding:utf-8-*-
import scrapy
from lxml import etree
from scrapy.crawler import CrawlerProcess
from zufang.items import ZufangItem

class zufang(scrapy.Spider):
    name="zufang"
    allowed_domains=['zhanjiang.58.com']
    start_urls=['https://zhanjiang.58.com/xiashan/chuzu/pn{}'.format(i) for i in range(1,70)]

    def parse(self, response):
        '''/ html / body / div[5] / div / div[5] / div[2] / ul / li[1] / div[2] / h2 / a
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / h2 / a
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[3] / div[2] / b
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / p[2] / text()
        / html / body / div[5] / div / div[5] / div[2] / ul / li[2] / div[2] / p[1]'''
        s=etree.HTML(response.text)
        print('开始爬虫')
        print(s)
        datas=s.xpath('/ html / body / div[5] / div / div[5] / div[2] / ul / li')
        for data in datas:
            name=data.xpath('./ div[2] / h2 / a/text()')
            price = data.xpath('./ div[3] / div[2] / b/text()')
            community = data.xpath('./ div[2] / p[2] / text()')
            decorate = data.xpath('./ div[2] / p[1]/text()')
            print(name,price,community,decorate)
            item=ZufangItem(name=name,price=price,community=community,decorate=decorate)
            yield item
        pass

if __name__ == '__main__':
    process = CrawlerProcess({
        })
    process.crawl(zufang)
    process.start()
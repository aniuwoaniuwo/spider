#-*-coding:utf-8-*-
import scrapy
import random
from scrapy.crawler import CrawlerProcess

class douban250(scrapy.Spider):
    name='douban'
    allowed_domains=["baidu.com"]
    start_urls=['http://baidu.com/']

    '''def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)#全局变量'''
    def parse(self,response):
        print(response.request.headers['User-Agent'])

        #print(response.cookies)
if __name__ == '__main__':
    process = CrawlerProcess({
        })
    process.crawl(douban250)
    process.start()
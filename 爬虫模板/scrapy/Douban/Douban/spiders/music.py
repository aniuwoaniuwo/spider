# -*- coding: utf-8 -*-
import scrapy
#链接提取器
from scrapy.linkextractors import LinkExtractor
#继承关系的库，Rule是提取连接的规则
from scrapy.spiders import CrawlSpider, Rule

#CrawlSpider这个类会自动提取链接，自动发送请求获取response，
# 和Spider类的继承就是多了一个Rule的规则来提取链接
#在文件夹下直接scrapy genspider -t crawl music music.douban.com即可新增这个spider.py


class MusicSpider(CrawlSpider):
    name = 'music'
    allowed_domains = ['music.douban.com']
    start_urls = ['http://music.douban.com/top250']
    #提取的规则
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

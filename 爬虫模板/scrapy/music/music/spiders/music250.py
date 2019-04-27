# -*- coding: utf-8 -*-
#抓取music250的每一个的数据
import scrapy
#链接提取器
from scrapy.linkextractors import LinkExtractor
#继承关系的库，Rule是提取连接的规则
from scrapy.spiders import CrawlSpider, Rule

#CrawlSpider这个类会自动提取链接，自动发送请求获取response，
# 和Spider类的继承就是多了一个Rule的规则来提取链接，自动去重
#在文件夹下直接scrapy genspider -t crawl music music.douban.com即可新增这个spider.py


class Music250Spider(CrawlSpider):
    name = 'music'
    allowed_domains = ['music.douban.com']
    start_urls = ['http://music.douban.com/top250']
    # 提取的规则，自动去重，是用set集合来去重
    # LinkExtractor链接提取器，创建一个提取器,看源码可以知道默认提取a，area标签和href属性也就是所有的链接
    #同时allow参数使用的是正则的匹配，就是允许匹配的url，也可以设置deny，不允许的url，还有allow_domains允许的域名
    #回调函数，

    #follow是否跟进，True是跟进也就是有符合的链接自动请求该链接继续提取一直循环，False不跟进也不循环
    # 默认不写的话，如果有回调函数就False，因为有了解析的函数所以就到头了不用继续挖函数了，没有回调就True继续挖函数

    # rules = (
    #     Rule(LinkExtractor(allow='start'), callback='parse_item', follow=False),
    # )

    # 可以有多个规则，第一个不回调了，一直循环找出符合第一条规则的url，
    #利用第一条获取的url访问，按照第二条规则查找url，这时候由于是到最终的页面，所以不跟随了
    rules = (
          Rule(LinkExtractor(allow='start'),  follow=True),
          Rule(LinkExtractor(allow='subject'), callback='parse_item',follow=False),
    )
    data=1

    def parse_item(self, response):
        self.data+=1
        print(self.data)
        print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

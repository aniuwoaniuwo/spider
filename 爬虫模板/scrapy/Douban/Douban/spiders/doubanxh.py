# -*- coding: utf-8 -*-
# 创建项目后，scrapy genspider douban douban.com 就可以创建出douban这个爬虫文件
# 并且对应着name和域名
# scrapy crawl douban 运行
import scrapy
from Douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban'
    # 域名范围
    allowed_domains = ['douban.com']
    # 爬取网页的入口网址，如果是网址list，name会多线程异步并发进行访问
    # 看源码。遍历所有的url，不过滤重复url
    url='https://www.douban.com/?p={}'
    page=1
    start_urls = [url.format(page)]



    def parse(self, response):
        # 定义item为字典，并且检查字段的格式是否为字典

        # 打印响应的body
        # with open('douban.html','w') as f:
        #     f.write(response.body)

        # 解析数据
        item = DoubanItem()
        # xpath解析，extract（）提取，出来是一个列表，可以用[0]进行进一步提取
        item['name'] = response.xpath('//*[@id="anony-time"]/div/div[3]/ul/li[1]/a[2]/text()').extract()[0]
        item['column'] = response.xpath('//*[@id="anony-time"]/div/div[3]/ul/li[1]/span/text()').extract()[0]
        # 详情页的url
        detail_url = response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/a/@href')
        print(item)
        #要传输item，所以不能现在就返回
        # yield item
        #通过meta传输数据，公用管道存储,将item传了过去
        yield scrapy.Request(detail_url, callback=self.parse_detail,meta={'item':item})

        # #循环开始，调用request函数，继续回调，然后就是一个递归
        # #这样的话就是一个线程了
        # self.page+=1
        # url=self.url.format(self.page)
        # yield scrapy.Request(url,callback=self.parse)
        # # return把数据传输到engine，然后engine把数据传给pipelines管道
    def parse_detail(self,response):
        item=response.meta['item']
        item['url']=response.xpath('').extract_first()
        yield item
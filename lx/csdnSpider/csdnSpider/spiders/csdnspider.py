#-*-coding:utf-8-*-
import scrapy
import sys
import os
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)
from csdnSpider.items import CsdnspiderItem
from scrapy.crawler import CrawlerProcess

class csdnspider(scrapy.Spider):  # 必须继承scrapy.Spider
    name = "csdn"  # 爬虫名称,这个名称必须是唯一的
    allowed_domains = ["csdn.net"]  # 允许的域名
    start_urls = [
        "https://www.csdn.net/nav/ai"
    ]

    def parse(self, response):
        # 实现网页的解析
        datas = response.xpath('//*[@id="feedlist_id"]/li/div')

        # # 检查代码是否达到特定位置
        # from  scrapy.shell   import inspect_response
        # inspect_response(response,self)

        print('hhhhhhhhhhhhhhh')
        for data in datas:
            read_count = data.xpath('./div[1]/h2/a/text()').extract()
            title = data.xpath('./ dl / div[2] / dd[1] / a / span[1]/text()').extract()

            read_count = read_count[0] if len(read_count) > 0 else ''
            title = title[0] if len(title) > 0 else ''

            print(read_count, title)
            item = CsdnspiderItem(read_count=read_count, title=title)  # 封装成Item对象
            yield item

        pass


if __name__ == '__main__':
    process = CrawlerProcess({
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'
    })
    process.crawl(csdnspider)
    process.start()
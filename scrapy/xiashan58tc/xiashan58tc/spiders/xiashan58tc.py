#-*-coding:utf-8-*-
import scrapy
from scrapy.http import Request
from xiashan58tc.items import Xiashan58TcItem
from scrapy.crawler import CrawlerProcess


class xiashan(scrapy.Spider):
    name="xiashan"
    allowed_domains=["zhanjiang.58.com"]
    start_urls=[
        "http://zhanjiang.58.com/xiashan/chuzu/?PGTID=0d3090a7-0031-7ae6-5800-aa67ca8a7042&ClickID=2"
    ]
    def parse(self,response):
        dizhis = response.xpath('/html/body/div[4]/div[1]/div[5]/div[2]/ul/li/div[2]/p[2]/a[2]/text()')  # li地址
        biaotis = response.xpath('/html/body/div[4]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a/text()')  # 标题的内容
        jiages = response.xpath('/html/body/div[4]/div[1]/div[5]/div[2]/ul/li/div[3]/div[2]/b/text()')  # 租房价格

        for i in range(0, len(dizhis)):
            dizhi = dizhis[i].extract()
            biaoti = biaotis[i].extract()
            jiage = jiages[i].extract()
            #print(dizhi,jiage)
            item=Xiashan58TcItem(dizhi=dizhi,biaoti=biaoti,jiage=jiage)
            yield item
        for i in range(1,41):
            url="http://zhanjiang.58.com/xiashan/chuzu/pn{}/?PGTID=0d3090a7-0031-9d42-0699-58e73d17d85b&ClickID=2".format(str(i))
            yield Request(url,callback=self.parse)#回调
if __name__ == '__main__':
    process = CrawlerProcess({
        })
    process.crawl(xiashan)
    process.start()
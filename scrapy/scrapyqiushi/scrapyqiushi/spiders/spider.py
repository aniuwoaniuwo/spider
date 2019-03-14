#-*-coding:utf-8-*-
import scrapy
import sys
import os
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
ffpath = os.path.abspath(os.path.join(fpath,".."))
print(ffpath)
sys.path.append(ffpath)
from scrapyqiushi.items import ScrapyqiushiItem

from scrapy.crawler import CrawlerProcess

class qiushi(scrapy.Spider):
    name="qiushi"
    allowed_domains=["qiushibaike.com"]
    start_urls=[
    'http://www.qiushibaike.com/hot/page/{}/'.format(pagei) for pagei in range(30)
    ]

    def parse(self,response):
        pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
        items = re.findall(pattern, response)
        for a in items:
            print(a)
            item=ScrapyqiushiItem(count=a)
            yield item
        pass


            #with open("yibuqiushi.txt", "a", encoding='utf-8') as f:  # a是追加,要加上第三个参数，否则读取不了
                #f.write(a + "\n")
if __name__ == '__main__':
    process = CrawlerProcess({
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.12 Safari/537.36'
    })
    process.crawl(qiushi)
    process.start()
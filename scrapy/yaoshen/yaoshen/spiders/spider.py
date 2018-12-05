#-*-coding:utf-8-*-
import scrapy
import random
from lxml import etree

from scrapy.crawler import CrawlerProcess
from yaoshen.items  import  YaoshenItem

class yaoshen(scrapy.Spider):
    name="yaoshen"
    allowed_domains=['movie.douban.com']
    start_urls=['https://movie.douban.com/subject/26752088/comments?start=80']

    cookies = {}
    cookie= 'll="118289"; bid=YeqEpAwe8XU; __yadk_uid=EtJvpv06cJP5CJdBh7R1ZAs9gypRtITn; douban-fav-remind=1; ps=y; douban-profile-remind=1; dbcl2="167986306:6t4e8DWCSPU"; _vwo_uuid_v2=D91AD00D97E0BCC0DBB2DFD8834DCB569|67c211ac2d584779c1bc62e82dca76c3; ck=3lHD; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1541826193%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=77dc2231794329c7.1535642645.11.1541826193.1540812634.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.17400769.1540812629.1540812629.1541826193.2; __utmb=30149280.0.10.1541826193; __utmc=30149280; __utmz=30149280.1540812629.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.954159437.1540812629.1540812629.1541826193.2; __utmb=223695111.0.10.1541826193; __utmc=223695111; __utmz=223695111.1540812629.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_noty_num=0; push_doumail_num=0'  # cookie大概是这么一个格式
    for line in cookie.split(';'):
        key, value = line.split("=", 1)

        cookies[key] = value  # 格式化操作，装载cookies

    def start_requests(self):
        for url in self.start_urls:#加上self..下面那里加了ip起作用了，并且mid也添加了，是mid的优先
            yield scrapy.Request(url,callback=self.parse,cookies=self.cookies)#,meta=self.proxies可以添加头，但是不能添加proxies和cookie，没用get的功能,用到meta的方法添加proxies要用到callback=self.parse,否则获取不了网页
    def parse(self,response):
        good = 100
        s=etree.HTML(response.text)
        print('hhhhhhhhhhhhhh')
        counts=s.xpath('//*[@id="comments"]/div/div[2]')
        print(response.request.headers['User-Agent'])
        for i in counts:
            count=i.xpath('./p/span/text()')[0]
            #// *[ @ id = "comments"] / div[3] / div[2] / p / span / text()
            name=i.xpath('./ h3 / span[2] / a/text()')[0]

            print(name,' ',count)
            item=YaoshenItem(count=count,name=name,good=good)
            yield item
        pass
if __name__ == '__main__':
    process = CrawlerProcess({
        })
    process.crawl(yaoshen)
    process.start()





# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyqiushiPipeline(object):
    def process_item(self, item, spider):
        try:
            print('hello world')
            count=str(item['count'])
            f = open("C:/pachong/scrapyqiushi/scrapyqiushi/spiders/sqiushi.txt","a+", encoding="utf-8")
            f.write(count + '\n')
            f.close()
        except:#这里要加pass
            pass

        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem

'''class CsdnspiderPipeline(object):

    def __init__(self):
        self.file = codecs.open('data.json','wb', encoding="utf-8")#要加第三个参数，不然爬不了数据


    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item))+"\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" %item)'''
class CsdnspiderPipeline(object):
    def process_item(self, item, spider):
        try:
            print(11111111111)
            title=str(item['title'])
            read_count=str(item['read_count'])
            f=open("C:/lx/csdnSpider/csdnSpider/spiders/shuju.txt","a+",encoding="utf-8")
            f.write(title+read_count+'\n')
            f.close()
        except:
            pass

        return item
			
			
			
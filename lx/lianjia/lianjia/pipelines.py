# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class LianjiaPipeline(object):

    def process_item(self, item, spider):
        with open('data1.txt','a') as f:
            place = str(item['place'])
            size = str(item['size'])
            price = str(item['price'])
            f.write(place + size + price + '\n')
        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
#底层实质是一个字典，是字典的子类
#可以判断字段是否正确，可以报错

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #需要定义好字典的name
    name=scrapy.Field()
    column=scrapy.Field()
    url = scrapy.Field()

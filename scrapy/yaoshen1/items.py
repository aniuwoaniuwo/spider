# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YaoshenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    count=scrapy.Field()
    name=scrapy.Field()
    good=scrapy.Field()
    pass

# -*- coding: utf-8 -*-
import scrapy


class Douban1Spider(scrapy.Spider):
    name = 'douban1'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass

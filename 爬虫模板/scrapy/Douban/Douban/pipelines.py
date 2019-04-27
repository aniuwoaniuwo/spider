# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#存储数据的,默认不开启管道，需要手动开启
#json导出器，写入的都是字节，看源码
#process_item方法是必须实现的
from scrapy.exporters import JsonItemExporter
import pymysql
class DoubanPipeline(object):
    def __init__(self,host,port,user,password,database):
        #初始化数据
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
    def open_spider(self,spider):
        #spider开启的时候自动调用，可以设置一些初始化的东西，比如数据库的连接
        self.db=pymysql.connect(self.host,self.user,self.password,self.database,charset='utf-8',port=self.port)
        self.cursor=self.db.cursor()
        pass

    @classmethod
    def from_crawl(cls,crawler):
        #这是一个类的方法，通过crawler，可以拿到scrapy的核心组件，比如全局配置的信息
        #这里获得的配置信息就是init的数据来源
        #当然这里只是给出了整个原理过程，直接在这里直接输入相应的信息其实更简单，不用写那么多的函数
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user= crawler.settings.get('MYSQL_USER'),
            password= crawler.settings.get('MYSQL_PASSWORD'),
            port= crawler.settings.get('MYSQL_PORT'),
            database= crawler.settings.get('MYSQL_DATABASE'),
        )
    def process_item(self, item, spider):
        #这里是注意的函数，清洗保存数据就在这实现，必须返回item对象
        #创建一个文件对象
        file=open('douban.json','wb')
        #创建导出器
        exporter=JsonItemExporter(file)
        #开启导出器
        exporter.start_exporting()
        #导出数据
        exporter.export_item(item)
        #关闭导出器
        exporter.finish_exporting()
        #关闭文件
        file.close()

        return item

    def close_spider(self, spider):
        #spider关闭的时候自动调用，可以试着关闭数据库
        self.db.close()
        pass

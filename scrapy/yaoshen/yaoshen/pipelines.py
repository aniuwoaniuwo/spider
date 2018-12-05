# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class YaoshenPipeline(object):
    def process_item(self, item, spider):

        name = str(item['name'])
        count=str(item['count'])
        good=str(item['good'])
        db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')
        cursor = db.cursor()
        data = {}
        data = {
            'name': name,
            'score': count,
            'good': good
        }
        table = 'musics'
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        update = ','.join([" {key}=%s".format(key=key) for key in data])  # 注意空格
        sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                            values=values)
        sql = sql + update
        try:
            if cursor.execute(sql, tuple(data.values()) * 2):  # 这是格式，第二个参数要有
                # if cursor.execute(sql,(title[i],score[i],renshu[i])):
                print('成功')
                db.commit()  # 执行保存
        except:
            db.rollback()
            print('失败！')

        return item

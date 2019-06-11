# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#excel储存的没试过行不行，需要验证
import pymysql
import xlwt,xlrd

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

    def process_item(self, item, spider):
        name = str(item['name'])
        count=str(item['count'])
        good=str(item['good'])
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            f.write(name,' ',count,' ',good)


    def __init__(self):  # 这个是适用excel储存
        self.m=0
        self.sheet = self.shuju.add_sheet(u'列表', cell_overwrite_ok=True)
        sheetcount = (u'编号', u'地址', u'标题', u'价格')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.shuju.save('xlsx.xlsx')

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style

    def process_item(self, item, spider):
        name = str(item['name'])
        count=str(item['count'])
        good=str(item['good'])
        data = []
        data.append(self.m + 1)
        data.append(name)
        data.append(count)
        data.append(good)
        for j in range(0, len(data)):
            self.sheet.write(self.m + 1, j, data[j])
        self.m = self.m + 1
        print(self.m)
        self.shuju.save('58tongcheng.xlsx')
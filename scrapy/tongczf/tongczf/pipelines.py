# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlrd
import xlwt

class TongczfPipeline(object):
    def process_item(self, item, spider):
        f = xlrd.open_workbook('tongcheng.xlsx')
        sheet1=f.sheets()[0]
        name=str(item['name'])
        price=str(item['price'])
        community=str(item['community'])
        decorate=str(item['decorate'])
        m=0
        data=[]
        data.append(m+1)
        data.append(name)
        data.append(price)
        data.append(community)
        data.append(decorate)
        for j in range(0, len(data)):
            sheet1.write(m + 1, j, data[j])

        m = m + 1
        print(m)
        f.save('tongcheng.xlsx')
        return item

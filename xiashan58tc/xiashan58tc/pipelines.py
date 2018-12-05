# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
class Xiashan58TcPipeline(object):
    tc=Workbook()
    sheet1=tc.active
    sheet1.append(['地址','名字','价格'])
    def process_item(self, item, spider):
        try:
            print(11111111111)
            dizhi=str(item['dizhi'])
            biaoti=str(item['biaoti'])
            jiage=str(item['jiage'])
            self.sheet1.append([dizhi,biaoti,jiage])
            self.tc.save('tongcheng.xlsx')  # 保存xlsx文件
            return item

        except:
            pass
        return item

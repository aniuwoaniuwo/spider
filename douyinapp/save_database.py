#-*-coding:utf-8-*-
import pymysql
import time

import get_detailed_data
def base(item):
    db=pymysql.connect(host='localhost',user='root',password='mysqlmm',port=3306,db='base731')
    cursor=db.cursor()
    #VARCHAR要指定最长的字符串，引号下面的sql语句最好大写
    #存在只是警告
    #遇到图形字符串怎么解决
    #在创建数据库的时候，utf8是最多三个字节。但是表情是四个字符组成的，会报错，可修改数据库的utf8mb4
    sql='CREATE TABLE IF NOT EXISTS douyin (num INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30) NOT NULL,share_id VARCHAR(30) NOT NULL,id VARCHAR(30) NOT NULL)'
    cursor.execute(sql)
    data={'num':0,
        'name':item['name'],
        'id':item['id'],
        'share_id':item['share_id']
    }
    table='douyin'
    #keys返回一个list
    keys=','.join(data.keys())
    #避免字符串出错
    values=','.join(['%s']*len(data))
    sql='INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    if cursor.execute(sql,tuple(data.values())):
        db.commit()
    else:
        db.rollback()
# base(item={'name':'asdd','id':666,'share_id':'ssss'})
def detaildata_save(item):
    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='base731')
    cursor = db.cursor()
    #字段名字不用跟sql语句的命令重复，比如like，否则报错
    sql = "CREATE TABLE IF NOT EXISTS douyindetail (num INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30) NOT NULL,share_id VARCHAR(30) NOT NULL,id VARCHAR(30) NOT NULL DEFAULT '无',introcdution VARCHAR(120) ,focus VARCHAR(10),zan VARCHAR(10),fans VARCHAR(10))"
    cursor.execute(sql)
    data = {'num': 0,
            'name': item['name'],
            'id': item['douyin_id'],
            'share_id': item['share_id'],
            'introcdution':item['introcdution'],
            'focus':item['focus'],
            'fans':item['fans'],
            'zan':item['like']
            }
    table = 'douyindetail'
    # keys返回一个list
    keys = ','.join(data.keys())
    # 避免字符串出错
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    if cursor.execute(sql, tuple(data.values())):
        db.commit()
    else:
        db.rollback()


#-*-coding:utf-8-*-
import get_detailed_data,time
import pymysql

def get_share_id():
    db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='base731')
    cursor = db.cursor()
    sql='select share_id from douyin'
    cursor.execute(sql)
    print(cursor.rownumber)
    result = cursor.fetchone()
    while result != None:
        get_detailed_data.detailed_data(result[0])
        # print(result[0], cursor.rownumber)
        result = cursor.fetchone()
        time.sleep(2)
    # return result[0]
    # print(result)
    # if cursor.execute(sql):
    #     print(cursor.execute(sql))
if __name__=='__main__':
    get_share_id()


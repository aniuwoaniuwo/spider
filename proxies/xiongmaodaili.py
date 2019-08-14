# 高效代理
#-*-coding:utf-8-*-

import sys
import time
import hashlib
import requests

def main():
    # while 1:
    for i in range(3):
        testnum = 0
        urlnum=0
        # apiurl = 'http://www.xiongmaodaili.com/xiongmao-web/api/glip?secret=875b4e2982286424c40ce89745387fe1&orderNo=GL20190721232704y8UK7256&count=1&isTxt=1&proxyType=1'
        #芝麻http每日免费代理
        apiurl='http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=11&pack=58655&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        ip_port = requests.get(apiurl).text.strip('\r\n')
        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port, }
        print('现在的ip是：',proxy)
        start=time.time()
        while 1:
            try:
                if testnum==3:
                    break
                time.sleep(2)
                r = requests.get("https://music.douban.com/top250?start=25",proxies=proxy)
                if r.status_code==200:
                    urlnum+=1
                    print(urlnum)
                    print(r.text)
            except:
                print('ip无效')
                testnum+=1
        end = time.time()
        data = end - start
        h = data // 3600
        yushu = data % 3600
        m = yushu // 60
        yushu = yushu % 60
        s = yushu
        print('此ip存活的时间：{}时{}分{}秒'.format(h, m, s))
if __name__ == '__main__':
    main()
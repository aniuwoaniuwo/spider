#-*-coding:utf-8-*-#-*-coding:utf-8-*-
#利用requests请求,采用了多线程的方法加快爬取速度，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，cookies，代理，
import re
import time,json,csv
import re,os,pymysql,random
import xlrd,xlwt
import requests
from multiprocessing import Pool,Process
import threading

class Spider(object):
    def __init__(self):#这个适用非excel储存
        self.succese=0
        self.fail=0
        self.rep=0
        self.start = time.time()


    def main(self):
        urls = ['https://www.tianyancha.com/' for i in range(10)] * 1000
        for url in urls:
            print(url)
            try:
                response=requests.get(url=2)
                if response.status_code==200:
                    self.succese += 1
                    print('succese:',self.succese)

                else:
                    self.fail += 1
                    print('fail:',self.fail)
            except Exception as e:
                self.rep+=1
                self.fail += 1
                print('出错了：', e)
                print('总次数：', self.succese + self.fail, '成功次数：', self.succese, '失败次数：', self.fail)
                end = time.time()
                data = end - self.start
                h = data // 3600
                yushu = data % 3600
                m = yushu // 60
                yushu = yushu % 60
                s = yushu
                print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))
                if self.rep>10000:
                    print('总次数：',self.succese+self.fail,'成功次数：',self.succese,'失败次数：',self.fail)
                    end = time.time()
                    data = end - self.start
                    h = data // 3600
                    yushu = data % 3600
                    m = yushu // 60
                    yushu = yushu % 60
                    s = yushu
                    print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))
                    break
        print('结束')



if __name__=='__main__':
    f = Spider()
    # pool = Pool(processes=1)
    threadlist=[]
    for i in range(4):
        t=threading.Thread(target=f.main)
        t.start()
        threadlist.append(t)
    for thread in threadlist:
        thread.join()
    # pool.close()#关闭进程池，不再接受新的进程
    # pool.join()#主进程阻塞等待子进程的退出
# 总次数： 58成功次数： 53失败次数： 5总共花费的时间：0.0时0.0分47.30070519447327秒
# 总次数： 55成功次数： 52失败次数： 3总共花费的时间：0.0时0.0分36.80510497093201秒

# 总次数： 129 成功次数： 118 失败次数： 11总共花费的时间：0.0时0.0分52.83733534812927秒
# 总次数： 123 成功次数： 116 失败次数： 7总共花费的时间：0.0时0.0分41.332364082336426秒
# 总次数： 119 成功次数： 105 失败次数： 14总共花费的时间：0.0时0.0分56.87299346923828秒

# 总次数： 129 成功次数： 117 失败次数： 12总共花费的时间：0.0时0.0分29.270674228668213秒
# 总次数： 137 成功次数： 120 失败次数： 17总共花费的时间：0.0时0.0分35.697041511535645秒
# 总次数： 135 成功次数： 119 失败次数： 16总共花费的时间：0.0时0.0分33.57156252861023秒

# 总次数： 138 成功次数： 119 失败次数： 19总共花费的时间：0.0时0.0分25.931483030319214秒
# 总次数： 145 成功次数： 124 失败次数： 21总共花费的时间：0.0时0.0分28.246615886688232秒
# 总次数： 159 成功次数： 132 失败次数： 27总共花费的时间：0.0时0.0分33.35790801048279秒

# 总次数： 153 成功次数： 129 失败次数： 24总共花费的时间：0.0时0.0分23.924368381500244秒
# 总次数： 164 成功次数： 139 失败次数： 25总共花费的时间：0.0时0.0分24.74741554260254秒

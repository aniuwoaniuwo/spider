#-*-coding:utf-8-*-
#从代理池的一个接口获取一个代理ip
#四个进程同时测试，每个ip最多重试4次
#单个ip重复测试后的ip可用率提高了，可用的ip还是挺可观的
#免费的ip确实太不稳定了，有的即使上一次访问还是可以的，下一次可能马上不能访问，不过也有个别的是稍微稳定
#referer+app


import requests
from multiprocessing import Pool
import time
import re

proxy_url='http://localhost:6666/test'


def get_ip(url):
    try:
        response=requests.get(url,timeout=2.5)#没必要默认10秒等待，免费的代理普遍响应慢，太浪费时间
        if response.status_code==200:
            pattern = re.compile('ip:(.*?)<br/>score:(.*)', re.S)
            items = re.findall(pattern, response.text)
            # print(items, '\n', items[0][0], items[0][1], len(items[0][0]))
            return items
        else:
            return None
    except:
        return None

def ceshi(y,n,i,re,iplist):
    while 1:
        # 单个ip重复测试的指数
        num=0
        f=0
        items = get_ip(proxy_url)
        proxy_ip = items[0][0]
        score = items[0][1]
        print('##################进程{}测试ip中###############'.format(i),'\n','此次测试的ip是：',proxy_ip, '分数为：{}'.format(score))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        proxies = {'http': 'http://' + proxy_ip, 'https': 'https://' + proxy_ip, }
        while num<4:
            num+=1
            try:
                res=requests.get('https://bj.58.com/diannao/?zz=zz',headers=headers,proxies=proxies,timeout=3)
                if res.status_code==200:
                    num=0
                    f+=1
                    iplist[proxy_ip]=score
                    print('进程{}：这是是是是是是是是是有效的ip:'.format(i),proxies,'分数为：{}'.format(score),'继续用','有{}次'.format(f))
            except Exception as e:
                print('继续测试')
        if num==4:
            print(iplist)

if __name__=='__main__':
    start = time.time()
    pool = Pool(processes=1)
    #有效ip指数
    y = 0
    #无效ip指数
    n = 0
    #重试后才成功的ip指数
    re=0
    #可用的ip池
    iplist={}
    for i in range(4):
        pool.apply_async(ceshi, (y,n,i,re,iplist,))
    pool.close()#关闭进程池，不再接受新的进程
    pool.join()#主进程阻塞等待子进程的退出
    end = time.time()
    data = end - start
    h = data // 3600
    yushu = data % 3600
    m = yushu // 60
    yushu = yushu % 60
    s = yushu
    print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))
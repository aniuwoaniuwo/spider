#-*-coding:utf-8-*-
#从代理池的一个接口获取一个代理ip
#四个进程同时测试，每个ip最多重试4次
#单个ip重复测试后的ip可用率提高了，可用的ip还是挺可观的


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
def output(y,n,i,re,iplist):
    print('进程{}:'.format(i),'有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n), '\n','重试后才成功的ip数:{}'.format(re),'\n','可用的ip池有：{}'.format(iplist))

def ceshi(y,n,i,re,iplist):
    while 1:
        # 单个ip重复测试的指数
        num=0
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
            print('进程{}第{}次测试：{}'.format(i,num,proxy_ip),'分数为：{}'.format(score))
            try:
                res=requests.get('https://movie.douban.com/subject/26584183/?tag=热门&from=gaia_video',headers=headers,proxies=proxies)
                if res.status_code==200:
                    iplist[proxy_ip]=score
                    if num!=1:
                        re+=1
                    y+=1
                    print('进程{}：这是是是是是是是是是有效的ip:'.format(i),proxies,'分数为：{}'.format(score))
                    # print('进程{}:'.format(i),'\n',res.text)
                    output(y, n,i,re,iplist)
                    ceshi(y, n,i,re,iplist)
            except Exception as e:
                print('继续测试')
                # print(e)
        if num==4:
            print('进程{}：这不不不不不不不是有效的ip:'.format(i), proxies,'分数为：{}'.format(score))
            n+=1
            output(y,n,i,re,iplist)

if __name__=='__main__':
    start = time.time()
    pool = Pool(processes=4)
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
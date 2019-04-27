#-*-coding:utf-8-*-
#爬取一亩三分地帖子的题目，作者，时间，标题，内容的url
#正则解析+lxml解析，保存到json，比较有可读性
#加头加代理，用类的知识,采取多进程爬取，以后注意采用异步就不用多进程了，异步造成的CPU负担太大
#进程不是函数，返回值就不像函数直接返回，需要其他方法返回，或者巧用字典，将每个进程的返回的值储存到字典里面，再遍历取出来
#匹配出来的内容本身就是一个字符串
#每一页20个网址，就是一个进程20个异步访问，进程池如果设置4process就会造成电脑卡顿了，建议2process
import requests
import re,time
import json
import aiohttp,asyncio,random
from multiprocessing import Pool,Process
from lxml import etree


class ymsfd(object):
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
                      'Cookie':'4Oaf_61d6_saltkey=cQtXVR69; 4Oaf_61d6_lastvisit=1551866410; 4Oaf_61d6_atarget=1; 4Oaf_61d6_hanchuan_tourist=1; 4Oaf_61d6_forum_lastvisit=D_27_1551870214; 4Oaf_61d6_visitedfid=29D27D28; 4Oaf_61d6_viewid=tid_422103; 4Oaf_61d6_lastact=1551870278%09forum.php%09ajax'}
        #self.proxies={'http': 'http://' + proxies, 'https': 'https://' + proxies,}

    def spider(self,url):
        '''
        获取每一页需要爬取的响应文本,返回response
        :return:
        '''
        response=requests.get(url,headers=self.headers)
        if response.status_code==200:
            return response.text
        print('无效网页:none')
        return None
    def spider1(self,response):
        '''
        获得每篇帖子的url编号，返回url编号
        :return:
        '''
        pattern=re.compile('<td.*?icn.*?href="(.*?)".*?</td>',re.S)
        url1s=re.findall(pattern,response)
        url1=[url2 for url2 in url1s]#单个就是字符串，不是数组
        return url1


async def spider2(urll,res_list):
    '''
    异步
    :param url:
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    async with aiohttp.ClientSession() as session:
        async with session.get(urll, headers=headers,verify_ssl=False) as res:
            assert res.status==200
            res_list.append({'res':await res.text(),'url':urll})
def jiexi(res,urll):
    '''
    解析每一页的内容，返回要保存的内容
    :param res:
    :return:
    '''
    pattern=re.compile('<span.*?thread_subject.*?>(.*?)</span>.*?xi2.*?>(.*?)</a>.*?<em.*?authorposton.*?>(.*?)</em>',re.S)
    items=re.findall(pattern,res)
    for item in items:
        if 'title' in item[2]:
            patterns=re.compile('title=\"(.*?)\"')
            ark=re.findall(patterns,item[2])
            return {
                'title': item[0],
                'author': item[1],
                'time': ark[0],
                'address':urll
            }
        return {
            'title':item[0],
            'author':item[1],
            'time':item[2],
            'address': urll
        }


def save(res,urll):
    '''
    保存数据
    :param response:
    :return:
    '''
    with open('sfd.json','a',encoding='utf-8') as f:
        g=[jiexi(res,urll)]
        f.write(json.dumps(g,indent=2,ensure_ascii=False))
        f.write(',')

def main(url,url2,i):
    '''
    主进程，访问目标内容的网址，异步爬取内容
    :param url:
    :return:
    '''
    print('爬取第{}页的内容'.format(i + 1))
    res_list = []
    f=ymsfd()
    response=f.spider(url+url2)
    if response:
        urllist=f.spider1(response)
        print(urllist)
        loop=asyncio.get_event_loop()
        tasks=[spider2(url+url3,res_list) for url3 in urllist]
        loop.run_until_complete(asyncio.wait(tasks))
        for h in range(len(res_list)):
            save(res_list[h]['res'],res_list[h]['url'])


if __name__=='__main__':
    print('开始爬取数据')
    start=time.time()
    url='https://www.1point3acres.com/bbs/'
    url2s = ['forum-27-{}.html'.format(x) for x in range(1,10)]
    pool=Pool(processes=2)
    for i in range(len(url2s)):
        pool.apply_async(main,(url,url2s[i],i,))
    pool.close()
    pool.join()
    '''p=Process(target=main,args=(url,url2s[i],))
        print('爬取第页的内容'.format(i+1))
        p.start()
        ps.append(p)
    for pp in ps:#每个子进程结束后才能运行最后的主程序
        pp.join()'''
    end=time.time()
    print('总的花费时间：'+(end-start))
    print('爬取完成！')




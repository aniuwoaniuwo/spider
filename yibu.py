#-*-coding:utf-8-*-
#异步爬取，正则表达式去解析，保存到text中，以后加个“=======”或者其他的可以更加清楚
import time
import re
import asyncio
import aiohttp
import requests
import os
import itchat
async def creat_joke(url,res_list):
    print("开始爬取joke")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as res:
            assert res.status==200
            res_list.append(await res.text())
def save_joke(response):
    pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
    items = re.findall(pattern, response)
    for i in range(0, len(items)):
        a = items[i].replace('<br/>', '')
        with open("yibuqiushi.txt", "a", encoding='utf-8') as f:  # a是追加,要加上第三个参数，否则读取不了
            f.write(a + "\n")
    #time.sleep(3)


def main():
    start=time.time()
    url_list = ['http://www.qiushibaike.com/hot/page/{}/'.format(str(k)) for k in range(1, 31)]  # format放在引号外面
    loop=asyncio.get_event_loop()
    res_list=[]
    tasks=[creat_joke(host,res_list) for host in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    for response in res_list:
        save_joke(response)
    print("joke爬取完成")
    print((time.time() - start))
main()
#creat_joke()26.849535703659058
#2.0631182193756104异步的速度真的快，比多进程快多了，哈哈哈
#send_news()
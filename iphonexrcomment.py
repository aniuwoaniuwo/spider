#-*-coding:utf-8-*-
#这是爬取淘宝评论的spider，ajax爬取，改变第几页的参数就可以。
# #存到mysql中，运用异步爬取,可是不知道如何添加代理了，一次就被封ip。
import requests
from lxml import etree
import re
import json
import asyncio
import aiohttp
import pymysql
import time
from urllib.parse import urlencode

async def spider(url,reslist):
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
    #cookies='miid=66021821398803028; cna=T5v6ExYKsioCAXjGir3cnUeC; UM_distinctid=165a526d791141-080dfd80d91323-10724c6f-100200-165a526d792352; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; enc=PDz5uyXaxLd%2FtRYC4zpNSBv9OTbd17ojQ7MA%2FaX3rYo8CPdX03TpG3SeQXA3KIrh1TF4ZsT59TdmKAD5%2BVLxNQ%3D%3D; _m_h5_tk=173d04d4312553c40aabd32435b2ef77_1545457016178; _m_h5_tk_enc=c48e4128186a41fe4c783444121511d4; v=0; unb=2425266207; sg=%E5%BA%8670; t=3cf9640ae786cf7788cf424d4e2b04d6; _l_g_=Ug%3D%3D; skt=60f124549b562473; cookie2=109692fac4b05b76de581466ad86b5b0; cookie1=VFXRORIILlkdvFXxq0y4EiXa3qaSxZ37HjntmI1cBbU%3D; csg=4c46df9a; uc3=vt3=F8dByRMDC0lieCWhnDY%3D&id2=UUwSD2zINIFCwg%3D%3D&nk2=qVXZ0zLin%2FI%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTU0NTQ0NzIwNg%3D%3D; tracknick=%5Cu662F%5Cu949F%5Cu542F%5Cu5E86; lgc=%5Cu662F%5Cu949F%5Cu542F%5Cu5E86; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu662F%5Cu949F%5Cu542F%5Cu5E86; _nk_=%5Cu662F%5Cu949F%5Cu542F%5Cu5E86; cookie17=UUwSD2zINIFCwg%3D%3D; tg=0; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTYM8KFA8YM2w%3D%3D&tag=8&lng=zh_CN; mt=ci=1_1; _tb_token_=738fe737433e8; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261545448306203; l=aBeC_B-dyF5MRlEXkMaO_VtnD707gyBzIA7wAMwLuTEhNPI1RDuMylrbk_wINJNQNrhX_U2D5052h; isg=BJSUS1SRtFoBcif4cOB56DIia9LGRbnT6giHvi51o5-VGTVjVvz0Z--fHVEk-vAv'
    #referer='https://item.taobao.com/item.htm?id=580000998253&ali_refid=a3_430673_1006:1150059063:N:iphone+xr:d04e39d0a3db9d268c4f78dd6c8a6fcd&ali_trackid=1_d04e39d0a3db9d268c4f78dd6c8a6fcd&spm=a2e15.8261149.07626516002.1'
    proxies = {'http': 'http://61.135.217.7:80'}
    t = str(time.time()).split('.')#去除时间秒数后的小数点
    #print(t[0],t[1])
    param={
        '_ksTS': '%s_%s' % (t[0], t[1]),
        'callback': 'jsonp%s' %(int(t[1])+1)
    }
    #url=url+urlencode(param)
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0','Connection': 'keep-alive'}
    #headers={'User-Agent':user_agent,'Cookies':cookies,'Connection': 'keep-alive','Referer':referer,'accept-encoding':'gzip, deflate, sdch, br','accept-language':'zh-CN,zh;q=0.8'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as res:
            assert res.status==200
            reslist.append(await res.text())
def save(res,k):
    print(res)
    jsons=re.findall(r'{.*}',res)[0]#除去json格式外的东西，匹配出来是list
    json1=json.loads(jsons)#这是一个字典模式，把字典变成json格式然后 可以用json的函数
    print(json1)
    comment2=json1.get('comments')
    print(comment2)
    data = {}
    for comment in comment2:
        comment1=comment.get('content')
        if comment1:
            print(comment1)
            data['id']=k#储存到mysql数据库
            data['comment'] = comment1
            table='tbcomment'
            keys=','.join(data.keys())
            values=','.join(['%$']*len(data))
            sql='INSERT INTO {table}({keys}) values({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
            update=','.join([" {key}=%$".format(key=key) for key in data])
            sql=sql+update
            try:
                if cursor.execute(sql,tuple(data.values())*2):
                    print('successful')
                    db.commit()
            except:
                print('failed')
                db.rollback()
        else:
            print('wrong')
if __name__=='__main__':
    try:
        db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, database='spider')
        cursor = db.cursor()#连接数据库
        k=1

        urllist = [
            'https://rate.taobao.com/feedRateList.htm?auctionNumId=580000998253&userNumId=2529466216&currentPageNum=1&_ksTS=1545448307516_2832&callback=jsonp_tbcrate_reviews_list'] #爬取的url
        reslist = []
        loop = asyncio.get_event_loop()
        tasks = [spider(host, reslist) for host in urllist]
        loop.run_until_complete(asyncio.wait(tasks))
        for res in reslist:
            save(res,k)
            print('正在爬取第{}页的评论:'.format(k))
            k+=1
        print('complete')
    except IOError:
        pass
    else:
        db.close()
#https://rate.taobao.com/feedRateList.htm?auctionNumId=580000998253&userNumId=2529466216&currentPageNum=1&_ksTS=1545448307516_2832&callback=jsonp_tbcrate_reviews_list
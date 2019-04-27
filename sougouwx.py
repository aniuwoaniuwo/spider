#-*-coding:utf-8-*-
#爬取搜狗微信站点的文章信息，文章题目，作者，时间，内容开头，网址
#需要登录才能爬取100页的内容，cookies，headers，用代理池加代理，
#设置访问失败回调，失败四次就放弃访问，放进一份名单里，lxml解析，获取,html是从1开始而不是0
#-*-coding:utf-8-*-
#requests+etree爬虫模板，带有headers，cookies，代理，数据库保存，txt保存，excel保存
import requests,csv
import time
import re,os,pymysql,random
from lxml import etree
import xlrd,xlwt,json
from multiprocessing import Pool
class Spider(object):
    def __init__(self):#这个适用非excel储存
        '''
        类的变量
        '''
        self.proxies = {}
        cookie='SUV=00234F7478C68ABD5B73ACEB47254783; pgv_pvi=6293245952; ssuid=6044945762; CXID=A061ABDEB4CEFE96E2967BE577FF685A; teleplay_play_records=teleplay_566683:1; sw_uuid=2331583150; sg_uuid=1511473282; SUID=BD8AC6784F18910A000000005B756B65; YYID=206983117D035E1CD6BB3D36FCF62E19; ad=wpoZqkllll2tYDvtlllllVh3BIGlllllTLPlvZllll9lllllRuecws@@@@@@@@@@; ABTEST=0|1552910409|v1; SMYUV=1553609034075858; cd=1553777013&1cd0495cfda7fba69826132beb674545; IPLOC=CN4400; JSESSIONID=aaa3_LgGCY35vhUacvjNw; ld=tyllllllll2txFfJgJhM3VhKy7NtXGVCKqo3ollllltlllll4klll5@@@@@@@@@@; LSTMV=254%2C78; LCLKINT=2737; weixinIndexVisited=1; sct=114; ppinf=5|1553941732|1555151332|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlOTElQkMlRTUlOTMlQTd8Y3J0OjEwOjE1NTM5NDE3MzJ8cmVmbmljazoxODolRTUlOTElQkMlRTUlOTMlQTd8dXNlcmlkOjQ0Om85dDJsdUpaOWtuLVVzQWhUVlZCVlpTU3RCNkFAd2VpeGluLnNvaHUuY29tfA; pprdig=CYQp3Rx-e947mE35Py0qAuio7_67SdbBjbodVIXhDS_jTzRDbaXifaTED0E03xgGhYQjlHVIG1hRWbvR4SuBUOHd3T4elLZ_NdCIxr0GO1Y7rIhi37s2kjxhMoOPvlBL5f38QriiXBmRaTiQ45A-wPUK1sJ_Tu0L-69NyDiobhE; sgid=12-39902461-AVyfROSfic7sxUUqpgKauLPA; ppmdig=1553941195000000a0c83cbdc5779714d5e9836ab4ace825; PHPSESSID=706ep4ob55ooham9l0i7g235r7; usid=ea-sq7v53o_ko1fq; SNUID=E098B206D9DC5F97937D7D83DA0DA383'
        # 重试阀值
        self.cu = 0
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
        self.headers = {'User-Agent': user_agent,  'Cookie': cookie}
        #请求失败的网址
        self.rest=[]
        self.k=1

    def get_ip(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:
            return None

    def spider(self,url):
        '''
        获取响应，返回响应
        :param url:
        :return:
        '''
        try:
            proxies=self.get_ip()
            if proxies:
                self.proxies={'http': 'http://' + proxies, 'https': 'https://' + proxies, }
                print('ip:',self.proxies)
            response=requests.get(url,headers=self.headers,proxies=self.proxies)
            if response.status_code==200:
                self.cu = 0
                return response.text
            else:
                if self.cu<4:
                    self.cu+=1
                    print('出错了，重试')
                    self.spider(url)
                else:
                    self.cu = 0
                    print('被封了，或者网页不存在,跳过')
                    self.rest.append(url)
                    return None
        except Exception as e:
            print(e)
            print('太频繁了，等待5s')
            time.sleep(5)
            if self.cu < 6:
                self.cu += 1
                self.spider(url)
            else:
                print('被封了，或者网页不存在')
                self.rest.append(url)

    def jiexi(self, response):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            s = etree.HTML(response)
            td = s.xpath('//*[@id="main"]/div[5]/ul/li')
            for p in td:
                title = p.xpath('./div[2]/h3/a/text()')
                author = p.xpath('.div[2]/div/a/text()')
                time = p.xpath('.div[2]/div/span/text()')
                content = p.xpath('.div[2]/p/text()')
                address = p.xpath('./div[2]/h3/a/@data-share')
                title = title[0] if len(title) > 0 else 'null'
                author = author[0] if len(author) > 0 else 'null'
                time = time[0] if len(time) > 0 else 'null'
                content = content[0] if len(content) > 0 else 'null'
                address = address[0] if len(address) > 0 else 'null'
                yield [title, author, time, content, address]
        else:
            return None

    def csv(self, item):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('wxouguan.csv', 'a', encoding='utf-8') as f:
            names = ['title', 'author','time','content','address']
            writer = csv.writer(f)
            if self.k == 1:
                writer.writerow(names)
                self.k += 1
            writer.writerow([item[0],item[1],item[2],item[3],item[4]])

    def main(self,url,i):
        '''
        进程启动入口
        :return:
        '''
        print('正在爬取第{}页'.format(i))
        response = self.spider(url)
        for item in self.jiexi(response):
            print(item)
            self.csv(item)
        time.sleep(4)

if __name__=='__main__':
    start = time.time()
    f = Spider()
    urls = [
        'http://weixin.sogou.com/weixin?query=%E6%AC%A7%E5%86%A0&_sug_type_=&sut=6545&lkt=1%2C1553941706038%2C1553941706038&s_from=input&_sug_=y&type=2&sst0=1553941706143&page={}&ie=utf8&w=01019900&dr=1'.format(
            i) for i in range(1, 101)]
    pool = Pool(processes=4)
    for i in range(len(urls)):
        pool.apply_async(f.main, (urls[i],i,))
    pool.close()
    pool.join()
    if len(f.rest)>0:
        print('总共还有{}个网址没有成功访问，现在继续。'.format(len(f.rest)))
        print(f.rest)
        for url1 in f.rest:
            f.main(url1)
    end = time.time()
    print('总共花费的时间：', (end - start))
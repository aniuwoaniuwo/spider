#-*-coding:utf-8-*-
#爬取小说，每一章的后面都有下一章的url，所以就不要用异步了，因为会导致取不到url报错
#小说是有先后的，可以运用多进程+正则表达式爬取，一个文本存一定的章数，一个文本一个进程爬取
#加上ip代理爬取，用到类最好
import requests
import re,time,random
from multiprocessing import Pool,Process

class novel(object):
    def __init__(self,url):
        self.baseurl = url#'https://xs.sogou.com'#全局变量
        iplist=['http://61.135.217.7:80']
        proxies=random.choice(iplist)
        proxies = {'http': proxies}
        print(proxies)
        self.proxies=proxies
    def spider(self,href):#爬取html与储存一起
        self.href = href#'/chapter/5153804174_168878114094447/'
        try:
            for i in range(0, 15):
                user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
                referer='https://xs.sogou.com/book/5153804174/'
                cookies='SUV=00234F7478C68ABD5B73ACEB47254783; pgv_pvi=6293245952; sw_uuid=9129834677; sg_uuid=561832967; ssuid=6044945762; CXID=A061ABDEB4CEFE96E2967BE577FF685A; teleplay_play_records=teleplay_566683:1; SUID=BD8AC6784F18910A000000005B756B65; YYID=206983117D035E1CD6BB3D36FCF62E19; usid=ea-sq7v53o_ko1fq; cd=1544926214&0e42495d0cba3090a50f2bfa2c5fa04c; IPLOC=CN4400; guest_uid=guest_2664698324; reader_help_tip=1; SNUID=41C06895E1E59C067EBAC15BE1494ADE; sct=66; ld=0yllllllll2txFfJgxQ1xOZ6y3HtVbypKqo3olllllwlllllpZlll5@@@@@@@@@@; LSTMV=381%2C396; LCLKINT=10917; SGS_FE_WAID=WAID2018102600000000000016597059; JSESSIONID=aaaPad4mHSdvEg7-e6ZFw'
                headers={'User-Agent':user_agent,'Referer':referer,'Cookies':cookies}
                url=self.baseurl+self.href
                response=requests.get(url,headers=headers,proxies=self.proxies).text
                #print(response)
                pattern=re.compile(r'<a href="(/chapter/.*?)"',re.S)#不能随便.*?匹配，不然匹配多了很多东西。看第二页的html，这样匹配不好。
                self.href=re.findall(pattern,response)[1]#匹配出来的是元组，所以需要取第一个
                #print(self.href)
                pattern1=re.compile(r'<title>(.*?)</title>')
                zhangjie=re.findall(pattern1,response)[0]
                print('正在爬取', zhangjie)
                pattern2=re.compile(r'<div id="contentWp" style="display:none">(.*?)</div>',re.S)#网页上面的跟requests.get的不一样，多了style，所以之前一直爬取不了
                comtent=re.findall(pattern2,response)[0]
                comtent=comtent.replace('<p>','\r\n\t')#换成换行符并且空两格
                comtent=comtent.replace('</p>','')
                comtent=comtent.replace('&ldquo;','"')
                comtent=comtent.replace('&rdquo;','"')
                comtent=comtent.replace('&hellip;&hellip;','······')
                comtent=comtent.replace('&mdash;','-')
                if i==0:
                    file=open("御仙诀{}后的15章.txt".format(zhangjie),"a",encoding='utf-8')#在循环中只运行一次，创建文件夹
                #print(comtent)
                file.write(zhangjie+"\n")
                file.write(comtent+"\n")
                if self.href=='':
                    return
        except EOFError as e:
            print('except:',e)
        finally:
            file.close()#确保可以保存
def main():
    start=time.time()
    ater=novel('https://xs.sogou.com')
    hreflist=['/chapter/5153804174_168878114094447/','/chapter/5153804174_168878114216928','/chapter/5153804174_168878114337129','/chapter/5153804174_168878114459186','/chapter/5153804174_168878114579100','/chapter/5153804174_168878114705337','/chapter/5153804174_168878114824932','/chapter/5153804174_168878114950638','/chapter/5153804174_168878115157343']
    for href in hreflist:
        p=Process(target=ater.spider,args=(href,))
        p.start()
    p.join()
    end=time.time()
    print('总共花费的时间为：', (end-start))
if __name__=='__main__':
    main()



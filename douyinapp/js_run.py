#-*-coding:utf-8-*-
import json
from selenium import webdriver
import requests,re
import time

share_id='83072448142'
share_url='https://www.douyin.com/share/user/{}'.format(share_id)
with open('decode_js.txt','r') as f:
    f5=f.read()

with open('decode_js1.txt','r') as f2:
    f6=f2.read().replace("&&&",share_id)


# headers={'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}
response=requests.get(share_url,headers=headers).text
# print(response)
#不需要匹配单引号，是url的字符串
pattern=re.compile("dytk: '(.*?)'",re.S)
dytk=re.findall(pattern,response)[0]
# print(dytk)
#注意匹配进去单引号，js里面的字符串括起来
pattern1=re.compile(r"<script>tac=(.*?)</script>",re.S)
tac="var tac="+re.findall(pattern1,response)[0]+";"
# print(tac)
# "<script>tac='i)69zsyk4vys!i#bs0s"0,<8~z|\x7f@QGNCJF[\\^D\\KFYSk~^WSZhg,(lfi~ah`{md"inb|1d<,%Dscafgd"in,8[xtm}nLzNEGQMKAdGG^NTY\x1ckgd"inb<b|1d<g,&TboLr{m,(\x02)!jx-2n&vr$testxg,%@tug{mn ,%vrfkbm[!cb|'</script>"

with open('decode_js.html','w') as f1:
    f1.write(f5+'\n'+str(tac)+'\n'+f6)
    # f1.write(f5 )

driver=webdriver.Chrome()
driver.get('C:\spider\douyinapp\decode_js.html')
_signature=driver.title
# _signature=input('输入_signature密匙：')
# print(_signature)
# _signature=
video_url='https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id='+share_id+'&sec_uid=&count=21&max_cursor=0&aid=1128&_signature='+_signature+'&dytk='+dytk
headers1={
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
# "authority":"www.iesdouyin.com",
# "method":"GET",
# "path":"/web/api/v2/aweme/post/?user_id=83072448142&sec_uid=&count=21&max_cursor=0&aid=1128&_signature=0CJdgBATjXEVRwUNDT5v49AiXZ&dytk=0091c461fa8e5292f574d08e67c552b1",
# "scheme":"https",
# "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
# "accept-encoding":"gzip,deflate, br",
# "accept-language":"zh-CN,zh;q=0.9",
# # "cache-control":"max-age=0",
# "upgrade-insecure-requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
}
while 1:
    response=requests.get(video_url,headers=headers)
    # print(response.text,response.url)
    if json.loads(response.text)['aweme_list']==[]:
        time.sleep(1)
        driver.get(video_url)
        print(driver.page_source)
        break
    else:
        print(response.text, response.url)
        break

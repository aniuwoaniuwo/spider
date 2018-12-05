#-*-coding:utf-8-*-
import requests,urllib.parse
from lxml import etree
import urllib.request
import re
import http.cookiejar

headers={'Cookie': 'll="118289"; bid=YeqEpAwe8XU; __yadk_uid=EtJvpv06cJP5CJdBh7R1ZAs9gypRtITn; douban-fav-remind=1; ps=y; douban-profile-remind=1; dbcl2="167986306:+pD3vncdkMY"; ck=tJgr; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1543125663%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%22%5D; _pk_id.100001.4cf6=77dc2231794329c7.1535642645.14.1543125663.1543112720.; __utma=30149280.17400769.1540812629.1543111710.1543125663.5; __utmc=30149280; __utmz=30149280.1543125663.5.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.16798; __utma=223695111.954159437.1540812629.1543111710.1543125663.5; __utmc=223695111; __utmz=223695111.1543125663.5.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D91AD00D97E0BCC0DBB2DFD8834DCB569|67c211ac2d584779c1bc62e82dca76c3',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
url='https://accounts.douban.com/login'


response=requests.get(url)
params= { }

#print(response.text)
if True:
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', response.text)
    captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', response.text)
    print(imgurl.group(1))
    urllib.request.urlretrieve(imgurl.group(1), 'C:\\lx\\yanzhengma\\' + '1.png')
    yzm=input('输入验证码：')
    params['captcha-solution'] = yzm
    params['form_email'] = '18813295794'
    params['form_password'] = '18898604973db'  # 这里写上已有的用户名和密码
    params["captcha-id"] = captcha.group(1)  # 这个是动态生成的，需要从网页中获得
    #params["user_login"] = "登录"

    #response1 = opener.open(url, urllib.parse.urlencode(params).encode(encoding='UTF8'))  # 登录豆瓣电影
    #response1 = requests.post(url, urllib.parse.urlencode(params).encode(encoding='UTF8'))  # 登录豆瓣电影
    response1=requests.post(url,headers=headers,data=params)
    print(response1,response1.text)
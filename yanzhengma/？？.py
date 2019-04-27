#-*-coding:utf-8-*-
import requests,urllib.parse
from lxml import etree
import urllib.request
import re
import http.cookiejar

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
url='https://accounts.douban.com/login'
response=requests.get(url,headers=headers)
params= { }
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
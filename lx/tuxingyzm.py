
import re
import urllib.request
import http.cookiejar

# from http.comkie import CookieJar  上面那句和这句等同
loginurl= 'https://www.douban.com/accounts/login'
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)  # 在已存的Cookie下建立连接

params= { }
params['form_email']= '18813295794'
params['form_password']= '18898604973db'  # 这里写上已有的用户名和密码
params['source']= 'http://www.douban.com/accounts/login'

# 从首页提交登陆
response = opener.open(loginurl, urllib.parse.urlencode(params).encode(
    'utf-8'))  # urllib.parse.urlencode(params).encode('utf-8')这个是向服务
# 器POST的内容，可以打印一下response.geturl()请求的连接看一下
# print(response.geturl()[0:33])
# 验证成功跳转至登陆页
if response.geturl()[0:33]== 'https://accounts.douban.com/login':
    html = response.read().decode('utf-8')
    # print(html)，可以先打印一下文件内容，为了看到网页元素更方便的写正则，可以复制下来，在需要获取的地方用(.+?)表示，然后用group()元组来取得，
    # 验证图片地址
    imgurl=re. search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>',html)
    if imgurl:
        url= imgurl .group(1)
        # print(url)
        # 将验证码以v.jpg保存在本地，在输入验证码的时候可以手工输入
        res= urllib .request.urlretrieve(url, 'v.jpg')
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>',html)
        # print(captcha.group(1))
        if captcha:
            vcode=input ( '请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)  # 这个是动态生成的，需要从网页中获得
            params["user_login"] = "登录"
            # 提交验证码验证
            response = opener.open(loginurl,urllib .parse.urlencode(params).encode('utf-8'))
            if response.geturl()== "https://www.douban.com/":
                print("login sucess",response.read())

                #print(cookie)
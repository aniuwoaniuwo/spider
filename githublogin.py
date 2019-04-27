#-*-coding:utf-8-*-
#session就是维持登录状态，通常登录的时候是post方法，data是递交的表单，
# 往往会在登录后响应的第一个包有（session或者join等），按照这个表单的内容构造
#一些看起来像是加密的参数并且会变的可以尝试在登录界面的html直接寻找，这里会有两个参数，看清楚选择第一个
# 一般是隐藏在其中，登录的时候网页自己加进去了，比如github网站的authenticity_token参数
#登录后就可以获取cookies了，或者session继续访问

import requests
from lxml import etree

class github(object):
    def __init__(self):
        self.login='https://github.com/login'
        self.post='https://github.com/session'
        self.session=requests.session()
        self.other='https://github.com/aniuwoaniuwo/qianduan'
        self.headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36'
                      ,'Referer':'https://github.com/','Host':'github.com'}

    def get_token(self):
        '''
        获取登录需要的token，返回token
        :param url:
        :return:
        '''
        response=self.session.get(self.login,headers=self.headers)
        if response.status_code==200:
            token=etree.HTML(response.text).xpath('/html/body/div[2]/div/form/input[2]/@value')[0]
            return token

    def postlogin(self):
        '''
        构造表单进行登录，打印响应的内容
        :param url:
        :return:
        '''
        formdata={
            'commit':'Sign in',
            'utf8':'✓',
            'authenticity_token':self.get_token(),
            'login':'1689463866@qq.com',
            'password':'1689463866git'
        }
        response=self.session.post(self.post,data=formdata,headers=self.headers)
        #print(self.get_token())
        #print(response.text)
        print(response.status_code)
        if response.status_code==200:
            print('成功登录')

    def sessions(self,url):
        '''
        继续访问其他节点，验证session
        :return:
        '''
        response=self.session.get(url,headers=self.headers)
        if response.status_code == 200:
            #print(response.text)
            print('又成功登录')

if __name__=='__main__':
    f=github()
    f.postlogin()
    f.sessions(f.other)



#-*-coding:utf-8-*-
#这里用到的是ajax爬虫，爬去的是今日头条的街拍妹子图，因为这个是ajax加载的，和微博一样，所以用了requests得到json文本然后用正则表达式获取图片的下载地址
import requests
import re
from urllib.parse import urlencode
import urllib.request

def get_json():

    baseurl='https://www.toutiao.com/search_content/?'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
    x=1
    for i in range(0,5):
        para=i*20
        print(para)
        params = {
            'offset': para,
            'format': 'json',
            'keyword': '街拍',
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab'
        }  # keyword那一段就是街拍的编码
        url=baseurl+urlencode(params)
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            ress1=response.json().get('data')
            print(response.text)
            print(response.json())
            for ress in ress1:
                #print(ress)
                if ress.get('image_list'):
                    for res in ress.get('image_list'):
                        if hasattr(res,'get'):#有的image_list是list有的是str，所以要判断,list中是字典，有get属性，此函数就是这个判断
                            item=res.get('url')
                            print(item)
                            urls = 'http:' + item
                            urllib.request.urlretrieve(urls, 'c:\\pachong\\jiepai\\' + '%s.jpg' % x)
                            x += 1
                        else:

                            #print(res)
                            #res1={'dd':'dnjd','dddd':'ooo'}这里只是验证正则表达式不能直接匹配字典，要遍历了字典才能匹配
                            #res2='55'这里辅助验证并不是我的其他语法有错，因为我用了字符串来匹配，结果是成功的
                            '''pattern = re.compile(r'^{url:"(.*?)"}$', re.S)
                            items = re.findall(pattern,res)
                            for item in items:
                                urls = 'http:' + item
                                urllib.request.urlretrieve(urls, 'c:\\pachong\\jiepai' + '%s.jpg' % x)
                                x += 1'''
def get_image(res,x):
    pattern=re.compile(r'^{url:"(.*?)"}$',re.S)
    items=re.findall(pattern,res)
    for item in items:
        urls='http:'+item
        urllib.request.urlretrieve(urls,'c:\\pachong\\jiepai'+'%s.jpg' % x)
        x+=1
if __name__=='__main__':
    get_json()
    print('done!')






#-*-coding:utf-8-*-
import requests
import requests

s = requests.Session()
s.get('http://www.baidu.com/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

'''url='http://httpbin.org/post'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
data={'value1':'1','value2':'2'}
r=requests.get(url,params=data,headers=header)
print(r.text,r.cookies,r.encoding,r.url)'''
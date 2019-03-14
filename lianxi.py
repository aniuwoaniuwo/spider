#-*-coding:utf-8-*-
import requests
import requests,json

s = requests.Session()
s.get('http://www.baidu.com/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

'''url='http://httpbin.org/post'

header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
data={'value1':'1','value2':'2'}
r=requests.get(url,params=data,headers=header)
print(r.text,r.cookies,r.encoding,r.url)'''
'''data=[{
    'ranking': '无数据',
    'pictrue':'无数据'
}]
with open('maoyan55.json', 'a', encoding='utf-8') as f:
    f.write(str(data))
print(json.dumps(data))
print(requests.get('https://hotel.qunar.com/city/guangzhou/').status_code,requests.get('https://hotel.qunar.com/city/guangzhou/').text)'''
'''str=[]
s=" "
print('s0:',s[0])
if s[0] not in str:
    str.append(s[0])
print(len(s))
print(len(str))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str=[]
        max=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in str:
                    str.append(s[j])
                else:
                    break
            f = len(str)
            str = []
            if max < f:
                max = f
        return max
if __name__=='__main__':
    f=Solution()
    s=" "
    print(f.lengthOfLongestSubstring(s))'''
'''from multiprocessing import Pool,Process
def jj(i):
    list=[]
    f=10+i
    for h in range(i,f)
        list.append(h)
    return list
def printg():
    print(list)
if __name__=='__main__':#暂时写到txt储存的，excel和数据库用到再改善

    for i in range(10):
        pi=Process(target=jj,args=(i,))
        pi.start()

    pi.join()#最后一个要结束才可以继续下面的进程'''
import re
r='ni'
print(r)
print('fff')
patterns=re.compile('title=\"(.*?)\">',re.S)
#-*-coding:utf-8-*-
import requests,re
share_id='83072448142'
share_url='https://www.douyin.com/share/user/'+share_id
headers1={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
headers={
"Host":"www.douyin.com",
"Connection":"keep-alive",
# "Cookie":"_ga=GA1.2.592071529.1564800335; _ba=BA0.2-20190803-5199e-3Xyum9eCvhg4E2QXOBe7; _gid=GA1.2.452702564.1565104599",
"Accept-Encoding":"gzip",
"sdk-version":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
"X-Gorgon":"0300b71d4001237cb4cc5a176a78a7d7c8f2862a8cfa600d9b33",
"X-Khronos":"1565002284",
}
response=requests.get(share_url,headers=headers).text
# print(response)
pattern=re.compile("dytk: '(.*?)'",re.S)
dytk=re.findall(pattern,response)
print(dytk)
pattern1=re.compile("<script>tac=(.*?)</script>",re.S)
# tac=re.findall(pattern1,response)
tac="var tac="+re.findall(pattern1,response)[0]+";"
print(tac)
a=1
b=input('?:')
print(a+int(b))
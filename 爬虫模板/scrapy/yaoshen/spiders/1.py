#-*-coding:utf-8-*-
import requests
import random
cookie = {}

cookies = 'll="118289"; bid=YeqEpAwe8XU; douban-fav-remind=1; __yadk_uid=wiDypSDJGAQYh6B6L4buy9SC6tXm8p0z; _vwo_uuid_v2=D91AD00D97E0BCC0DBB2DFD8834DCB569|67c211ac2d584779c1bc62e82dca76c3; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1540560769%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D18813295794%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252F%26source%3Dindex_nav%26error%3D1013%22%5D; dbcl2="167986306:1Vq9vX08upY"; ck=sPgT; douban-profile-remind=1; _pk_id.100001.8cb4=5667ffad47e24e7a.1534860416.5.1540563012.1540557104.; _pk_ses.100001.8cb4=*; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0'#cookie大概是这么一个格式



for line in cookies.split(';'):

    key,value = line.split("=", 1)

    cookie[key] = value #格式化操作，装载cookies


accept = 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8'
accept_encoding = 'gzip, deflate, sdch, br'
accept_language = 'zh-CN, zh;q = 0.8'
cache_control = 'max-age = 0'#下滑线一定是最下面，不能在中间
#cookie= 'll="118289"; bid=YeqEpAwe8XU; douban-fav-remind=1; __yadk_uid=wiDypSDJGAQYh6B6L4buy9SC6tXm8p0z; _vwo_uuid_v2=D91AD00D97E0BCC0DBB2DFD8834DCB569|67c211ac2d584779c1bc62e82dca76c3; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1540560769%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D18813295794%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252F%26source%3Dindex_nav%26error%3D1013%22%5D; dbcl2="167986306:1Vq9vX08upY"; ck=sPgT; douban-profile-remind=1; _pk_id.100001.8cb4=5667ffad47e24e7a.1534860416.5.1540563012.1540557104.; _pk_ses.100001.8cb4=*; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0'
host= 'movie.douban.com'

user_agent= 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
headers={'Accept':accept, 'User-Agent':user_agent,'Host': host,'Accept-Encoding':accept_encoding,'Cookie':cookie, 'Accept-Language': accept_language,'Cache-Control':cache_control}


ip_list = ['http://118.190.95.35:9001', 'http://61.135.217.7:80', 'http://125.70.13.77:8080']
proxy_ip = random.choice(ip_list)
print(proxy_ip)
proxies = {'http': proxy_ip}

cookies={'ll':'118289', 'bid':'YeqEpAwe8XU'}#这里失败的原因是并不是全部的cookie
print(cookie)
s=requests.get('https://movie.douban.com/subject/26752088/comments?start=280',cookies=cookie,proxies=proxies)#cookie是一个字典{'ll': '"118289"', ' bid': 'YeqEpAwe8XU', ' douban-fav-remind': '1', ' __yadk_uid': 'wiDypSDJGAQYh6B6L4buy9SC6tXm8p0z', ' _vwo_uuid_v2': 'D91AD00D97E0BCC0DBB2DFD8834DCB569|67c211ac2d584779c1bc62e82dca76c3', ' ps': 'y', ' _pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1540560769%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D18813295794%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252F%26source%3Dindex_nav%26error%3D1013%22%5D', ' dbcl2': '"167986306:1Vq9vX08upY"', ' ck': 'sPgT', ' douban-profile-remind': '1', ' _pk_id.100001.8cb4': '5667ffad47e24e7a.1534860416.5.1540563012.1540557104.', ' _pk_ses.100001.8cb4': '*', ' ap_v': '0,6.0', ' push_noty_num': '0', ' push_doumail_num': '0'}
print(s.text)
print(s.cookies)
print(s.cookies.get_dict())
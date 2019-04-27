#-*-coding:utf-8-*-
#从代理池的一个接口获取一个代理ip
import requests


proxy_url='http://localhost:5555/random'
def get_ip(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            return None
    except:
        return None
def ceshi():
    proxy_ip=get_ip(proxy_url)
    print(proxy_ip)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    proxies={'http': 'http://'+proxy_ip,'https': 'https://'+proxy_ip,}
    try:
        res=requests.get('http://httpbin.org/get',headers=headers,proxies=proxies)
        print(res.text)
        if res.status_code==200:
            print('这是有效的ip:',proxies)
        else:
            ceshi()
    except Exception as e:
        print('继续测试')
        ceshi()
        print(e)

ceshi()
#-*-coding:utf-8-*-
#从代理池的一个接口获取一个代理ip
#ip可利用率大概有10%
import requests

proxy_url='http://localhost:5555/random'
y=0
n=0
def get_ip(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            return None
    except:
        return None
def output(y,n):
    print('有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n), '\n')

def ceshi(y,n):
    while 1:
        print('##################测试ip中###############')
        proxy_ip = get_ip(proxy_url)
        print('此次测试的ip是：',proxy_ip)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        proxies = {'http': 'http://' + proxy_ip, 'https': 'https://' + proxy_ip, }
        try:
            res=requests.get('https://movie.douban.com/subject/26584183/?tag=热门&from=gaia_video',headers=headers,proxies=proxies)
            # print(res.text)
            if res.status_code==200:
                y+=1
                print('这是有效的ip:',proxies)
                output(y, n)
            else:
                n+=1
                output(y, n)
                print('这不是有效的ip:', proxies)
                ceshi(y,n)
        except Exception as e:
            n+=1
            print('这不是有效的ip:', proxies)
            print('继续测试')
            print(e)
            output(y, n)
            ceshi(y,n)

ceshi(y,n)
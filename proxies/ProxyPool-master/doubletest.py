#-*-coding:utf-8-*-
#从代理池的一个接口获取一个代理ip
#可以有效访问http://httpbin.org/get的不一定可以访问其他的网址，比列也很低
import requests,re

# proxy_url='http://localhost:6666/random'
proxy_url='http://localhost:6666/test'
y=0
n=0
num=0
def get_ip(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            pattern = re.compile('ip:(.*?)<br/>score:(.*)', re.S)
            items = re.findall(pattern, response.text)
            # print(items, '\n', items[0][0], items[0][1], len(items[0][0]))
            return items
        else:
            return None
    except:
        return None
def output(y,n,num,score):
    print('有效的ip数：{}'.format(y), '\n', '无效的ip数：{}'.format(n),'\n','分数为：{}'.format(score), '\n', '通用的ip数：{}'.format(num))

def ceshi(y,n,num):
    while 1:
        print('##################测试ip中###############')
        items = get_ip(proxy_url)
        proxy_ip=items[0][0]
        score=items[0][1]
        print('此次测试的ip是：',proxy_ip,'分数为：{}'.format(score))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        proxies = {'http': 'http://' + proxy_ip, 'https': 'https://' + proxy_ip, }
        try:
            res=requests.get('http://httpbin.org/get',headers=headers,proxies=proxies)
            # print(res.text)
            if res.status_code==200:
                y+=1
                print('这是有效的ip:',proxies)
                try:
                    res1 = requests.get('https://movie.douban.com/subject/26584183/?tag=热门&from=gaia_video', headers=headers, proxies=proxies)
                    if res1.status_code == 200:
                        print(res1.text)
                        num+=1
                        print('这是通用的ip:',proxy_ip)
                        output(y, n, num)
                    else:
                        print('这是不通用的ip')
                        output(y, n, num)
                except Exception as e:
                    print('这是不通用的ip')
                    print(e)
                    output(y, n, num)

            else:
                n+=1
                output(y, n, num)
                ceshi(y,n,num)
        except Exception as e:
            n+=1
            print('继续测试')
            print(e)
            output(y, n, num)
            ceshi(y,n,num)

ceshi(y,n,num)
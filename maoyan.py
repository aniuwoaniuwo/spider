#-*-coding:utf-8-*-
#爬取猫眼的top100电影信息，json保存，正则表达式解析
#生成器就相当于一个独立的函数，不能嵌套也最好不要用类
import requests,re,json,time

def spider(url):
    User_Agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    headers={'user-agent':User_Agent}
    response=requests.get(url,headers=headers)
    return response
def jiexi(response):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,response.text)
    for item in items:
        yield {
            'ranking':item[0] if item[0] else '无数据',
            'pictrue':item[1] if item[1] else '无数据',
            'name':item[2] if item[2] else '无数据',
            'star':item[3].strip()[3:] if item[3] else '无数据',
            'time':item[4].strip()[5:] if item[4] else '无数据',
            'score':item[5]+item[6] if item[5] and item[6] else '无数据'
        }
def save(comtent):
    with open('maoyan.json','a',encoding='utf-8') as f:
        f.write(json.dumps(comtent,indent=2,ensure_ascii=False))
    with open('maoyan.txt','a',encoding='utf-8') as f:
        f.write(str(comtent))

if __name__=='__main__':
    urls=['https://maoyan.com/board/4?offset={}'.format(i*10) for i in range(10)]
    for url in urls:
        g=spider(url)
        for item in jiexi(g):
            print(item)
            save(item)
        time.sleep(1)

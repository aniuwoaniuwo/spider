# -*- coding: utf-8 -*-
#创建项目后，scrapy genspider douban douban.com 就可以创建出douban这个爬虫文件
#并且对应着name和域名
#scrapy crawl douban 运行
import scrapy
from Douban.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    #爬虫名字
    name = 'douban'
    #域名范围
    allowed_domains = ['douban.com']
    #爬取网页的入口网址，如果是网址list，name会多线程异步并发进行访问
    #看源码。遍历所有的url，不过滤重复url
    start_urls = ['http://douban.com/','https://douban.com/','http://douban.com/','http://douban.com/','http://douban.com/']

    #这是解析的方法，上面的响应response传到这里进行解析数据或者获取新的url
    #response是从engine来，spider传给engine的

    #增加cookie，看源码，从spider找，所以要自定义request对象,重写了源代码的请求，并且回调返回
    #这是手动添加cookie登录的方法，接下来还有模拟自动登录,不过还是手动比较方便
    cookie = 'll="118288"; bid=CFXSFuC2-o8; __yadk_uid=89kVXIIzumb6tCGYqc9podmp7LDwGeFv; gr_user_id=4b2b706c-3b66-475d-b494-f62622a36f6b; __utma=30149280.1559669765.1545578295.1547452345.1554044644.4; __utmz=30149280.1545580666.2.2.utmcsr=sogou.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __utmv=30149280.16798; _vwo_uuid_v2=DCF442F5C0A235FB578E77DBF12FFED3A|9b84a1e7866efa3ab0debcf4546f59f9; _ga=GA1.2.1559669765.1545578295; _gid=GA1.2.988962757.1555834566; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1555836848%2C%22https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DDSOYnZeCC_oPL4RhSawS82YvcrgiTSe0%22%5D; _pk_id.100001.8cb4=17211b71b4880cc1.1547452249.12.1555836848.1555834557.; _pk_ses.100001.8cb4=*'
    # 字符串转字典
    cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split(';')}
    #自定义request请求对象就不能
    def start_requests(self):
        for url in self.start_urls:
            print(url)
            #不筛选url的参数需要设置
            #这个函数是request的函数，可以设置cookies等参数，看源码
            yield scrapy.Request(url,cookies=self.cookies,callback=self.parse, dont_filter=True)

    def parse(self, response):
        #定义item为字典，并且检查字段的格式是否为字典

        #打印响应的body
        # with open('douban.html','w') as f:
        #     f.write(response.body)

        #解析数据
        item=DoubanItem()
        #xpath解析，extract（）提取，出来是一个列表，可以用[0]进行进一步提取
        #解析有xpath提取，css提取，正则提取

        #首先xpath，直接response.xpath()，再加extract()提取成列表，[0]就是第一个
        #或者extract_first('无数据')也是提取第一个，无数据的话不会出现导致数组越界报错，会返回无数据
        #css，直接response.css('.text a::text')，.是class，#是id，空格加a就是标签，
        # ：：text是文本属性，：：attr（href）是获取属性。。或者就是css选择器
        #两者可以互相嵌套
        #正则一定要在xpath后接上，不然报错
        #response.xpath('.').re('')，re_first是获取第一个，

        item['name']=response.xpath('//*[@id="anony-time"]/div/div[3]/ul/li[1]/a[2]/text()').extract()[0]
        item['column']=response.xpath('//*[@id="anony-time"]/div/div[3]/ul/li[1]/span/text()').extract()[0]
        #详情页的url
        detail_url=response.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/a/@href')
        print(item)
        # return把数据传输到engine，然后engine把数据传给pipelines管道
        yield item

'''
        #模拟登陆豆瓣
        login_url='https://accounts.douban.com/passport/login'
        #登陆所需的参数
        formdata={
            'username':'18813295794',
            'password':'18898604973db',
            ' ':response.xpath('').extract_first(),
            '':response.xpath('').extract_first(),
        }
        #重写FormRequest,默认post请求，需要时可以修改请求方法；要回调
        #这个函数是登录的函数，带有formdata上传
        yield scrapy.FormRequest(
            login_url,
            formdata=formdata,
            callback=self.parse_login
        )

        

    #登录后的页面,需要接受上一个的response
    def parse_login(self,response):
        #这个页面是登录后才能访问的
        member_url='https://www.douban.com/people/167986306/'
        yield scrapy.Request(member_url,callback=self.parse_member)

    #查看页面是否登陆成功，需要接受response
    def parse_member(self,response):
        with open('01douban.html','w') as f:
            f.write(response.body)
            '''

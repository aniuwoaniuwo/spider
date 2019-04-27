# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


#设置请求头，User-Agent池
#两个中间件都要requests，所以两个都可以设置，但是可能会覆盖，所以一般只设置下载中间件
#下载中间件，从位置就可以看出其作用，请求前修改request，response传给engine前修改response
import random
class DoubanUserAgentMiddlewares(object):
    def __init__(self):
        #一直用这几个就好，直接浏览器复制的有时候爬取不了数据
        self.user_agent_list=[
    'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
    'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
    'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
    'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
    'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
    'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
    'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
    'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
            ]
    def process_request(self, request, spider):
        #处理请求的，下载前修改
        # 调用请求对象，可以设置请求头
        #返回空，request，response（不会送到下载器，直接到spider解析，对接selenium就是返回response）或者报错
        user_agent=random.choice(self.user_agent_list)
        request.headers['User-Agent']=user_agent

    def process_response(self, request, response, spider):
        # 从下载器出来的response解析之前
        # 验证设置请求头是否生效，同时修改response的一些参数
        user_agent=request.headers['User-Agent']
        print(user_agent)
        #该方法要返回一个response或者request，不能为空，否则报错
        return response


class DoubanproxiesMiddlewares(object):
    def __init__(self):
        self.proxies_list=['http://188.188.188.18:5000']

    def process_request(self, request, spider):
        #同样也是requets这个函数设置ip
        proxies=random.choice(self.proxies_list)
        #传递proxy，这个也是框架里面的传递函数
        request.meta['proxy']=proxies

# 爬虫中间件，response给spider解析前可以修改，spider把request给调度前（其实是engine）修改request，spider把item给engine前修改item
# 调用请求对象，可以设置请求头
'''
from scrapy import signals


#爬虫中间件
class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    #response从engine到spider解析之前修改
    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    #spider解析后，传递item，response前修改，迭代，
    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i
    #处理异常
    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    #类似process_spider_output，构建初始化请求对象，
    #也就是程序一开始的传输request，只能返回请求对象而没有response，传初始化请求对象requests
    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


#下载中间件
class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        #调用请求对象，可以设置请求头
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:可以为空
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        #从下载器调用每一个响应对象
        # Called with the response returned from the downloader.

        # Must either;一定有响应对象
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
    #处理异常函数
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:可以为空
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
'''
# -*- coding: utf-8 -*-

# Scrapy settings for Douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#爬虫的名字
BOT_NAME = 'Douban'

#爬虫模板，就那个爬虫文件名
SPIDER_MODULES = ['Douban.spiders']
NEWSPIDER_MODULE = 'Douban.spiders'

#定义数据库的连接数据
MYSQL_HOST='localhost'
MYSQL_DATABASE='douban'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD='mysqlmm'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#请求头，不过此处只能设置一个，不能批量
# USER_AGENT = 'Douban (+http://www.yourdomain.com)'

# Obey robots.txt rules
#默认是遵守，需要修改成为不遵守才能爬取数据，因为这是给出了哪里可以抓取
ROBOTSTXT_OBEY = False

#设置日志文件,除了打印输出，其他日志会保存到文件中
# LOG_FILE="douban.log"
#设置日志等级，等级分为五种，1.DEBUG,2.INFO,3.WARNING,4.ERROR,5.CRITCAL，等级越高输出日志越少，默认info
LOG_LEVEL="ERROR"

#最大请求并发数，默认16个，下面是修改到多少个
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#设置批量延迟，默认3秒，3秒发一批，也就是16个
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#cookie不生效，默认不生效，修改可以去掉#号
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

#远程控制
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

#加载默认请求头
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#爬虫中间件，默认不开启，需要开启
#spider通过他传requests，item到引擎，或者引擎传response给spider
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Douban.middlewares.DoubanSpiderMiddleware': 543,
#}

#下载中间件，默认不开，需要手动开启
#引擎通过它传requests给下载器，或者下载器传response给引擎
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Douban.middlewares.DoubanUserAgentMiddlewares': 543,
    # 'Douban.middlewares.DoubanproxiesMiddlewares':544,
}

#远程控制扩张件
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#管道默认不开启，需要手动添加开启，300是优先级等级，0-1000之间，越低越优先
#先调用优先级高的，再到低的
ITEM_PIPELINES = {
    'Douban.pipelines.DoubanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

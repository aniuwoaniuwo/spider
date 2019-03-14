#-*-coding:utf-8-*-
#这个文件用来判断某些网址是否可以爬取
from urllib.robotparser import RobotFileParser

rb=RobotFileParser()
rb.set_url('https://www.douban.com/robots.txt')#robots文件的链接
rb.read()#这个方法一定要引用，读取robots文件
print(rb.can_fetch('*','https://www.douban.com/location/maoming/'))
#第一个参数是User-agent，第二个参数是需要判断是否可以爬取的url，返回True则可爬取，False则不能爬取

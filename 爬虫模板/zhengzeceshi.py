#-*-coding:utf-8-*-
#这是正则表达式的测试模板，在网页中复制需要匹配的HTML，然后这里匹配是否正确
import re

HTML=''''''
pattern=re.compile('<span.*?thread_subject.*?>(.*?)</span>.*?xi2.*?>(.*?)</a>.*?<em.*?authorposton.*?>(.*?)</em>.*?atips_close.*?>.*?</span>(.*?)<font.*?jammer.*?>.*?<br/>',re.S)
items=re.findall(pattern,HTML)
for item in items:
    print(item)
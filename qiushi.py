#-*-coding:utf-8-*-
#用正则表达式来抓取
import re
import requests
import xlrd
import xlwt
import time
class qs(object):
    def __init__(self):
        self.qiushi=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.qiushi.add_sheet(u'糗事',cell_overwrite_ok=True)
        self.qiushi.save('qiushi.xlsx')
        self.datas=[]#全局变量，全部函数都可以用
        self.page=1
        self.k=0
        self.p=0
    def getpage(self,pagei):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        url='http://www.qiushibaike.com/hot/page/{}/'.format(str(pagei))#format放在引号外面
        response=requests.get(url,headers=headers).text
        print(url)
        pattern=re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
        items=re.findall(pattern,response)
        data=[]
        m=len(items)
        for i in range(0,m):
            a=items[i].replace('<br/>','')
            data.append(a)
            f=xlrd.open_workbook('qiushi.xlsx')
            self.sheet.write(self.p,0,a)
            self.p+=1

        return data
    def shuchu(self):
        while True:#给一个无限循环
            if len(self.datas)<2:
                self.datas=self.getpage(self.page)
                self.page+=1
            data1=input()
            if data1=="Q":
                print("程序已经退出")
                return
            print(self.datas[0])
            del self.datas[0]

    def export(self):
        for i in range(1,21):
                self.getpage(self.page)
                self.page = self.page + 1
                print(self.page)
                self.k+=1
                time.sleep(3)#给个延迟，不然存不了
        self.qiushi.save('qiushi.xlsx')
if __name__=='__main__':
    print('摁Q退出程序，回车出现一个笑话，祝你开心每一天')
    aa=qs()
    #aa.shuchu()
    aa.export()










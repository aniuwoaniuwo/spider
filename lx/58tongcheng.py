import time
from selenium import webdriver
from lxml import etree
import xlrd
import xlwt

class tongcheng(object):
    def __init__(self):
        self.shuju=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.shuju.add_sheet(u'列表',cell_overwrite_ok=True)
        sheetcount=(u'编号',u'地址',u'标题',u'价格')
        for i in range(0,len(sheetcount)):
            self.sheet.write(0,i,sheetcount[i],self.set_style('Time new Roman',220,True))
        self.shuju.save('58tongcheng.xlsx')

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style


    def denglu(self):
        driver=webdriver.Firefox()#获取驱动
        driver.get('http://zhanjiang.58.com/chuzu/?PGTID=0d100000-0031-73a4-da1f-d7b584e2777e&ClickID=2')#登陆湛江58同城

        #http://zhanjiang.58.com/chuzu/pn2/?PGTID=0d3090a7-0031-7f4b-4227-b18b26cc95c7&ClickID=2
        #http://zhanjiang.58.com/chuzu/pn3/?PGTID=0d3090a7-0031-7c6e-2355-40e628d3320a&ClickID=2
        time.sleep(2)#登陆延迟2秒
        #driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a').click()#点击租房
        #driver.switch_to.default_content()#让webdriver操纵当前页
        #driver.find_element_by_xpath('//*[@id="keyword1"]').sendkeys("123")#发送搜索内容
        datas=xlrd.open_workbook('58tongcheng.xlsx')
        m = 0
        for f in range(0,71):
            driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/dl[1]/dd/a[2]').click()#选择霞山
            print(driver.page_source)
            selector=etree.HTML(driver.page_source)#

            dizhis=selector.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/p[2]/a[2]/text()')#li地址

            biaotis=selector.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/h2/a/text()')#标题的内容

            jiages=selector.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[3]/div[2]/b/text()')#租房价格
            #print(dizhis,biaotis,jiages)

            print(jiages)

            for i in range(0,len(dizhis)):
                data = []  # 建立空的list
                dizhi=dizhis[i]
                biaoti=biaotis[i]
                jiage=jiages[i]
                data.append(m+1)
                data.append(dizhi)
                data.append(biaoti)
                data.append(jiage)
                for j in range(0,len(data)):
                    self.sheet.write(m+1,j,data[j])

                m=m+1
                print(m)

            driver.find_element_by_xpath('//*[@id="bottom_ad_li"]/div[2]/a[4]/span').click()#点击下一页
        self.shuju.save('58tongcheng.xlsx')
if __name__=='__main__':
    ff=tongcheng()
    ff.denglu()

#http://zhanjiang.58.com/xiashan/chuzu/?PGTID=0d3090a7-0031-7ae6-5800-aa67ca8a7042&ClickID=2
#http://zhanjiang.58.com/xiashan/chuzu/pn2/?PGTID=0d3090a7-0031-9d42-0699-58e73d17d85b&ClickID=2
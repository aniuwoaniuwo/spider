#-*-coding:utf-8-*-
#利用selenium+firefox爬取天眼查制造业企业的信息，保存到excel网页中
#本次还遇到了小弹窗和登录界面加载慢的问题，以及ip被封的问题，都解决了
from selenium import webdriver
import time
from lxml import etree
import xlwt,xlrd,re
from selenium.webdriver.common.proxy import Proxy, ProxyType

class tyc(object):
    def __init__(self):
        self.tianyancha = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.tianyancha.add_sheet(u'企业信息', cell_overwrite_ok=True)
        sheetcount = (u'编号', '企业名称', '法定代表人', '注册资本', '成立日期', '联系电话', '综合评分')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.tianyancha.save('tianyancha.xlsx')
    def excel(self, time=time):
        m=0
        #f=xlrd.open_workbook('tianyancha.xlsx')
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", '121.61.0.151')
        ff_profile.set_preference("network.proxy.http_port", int(9999))
        ff_profile.set_preference("network.proxy.ssl", '121.61.0.151')
        ff_profile.set_preference("network.proxy.ssl_port", int(9999))
        ff_profile.set_preference("network.proxy.ftp", '121.61.0.151')
        ff_profile.set_preference("network.proxy.ftp_port", int(9999))
        ff_profile.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
        #driver=webdriver.Firefox()#获取驱动
        driver.maximize_window()#窗口最大
        driver.get('https://www.tianyancha.com/search/ocC?base=guangzhou')#天眼查制造业企业的信息
        time.sleep(5)#给个五秒延迟,必须先定义，不能在函数中直接用
        g=0
        for i in range(5):
            '''for j in range(1, 3):
                height = 20000 * j  # 每次滑动20000像素
                strWord = "window.scrollBy(0," + str(height) + ")"
                driver.execute_script(strWord)
                time.sleep(2)'''
            selector=driver.page_source
            s=etree.HTML(selector)
            if g == 0:
                driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[4]/a').click()#点击登录
                time.sleep(3)#有网络延迟
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]').click()#点击密码登录
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[2]/input').send_keys("18813295794")
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[3]/input').send_keys("18826690336tyc")
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div[2]/div[5]').click()
                time.sleep(3)
                g=1
            '''/html/body/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/a
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[3] / div[1] / a
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[3] / div[2] / div[1] / a
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[3] / div[2] / div[2] / span
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[3] / div[2] / div[3] / span
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[3] / div[3] / div[1] / span[2]
            // *[ @ id = "web-content"] / div / div[1] / div / div[3] / div[2] / div / div[4] / span[1]'''
            pattern=re.compile(r'<text class="tyc-num lh24">(.*?)</text>',re.S)
            names=re.findall(pattern,selector)
            #print(names)
            trs=s.xpath('/html/body/div[2]/div/div[1]/div/div[3]/div/div')
            for t in range(0,len(trs)):
                m=m+1
                name=trs[t].xpath('./ div[3]/ div[1] / a/text()')
                #name=names[t]
                #print(name)
                representative=trs[t].xpath('./ div[3]/ div[2] / div[1] / a/text()')
                capital=trs[t].xpath('./ div[3]/ div[2] / div[2] / span/text()')
                times=trs[t].xpath('./ div[3]/ div[2] / div[3] / span/text()')
                telephone=trs[t].xpath('./ div[3]/ div[3] / div[1] / span[2]/text()')
                score=trs[t].xpath('./ div[4] / span[1]/text()')
                name=name[0] if len(name)>0 else '无数据'
                print(name)
                representative = representative[0] if len(representative) > 0 else '无数据'
                capital = capital[0] if len(capital) > 0 else '无数据'
                times = times[0] if len(times) > 0 else '无数据'
                telephone = telephone[0] if len(telephone) > 0 else '无数据'
                score = score[0] if len(score) > 0 else '无数据'
                data=[]
                data.append(m)
                data.append(name)
                data.append(representative)
                data.append(capital)
                data.append(times)
                data.append(telephone)
                data.append(score)
                for k in range(0,len(data)):
                    self.sheet.write(m,k,data[k])
                self.tianyancha.save('tianyancha.xlsx')
            time.sleep(2)
            s=self.exit(driver,'//*[@id="tyc_banner_close"]')
            if s==True:
                print('有小弹窗')
                driver.find_element_by_xpath('//*[@id="tyc_banner_close"]').click()
            else:
                print('无弹窗')
            #s=driver.find_element_by_xpath('//*[@id="tyc_banner_close"]')

            '''if s!='':#判断元素是否存在
                print('有小弹窗')
                s.click()#点击下一页
            else:
                print('无弹窗')'''
            time.sleep(2)
            driver.find_element_by_css_selector('html body.font-bb49248c div#web-content.mt74 div.container.pt25 div.container-left div.search-block div.result-footer div ul.pagination li a.num.-next').click()
            time.sleep(5)
        self.tianyancha.save('tianyancha.xlsx')
    def exit(self,driver,css):#判断是否有小弹窗
        try:
            driver.find_element_by_xpath(css)
            return True
        except:
            return False
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style
if __name__=='__main__':
    start=time.time()
    f=tyc()
    f.excel(time)
    end=time.time()
    print('花费的总时间：',(end-start))
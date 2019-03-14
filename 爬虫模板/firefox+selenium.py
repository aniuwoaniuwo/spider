#-*-coding:utf-8-*-
#利用requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，暂时不需要cookies，代理，
import time
from selenium import webdriver
import urllib.request
import re
from lxml import etree
import xlwt,xlrd,pymysql
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
        ip='61.161.46.179'
        port=8118
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", ip)
        ff_profile.set_preference("network.proxy.http_port", int(port))
        ff_profile.set_preference("network.proxy.ssl", ip)
        ff_profile.set_preference("network.proxy.ssl_port", int(port))
        ff_profile.set_preference("network.proxy.ftp", ip)
        ff_profile.set_preference("network.proxy.ftp_port", int(port))
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
		wait=WebDriverWait(driver,15)
        try:
            #driver=webdriver.Firefox()#获取驱动
            driver.maximize_window()#窗口最大
            driver.get('https://www.tianyancha.com/search/ocC?base=guangzhou')#天眼查制造业企业的信息
            time.sleep(5)#给个五秒延迟,必须先定义，不能在函数中直接用
			submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#searchHotelPanel > div.b_tool.clr_after > div.pager.js_pager > div > ul > li.item.next > a > span:nth-of-type(1)')))#直到此元素可以点击
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
		except:
            print('出错了')
        finally:
            driver.close()
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


    def tupian(self):
        '''options = webdriver.ChromeOptions()
        # 设置成中文
        options.add_argument('lang=zh_CN.UTF-8')
        # 添加头部
        options.add_argument(
            'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36"')
        options.add_argument("--proxy-server=http://202.20.16.82:10152")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("url")'''

        ip='61.161.46.179'
        port=8118
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", ip)
        ff_profile.set_preference("network.proxy.http_port", int(port))
        ff_profile.set_preference("network.proxy.ssl", ip)
        ff_profile.set_preference("network.proxy.ssl_port", int(port))
        ff_profile.set_preference("network.proxy.ftp", ip)
        ff_profile.set_preference("network.proxy.ftp_port", int(port))
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
        try:
            # driver=webdriver.Firefox()#获取驱动
            driver.maximize_window()  # 窗口最大
            driver.get('http://jandan.net/ooxx/page-1')  # 模拟登陆网页
            time.sleep(5)  # 给个两秒的延迟
            x = 1
            # print(driver.page_source)
            for i in range(11):
                for j in range(1, 6):
                    height = 20000 * j  # 每次滑动20000像素
                    strWord = "window.scrollBy(0," + str(height) + ")"
                    driver.execute_script(strWord)
                    time.sleep(4)
                selector = driver.page_source  # 获取网页文本
                pattern = re.compile(r'<div class="text">.*?<p>.*?<img src="(.*?)".*?</p>', re.S)
                items = re.findall(pattern, selector)
                #s = etree.HTML(selector)
                #items = s.xpath('')
                for item in items:
                    print(item)
                    print(x)
                    urllib.request.urlretrieve(item,'c:\\pachong\\meizitu\\'+'%s.jpg' % x)
                    x += 1
                #driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/a[3]').click()#点击下一页

                driver.find_element_by_xpath('//*[@id="comments"]/div[2]/div/a[1]').click()  #
                time.sleep(5)#5秒延迟
            # 退出，清除浏览器缓存
        finally:
            #driver.quit()
            driver.close()
    def txt(self):
        ip='61.161.46.179'
        port=8118
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", ip)
        ff_profile.set_preference("network.proxy.http_port", int(port))
        ff_profile.set_preference("network.proxy.ssl", ip)
        ff_profile.set_preference("network.proxy.ssl_port", int(port))
        ff_profile.set_preference("network.proxy.ftp", ip)
        ff_profile.set_preference("network.proxy.ftp_port", int(port))
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
        try:
            # driver=webdriver.Firefox()#获取驱动
            driver.maximize_window()  # 窗口最大
            driver.get('http://jandan.net/ooxx/page-1')  # 模拟登陆网页
            time.sleep(5)  # 给个两秒的延迟
            x = 1
            # print(driver.page_source)
            for i in range(11):
                for j in range(1, 6):
                    height = 20000 * j  # 每次滑动20000像素
                    strWord = "window.scrollBy(0," + str(height) + ")"
                    driver.execute_script(strWord)
                    time.sleep(4)
                selector = driver.page_source
                s = etree.HTML(selector)
                contents = s.xpath('')
                with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
                    for content in range(0, len(contents)):
                        print(content)
                        f.write(content)
                driver.find_element_by_xpath('//*[@id="comments"]/div[2]/div/a[1]').click()  #
                time.sleep(5)  # 5秒延迟
            # 退出，清除浏览器缓存
        finally:
            #driver.quit()
            driver.close()


    def base(self):
        ip='61.161.46.179'
        port=8118
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("network.proxy.type", 1)
        ff_profile.set_preference("network.proxy.http", ip)
        ff_profile.set_preference("network.proxy.http_port", int(port))
        ff_profile.set_preference("network.proxy.ssl", ip)
        ff_profile.set_preference("network.proxy.ssl_port", int(port))
        ff_profile.set_preference("network.proxy.ftp", ip)
        ff_profile.set_preference("network.proxy.ftp_port", int(port))
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)
        try:
            # driver=webdriver.Firefox()#获取驱动
            driver.maximize_window()  # 窗口最大
            driver.get('http://jandan.net/ooxx/page-1')  # 模拟登陆网页
            time.sleep(5)  # 给个两秒的延迟
            x = 1
            for i in range(11):
                for j in range(1, 6):
                    height = 20000 * j  # 每次滑动20000像素
                    strWord = "window.scrollBy(0," + str(height) + ")"
                    driver.execute_script(strWord)
                    time.sleep(4)
                selector = driver.page_source
                s = etree.HTML(selector)
                db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')  # db选择相应的数据库名称
                cursor = db.cursor()
                td = s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')

                for p in td:

                    title = p.xpath('./td[2]/div/a/text()')
                    score = p.xpath('./td[2]/div/div/span[2]/text()')
                    renshu = p.xpath('./td[2]/div/div/span[3]/text()')
                    qita = p.xpath('./td[2]/div/p/text()')
                    tupian = p.xpath('./td[1]/a/img/@src')

                    title = title[0] if len(title) > 0 else ''
                    score = score[0] if len(score) > 0 else ''
                    renshu = renshu[0] if len(renshu) > 0 else ''
                    qita = qita[0] if len(qita) > 0 else ''
                    tupian = tupian[0] if len(tupian) > 0 else ''
                    data = {}
                    data = {
                        'name': title,
                        'score': score,
                        'good': renshu
                    }
                    table = 'musics'
                    keys = ','.join(data.keys())
                    values = ','.join(['%s'] * len(data))
                    update = ','.join([" {key}=%s".format(key=key) for key in data])  # 注意空格
                    sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                                        values=values)
                    sql = sql + update
                    try:
                        if cursor.execute(sql, tuple(data.values()) * 2):  # 这是格式，第二个参数要有
                            # if cursor.execute(sql,(title[i],score[i],renshu[i])):
                            print('成功')
                            db.commit()  # 执行保存
                    except:
                        db.rollback()
                        print('失败！')

                pass
                driver.find_element_by_xpath('//*[@id="comments"]/div[2]/div/a[1]').click()  #
                time.sleep(5)  # 5秒延迟
            # 退出，清除浏览器缓存
        finally:
            driver.close()
            #driver.quit()

if __name__=='__main__':
    start=time.time()
    f=tyc()
    f.excel(time)
    end=time.time()
    print('花费的总时间：',(end-start))
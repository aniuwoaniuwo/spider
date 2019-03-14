#-*-coding:utf-8-*-
#未完成！！！！！！！！！！！！！！！！
#爬取去哪儿的酒店信息，用正则爬取，储存到excel中，包括代理，加cookies，头部，
#selenium加载该网址加载很慢，需要实时的信息一直在加载，建议直接requests
#-*-coding:utf-8-*-
#利用requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，暂时不需要cookies，代理，
import time
from selenium import webdriver
import urllib.request
import re
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
import xlrd,xlwt
import pymysql

def tupian():
    '''options = webdriver.ChromeOptions()
    # 设置成中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 添加头部
    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36"')
    options.add_argument("--proxy-server=http://202.20.16.82:10152")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("url")'''

    driver = webdriver.Firefox()  # 获取驱动
    driver.maximize_window()  # 窗口最大化
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
    driver.quit()

def txt():
    driver = webdriver.Firefox()  # 获取驱动
    driver.maximize_window()  # 窗口最大化
    driver.get('http://hotel.qunar.com/city/guangzhou/#fromDate=2019-02-19&from=qunarindex&toDate=2019-02-20')  # 模拟登陆网页
    time.sleep(3)  # 给个两秒的延迟
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
    driver.quit()
class gowhere(object):
    def __init__(self):
        self.gowhere = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.gowhere.add_sheet(u'去哪儿', cell_overwrite_ok=True)
        sheetcount = (u'编号', u'图片', u'名字', u'类型', u'地点', u'评分', u'推荐指数', u'价格')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.gowhere.save('gowhere.xlsx')
    def excel(self):
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
        m = 0
        driver = webdriver.Firefox()  # 获取驱动
        wait=WebDriverWait(driver,15)
        driver.maximize_window()  # 窗口最大化
        driver.get('https://hotel.qunar.com/city/guangzhou/')  # 模拟登陆网页
        time.sleep(5)  # 给个两秒的延迟
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/div/div[3]/div/div/ul/li[3]/em').click()#三星级的
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/div/div[3]/div/div/ul/li[4]/em').click()#四星级的
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div[1]/div/div[3]/div/div/ul/li[5]/em').click()
        time.sleep(3)
        x = 1
        for i in range(11):
            for j in range(1, 6):
                height = 20000 * j  # 每次滑动20000像素
                strWord = "window.scrollBy(0," + str(height) + ")"
                driver.execute_script(strWord)
                time.sleep(2)
            submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#searchHotelPanel > div.b_tool.clr_after > div.pager.js_pager > div > ul > li.item.next > a > span:nth-of-type(1)')))
            s= driver.page_source
            pattern=re.compile('<div.*?clrfix.*?js-list_hotelpic.*?src="(.*?)".*?e_title js_list_name.*?>(.*?)</a>.*?sort dangci.*?>(.*?)</em>.*?adress.*?<em>.*?</b>(.*?)</em>.*?js_list_score.*?<b>(.*?)</b>.*?num.*?>(.*?)</span>.*?item_price js_hasprice.*?</cite><b>(.*?)</b>.*?</div>',re.S)
            items=re.findall(pattern,s)
            print('正在爬取第一页')
            for item in items:
                data = []  # 建立空的list
                picture = items[0] if item[0] else '无数据'
                picture = 'http:'+picture
                name = items[1] if item[1] else '无数据'
                print('现在爬取的是{}'.format(name))
                type = items[2] if item[2] else '无数据'
                address = items[3] if item[3] else '无数据'
                score = items[4] if item[4] else '无数据'
                recommended= items[5] if item[5] else '无数据'#试睡员推荐的人数
                price = items[6] if item[6] else '无数据'
                data.append(m + 1)
                data.append(picture)
                data.append(name)
                data.append(type)
                data.append(address)
                data.append(score)
                data.append(recommended)
                data.append(price)
                print(picture,name,type,address,score,recommended,price)
                for j in range(0, len(data)):
                    self.sheet.write(m + 1, j, data[j])
                m = m + 1
                print(m)
                submit.click()
            #driver.find_element_by_xpath('//html/body/div[4]/div/div[4]/div[3]/div[1]/div[3]/div[6]/div[1]/div/ul/li[10]/a/span[1]').click()  #下一页
            time.sleep(5)  # 5秒延迟
        self.gowhere.save('gowhere.xlsx')
        # 退出，清除浏览器缓存
        driver.quit()
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style

def base():
    driver = webdriver.Firefox()  # 获取驱动
    driver.maximize_window()  # 窗口最大化
    driver.get('http://jandan.net/ooxx/page-1')  # 模拟登陆网页
    time.sleep(5)  # 给个两秒的延迟
    x = 1
    for i in range(11):
        for j in range(1, 4):
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
    driver.quit()

if __name__=='__main__':
    start=time.time()
    #tupian()
    #txt()
    f=gowhere()
    f.excel()
    #base()
    end=time.time()
    print('总共花费的时间：',(end-start))
#-*-coding:utf-8-*-
#利用selenium+requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，暂时不需要cookies，代理，
import time,csv
from selenium import webdriver
import urllib.request
import re,requests
from lxml import etree
import xlwt,xlrd,pymysql
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from lxml import etree
import xlwt,xlrd,re,json
from selenium.webdriver.common.proxy import Proxy, ProxyType

class Spider(object):
    def __init__(self):
        self.k=1
        self.n=1
        self.tianyancha = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.tianyancha.add_sheet(u'企业信息', cell_overwrite_ok=True)
        sheetcount = (u'编号', '企业名称', '法定代表人', '注册资本', '成立日期', '联系电话', '综合评分')
        for i in range(0, len(sheetcount)):
            self.sheet.write(0, i, sheetcount[i], self.set_style('Time new Roman', 220, True))
        self.tianyancha.save('tianyancha.xlsx')

    def get_ip(self):
        try:
            response = requests.get('http://localhost:5555/random')
            if response.status_code == 200:
                return response.text
            else:
                return None
        except:
            return None

    def spider(self,url, time=time):
        m=0
        #f=xlrd.open_workbook('tianyancha.xlsx')
        ip='61.161.46.179'
        port=8118
        proxies = self.get_ip()
        if proxies:
            items = re.findall('(.*?):(.*)', proxies)
            ip=items[0][0]
            port=items[0][1]
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
            driver.maximize_window()#窗口最大
            driver.get(url)#天眼查制造业企业的信息
            time.sleep(5)#给个五秒延迟,必须先定义，不能在函数中直接用
            submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#searchHotelPanel > div.b_tool.clr_after > div.pager.js_pager > div > ul > li.item.next > a > span:nth-of-type(1)')))#直到此元素可以点击
            for i in range(5):
                '''for j in range(1, 3):
                    height = 20000 * j  # 每次滑动20000像素
                    strWord = "window.scrollBy(0," + str(height) + ")"
                    driver.execute_script(strWord)
                    time.sleep(2)'''
                selector=driver.page_source
                yield selector
                e=self.exit(driver,'//*[@id="tyc_banner_close"]')
                if e==True:
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
        except Exception as e:
            print(e)

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

    def jiexi(self, response):
        '''
        解析，返回要爬取的内容
        :param response:
        :return:
        '''
        if response:
            pattern1 = re.compile('</head><body(.*?)珍爱首页', re.S)
            HTML = re.findall(pattern1, response)[0]
            pattern = re.compile(
                '<div.*?f-item.*?>.*?href="(.*?)".*?src="(.*?)".*?f-nickname.*?>(.*?)<span.*?t-info.*?>(.*?)\|(.*?)\|(.*?)</pre.*?c-tag.*?tag.*?>(.*?)</div.*?tag.*?>(.*?)</div.*?t-introduce.*?>(.*?)</div>',
                re.S)
            items = re.findall(pattern, HTML)
            for item in items:
                yield item
        else:
            return None

    def txt(self,item):
        with open('txt.txt', 'a', encoding='utf-8') as f:  # 不管存储过程发生什么错误都会保存
            f.write(item[0])
            f.write(item[1])

    def csv(self, item):
        '''
        保存数据到csv
        :param items:
        :return:
        '''
        with open('wxouguan.csv', 'a', encoding='utf-8') as f:
            names = ['title', 'author','time','content','address']
            writer = csv.writer(f)
            if self.k == 1:
                writer.writerow(names)
                self.k += 1
            writer.writerow([item[0],item[1],item[2],item[3],item[4]])

    def json(self,item):
        '''
        保存数据
        :param response:
        :return:
        '''
        item={'item0':item[0],'item1':item[1]}
        with open('sfd.json', 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, indent=2, ensure_ascii=False))
            f.write(',')

    def excel(self,item):
        for j in range(0, len(item)):
            self.sheet.write(self.n + 1, j, item[j])
            self.n+=1
            print(self.n)
            self.shuju.save('58tongcheng.xlsx')

    def base(self,item):
        if item:
            db = pymysql.connect(host='localhost', user='root', password='mysqlmm', port=3306, db='douban')#db选择相应的数据库名称
            cursor = db.cursor()
            data = {
                    'name': item[0],
                    'score': item[1],
                    'good': 0
                }
            table = 'musics'
            keys = ','.join(data.keys())
            values = ','.join(['%s'] * len(data))
            update = ','.join([" {key}=%s".format(key=key) for key in data])  # 注意空格
            sql = 'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,values=values)
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

    def main(self):
        '''
        进程启动入口
        :return:
        '''
        start = time.time()
        urls = ['https://music.douban.com/top250?start={}'.format(i * 25) for i in range(1, 20)]
        for url in urls:
            for response in self.spider(url):
                for item in self.jiexi(response):
                    self.txt(item)
            time.sleep(4)
        end = time.time()
        data = end - start
        h = data // 3600
        yushu = data % 3600
        m = yushu // 60
        yushu = yushu % 60
        s = yushu
        print('总共花费的时间：{}时{}分{}秒'.format(h, m, s))

if __name__=='__main__':
    f=Spider()
    f.main()
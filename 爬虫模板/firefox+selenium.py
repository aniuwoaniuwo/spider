#-*-coding:utf-8-*-
#利用requests请求，正则表达式来解析网页，TXT、excel、数据库保存，带有headers，暂时不需要cookies，代理，
import time
from selenium import webdriver
import urllib.request
import re
from lxml import etree

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
    driver.quit()
def excel():
    m = 0
    shuju = xlwt.Workbook(encoding='utf-8')
    sheet = shuju.add_sheet(u'列表', cell_overwrite_ok=True)
    sheetcount = (u'编号', u'地址', u'标题', u'价格')
    for i in range(0, len(sheetcount)):
        sheet.write(0, i, sheetcount[i], set_style('Time new Roman', 220, True))
    shuju.save('xlsx.xlsx')
    driver = webdriver.Firefox()  # 获取驱动
    driver.maximize_window()  # 窗口最大化
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
        dizhis = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/p[2]/a[2]/text()')  # li地址
        biaotis = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[2]/h2/a/text()')  # 标题的内容
        jiages = s.xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li/div[3]/div[2]/b/text()')  # 租房价格
        # print(dizhis,biaotis,jiages)
        for i in range(0, len(dizhis)):
            data = []  # 建立空的list
            dizhi = dizhis[i]
            biaoti = biaotis[i]
            jiage = jiages[i]
            data.append(m + 1)
            data.append(dizhi)
            data.append(biaoti)
            data.append(jiage)
            for j in range(0, len(data)):
                sheet.write(m + 1, j, data[j])
            m = m + 1
            print(m)
        driver.find_element_by_xpath('//*[@id="comments"]/div[2]/div/a[1]').click()  #
        time.sleep(5)  # 5秒延迟
    shuju.save('58tongcheng.xlsx')
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
    driver.quit()

if __name__=='__main__':
    start=time.time()
    tupian()
    #txt()
    #excel()
    #base()
    end=time.time()
    print('总共花费的时间：',(end-start))
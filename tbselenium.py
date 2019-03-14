#-*-coding:utf-8-*-
#用到selenium来爬取淘宝的物品信息，用lxml来解析，保存到csv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import re,csv,time
from lxml import etree
class tb(object):
    def __init__(self):
        self.k=1
    def spider(self):
        firefox_options = webdriver.FirefoxOptions()
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("general.useragent.override",
                                  "Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        ff_profile.update_preferences()
        driver = webdriver.Firefox(firefox_options=firefox_options, firefox_profile=ff_profile)

        #driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 10)
        try:
            driver.get('https://uland.taobao.com/sem/tbsearch?refpid=mm_15891853_2192459_8654707&keyword=%E5%A5%B3%E8%A3%85&clk1=315358d81a06b080c93ddffd4a756ba9&upsid=315358d81a06b080c93ddffd4a756ba9')
            time.sleep(2)
            '''driver.find_element_by_xpath('//*[@id="q"]').clear()
            driver.find_element_by_xpath('//*[@id="q"]').send_keys('手机')
            driver.find_element_by_xpath('//*[@id="J_searchForm"]/input[4]').click()
            time.sleep(5)
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()#点击登录按钮
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[3]/form/div[2]/span').send_keys('18813295794')
            driver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys('18898604973tb')
            driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()#登录'''
            input=wait.until(EC.presence_of_element_located((By.ID,'q')))#直到“搜索”节点加载出来，后面是定位元素
            submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.submit')))#直到‘搜索’节点可以点击
            input.clear()
            input.send_keys('手机')#搜索手机
            submit.click()
            time.sleep(5)
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
            for i in range(1,6):
                print('正在爬取第{}页：'.format(i))
                #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.view .item')))#直到信息框加载出来
                #driver.switch_to.default_content()
                response=driver.page_source
                pattern = re.compile('<p.*?pricedetail.*?strong.*?>(.*?)</strong>.*?title.*?>(.*?)<.*?shopName.*?payNum.*?>(.*?)</span>.*?</div>',re.S)
                #selector = etree.HTML(driver.page_source)
                #items=selector.xpath('/html/body/div[3]/div[3]/div/div/div/a/div[2]/span/text()')
                items = re.findall(pattern,response)
                print('items:' ,items)#不能用+号，字符串和数组不能相加
                with open('tb1.csv', 'a', encoding='utf-8') as f:
                    print(55555)
                    for item in items:
                        print(item)
                        writer = csv.writer(f)
                        if self.k == 1:
                            writer.writerow(['name'])#用数组表示，否则当做字符串一个一个字符输进去
                            self.k += 1
                        writer.writerow([item[0]])
                '''item=self.jiexi(response)
                print('正在保存第{}页的数据'.format(i))
                self.save(item)
                print('第{}页的数据保存完毕'.format(i))'''

                page=wait.until(EC.presence_of_element_located((By.ID,'Jumper')))#直到第几页北加载出来
                #page=driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/a[4]')#点击下一页
                page.clear()
                #page.click()
                page.send_keys(i)#直接跳到第几页不能执行，会报错
                driver.find_element_by_xpath('/html/body/div[3]/div[4]/div/div/div/a[6]').click()
        except:
            print('出错了')
        finally:
            print('爬取完毕')
            #driver.close()


    def jiexi(self,response):
        pattern=re.compile('<div.*?info.*?pricedetail.*?>.*?<strong>(.*?)</strong>.*?title.*?>(.*?)<font.*?payNum.*?>(.*?)</span>.*?</p>',re.S)
        items=re.findall(pattern,response)
        print('items'+items)
        for item in items:
            return {
                'name':item[2] if item[2] else '无数据',
                'price':item[0] if item[0] else '无数据',
                'renshu':item[1] if item[1] else '无数据'
            }
    def save(self,item):
        with open('tb.csv','a',encoding='utf-8') as f:
            writer=csv.writer(f)
            if self.k==1:
                writer.writerow('name','price','renshu')
                self.k+=1
            writer.writerow(item[2],item[0],item[1])

if __name__=='__main__':
    run=tb()
    run.spider()

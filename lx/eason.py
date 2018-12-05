import os
import time
from selenium import webdriver
from lxml import etree
import sys
sys.getdefaultencoding( )



driver=webdriver.Firefox()
driver.maximize_window()

driver.get("http://pic.sogou.com/pics?query=%B3%C2%DE%C8%D1%B8%CD%BC%C6%AC&p=40230500&st=255&mode=255&policyType=0")


while True:
	for i in range(1,10):
            height = 20000*i#每次滑动20000像素
            strWord = "window.scrollBy(0,"+str(height)+")"
            driver.execute_script(strWord)
            time.sleep(4)
		
	
	selector = etree.HTML(driver.page_source)
	divs=selector.xpath('//*[@id="picList1"]/li')

	with open('eason.txt','a') as f:
		for div in divs:
			pic=div.xpath('./a[2]/img/@src')
			
			pic=pic[0] if len(pic)!=0 else ''
			print(pic)
			f.write(pic+"\n")
	
	
	
	

if __name__ == '__main__':
    wordcloud('kongjian')
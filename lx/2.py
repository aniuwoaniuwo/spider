from selenium import webdriver
import time 
import urllib.request
from lxml import etree

driver=webdriver.Firefox()#获取火狐驱动
driver.maximize_window()#窗口最大化

driver.get('http://pic.sogou.com/pics?query=%B3%C2%DE%C8%D1%B8%D5%D5%C6%AC&p=40230500&st=255&mode=255&policyType=0')#打开链接

#模拟翻滚滑条
#<div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/042b51ccd/042b51ccd.webp&quot;); background-position: -13px 0px;"></div>


for i in range(1,2):
        height = 20000*i#每次滑动20000像素
        strWord = "window.scrollBy(0,"+str(height)+")"
        driver.execute_script(strWord)
        time.sleep(4)


selector = etree.HTML(driver.page_source)
print(0)
for i in range(1,2):
		meitu=selector.xpath('//*[@id="picList1"]/li/a[2]/img/@src')
		print(1)
		x=0
		for tu in meitu:
				print(tu)
				urllib.request.urlretrieve(tu,'C:\\lx\\patu\\'+'%s.jpg' % x)
				x=x+1
		#html=requests.get('http://pic.sogou.com/pics?query=%B7%E7%BE%B0%CD%BC%C6%AC&p=40230500&st=255&mode=255&policyType=0'')
		#meitu=re.compile(r'src=[.+?].jpg')
		#tupian=re.findall(meitu,)


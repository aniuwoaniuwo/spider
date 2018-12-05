from selenium import webdriver
import urllib.request
import xlwt
import xlrd
import time
from lxml import etree
user="18813295794"
password="18898604973db"
driver=webdriver.Firefox()#获取火狐驱动
driver.maximize_window()#窗口最大化
driver.get('https://movie.douban.com/')#模拟登陆豆瓣首页
time.sleep(2)

	
		
def set_style(name, height, bold=False):
	style = xlwt.XFStyle()  # 初始化样式
	font = xlwt.Font()  # 为样式创建字体
	font.name = name
	font.bold = bold
	font.colour_index = 2
	font.height = height
	style.font = font
	return style
def denglu():
		
	#print(1)
	driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/a[1]').click()#找到登陆按钮登陆
	time.sleep(2)
	driver.find_element_by_id('email').clear()
	driver.find_element_by_id('email').send_keys(user)#输入账号
	driver.find_element_by_id('password').clear()
	driver.find_element_by_id('password').send_keys(password)#输入密码
		
	
	ff=input('输入验证码:')
	print(ff)
	if 1==0:
			yzm=driver.find_element_by_id('captcha_image').get_attribute('src')#验证码图片链接
			print(yzm)
			ff=yanzheng(yzm)
			print('验证码是：')
			print(ff)
			time.sleep(3)
	driver.find_element_by_name("captcha-solution").clear()
	driver.find_element_by_name("captcha-solution").send_keys(ff)#输入验证码
	driver.find_element_by_name('login').click()#登陆
def yanzheng(s):
	zi=urllib.request.urlretrieve(s,'C:\\lx\\yanzhengma\\'+'1.png')
	print('看验证码图片')
	time.sleep(3)
	shuru=input('输入验证码:')
	print (shuru)
	return shuru
def sousuo():
	yaoshen=xlwt.Workbook(encoding='utf-8')
	sheet1=yaoshen.add_sheet(u'药神',cell_overwrite_ok=True)
	biaoti=[u'编号',u'名字1',u'点赞',u'短评']
	for i in range(len(biaoti)):
			sheet1.write(0,i,biaoti[i],set_style('Time new Roman',220,True))
	yaoshen.save('yaoshen.xlsx')
	time.sleep(5)
	driver.find_element_by_id('inp-query').clear()
	driver.find_element_by_id('inp-query').send_keys("我不是药神")#输入我不是药神
	driver.find_element_by_xpath('//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()#点击搜索
	driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a').click()#点击进去
	driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[8]/div[1]/h2/span/a').click()#点击全部短评
	m = 0
	for f in range(11):
			selector=etree.HTML(driver.page_source)
			mingzis=selector.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/a/text()')
			shijians=selector.xpath('/html/body/div[3]/div[1]/div/div[1]/div[4]/div/div[2]/h3/span[1]/span/text()')
			duanpings=selector.xpath('//*[@id="comments"]/div/div[2]/p/span/text()')
			data=xlrd.open_workbook('yaoshen.xlsx')

			for i in range(len(mingzis)):
					data1=[]
					mingzi=mingzis[i]
					shijian=shijians[i]
					duanping=duanpings[i]
					data1.append(1+m)
					data1.append(mingzi)
					data1.append(shijian)
					data1.append(duanping)
					print(duanping,shijian)
						
					for k in range(len(data1)):
							sheet1.write(1+m,k,data1[k])#写进else
					m=m+1
			yaoshen.save('yaoshen.xlsx')
			driver.find_element_by_class_name('next').click()#点击下一页
			time.sleep(3)

	

if __name__=='__main__':
	
	denglu()
	
	sousuo()
	

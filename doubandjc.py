import requests
import time
import xlwt
import xlrd
from lxml import etree
from multiprocessing import Pool,Lock,Process
import os
import openpyxl
'''多进程的时间缩短了，可是存在xlsx这里会出错，因为各个进程基本同时进行，同时打开了xlsx，不能同时操作xlsx来保存数据，只保存了一个进程的数据，不过ide上打印出了所有的数据，考虑txt保存或者存入数据库或者加Lock就可以解决当前问题!!!经过验证，用TXT也不能解决，同样的原因。'''



		
'''		def set_style(self,name, height, bold=False):
		style = xlwt.XFStyle()  # 初始化样式
		font = xlwt.Font()  # 为样式创建字体
		font.name = name
		font.bold = bold
		font.colour_index = 2
		font.height = height
		style.font = font
		return style'''


def geturl(lock, i):
	print(1)
	print('now running process:%s' % os.getpid())

	url = 'https://music.douban.com/top250?start={}'.format(i * 25)
	re = i * 25
	getxpath(url, lock, re)


def getxpath(url, lock, re):
	if url is None:
		return None
	#lock.acquire()  # 锁住
	#with open('doubandjc.xlsx', 'a', encoding='utf-8') as f:
	#try:

		#wb = openpyxl.load_workbook("doubandjc.xlsx")

		#table = wb.get_sheet_by_name('sheet1')  # 取第一张工作簿
		#table = data.sheets()[0]  # 通过索引顺序获取table，Sheet1索引为0
		#rowcount = table.nrows  # 总行数colsNum=table.ncols#获取列数
	proxies = {
		'http': 'http://124.72.109.183:8118'

	}
	cookie = 'll = "118288";bid = CFXSFuC2 - o8;ps = y;ap_v = 0, 6.0;dbcl2 = "167986306:/8RFXuXSZKo";ck = xdv3;_vwo_uuid_v2 = DCF442F5C0A235FB578E77DBF12FFED3A | 9b84a1e7866efa3ab0debcf4546f59f9;push_noty_num = 0;push_doumail_num = 0'
	referer = 'https: // www.douban.com / accounts / login?source = music'
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
	headers = {'User-Agent': user_agent, 'Referer': referer, 'Cookie': cookie}
	html = requests.get(url, headers=headers, timeout=3, proxies=proxies).text
	td = etree.HTML(html).xpath('//*[@id="content"]/div/div[1]/div/table/tr')
	m = 0
	for p in td:
		data = []
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

		data.append(re + m + 1)
		data.append(title)
		data.append(score)
		data.append(renshu)
		data.append(qita)
		data.append(tupian)

		for i in range(len(data)):
			table.write(re + m + 1, i, data[i])
			#f.write(str(1))

		m = m + 1
		print(re + m + 1)
		print(title, score, renshu, qita)
'''	except Exception as e:
		print('出错了！请看代码！')
	finally:

		wb.save("doubandjc.xlsx")
		lock.release()  # 释放锁'''
		
if __name__=='__main__':
	start=time.time()
	data = xlrd.open_workbook('doubandjc.xlsx')
	table = data.sheets()[0]
	lock = Lock()
	print('now running process:%s' % os.getpid())

	#p=Pool(4)
	q=0

	for f in range(10):
		p=Process(target=geturl,args=(lock,f,))
		#q=25*f
		#print(q)
		p.start()
	p.join()
	#p.close()
	#p.join()
	data.save("doubandjc.xlsx")
	end=time.time()
	print((end-start))#用了19.56002712249756秒，现在对比多进程爬虫
		
		
		
		
		
		
	
	
	
	
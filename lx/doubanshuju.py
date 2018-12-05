import requests
import time
import xlwt
import xlrd
from lxml import etree

class douban(object):
	def __init__(self):
		self.f=xlwt.Workbook(encoding='utf-8')
		self.sheet1=self.f.add_sheet(u'任务列表',cell_overwrite_ok=True)
		self.rowstitle=[u'编号',u'标题',u'评分',u'人数',u'其他',u'图片']
		for i in range(0,len(self.rowstitle)):
			self.sheet1.write(0,i,self.rowstitle[i],self.set_style('Time new Roman',220,True))
		self.f.save('doubanshuju.xlsx')
		
	def set_style(self,name, height, bold=False):
		style = xlwt.XFStyle()  # 初始化样式
		font = xlwt.Font()  # 为样式创建字体
		font.name = name
		font.bold = bold
		font.colour_index = 2
		font.height = height
		style.font = font
		return style
		
	def geturl(self):
		for i in range(1,11):
			url='https://music.douban.com/top250?start={}'.format(i*25)
			self.getxpath(url)
	def getxpath(self,url):
		if url is None:
			return None
		try:
			data=xlrd.open_workbook('doubanshuju.xlsx')
			table=data.sheets()[0]
			rowcount=table.nrows
			proxies = {
				'http': 'http://124.72.109.183:8118'


			}
			cookie='ll = "118288";bid = CFXSFuC2 - o8;ps = y;ap_v = 0, 6.0;dbcl2 = "167986306:/8RFXuXSZKo";ck = xdv3;_vwo_uuid_v2 = DCF442F5C0A235FB578E77DBF12FFED3A | 9b84a1e7866efa3ab0debcf4546f59f9;push_noty_num = 0;push_doumail_num = 0'
			referer='https: // www.douban.com / accounts / login?source = music'
			user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400'
			headers = {'User-Agent': user_agent,'Referer':referer,'Cookie':cookie}
			html = requests.get(url, headers=headers, timeout=3,proxies=proxies).text
			td=etree.HTML(html).xpath('//*[@id="content"]/div/div[1]/div/table/tr')
			m=0
			for p in td:
				data=[]
				title=p.xpath('./td[2]/div/a/text()')
				score=p.xpath('./td[2]/div/div/span[2]/text()')
				renshu=p.xpath('./td[2]/div/div/span[3]/text()')
				qita=p.xpath('./td[2]/div/p/text()')
				tupian=p.xpath('./td[1]/a/img/@src')
			
				title=title[0] if len(title)>0 else ''
				score=score[0] if len(score)>0 else ''
				renshu=renshu[0] if len(renshu)>0 else ''
				qita=qita[0] if len(qita)>0 else ''
				tupian=tupian[0] if len(tupian)>0 else ''
			
				data.append(rowcount+m)
				data.append(title)
				data.append(score)
				data.append(renshu)
				data.append(qita)
				data.append(tupian)
				
				for i in range(len(data)):
					self.sheet1.write(rowcount+m,i,data[i])
					
				m=m+1
				print(m)
				print(title,score,renshu,qita)
		except Exception as e:
			print('出错了！请看代码！')
		finally:
			self.f.save('doubanshuju.xlsx')
		
if __name__=='__main__':
	start=time.time()
	doubanshuju=douban()
	doubanshuju.geturl()
	end=time.time()
	print((end-start))#用了19.56002712249756秒，现在对比多进程爬虫
		
		
		
		
		
		
	
	
	
	
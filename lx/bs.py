import bs4
import requests
import re
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
		
url='https://book.douban.com/'#网址
data=requests.get(url,headers=headers)
#data.encoding='utf-8'
soup=bs4.BeautifulSoup(data.text,"html.parser")
patter=re.compile(r'src="(.*?)"',re.S)
tupians=re.findall(patter,data.text)
#print(tupians)
for tupian in tupians:
		print(tupian)


#print(soup)
#print(data.text)
'''biaoti=soup.find_all('div','title')					
#biaoti=soup.select("#content > div > div.article > div.section.books-express > div.bd > div > div > ul:nth-of-type(1) > li:nth-of-type(2) > div.info > div.title > a")#ul代表页数，
#zhaopian=soup.select("#anony-sns > div > div.main > div > div.albums > ul > li:nth-of-type(1) > div > a > img")
print(biaoti)
#print(zhaopian)
data=[]
for i in biaoti:
		ff=i.get_text()
		print(ff)
	#data.append(ff)	
tupian=soup.select("#content > div > div.article > div.section.books-express > div.bd > div > div > ul:nth-of-type(1) > li:nth-of-type(2) > div.cover > a > img")
#content > div > div.article > div.section.books-express > div.bd > div > div > ul:nth-of-type(2) > li:nth-of-type(2) > div.cover > a > img
print(tupian)
tupian1=soup.find_all('div','src')
print(tupian1)
tag=soup.li.div.find_all('img')
print(tag)
'''


#-*-coding:utf-8-*-
import requests
import time
import xlwt
import xlrd
from lxml import etree
from multiprocessing import Pool,Lock,Process
import os

'''多进程的时间缩短了，可是存在xlsx这里会出错，因为各个进程基本同时进行，同时打开了xlsx，不能同时操作xlsx来保存数据，只保存了一个进程的数据，不过ide上打印出了所有的数据，考虑txt保存或者存入数据库就可以解决当前问题'''


class douban(object):
    def __init__(self):
        self.f = xlwt.Workbook(encoding='utf-8')
        self.sheet1 = self.f.add_sheet(u'任务列表', cell_overwrite_ok=True)
        self.rowstitle = [u'编号', u'标题', u'评分', u'人数', u'其他', u'图片']
        for i in range(0, len(self.rowstitle)):
            self.sheet1.write(0, i, self.rowstitle[i], self.set_style('Time new Roman', 220, True))
        self.f.save('doubandjc.xlsx')

    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = name
        font.bold = bold
        font.colour_index = 2
        font.height = height
        style.font = font
        return style

    def geturl(self, i,lock):
        print('now running process:%s' % os.getpid())

        url = 'https://music.douban.com/top250?start={}'.format(i * 25)
        re = i * 25
        self.getxpath(url, re,lock)

    def getxpath(self, url, re,lock):
        lock.acquire()  # 锁住
        if url is None:
            return None
        with open('doubantxt.txt','a',encoding='utf-8') as f:
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
            print(1)
            for p in td:
                data = []
                title = p.xpath('./td[2]/div/a/text()')
                #// *[ @ id = "content"] / div / div[1] / div / table[1] / tbody / tr / td[2] / div / a
                score = p.xpath('./td[2]/div/div/span[2]/text()')
                renshu = p.xpath('./td[2]/div/div/span[3]/text()')
                qita = p.xpath('./td[2]/div/p/text()')
                tupian = p.xpath('./td[1]/a/img/@src')
                print(title[0])
                print(1)
                f.write(title[0]+"\n")
                #print(title, score, renshu, qita)
        lock.release()  # 释放锁

if __name__ == '__main__':
    start = time.time()
    print('now running process:%s' % os.getpid())
    ff = douban()
    #p = Pool(4)
    lock=Lock()
    for f in range(10):
        p=Process(target=ff.geturl, args=(f,lock,))
        q = 25 * f
        p.start()

    #p.close()
    p.join()
    end = time.time()
    print((end - start))  # 加锁用了16.83242964744568秒，不加锁用了4.321207523345947秒，顺序变了不过数据完整










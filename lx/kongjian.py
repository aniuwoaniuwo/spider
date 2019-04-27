import os
import time
from selenium import webdriver
from lxml import etree
import sys

sys.getdefaultencoding()

user = "1689463866"
password = "3114001154yy"
friend = "956325873"

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://i.qq.com")
driver.switch_to.frame("login_frame")  # 切换到登陆的frame

driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()  # 切换到登陆界面
driver.find_element_by_xpath('//*[@id="u"]').send_keys(user)  # 账号
driver.find_element_by_id("p").send_keys(password)  # 密码
driver.find_element_by_id("login_button").click()  # 登陆
time.sleep(2)  # 加个2秒延迟，登陆需要时间，电脑跟不上
driver.switch_to.default_content()  # 让webdriver操纵当前页

driver.get("http://user.qzone.qq.com/" + friend + "/311")  # 访问朋友空间

next_num = 0
while True:
    for i in range(1, 6):
        height = 20000 * i  # 每次滑动20000像素
        strWord = "window.scrollBy(0," + str(height) + ")"
        driver.execute_script(strWord)
        time.sleep(4)

    driver.switch_to.frame("app_canvas_frame")  # 切换到说说这个框架
    selector = etree.HTML(driver.page_source)
    divs = selector.xpath('/html/body/div[1]/div[2]/div[3]/div/div[1]/div/div[3]/ol/li/div[3]')

    with open('kongjian.txt', 'a') as f:
        for div in divs:
            mingzi = div.xpath('./div[2]/a/text()')
            shijian = div.xpath('./div[4]/div[1]/span/a/text()')
            neirong = div.xpath('./div[2]/pre/text()')
            mingzi = mingzi[0] if len(mingzi) != 0 else ''
            shijian = shijian[0] if len(shijian) != 0 else ''
            neirong = neirong[0] if len(neirong) != 0 else ''
            print(mingzi, shijian, neirong)
            f.write(neirong + "\n")
    if driver.page_source.find('pager_next_' + str(next_num)) == -1:
        break
    driver.find_element_by_id('pager_next_' + str(next_num)).click()
    next_num = next_num + 1
    driver.switch_to.parent_frame()
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(ss):
    text = open('%s.txt' % ss).read()

    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=2000,
        # 这种字体都在电脑字体中，一般路径
        font_path='C:\Windows\Fonts\simfang.ttf',
        height=1200,
        width=1600,
        # 设置字体最大值
        max_font_size=100,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )
    mywc = wc.generate(text)
    plt.imshow(mywc)
    plt.axis("off")
    plt.show()
    wc.to_file('wcbook.png')


if __name__ == '__main__':
    wordcloud('kongjian')

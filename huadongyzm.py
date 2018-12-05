#-*-coding:utf-8-*-
#这是破解爬虫滑动验证码的代码，先是算出需要滑动的距离，
# 再用selenium来模拟鼠标拖拽这个距离进行验证，有必要的话拖拽的速度也要模拟人类
#<div class="gt_slice gt_show" style="left: 99px; background-image: url(&quot;https://static.geetest.com/pictures/gt/8bc4cb7fa/slice/ae62f4207.png&quot;); width: 61px; height: 55px; top: 21px;"></div>
from selenium import webdriver
import io,requests,time
from PIL import Image


driver=webdriver.Firefox()
driver.maximize_window()
url='https://www.huxiu.com/'
driver.get(url)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="top"]/div/ul[2]/li[3]/a').click()#点击登录按钮
time.sleep(2)#网速不好，给个延迟不然会报错
#driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div/div[2]/div[1]/div[2]/a[1]').click()#点击账号密码登录
#time.sleep(2)
driver.find_element_by_xpath('//*[@id="sms_username"]').clear()#清空
driver.find_element_by_xpath('//*[@id="sms_username"]').send_keys('18813295794')
#driver.find_element_by_xpath('//*[@id="login_username"]').clear()#清空
#driver.find_element_by_xpath('//*[@id="login_username"]').send_keys('18813295794')
#driver.find_element_by_xpath('//*[@id="login_password"]').clear()
#driver.find_element_by_xpath('//*[@id="login_password"]').send_keys('18898604973hx')
#接下来就是模拟鼠标拖动了，重要的是拖动的距离要先算出来，
source = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[3]/div[2]')#选中拖动的元素
#target = driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]/a[2]/div[1]/div[11]')
actions = webdriver.ActionChains(driver)#声明对象
actions.drag_and_drop_by_offset(source,280,0)#实现拖拽
actions.perform()#执行这个操作<a class="gt_fullbg gt_hide" href="https://api.geetest.com/click.php?challenge=a390298e4b85abe54402484565669c1853" target="_blank" style="background-image: none;"><div class="gt_cut_fullbg gt_show"><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -157px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -145px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -265px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -277px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -181px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -169px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -241px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -253px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -109px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -97px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -289px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -301px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -85px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -73px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -25px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -37px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -13px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -1px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -121px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -133px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -61px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -49px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -217px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -229px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -205px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -193px -58px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -145px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -157px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -277px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -265px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -169px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -181px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -253px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -241px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -97px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -109px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -301px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -289px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -73px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -85px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -37px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -25px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -1px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -13px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -133px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -121px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -49px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -61px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -229px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -217px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -193px 0px;"></div><div class="gt_cut_fullbg_slice" style="background-image: url(&quot;https://static.geetest.com/pictures/gt/fd70e3bfe/fd70e3bfe.webp&quot;); background-position: -205px 0px;"></div></div><div class="gt_flash" style="height: 94px;"></div><div class="gt_ie_success"></div></a>
driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div/div[2]/div[1]/div[1]/button').click()#点击登录按钮

'''def get_slider_offset(image_url, image_url_bg, css):

    image_file = io.BytesIO(requests.get(image_url).content)

    im = Image.open(image_file)

    image_file_bg = io.BytesIO(requests.get(image_url_bg).content)

    im_bg = Image.open(image_file_bg)

    # 10*58 26/row => background image size = 260*116

    captcha = Image.new('RGB', (260, 116))

    captcha_bg = Image.new('RGB', (260, 116))

    for i, px in enumerate(css):

        offset = convert_css_to_offset(px)

        region = im.crop(offset)

        region_bg = im_bg.crop(offset)

        offset = convert_index_to_offset(i)

        captcha.paste(region, offset)

        captcha_bg.paste(region_bg, offset)

    diff = ImageChops.difference(captcha, captcha_bg)

    return get_slider_offset_from_diff_image(diff)'''
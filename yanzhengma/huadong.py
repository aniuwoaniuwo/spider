#-*-coding:utf-8-*-
#思路：输入账号密码---(点击验证按钮）---弹出验证码--获取验证码的坐标---全屏截图---按照坐标截图---
#---点击拖动按钮---获取有缺陷的全屏截图---获取有缺陷的验证码---
# ---遍历两个图的像素点，找到缺陷的位置，x坐标---x-6就是移动的距离了---模拟出人为的移动轨迹list，元素是0.2秒一个距离
# ---按照轨迹模拟拖动---验证是否成功---点击登录

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import time

zhanghao=''
password=''
url=''
BORDER=6#一个小图12px宽，图中看到大概是一半，且验证码拖动差一点无所谓

class huadong(object):
    def __init__(self):
        self.email=zhanghao
        self.password=password
        self.driver=webdriver.Firefox()
        self.wait=WebDriverWait(self.driver,20)
        self.url=url

    def __del__(self):
        self.driver.close()

    def open(self):
        '''
        打开网页输入用户名，密码，selenium操作
        :return:
        '''
        self.driver.get(self.url)
        #等到节点被加载出来
        email=self.wait.until(EC.presence_of_element_located((By.ID,'')))
        password=self.wait.until(EC.presence_of_element_located((By.ID,'')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_geetest_button(self):
        '''
        获取初始验证的按钮，返回按钮
        :return:
        '''
        button=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'geetest_radar_tip')))
        return button

    def get_screenshot(self):
        '''
        获取全屏截图，返回截图
        :return:
        '''
        screenshot=self.driver.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        '''
        获取验证码的坐标，返回四个坐标
        :return:
        '''
        img=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'geetest_canvas_img')))
        time.sleep(2)
        location=img.location
        size=img.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_geetest_image(self,name='captcha.png'):
        '''
        导入全屏截图，按照坐标裁剪，返回验证码的截图
        :param name:
        :return:
        '''
        top,bottom,left,right=self.get_position()
        print('验证码的位置：',top,bottom,left,right)
        screenshot=self.get_screenshot()
        captcha=screenshot.crop((left,top,right,bottom))
        return captcha

    def get_slider(self):
        '''
        获取滑块，返回滑块对象
        :return:
        '''
        slider=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'geetest_slider_button')))
        return slider

    def is_pixel_equal(self,image1,image2,x,y):
        '''
        判断两个图的像素是否相同，返回对错
        :param image1:
        :param image2:
        :param x:
        :param y:
        :return:
        '''
        pixel1=image1.load()[x,y]
        pixel2=image2.load()[x,y]
        threshold=60
        if abs(pixel1[0]-pixel2[0]) < threshold and abs(pixel1[1]-pixel2[1]) < threshold and abs(
                pixel1[2]-pixel2[2]) <threshold:
            return True
        else:
            return False

    def get_gap(self,image1,image2):
        '''
        获取缺口的偏移量，返回偏移量
        :param image1:
        :param image2:
        :return:
        '''
        left=60
        for i in range(left,image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1,image2,i,j):
                    left=i
        return left

    def get_track(self,distance):
        '''
        根据偏移量获取移动轨迹，返回移动轨迹
        :param distance:
        :return:
        '''
        #移动轨迹
        track=[]
        #当前位移
        current=0
        #减速阀值
        mid=distance * 4/5
        #计算间隔
        t=0.2
        #初速度
        v=0

        while current < distance:
            if current < mid:
                #加速度为正2
                a=2
            else:
                #加速度为负3
                a=-3
            #初速度为v0
            v0=v
            #当前的速度
            v=v0+a*t
            #移动的距离
            move=v0*t + 1/2*a*t*t
            #当前位移
            current += move
            #加入到移动轨迹
            track.append(round(move))
        return track

    def move_to_gap(self,slider,tracks):
        '''
        拖动滑块到缺口处，完成破解
        :param slider:
        :param tracks:
        :return:
        '''
        webdriver.ActionChains(self.driver).click_and_hold(slider).perform()
        for x in tracks:
            webdriver.ActionChains(self.driver).move_by_offset(xoffset=x,yoffset=0).perform()
        time.sleep(0.5)
        webdriver.ActionChains(self.driver).release().perform()

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def main(self):
        '''
        破解的入口
        :return:
        '''
        #登录，输入账号密码
        self.open()
        #点击验证按钮
        button = self.get_geetest_button()
        button.click()
        #获取无缺口的验证码
        image1=self.get_geetest_image()
        #单击滑块，获取有缺口的验证码的图片
        slider=self.get_slider()
        slider.click()
        image2=self.get_geetest_image()
        #找出缺口的位置
        gap=self.get_gap(image1,image2)
        print('缺口位置', gap)
        gap -= BORDER
        #获取运动轨迹
        tracks=self.get_track(gap)
        print('滑动轨迹', tracks)
        # 拖动滑块
        self.move_to_gap(slider, tracks)
        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        print(success)

        # 失败后重试
        if not success:
            self.crack()
        else:
            self.login()

if __name__=='__main__':
    f=huadong()
    f.main()




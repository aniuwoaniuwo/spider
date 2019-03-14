#-*-coding:utf-8-*-
#此类验证码往往需要你点击图中的字
#思路：输入账号密码弹出验证码--获取验证码坐标---截全图--按照坐标裁剪---传到打码平台
#---传回字的坐标--模拟点触---完成破解。
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from yanzhengma.chaojiying import Chaojiying_Client#导入超级鹰的类
import time
from PIL import Image
from io import BytesIO

EMAIL='zhongqq163yx@163.com'
PASSWORD='zhongqq163mm'
#超级鹰的用户名、密码、软件ID、验证码类型（参考http://www.chaojiying.com/price.html）
CHAOJIYING_USERNAME='18813295794'
CHAOJIYING_PASSWORD='18826690336cjy'
CHAOJIYING_SOFT_ID='898764'
CHAOJIYING_KIND='9102'#点击两个相同的字,返回:x1,y1|x2,y2



class CrackTouCLICK(object):
    def __init__(self):
        self.url='http://admin.touclick.com/login.html'
        self.driver=webdriver.Firefox()
        self.wait=WebDriverWait(self.driver,20)
        self.email=EMAIL
        self.password=PASSWORD
        self.chaojiying=Chaojiying_Client(CHAOJIYING_USERNAME,CHAOJIYING_PASSWORD,CHAOJIYING_SOFT_ID)

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
    def get_touclick_buttun(self):
        '''
        获取验证码点击的按钮,返回点击元素的节点
        :return:
        '''
        #等到节点可以被点击
        buttun=self.wait.until(EC.element_to_be_clickable((By.ID,'')))
        return buttun

    def get_element(self):
        '''
        获取验证码图片对象，返回图片对象
        :return:
        '''
        element=self.wait.until(EC.presence_of_element_located((By.ID,'')))
        return element

    def get_position(self):
        '''
        获取验证码的位置，返回验证码的位置
        :return:
        '''
        element=self.get_element()
        time.sleep(2)
        location=element.location
        size=element.size
        top,bottom,left,right=location['y'],location['y']+size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_screenshot(self):
        '''
        获取网页的截图，返回截图对象
        :return:
        '''
        screenshot=self.driver.get_screenshot_as_png()
        screenshot=Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self,name='captcha.png'):
        '''
        从大截图中获取验证码图片，返回图片
        :param name:
        :return:
        '''
        top,bottom,left,right=self.get_position()
        print('验证码的位置：',top,bottom,left,right)
        screenshot=self.get_screenshot()
        captcha=screenshot.crop((left.top,right,bottom))
        return captcha

    def get_points(self,captcha_result):
        '''
        解析识别的结果，返回转化后的结果，包括坐标
        :param captcha_result:
        :return:
        '''
        groups=captcha_result.get('pic_str').split('|')
        #list 生成列表可以循环嵌套
        locations=[[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self,locations):
        '''
        点击验证码的字，破解验证码，
        :param locations:
        :return:
        '''
        for location in locations:
            print(location)
            webdriver.ActionChains(self.driver).move_to_element_with_offset(self.get_touclick_element(),location[0],location[1]).click().perform()
        time.sleep(1)

    def touch_click_verify(self):
        """
        点击验证按钮
        :return: None
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'touclick-pub-submit')))
        button.click()

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, '_submit')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def main(self):
        '''
        破解的入口
        :return:
        '''
        #登录网址
        self.open()
        #获取验证码，点击出现验证码
        buttom=self.get_touclick_buttun()
        buttom.click()
        #获取验证码的图片
        image=self.get_touclick_image()
        bytes_array=BytesIO()
        image.save(bytes_array,format='PNG')
        #识别验证码
        result=self.chaojiying.PostPic(bytes_array.getvalue(),CHAOJIYING_KIND)
        print(result)
        #解析识别的验证码，
        locations = self.get_points(result)
        #处理解析的结果，模拟点击破解验证码
        self.touch_click_words(locations)
        self.touch_click_verify()
        # 判定是否成功
        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'touclick-hod-note'), '验证成功'))
        print(success)
        # 失败后重试
        if not success:
            self.main()
        else:
            self.login()
if __name__=="__main__":
    tou=CrackTouCLICK()
    tou.main()

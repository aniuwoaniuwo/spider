#-*-coding:utf-8-*-
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

cap={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62025",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",cap)#程序连接appium，4723是appium端口

def get_size():
    width=driver.get_window_size()['width']
    height=driver.get_window_size()['height']
    return(width,height)
try:
    if WebDriverWait(driver,15).until(lambda x:x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']").send_keys('aniuwo')
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']").send_keys('zhongqq163mm')
        driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']").click()
except:
    pass
try:
    if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[5]")):
        driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[5]").click()
except:
    pass
if WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[2]/android.widget.ImageView[1]")):
    driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[2]/android.widget.ImageView[1]").click()
    size=get_size()
    x1=int(size[0]*0.5)
    y1=int(size[1]*0.75)
    x2=int(size[0]*0.5)
    y2=int(size[1]*0.25)
    while 1:
        driver.swipe(x1,y1,x2,y2)
        time.sleep(2)

#-*-coding:utf-8-*-
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from multiprocessing import Process,Pool

# cap=
#
# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',cap)
#-*-coding:utf-8-*-
from appium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait


def get_coordinates(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def get_share_url(device,port):
    cap={
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": device,
      "udid":device,
      "appPackage": "com.ss.android.ugc.aweme",
      "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
      "noReset": True,
      "unicodeKeyboard": True,#使用unicode编码方式发送字符串
      "resetKeyboard": True#隐藏键盘
    }

    driver=webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port),cap)#程序连接appium，4723是appium端口
    print('等10秒')
    time.sleep(10)
    TouchAction(driver).tap(x=79, y=124).perform()
    print('等待元素出现')
    if WebDriverWait(driver,15).until(lambda x:x.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View")):
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View").click()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View").clear()
        print(driver.page_source)

        # #切换输入法
        # TouchAction(driver).tap(x=282, y=1817).perform()
        # driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View").click()
        #抖音id，不是share_id
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.View").send_keys(191433445)
        driver.find_element_by_id("com.ss.android.ugc.aweme:id/dgz").click()
    if WebDriverWait(driver,15).until(lambda x:x.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.TextView")):
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.TextView").click()
    if WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView")):
        driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView").click()

    #点击粉丝数
    if WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.ss.android.ugc.aweme:id/agw')):
        driver.find_element_by_id('com.ss.android.ugc.aweme:id/agw').click()
    #等1秒
    time.sleep(2)

    coordinates=get_coordinates(driver)
    x=int(coordinates[0]*0.5)
    y1=int(coordinates[1]*0.15)
    y2=int(coordinates[1]*0.9)
    while 1:
        # print(driver.page_source)#安卓版本低不能获取页面元素，内容，首页那里也是
        # time.sleep(3)
        # if '没有更多了' in driver.page_source:
        #     break
        # else:
            driver.swipe(x, y2, x, y1)
            time.sleep(0.2)
if __name__=='__main__':
    device_list=['127.0.0.1:62025','127.0.0.1:62026']
    data=[]
    pool=Pool(processes=4)
    # for i in len(device_list):
    for i in range(1,2):
        port=4723+i*2
        pool.apply_async(get_share_url,(device_list[i],port,))
    pool.close()
    pool.join()

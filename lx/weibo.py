from selenium import webdriver
import os
import time

username = "18813295794"
password = "18898604973xl"

driver=webdriver.Firefox()
driver.maximize_window()

driver.get('http://weibo.com/login.php')

driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a').click()
time.sleep(3)

print(driver.title)
os.system(pause)


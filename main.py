#coding=utf-8
from PhoneDeal import *
from selenium import webdriver

driver = webdriver.Chrome('/Users/dong/projects/selenium/chromedriver')  # Optional argument, if not specified will search path.

test=PhoneDeal("lktop","huanxiang")
test.GetBalanceStr()
test.PrintAccountInformation()

#test.GetPhoneNumber()
#test.GetYzm()


chromeOptions = webdriver.ChromeOptions()
#无界面
#chromeOptions.add_argument('--headless')
#关闭图片
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
#禁用gpu加速
chromeOptions.add_argument('--disable-gpu')
browser=webdriver.Chrome(chrome_options=chromeOptions)
browser.set_window_size(1280,800)
browser.get("https://www.nike.com/cn/launch/t/air-jordan-6-diffused-blue-court-blue/")
regbut=browser.find_elements_by_tag_name('button')
regbut[2].click()
join=browser.find_elements_by_tag_name('a')
join[14].click()
browser.find_element_by_class_name('phoneNumber').send_keys("15245871026")
browser.find_element_by_class_name('sendCodeButton').click()
k=browser.find_elements_by_tag_name('input')
s=0
for i in k:
    print s
    print i.get_attribute("id")
    s=s+1

# browser.find_element_by_class_name('code blurred').send_keys(yzm)


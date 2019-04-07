#coding=utf-8
from PhoneDeal import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random, string

s = string.ascii_letters
mail = ""
for i in range(random.randint(5, 10)):
    mail = mail + random.choice(s)

for i in range(random.randint(5, 10)):
    mail = mail + str(random.randint(0,9))

print("-"+mail + "-")

sms = "【NIKE中国】您的 NIKE 手机验证码是 936944"
sms = sms[len(sms)-6:]
sms = sms.replace(" ", "")
print("-"+str(sms) + "-")
#driver = webdriver.Chrome('C:/Users/admin/Desktop/NikeRegMach/chromedriver.exe')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.

#test=PhoneDeal("lktop","huanxiang")
#test.GetBalanceStr()
#test.PrintAccountInformation()

#test.GetPhoneNumber()
#test.GetYzm()

sleep = True

chromeOptions = webdriver.ChromeOptions()
#无界面
#chromeOptions.add_argument('--headless')
#关闭图片
#prefs = {"profile.managed_default_content_settings.images": 2}
#chromeOptions.add_experimental_option("prefs", prefs)
#禁用gpu加速
chromeOptions.add_argument('--disable-gpu')
browser=webdriver.Chrome(chrome_options=chromeOptions)
browser.set_window_size(1280,800)
browser.get("https://www.nike.com/cn/launch/t/air-jordan-6-diffused-blue-court-blue/")
regbut=browser.find_elements_by_tag_name('button')
regbut[3].click()
if sleep:
    time.sleep(2)
join=browser.find_elements_by_tag_name('a')
join[15].click()
if sleep:
    time.sleep(2)
country = browser.find_element_by_name('country')
s = Select(country)
country_index = 0
for i in range(len(s.options)):
    if s.options[i].text == u'香港' or s.options[i].text == u'中国香港特别行政区':
        print("got country index: " + str(i))
        country_index = i
        break

Select(country).select_by_index(country_index)  #240:香港
if sleep:
    time.sleep(3)

#https://www.cnblogs.com/zuodaozhudemeng/p/7487798.html
email = browser.find_element_by_css_selector("input[name='emailAddress'][type='email']")
email.send_keys("test255233424535@qq.com")
if sleep:
    time.sleep(random.randint(3,6))
password = browser.find_element_by_css_selector("input[name='password'][type='password']")
password.send_keys("Passw0rd!")
if sleep:
    time.sleep(random.randint(3,6))
firstname = browser.find_element_by_css_selector("input[name='firstName'][type='text']")
firstname.send_keys("Zoe")
if sleep:
    time.sleep(random.randint(2,5))
lastname = browser.find_element_by_css_selector("input[name='lastName'][type='text']")
lastname.send_keys("Zhang")
if sleep:
    time.sleep(random.randint(2,5))
dateOfBirth = browser.find_element_by_css_selector("input[name='dateOfBirth'][type='date']")
dateOfBirth.send_keys("07/02/1983")        #不丹07/02/1983； 香港001983-09-21
if sleep:
    time.sleep(random.randint(2,5))
dateOfBirth = browser.find_element_by_css_selector("input[name='dateOfBirth'][type='date']")
print(dateOfBirth.get_attribute('value'))
#sex=browser.find_element_by_css_selector("ul[data-componentname='gender']>li(1)")
sex=browser.find_element_by_xpath("//span[text()='女']")
sex.click()
if sleep:
    time.sleep(random.randint(1,3))
submit = browser.find_element_by_css_selector("input[type='button'][value='建立帳號']") #
submit.click()



# browser.find_element_by_class_name('code blurred').send_keys(yzm)


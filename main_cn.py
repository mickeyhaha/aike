#coding=utf-8
from selenium.common.exceptions import NoSuchElementException

from PhoneDeal import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
import random
import requests
import datetime, time, string

#driver = webdriver.Chrome('C:/Users/admin/Desktop/NikeRegMach/chromedriver.exe')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome('chromedriver')  # Optional argument, if not specified will search path.

#test=PhoneDeal("lktop","huanxiang")
#test.GetBalanceStr()
#test.PrintAccountInformation()

#test.GetPhoneNumber()
#test.GetYzm()

token='01358262d69b4e876e410c0cc9ef2fca3bbab30f4001'
project_no='723'

sleep = True

chromeOptions = webdriver.ChromeOptions()
#无界面
#chromeOptions.add_argument('--headless')
#关闭图片
#prefs = {"profile.managed_default_content_settings.images": 2}
#chromeOptions.add_experimental_option("prefs", prefs)
#禁用gpu加速
chromeOptions.add_argument('--disable-gpu')

for i in range(4):
    browser=webdriver.Chrome(chrome_options=chromeOptions)
    browser.set_window_size(1280,800)
    browser.get("https://www.nike.com/cn/launch/t/air-jordan-6-diffused-blue-court-blue/")
    regbut=browser.find_elements_by_tag_name('button')
    regbut[3].click()
    if sleep:
        time.sleep(random.randint(2,5))
    join=browser.find_elements_by_tag_name('a')
    join[15].click()
    if sleep:
        time.sleep(random.randint(2,5))


    #http://www.51ym.me/User/apidocs.html#getmobile
    #发送get请求
    timestamp=str(datetime.datetime.now())

    phone = ""
    sms = ""
    while True:
        print("getting phone number...")
        get_phone = requests.get("http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token="+token+
                      "&itemid="+project_no+"&timestamp="+timestamp)
        if get_phone.content.startswith("success"):
            phone = get_phone.content.replace("success|", "")
            print("got phone number: " + phone)
            break
        print("error getting phone number: " + get_phone.content)
        time.sleep(6)

    browser.find_element_by_class_name('phoneNumber').send_keys(phone)
    browser.find_element_by_class_name('sendCodeButton').click()
    time.sleep(random.randint(2,5))
    while True:
        print("getting sms...")
        get_sms = requests.get("http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token="+token+"&itemid="+project_no+"&mobile="+phone+"&release=1&timestamp="+timestamp)
        if get_sms.content.startswith("success"):
            sms = get_sms.content.replace("success|", "")
            sms = sms[len(sms)-6:]
            sms = sms.replace(" ", "")
            print("got sms: " + sms)    #【NIKE中国】您的 NIKE 手机验证码是 936944
            break
        print("error getting sms: " + get_sms.content)
        time.sleep(6)

    browser.find_element_by_css_selector("input[type='number']").send_keys(sms)

    time.sleep(random.randint(2,5))

    submit = browser.find_element_by_css_selector("input[type='button'][value='继续']")
    submit.click()
    time.sleep(random.randint(5,10))

    lastname = browser.find_element_by_css_selector("input[name='lastName'][type='text']")
    lastname.send_keys("Dong")
    if sleep:
        time.sleep(random.randint(2,5))

    firstname = browser.find_element_by_css_selector("input[name='firstName'][type='text']")
    firstname.send_keys("Pei Jian")
    if sleep:
        time.sleep(random.randint(2,5))

    pwd = "Passw0rd!"
    pwd = pwd + str(random.randint(1,10000))
    password = browser.find_element_by_css_selector("input[name='password'][type='password']")
    password.send_keys(pwd)
    if sleep:
        time.sleep(random.randint(3,6))

    sex=browser.find_element_by_xpath("//span[text()='男子']")
    sex.click()
    if sleep:
        time.sleep(random.randint(1,4))

    submit = browser.find_element_by_css_selector("input[type='button'][value='注册']") #
    submit.click()

    if sleep:
        time.sleep(random.randint(3,6))

    s = string.ascii_letters
    mail = ""
    for i in range(random.randint(5, 10)):
        mail = mail + random.choice(s)

    for i in range(random.randint(5, 10)):
        mail = mail + str(random.randint(0, 9))

    mail = mail + "@yopmail.com"
    success = True
    try:
        email = browser.find_element_by_css_selector("input[name='emailAddress'][type='email']")
    except NoSuchElementException as e:
        print('except:', e)
    finally:
        success = False
    if success:
        email.send_keys(mail)
        if sleep:
            time.sleep(random.randint(3,6))

        submit = browser.find_element_by_css_selector("input[type='button'][value='保存']") #
        submit.click()

        if sleep:
            time.sleep(random.randint(3,6))

        submit = browser.find_element_by_css_selector("input[type='button'][value='跳过']") #
        submit.click()

        if sleep:
            time.sleep(random.randint(3,6))

        f = open('accounts.txt', 'w')  # 若是'wb'就表示写二进制文件
        f.write(phone + "," + email + "," + pwd + "\n")
        f.close()

    browser.close()



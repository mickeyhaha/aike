#coding=utf-8
import requests
import datetime, time

token=''
project_no='723'

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
    time.sleep(6)

while True:
    print("getting sms...")
    get_sms = requests.get("http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token="+token+"&itemid="+project_no+"&mobile="+phone+"&release=1&timestamp="+timestamp)
    if get_sms.content.startswith("success"):
        sms = get_sms.content.replace("success|", "")
        print("got sms: " + phone)
        break
    time.sleep(6)



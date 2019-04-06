#PhoneDeal.py
#coding=utf-8
import requests
import time

class PhoneDeal(object):
    username=''
    password=''
    Token=''
    Balance=''
    NowPhone=''
    NowYzm=''
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.Token=requests.get(url='http://47.96.183.58:9180/service.asmx/UserLoginStr?name='+self.username+'&psw='+self.password).content

    def GetBalanceStr(self):
        self.Balance=requests.get(url='http://47.96.183.58:9180/service.asmx/GetBalanceStr?name='+self.username+'&psw='+self.password).content

    def PrintAccountInformation(self):
        print "Id: %s  Token: %s   Banlance: %s"%(self.username,self.Token,self.Balance)

    def GetPhoneNumber(self):
        self.NowPhone=requests.get(url='http://47.96.183.58:9180/service.asmx/GetHM2Str?token=%s&xmid=3119&sl=1&lx=6&a1=&a2=&pk=&ks=0&rj='%(self.Token)).content.split('=')[1]
        print self.NowPhone

    def GetYzm(self):
        yzmcontent='1'
        while(yzmcontent=='1'):
            time.sleep(5)
            yzmcontent=requests.get(url='http://47.96.183.58:9180/service.asmx/GetYzm2Str?token=%s&xmid=3119&hm=%s&sf=1'%(self.Token,self.NowPhone)).content
            try:
                yzm=yzmcontent.split(' ')[5]
            except:
                continue
        print yzm
        return yzm
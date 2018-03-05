# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from baidu import Baidu


START_URL = r'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=car&step_word=&hs=0&pn=0&spn=0&di=166934340210&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1328865088%2C2207862393&os=2317468077%2C3874901594&simid=3419366795%2C412181702&adpicid=0&lpn=0&ln=1999&fr=&fmq=1520250502306_R&fm=index&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.onquan.com%2Fhtml%2Fuploadfile%2F2009%2F1130%2F20091117161721994.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B5gq7wg_z%26e3Bv54AzdH3Fip4sAzdH3Fs2AzdH3FfwgojtAzdH3F0mcl_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0'


driver = webdriver.Edge(executable_path='driver/MicrosoftWebDriver.exe')
# driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')

driver.get(START_URL)

time.sleep(3)

baidu = Baidu(driver)
baidu.retrieve_image(r'D:/img/')

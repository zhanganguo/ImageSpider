# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from engine.baidu import Baidu
from engine.bing import Bing



BAIDU_URL = r'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=car&step_word=&hs=0&pn=0&spn=0&di=166934340210&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1328865088%2C2207862393&os=2317468077%2C3874901594&simid=3419366795%2C412181702&adpicid=0&lpn=0&ln=1999&fr=&fmq=1520250502306_R&fm=index&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.onquan.com%2Fhtml%2Fuploadfile%2F2009%2F1130%2F20091117161721994.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B5gq7wg_z%26e3Bv54AzdH3Fip4sAzdH3Fs2AzdH3FfwgojtAzdH3F0mcl_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0'
BING_URL = r'https://cn.bing.com/images/search?view=detailV2&ccid=GXdER3ig&id=7CF7471249A9ED76C2E5A0D742DF030A262135CB&thid=OIP.GXdER3igplPsqpQ2WrDm0wHaE8&q=cat&simid=608014672341436785&selectedindex=4&qpvt=cat&mode=overlay&first=1'

driver = webdriver.Edge(executable_path='driver/MicrosoftWebDriver.exe')
# driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')

storing_folder = r'D:/img/'

# image_engine = Baidu(driver, BAIDU_URL, storing_folder)
image_engine = Bing(driver, BING_URL, storing_folder)

image_engine.retrieve_image()





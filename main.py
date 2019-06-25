# -*- coding: utf-8 -*-
from selenium import webdriver
from engine.baidu import Baidu
from engine.bing import Bing


driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')

# 爬取图像的保存位置
storing_folder = r'D:/img/'

# 百度图片的爬虫起始地址
BAIDU_URL = r'https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=car&step_word=&hs=0&pn=0&spn=0&di=166934340210&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=1328865088%2C2207862393&os=2317468077%2C3874901594&simid=3419366795%2C412181702&adpicid=0&lpn=0&ln=1999&fr=&fmq=1520250502306_R&fm=index&ic=0&s=undefined&se=&sme=&tab=0&width=&height=&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.onquan.com%2Fhtml%2Fuploadfile%2F2009%2F1130%2F20091117161721994.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B5gq7wg_z%26e3Bv54AzdH3Fip4sAzdH3Fs2AzdH3FfwgojtAzdH3F0mcl_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0'
# 必应图片的爬虫其实地址
# BING_URL = r'https://cn.bing.com/images/search?view=detailV2&ccid=GEOc5PJD&id=18C03B0B631A5D4AB00318106607A85874425DEF&thid=OIP.GEOc5PJD-h_qBd5eIo6KHgHaEK&mediaurl=http%3a%2f%2fassetto-db.com%2fimg%2fpreviews%2fmclaren_570s%2fwhite.png&exph=768&expw=1366&q=car&simid=608051047430947137&selectedIndex=0&ajaxhist=0'

image_engine = Baidu(driver, BAIDU_URL, storing_folder)
# image_engine = Bing(driver, BING_URL, storing_folder)

image_engine.retrieve_image()



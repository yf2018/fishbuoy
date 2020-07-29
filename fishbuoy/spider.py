#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 21:41
# @File    : spider.py
# @Software: Pycharm
# @Author  : Changan
import pandas
import time
import re
from lxml import etree
from selenium import webdriver
import pymysql
import json
from urllib.request import urlopen, quote
import requests
browser = webdriver.Chrome()
def get_data(sql):
    conn = pymysql.connect('127.0.0.1','root','132441','aqi',charset = 'utf8')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return 0
def get_all_aqi(url):
    browser.get(url)
    selector = etree.HTML(browser.page_source, parser=None, base_url=None)
    for i in range(1,353):
        ranknum = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[1]/text()' % (i))
        quality = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[2]/em/text()' % (i))
        location = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/a/text()' % (i))
        province = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[3]/text()' % (i))
        aqi = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[4]/text()' % (i))
        pm25 = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[5]/text()' % (i))
        getlnglat(''.join(province)+''.join(location))
        # sql = "insert into aqi.city_aqi(ranknum,quality,location,province,aqi,pm25)\
        #      values("+''.join(ranknum)+","+"'"+''.join(quality)+"'"+","+"'"+''.join(location)+"'"+","+"'"+''.join(province)+"'"+","+''.join(aqi)+","+''.join(pm25)+");"
        # sql = "insert into aqi.city_aqi(ranknum,quality,location,province,aqi,pm25)values(%s,%s,%s,%s,%s,%s);"
        # get_data(sql)

def getlnglat(address):
    # address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
    base_url = "http://api.map.baidu.com/geocoder?address={address}&output=json&ak=WHEAK2BlGjK2yGy0RD06Ym2nGYGrmzmm".format(address = address)
    response = requests.get(base_url)
    answer = response.json()
    lng = answer['result']['location']['lng']
    lat = answer['result']['location']['lat']
    print(address,lng,lat)
    return 0
get_all_aqi('http://www.pm25.com/rank.html')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 21:41
# @File    : spider.py
# @Software: Pycharm
# @Author  : Changan

url = 'http://www.pm25.com/rank.html'
import pandas
import time
import re
from lxml import etree
from selenium import webdriver
import pymysql
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
        data = []
        ranknum = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[1]/text()' % (i))
        quality = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[2]/em/text()' % (i))
        location = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/a/text()' % (i))
        province = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[3]/text()' % (i))
        aqi = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[4]/text()' % (i))
        pm25 = selector.xpath('/html/body/div[5]/div/div[3]/ul[2]/li[%d]/span[5]/text()' % (i))
        data.append(''.join(ranknum))
        data.append(''.join(quality))
        data.append(''.join(location))
        data.append(''.join(province))
        data.append(''.join(aqi))
        data.append(''.join(pm25))
        sql = "insert into aqi.city_aqi(ranknum,quality,location,province,aqi,pm25)\
             values("+''.join(ranknum)+","+"'"+''.join(quality)+"'"+","+"'"+''.join(location)+"'"+","+"'"+''.join(province)+"'"+","+''.join(aqi)+","+''.join(pm25)+");"
        # sql = "insert into aqi.city_aqi(ranknum,quality,location,province,aqi,pm25)values(%s,%s,%s,%s,%s,%s);"
        print(sql)
        get_data(sql)
get_all_aqi(url)
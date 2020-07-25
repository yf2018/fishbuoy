#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 20:09
# @File    : views.py
# @Software: Pycharm
# @Author  : Changan

from django.http import HttpResponse
from django.shortcuts import render
import pymysql

def index(request):
    return render(request,'index.html')
def mapshow(request):
    sql = "select * from city_aqi"
    m_data = get_data(sql)
    ranknum = []
    quality = []
    location = []
    province = []
    aqi = []
    pm25 = []
    for list in m_data:
        ranknum.append(list[0])
        quality.append(list[1])
        location.append(list[2])
        province.append(list[3])
        aqi.append(list[4])
        pm25.append(list[5])
    print(location)
    return render(request,'mapshow.html',{'data':location})
def get_data(sql):
    conn = pymysql.connect('127.0.0.1', 'root', '132441', 'aqi', charset = 'utf8')
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()  # 搜取所有结果
    cur.close()
    conn.close()
    return results
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 20:09
# @File    : views.py
# @Software: Pycharm
# @Author  : Changan

from django.http import HttpResponse
from django.shortcuts import render
import pymysql
import requests

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
    longitude = []
    latitude = []
    for list in m_data:
        m_list = []
        ranknum.append(list[0])
        quality.append(list[1])
        location.append(list[2])
        province.append(list[3])
        aqi.append(list[4])
        pm25.append(list[5])
    # m_address = []
    大兴安岭
    for address in location:
        print(address)
    return render(request,'mapshow.html',{'data':m_data})
def get_data(sql):
    conn = pymysql.connect('127.0.0.1', 'root', '132441', 'aqi', charset = 'utf8')
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()  # 搜取所有结果
    cur.close()
    conn.close()
    return results
def geocode(address):
    """
    @ address: 名称字符串
    @ 返回值：经度，纬度
    """
    base_url = "http://api.map.baidu.com/geocoder?address={address}&output=json&ak=WHEAK2BlGjK2yGy0RD06Ym2nGYGrmzmm".format(address=address)
    response = requests.get(base_url)
    answer = response.json()
    longitude = answer['result']['location']['lng']
    latitude = answer['result']['location']['lat']
    list = [longitude,latitude]
    # print(list)
    return list
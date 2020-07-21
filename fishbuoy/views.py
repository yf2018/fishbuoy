#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 20:09
# @File    : views.py
# @Software: Pycharm
# @Author  : Changan

from django.http import HttpResponse
from django.shortcuts import render
from pymysql import *

def index(request):
    return render(request,'index.html')
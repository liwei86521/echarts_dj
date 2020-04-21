# -*- coding:utf-8 -*-
'''
@Author:F7687778 
@File: url.py
@Time: 2020/4/21 下午 02:28
'''
from django.urls import path
from django.conf.urls import include, url
from echartAppDemo import views

urlpatterns = [
    path('linecharts/', views.line_chars),
]

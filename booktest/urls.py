from booktest import views
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^index$', views.index),  # 图书信息页面
    url(r'^create$', views.create),  # 图书信息页面
    url(r'^delete(\d+)$', views.delete),  # 删除点击的图书
    # (\d+) 让Django进行地址匹配时将这一部分数字作为参数传递给视图

]

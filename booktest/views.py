from datetime import date
from django.shortcuts import render, redirect
# redirect 导入重定向函数
from booktest.models import BookInfo
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# 创建视图


def index(request):
    '''显示图书信息'''
    # 　１　查询图书信息
    books = BookInfo.objects.all()
    # 2 使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''新增一本书'''
    # 1 创建一个BookInfo对象
    b = BookInfo()
    b.btitle = '倚天屠龙记'
    b.bpub_date = date(2012, 4, 30)
    # 2 保存数据库
    b.save()
    # f返回应答,让浏览器访问首页index,重定向
    # return HttpResponse('OK')  # 返回给浏览器显示内容
    # return HttpResponseRedirect('/index')  # HttpResponseRedirect 参数写浏览器访问的地址
    return redirect('/index')  # 同上


def delete(request, bid):
    '''删除点击的图书'''
    # 1通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2 删除
    book.delete()
    # 3 重定向，让浏览器还是访问首页
    # return HttpResponseRedirect('/index')
    return redirect('/index')

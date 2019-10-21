from django.db import models


# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)  # CharField 必须指定max_length 否则报错
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)  # 阅读量，设置默认为0
    b_comment = models.IntegerField(default=0)  # 评论数
    isDelete = models.BooleanField(default=False)  # 设置逻辑删除,默认不删除/软删除标记


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=256)  # 备注
    # 两个类有一对多关系时，需要设置一个关系属性
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)  # 设置逻辑删除,默认不删除/软删除标记

# 两个类有一对多的额关系
# 仅仅是修改注释

#  rm -rf .navicat64/

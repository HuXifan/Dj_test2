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


# 两个类有一对多的关系,类之间有一对一，一对多，多对多的关系

class NewsType(models.Model):
    '''新闻类型类'''
    typename = models.CharField(max_length=128)
    # 关系类型代表下面的信息
    typenews = models.ManyToManyField('NewInfo')


class NewInfo(models.model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_created=True)
    content = models.TextField()

    # 定义关联属性。代表信息所属的类型
    # news_tpye = models.ManyToManyField('NewsType')

#  rm -rf .navicat64/

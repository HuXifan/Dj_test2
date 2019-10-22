from django.db import models


# Create your models here.
class BookInfoManager(models.Manager):
    # 继承自models.Manager  图书模型管理器类
    # self.model 获取self所在模型类的类名

    # 1 改变查询的结果集 .>>>重写all方法
    def all(self):
        # 1 调用父类all方法
        books = super().all()  # 返回查询集
        # 2 对数据进行过滤，调用filter过滤
        books = books.filter(isDelete=False)
        return books  # 3 返回

    # 封装函数：操作模型类对应的数据表(增删改查)
    def create_book(self, btitle, bpub_date):
        # 封装在模型类中，类方法classmethod
        model_class = self.model  # 使用self.model()就可以创建一个跟自定义管理器对应的模型类对象。
        book = model_class()
        # 1 创建一个图书对象
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2保存进数据库
        book.save()
        # 3 返回obj
        return book

    ''''''


# 一类
class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)  # CharField 必须指定max_length 否则报错
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)  # 阅读量，设置默认为0
    b_comment = models.IntegerField(default=0)  # 评论数
    isDelete = models.BooleanField(default=False)  # 设置逻辑删除,默认不删除/软删除标记
    # 自定义一个Manager对象
    # book = models.Manager()
    objects = BookInfoManager()  # 这里的objects对象是自己取得，非默认的objects
    '''>>> type(BookInfo.objects)
        <class 'booktest.models.BookInfoManager'>   '''

    # @classmethod
    # def create_book(cls, btitle, bpub_date):
    #     # 封装在模型类中，类方法classmethod
    #     # 1 创建一个图书对象
    #     obj = cls()
    #     obj.btitle = btitle
    #     obj.bpub_date = bpub_date
    #     # 2保存进数据库
    #     obj.save()
    #     # 3 返回obj
    #     return obj
    # '''有了这个方法，再添加数据只需要使用类名.类方法就可以'''

    class Meta:
        db_table = 'bookinfo'  # 指定模型类对应的表名


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=256)  # 备注
    # 两个类有一对多关系时，需要设置一个关系属性,在多的里面
    hbook = models.ForeignKey('BookInfo')
    isDelete = models.BooleanField(default=False)  # 设置逻辑删除,默认不删除/软删除标记


# 两个类有一对多的关系,类之间有一对一，一对多，多对多的关系
'''
class NewsType(models.Model):
    # 新闻类型类
    typename = models.CharField(max_length=128)
    # 关系类型代表下面的信息
    typenews = models.ManyToManyField('NewInfo')


class NewInfo(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_created=True)
    content = models.TextField()

    # 定义关联属性。代表信息所属的类型
    # news_tpye = models.ManyToManyField('NewsType')


# 员工基本信息类,一对一定义在任何一个就可以
class EmployeeBassicInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gneder = models.BooleanField(default=False)
    employee_detail = models.OneToOneField('EmployeeDetailInfo')


class EmployeeDetailInfo(models.Model):
    addr = models.CharField(max_length=128)
    tel = models.IntegerField(max_length=11)

    # 关系属性，代表员工基本信息
    # employee_bassic = models.OneToOneField('EmployeeBassicInfo')
'''


#  地域自关联 模型类
class AreaInfo(models.Model):
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True)

    # class Meta:
    #     db_table = 'areas'  # 指定模型类对应的表名

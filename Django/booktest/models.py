from django.db import models


class BookInfoManager(models.Manager):
    '''图书模型管理器类'''
    # 1.改变原有查询的结果集
    def all(self):
        # 1.调用父类的all方法，获取所有数据
        books = super().all() # QuerySet
        # 2.对books中的数据进行过滤
        books = books.filter(isDelete=False)
        # 返回books
        return books

    # 2.封装方法，操作模型类对应的数据表（增删改查)
    def create_book(self, btitle, bpub_date):
        '''添加一本图书'''
        # 1.创建一个图书对象
        # 获取self所在的模型类,self是模型管理器类，self.model可以获取对应模型类的类名
        model_class = self.model
        book = model_class()         # 等价于book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 2.添加进数据库
        book.save()
        # 3.返回book
        return book


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,unique=True)
    bpub_date = models.DateField(auto_now_add=True)
    # 价格,最大位数为10,小数为2
    # bprice = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    record_modify_time=models.DateTimeField(auto_now=True)

    objects=BookInfoManager()

    books=models.Manager()  #如果要所有的，不管是否进行了软删除

    def __str__(self):
        """
        重写改方法会改变对象的打印效果
        :return:
        """
        return self.btitle

    class Meta:
        db_table = 'bookinfo'  # 指定模型类对应表名

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20,db_index=True)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=100,null=True,blank=True)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE,db_constraint=False)
    # 删除标记
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.hname

# 下面内容是day76的

class NewsType(models.Model):
    """
    新闻类型类
    """
    # 类型名
    type_name = models.CharField(max_length=20)
    # 关系属性，代表类型下面的信息
    type_news = models.ManyToManyField('NewsInfo')

class NewsInfo(models.Model):
    """
    新闻类
    """
    # 新闻标题
    title = models.CharField(max_length=128)
    # 发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()

class EmployeeBasicInfo(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.IntegerField()
    # 关系属性,代表员工的详细信息
    #employee_detail = models.OneToOneField('EmployeeDetailInfo',on_delete=models.CASCADE,)

# 员工详细信息类
class EmployeeDetailInfo(models.Model):
    # 联系地址
    addr = models.CharField(max_length=256)
    # 教育经历
    # 关系属性，代表员工基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo',on_delete=models.CASCADE,)


class Areas(models.Model):
    '''地区模型类'''
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 关系属性，代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True,
                                on_delete=models.CASCADE,)
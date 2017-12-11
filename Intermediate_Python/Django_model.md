## Django--模型层(model)
- 对象关系映射(ORM)映射关系
	- 表名  <－－－－－－－> 类名
	- 字段  <－－－－－－－> 属性
	- 表记录 <－－－－－－－>类实例对象

### 创建表
#### 实例分析：
- 模型
	- 作者模型：一个作者有姓名和年龄。
	- 作者详细模型：把作者的详情放到详情表，包含生日，手机号，家庭住址等信息。
	- 版商模型：出版商有名称，所在城市以及email。
	- 书籍模型： 书籍有书名和出版日期
- 模型关系
	- 作者详情模型和作者模型之间是一对一的关系（one-to-one）
	- 作者和书籍的关系是多对多的关系(many-to-many)
	- 出版商和书籍是一对多的关系(one-to-many)
- 代码构建模型

	```python
	class Author(models.Model):
	    aid = models.AutoField(primary_key=True)
	    name=models.CharField(max_length=32)
	    age=models.IntegerField()
	 
	    # 与AuthorDetail建立一对一的关系
	    authorDetail=models.OneToOneField(to="AuthorDetail")
	 
	class AuthorDetail(models.Model):
	 
	    did = models.AutoField(primary_key=True)
	    birthday=models.DateField()
	    telephone=models.BigIntegerField()
	    addr=models.CharField(max_length=64)
	    
	class Publish(models.Model):
	    pid = models.AutoField(primary_key=True)
	    name=models.CharField(max_length=32)
	    city=models.CharField(max_length=32)
	    email=models.EmailField()
	 
	 
	class Book(models.Model):
	 
	    bid = models.AutoField(primary_key=True)
	    title = models.CharField(max_length=32)
	    publishDate=models.DateField()
	    price=models.DecimalField(max_digits=5,decimal_places=2)
	    keepNum=models.IntegerField()<br>    commentNum=models.IntegerField()
	 
	    # 与Publish建立一对多的关系,外键字段建立在多的一方
	    publish=models.ForeignKey(to="Publish",to_field="pid")
	 
	    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
	    authors=models.ManyToManyField(to='Author')　　
	```
	- 在logging可以查看翻译成的sql语句

	```python
	LOGGING = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'handlers': {
	        'console':{
	            'level':'DEBUG',
	            'class':'logging.StreamHandler',
	        },
	    },
	    'loggers': {
	        'django.db.backends': {
	            'handlers': ['console'],
	            'propagate': True,
	            'level':'DEBUG',
	        },
	    }
	}　　
	```

- 注意事项
	1. 表的名称myapp_modelName，是根据 模型中的元数据自动生成的，也可以覆写为别的名称　　
	2. id 字段是自动添加的
	3. 对于外键字段，Django 会在字段名上添加"_id" 来创建数据库中的列名
	4. 这个例子中的CREATE TABLE SQL 语句使用PostgreSQL 语法格式，要注意的是Django 会根据settings 中指定的数据库类型来使用相应的SQL 语句。
	5. 定义好模型之后，你需要告诉Django _使用_这些模型。你要做的就是修改配置文件中的INSTALL_APPSZ中设置，在其中添加models.py所在应用的名称。
	6. 外键字段 ForeignKey 有一个 null=True 的设置(它允许外键接受空值 NULL)，你可以赋给它空值 None 。

#### 字段类型
- IntegerField
	- 整数
- BigIntegerField
	- 大整数
- AutoField
	- 整数自增
- CharField
	- 字符串
- FloatField
	- 浮点数
- DecimalField
	- 小数
- BooleanField
	- 布尔值
- DateField
	- 日期


- Field
	- Base class for all field types
- BLANK_CHOICE_DASH
- BigAutoField
- BinaryField
- CommaSeparatedIntegerField
- DateTimeField
- DurationField
- EmailField
- Empty
- FieldDoesNotExist
- FilePathField
- GenericIPAddressField
- IPAddressField
- NOT_PROVIDED
- NullBooleanField
- PositiveIntegerField
- PositiveSmallIntegerField
- SlugField
- SmallIntegerField
- TextField
- TimeField
- URLField
	- URL
- UUIDField


#### 字段选项
- max_length=None
	- 最大长度
- primary_key=False
	- 主键
- auto_created=False
	- 是否自增
- unique=False
	- 唯一键
- default=NOT_PROVIDED
	- 默认值
- choices=None
	- 它是一个可迭代的结构(比如，列表或是元组)，由可迭代的二元组组成(比如[(A, B), (A, B) ...])，用来给这个字段提供选择项。
	- 如果设置了 choices ，默认表格样式就会显示选择框，而不是标准的文本框，而且这个选择框的选项就是 choices 中的元组。
	- 一般来说，最好在模型类内部定义choices，然后再给每个值定义一个合适名字的常量。

	```python
	user_types = (
	        (1, "员工"),
	        (2, "老板"),
	    )
    identity = models.IntegerField(choices=user_types)
	```

- verbose_name=None
	- 可读性更高的文字
- help_text=''
	- 额外的 ‘help' 文本将被显示在表单控件form中
	- 需要在help_text文本中添加html样式
- validators=()
	- 该字段将要运行的一个Validator 的列表
	- 验证器是一个可调用的对象，它接受一个值，并在不符合一些规则时抛出ValidationError异常
- null=False
	- 数据库是否允许为空
- blank=False
	- django自带的admin页面下修改表记录可以为空
	- 与null字段没有关系，即便设置了null=True，在使用admin插入数据时依然无法设置为空
- 当为外键，一对一关系时可以设置级联删除（on cascade delete）:
	- on_delete
	- 必须使用models.SET_NULL修改
	- 均默认为True


- db_index=False
- rel=None
- editable=True
- serialize=True
- unique_for_date=None
- unique_for_month=None
- unique_for_year=None
- db_column=None
- db_tablespace=None
- error_messages=None

### 添加表记录
- 普通字段
	- 方法1：

	```python
	publish_obj=Publish(name="人民出版社",city="北京",email="renMin@163.com"
	publish_obj.save() # 将数据保存到数据库
	```
	- 方法2：

	```python
	publish_obj=Publish.objects.create(name="人民出版社",city="北京",email="renMin@163.com")
	```
- 外键字段
	- 方法1：

	```python
	publish_obj=Publish.objects.get(nid=1)
	Book.objects.create(title="Django从入门到放弃", publishDate="2012-12-12", price=665, pageNum=334, publish=publish_obj)
	```

	- 方法2：

	```python
	book_obj=Book.objects.create(title="Django从入门到放弃",publishDate="2012-12-12",price=665,pageNum=334,publish_id=1)
	```
- 多对多字段
	- 建立联系

	```python
	book_obj=Book.objects.create(title="追风筝的人",publishDate="2012-11-12",price=69,pageNum=314,publish_id=1)
	 
	author_yuan=Author.objects.create(name="yuan",age=23,authorDetail_id=1)
	author_egon=Author.objects.create(name="egon",age=32,authorDetail_id=2)
	 
	book_obj.authors.add(author_egon,author_yuan)    #  将某个特定的 model 对象添加到被关联对象集合中。   =======    book_obj.authors.add(*[])
	 
	book_obj.authors.create()      #创建并保存一个新对象，然后将这个对象加被关联对象的集合中，然后返回这个新对象。
	```
	- 解除关系

	```python
	book_obj.authors.remove()     # 将某个特定的对象从被关联对象集合中去除。    ======   book_obj.authors.remove(*[])
	book_obj.authors.clear()       #清空被关联对象集合。
	```

#### class RelatedManager类关系管理器


### 删除表记录
- delete()
	- 该方法必须的对象必须是QuerySet，不能是对象
	- 默认级联删除（sql中的on casade delete）


### 查找表记录
#### 通用查询
- all()
	- 查询所有结果
	- 返回QuerySet，一个列表，元素是表记录（对象）
	- only(*args):只要对象指定的字段名
		- 但在额外取未指定的字段会重新发一次sql语句，耗时耗性能
	- defer(*args):不要指定的字段名
- filter(**kwargs)
	- 它包含了与所给筛选条件相匹配的对象
	- 返回QuerySet，一个列表，元素是表记录（对象）
- get(**kwargs)
	- 返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。
	- 返回与所给筛选条件相匹配的对象
- exclude(**kwargs)
	- 它包含了与所给筛选条件不匹配的对象
	- 返回QuerySet
- values(*field)
	- 使用对象必须是QuerySet
	- 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列model的实例化对象，元素是**字典**，键为values指定的field，值为表记录的值
- values_list(*field)
	- 使用对象必须是QuerySet
	- 它与values()非常相似，它返回的是一个**元组**序列，values返回的是一个字典序列
	- 元组元素为指定查询的字段的值
- order_by(*field)
	- 使用对象必须是QuerySet
	- 对查询结果排序
- reverse()
	- 使用对象必须是QuerySet	
	- 对查询结果反向排序
- distinct()
	- 使用对象必须是QuerySet
	- 从返回结果中剔除重复纪录
- count()
	- 返回数据库中匹配查询(QuerySet)的对象数量。
- first()
	- 返回第一条记录
	- 返回对象
- last()
	- 返回最后一条记录
	- 返回对象
- exists()
	- 如果QuerySet包含数据，就返回True，否则返回False

##### QuerySet数据类型的特性
- 可切片，可迭代，具有部分列表的性质————[obj,...]
- 惰性查询:
	- 当不使用QuerySet时，不会生成sql语句
	- 何为使用？
		- 对查询数据增删改查



#### 双下划线之单表查询
- __gt:大于
- __gte:大于等于
- __lt:小于
- __lte：小于等于
	- models.Tb1.objects.filter(id\_\_lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
- __in:
	- models.Tb1.objects.filter(id\_\_in=[11, 22, 33])   # 获取id等于11、22、33的数据
	- models.Tb1.objects.exclude(id\_\_in=[11, 22, 33])  # not in
- __range:指定范围
	- models.Tb1.objects.filter(id\_\_range=[1, 2])      # 范围bettwen and
- __contains:包含指定字符
	- models.Tb1.objects.filter(name\_\_contains="ven")
- __icontains：包含指定字符，不区分大小写
	- models.Tb1.objects.filter(name\_\_icontains="Ven") # icontains大小写不敏感 
- __startswith:以指定字符开头
- __istartswith:以指定字符开头，不区分大小写
- __endswith:以指定字符结尾
- __iendswith:以指定字符结尾，不区分大小写

- 日期查询
	- __year
	- __month
	- __day
	- __week_day

#### 跨表查询
##### 基于对象查询
- 一对多查询
	- 正向查询，字段
		- `models.`
	- 反向查询，表名_set
- 一对一
	- 正向查询，字段
	- 反向查询，表名
- 多对多
	- 正向查询，字段
	- 反向查询，表名_set

##### 基于双下划线查询
- 一对多查询
	- 正向查询，字段名__跨表字段名
		- 查询linux这本书的出版社名字
		- modles.Book.objects.filter(title="Linux").values("press__name")
	- 反向查询，表名__跨表字段名
		- 查询人民出版社出版的所有书的名字
		- modles.Press.objects.filter(name="人民出版社").values("book__tilte")
- 一对一查询
	- 正向查询，字段名__跨表字段名
		- models.Author.obects.filter(name="egon").values("authorInfo__tel")
	- 反向查询，表名__跨表字段名
		- models.AuthorInfo.objects.filter(tel="152").values("author__name")
- 多对多查询
	- 正向查询，字段名__跨表字段名
		- models.Book.objects.filter(title="python").vlaues("authors__name")
	- 反向查询，表名__跨表字段名
		- models.Author.objects.filter(name="alex").vlaues("book__price")

#### 聚合查询
- 对QuerySet对象调用，返回字典，默认所有数据为一组
- models.Book.objects.aggregate(Avg("price"))

#### 分组查询
- 对QuerySet对象调用，返回uerySet对象，对已分组的数据的每一组进行操作
- models.Book.objects.annotate(author_num=Count("authors"))


#### F查询和Q查询
- F查询
	- 可以将表的字段当作查询条件
	- 查询书籍字数大于阅读数的书籍
	- models.Book.objects.filter(word_num__lt=F(read_num))
- Q查询
	- 可以使用更加复杂的逻辑判断
	- 查询单价大于100或书名以A开头的书籍
	- models.Book.objects.filter(Q(price__lt=100)\|Q(title__startswith="A"))


[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/models)
[综合练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/CMS)


### 事物

```python
from django.db import transaction
with transaction.atomic():
    sql操作
```










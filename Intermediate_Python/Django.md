# Django

1. 安装Django
	- 'pip3 install django'
2. 创建django项目
	- 'django-admin startproject 项目名'
3. 创建一个应用
	- 'python manage.py startapp 应用名'
4. 运行django项目
	- 'python manage.py runserver [[ip:]port]'
	- 默认host：127.0.0.1:8000
5. 


Django使用的框架模型是MTV模型加控制，其中控制主要是URl的分发和映射。

<img src="http://chuann.cc/Intermediate_Python/MTV.png" width="500px">

- Django框架下的请求响应流程：
	1. 浏览器向服务器发出请求信息；
	2. 全局环境下的urls.py对请求信息中的URL处理，将URL中指定的路径分发至应用下的url处理文件或直接映射至应用下的视图函数；
	3. 视图函数接收请求数据，并根据请求数据做相应处理；
	4. 根据请求数据访问数据库，并提取数据；
	4. 将数据嵌入模板；
	5. 生成响应信息返回给浏览器。

## URL的分发和映射(urls.py)
结构：
```
urlpatterns = {
	url("^blog/", views.bolg)
}
```

- url(regex, view, kwargs=None, name=None)
	- 建立起URL与视图函数的映射关系
	- 正则表达式：匹配url中的路径
	- 视图函数：view
	- 别名name:正则匹配的路径的别名
- 注意
	- 出现覆盖URL，只匹配第一个视图函数
	- 无名分组
		- 正则表达式中使用分组^blog/(\d{4})/(\d{2})
		- 将匹配到的分组数据按位置传参给视图函数
	- 有名分组
		- 正则表达式中使用命名分组^blog/(?P<year>\d{4})/(?P<month>\d{2})
		- 将匹配到的分组数据按关键字传参给视图函数
	- URL分发
		- url(r'^blog/', include('blog.urls'))
		- urls为blog应用文件夹下的urls.py
	- 反向查询
		- 在模板中使用<code>{\% url "别名" \%}</code>，表示此处为指定别名代表的路径
		- 当修改路径时可以自动同步

[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/URLconf)


- 周一：
	- 视图函数
	- 模板一
- 周二：
	- 模板二
- 周三：
	- models一
- 周四：
	- models二
- 周五：
	- models三，cookie&session
- 大作业
	- 图书管理系统(CMS,Content Management System)
	- 前端修改数据，同步后台数据库

## 视图函数
- request--->请求信息
	- request.GET:GET请求的数据，字典
	- request.POST:POST请求的数据，字典
		- request.POST.getlist(""): 获取具有多个值的表单，列表
	- request.method:请求方式，GET or POST，字符串
	- request.path:URL的路径，字符串
	- request.get_full_path():路径加之后的请求数据（GET请求才有）
- Httpresponse--->响应字符串
	- render(request, template_name, context=None, content_type=None, status=None, using=None)
		- request：用于生成响应的请求对象
		- template_name: 模板下的文件名
		- context: 模板中需要替换的内容
		- context_type: 生成文档要使用的MIME类型，默认为DEFAULT_CONTENT设置的值
		- status：响应的状态码
		- 将模版组合完毕后给浏览器返回一个响应，响应信息是一个大字符串
	- redirect(to, *args, **kwargs)
		- to: 指定URL路径，"/profile"
		- 根据to指定的URl路径，重新走一次服务器的URL请求，返回重走视图函数的响应过程
	- 对比：
		- render：只是返回页面内容，但是未发送第二次请求
		- redirect：服务器会让浏览器重新发送一次请求，URL地址为重定向的地址

[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/views)


## 模板(templates)
- 什么是模板？
	- 模板：html+模板语法
	- 模版包括在使用时会被值替换掉**变量**，和控制模版逻辑的**标签**。

```python
def current_time(req):
    # ================================原始的视图函数
    # import datetime
    # now=datetime.datetime.now()
    # html="<html><body>现在时刻：<h1>%s.</h1></body></html>" %now

    # ================================django模板修改的视图函数
    # from django.template import Template,Context
    # now=datetime.datetime.now()
    # t=Template('<html><body>现在时刻是:<h1>{{current_date}}</h1></body></html>')
    # #t=get_template('current_datetime.html')
    # c=Context({'current_date':str(now)})
    # html=t.render(c)
    #
    # return HttpResponse(html)

    # 另一种写法(推荐)
    import datetime
    now=datetime.datetime.now()
    return render(req, 'current_datetime.html', {'current_date':str(now)[:19]})
```

### 变量
格式：{{ 变量名 }}

- 深度查询：使用句点符

	```
	python变量
	i = 100
	l = [11,22,33]
	d={"name":"chuck","age":20}
	
	模板语法
	<h1>Hello {{ name }}</h1>
	<h1>{{ i }}</h1>
	<h1>{{ l }}</h1>
	<h1>{{ l.1 }}</h1>
	<h1>{{ d }}</h1>
	<h1>{{ d.age }}</h1>
	```

#### 过滤器filter
类似内置函数的功能
- 语法：{{obj|filter__name:param}}
- default：如果一个变量是false或者为空，使用给定的默认值。否则，使用变量的值。
	- <code>{{ value|default:"nothing" }}</code>
- length:返回值的长度。它对字符串和列表都起作用。
	- <code>{{ value|length }}</code>
	- 如果 value 是 ['a', 'b', 'c', 'd']，那么输出是 4。
- filesizeformat:将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等）。
	- <code>{{ value|filesizeformat }}</code>
	- 如果 value 是 123456789，输出将会是 117.7 MB。　
- date:value需要是时间对象，如datetime.datetime.now()
	- <code>{{ value|date:"Y-m-d" }}</code>
- slice:顾头不顾尾，对序列进行切片
	- <code>{{ value|slice:"2:-1" }}</code>
- truncatechars:如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。
	- <code>{{ value|truncatechars:9 }}</code>
- safe:Django的模板中为了安全会对HTML标签和JS等语法标签进行自动转义，
	- 但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，如果自动转义的话显示的就是保护HTML标签的源文件。
	- 在Django中关闭HTML的自动转义可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义。
	- <code>{{ value|safe}}</code>

:blush:
### 标签
标签看起来像是这样的： {\% tag \%}。标签比变量更加复杂：一些在输出中创建文本，一些通过循环或逻辑来控制流程，一些加载其后的变量将使用到的额外信息到模版中。         
一些标签需要开始和结束标签 （例如{\% tag \%} ...标签 内容 ... {\% endtag \%}）。
- for标签:遍历每一个元素

	```template
	{% for person in person_list %}
	    <p>{{ person.name }}</p>
	{% endfor %}
	```
	- 可以利用<code>{\% for obj in list reversed \%}</code>反向完成循环。

	```template
	{% for key,val in dic.items %}
	    <p>{{ key }}:{{ val }}</p>
	{% endfor %}
	```
	- 循环序号可以通过{{forloop}}显示

	```
	forloop.counter         The current iteration of the loop (1-indexed)
	forloop.counter0    	The current iteration of the loop (0-indexed)
	forloop.revcounter  	The number of iterations from the end of the loop (1-indexed)
	forloop.revcounter0 	The number of iterations from the end of the loop (0-indexed)
	forloop.first           True if this is the first time through the loop
	forloop.last            True if this is the last time through the loop
	```
- for ... empty:for 标签带有一个可选的{\% empty \%} 从句，以便在给出的组是空的或者没有被找到时，可以有所操作。

	```template
	{% for person in person_list %}
	    <p>{{ person.name }}</p>
	
	{% empty %}
	    <p>sorry,no person here</p>
	{% endfor %}
	```

- if 标签:{\% if \%}会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出。

	```template
	{% if num > 100 or num < 0 %}
	    <p>无效</p>
	{% elif num > 80 and num < 100 %}
	    <p>优秀</p>
	{% else %}
	    <p>凑活吧</p>
	{% endif %}
	```
- with:使用一个简单地名字缓存一个复杂的变量，当你需要使用一个“昂贵的”方法（比如访问数据库）很多次的时候是非常有用的

	```template
	{% with total=business.employees.count %}
	    {{ total }} employee{{ total|pluralize }}
	{% endwith %}
	```

- csrf_token:这个标签用于跨站请求伪造保护
```.+({%).+(%}).+```


### 自定义标签和过滤器
1. 在settings中的INSTALLED_APPS配置当前app，不然django无法找到自定义的simple_tag.
2. 在app中创建templatetags模块(模块名只能是templatetags)
3. 创建任意 .py 文件，如：my_tags.py

	```python
	from django import template
	from django.utils.safestring import mark_safe
	 
	register = template.Library()   #register的名字是固定的,不可改变
	 
	 
	@register.filter
	def filter_multi(v1,v2):
	    return  v1 * v2
	
	@register.simple_tag
	def simple_tag_multi(v1,v2):
	    return  v1 * v2
	
	@register.simple_tag
	def my_input(id,arg):
	    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
	    return mark_safe(result)
	```
4. 在使用自定义simple_tag和filter的html文件中导入之前创建的 my_tags.py
	- <code>{\% load my_tags \%}　</code>
5. 使用simple_tag和filter（如何调用）

	```template
	-------------------------------.html
	{% load xxx %}  
	      
	# num=12
	{{ num|filter_multi:2 }} #24
	 
	{{ num|filter_multi:"[22,333,4444]" }}
	 
	{% simple_tag_multi 2 5 %}  参数不限,但不能放在if for语句中
	{% simple_tag_multi num 5 %}
	```
- 注意：filter可以用在if等语句后，simple_tag不可以

### 模板继承
模板继承将模板分为两种
- 基模板:block 标签定义的元素可在衍生模板中修改
- 衍生模板：extends 指令声明这个模板衍生自 base.html。在 extends 指令之后，基模板中的 block块被重新定义，模板引擎会将其插入适当的位置。在基模板中其内容不是空的block，需要使用 super() 获取原来的内容。     

通过从下面这个base.html开始：

```template
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="style.css" />
    <title>{% block title %}My amazing site{% endblock %}</title>
</head>

<body>
    <div id="sidebar">
        {% block sidebar %}
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/blog/">Blog</a></li>
        </ul>
        {% endblock %}
    </div>

    <div id="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

	- <code></code>
	- <code></code>
	- 











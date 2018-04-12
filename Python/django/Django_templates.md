## Django--模板(templates)
{% raw %}
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


### 标签
标签看起来像是这样的： {% tag %}。标签比变量更加复杂：一些在输出中创建文本，一些通过循环或逻辑来控制流程，一些加载其后的变量将使用到的额外信息到模版中。         
一些标签需要开始和结束标签 （例如{% tag %} ...标签 内容 ... {% endtag %}）。
- for标签:遍历每一个元素

	```template
	{% for person in person_list %}
	    <p>{{ person.name }}</p>
	{% endfor %}
	```
	- 可以利用<code>{% for obj in list reversed %}</code>反向完成循环。

	```template
	{% for key,val in dic.items %}
	    <p>{{ key }}:{{ val }}</p>
	{% endfor %}
	```
	- 循环序号可以通过｛｛forloop｝｝显示

	```
	forloop.counter         The current iteration of the loop (1-indexed)
	forloop.counter0    	The current iteration of the loop (0-indexed)
	forloop.revcounter  	The number of iterations from the end of the loop (1-indexed)
	forloop.revcounter0 	The number of iterations from the end of the loop (0-indexed)
	forloop.first           True if this is the first time through the loop
	forloop.last            True if this is the last time through the loop
	```
- for ... empty:for 标签带有一个可选的{% empty %} 从句，以便在给出的组是空的或者没有被找到时，可以有所操作。

	```template
	{% for person in person_list %}
	    <p>{{ person.name }}</p>
	
	{% empty %}
	    <p>sorry,no person here</p>
	{% endfor %}
	```

- if 标签:{% if %}会对一个变量求值，如果它的值是“True”（存在、不为空、且不是boolean类型的false值），对应的内容块会输出。

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
	- <code>{% load my_tags %}　</code>
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

- 基模板base.html：

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

- 子模版：

	```template
	{% extends "base.html" %}
	 
	{% block title %}My amazing blog{% endblock %}
	 
	{% block content %}
	{% for entry in blog_entries %}
	    <h2>{{ entry.title }}</h2>
	    <p>{{ entry.body }}</p>
	{% endfor %}
	{% endblock %}
	```
	- 效果

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <link rel="stylesheet" href="style.css" />
	    <title>My amazing blog</title>
	</head>
	 
	<body>
	    <div id="sidebar">
	        <ul>
	            <li><a href="/">Home</a></li>
	            <li><a href="/blog/">Blog</a></li>
	        </ul>
	    </div>
	 
	    <div id="content">
	        <h2>Entry one</h2>
	        <p>This is my first entry.</p>
	 
	        <h2>Entry two</h2>
	        <p>This is my second entry.</p>
	    </div>
	</body>
	</html>
	```
	
	- 使用{{ block.super }}继承父block的内容



- 注意事项
	- 如果你在模版中使用 {% extends %} 标签，它必须是模版中的第一个标签。其他的任何情况下，模版继承都将无法工作。
	- 在base模版中设置越多的 {% block %} 标签越好。请记住，子模版不必定义全部父模版中的blocks，所以，你可以在大多数blocks中填充合理的默认内容，然后，只定义你需要的那一个。多一点钩子总比少一点好。
	- 如果你发现你自己在大量的模版中复制内容，那可能意味着你应该把内容移动到父模版中的一个 {% block %} 中。
	- 使用{{ block.super }} 继承父模板的内容
	- 为了更好的可读性，你也可以给你的 {% endblock %} 标签一个名字 

	```
	{% block content %}
	...
	{% endblock content %}　　
	```
{% endraw %}
[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/templatePro)

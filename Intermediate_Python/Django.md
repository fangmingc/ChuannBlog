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

- url(正则表达式, 视图函数)
	- 建立起URL与视图函数的映射关系
	- 正则表达式：匹配url中的路径
	- 视图函数
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
	- render(request, template_name[, context])
		- template_name: 模板下的文件名
		- context: 模板中需要替换的内容
		- 将模版组合完毕后给浏览器返回一个响应，响应信息是一个大字符串
	- redirect(to, *args, **kwargs)
		- to: 指定URL路径，"/profile"
		- 根据to指定的URl路径，重新走一次服务器的URL请求，返回重走视图函数的响应过程
	- 对比：
		- render：只是返回页面内容，但是未发送第二次请求
		- redirect：服务器内部发送了第二次请求，浏览器url更新


[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/views)













# Django

- [URl的分发和映射](Django_URLconf.md)
- [views视图函数](Django_views.md)
- [template模板](https://github.com/fangmingc/Python/tree/master/Frame/Django/Django_templates.md)
- [model](Django_model.md)


1. 安装Django
	- 'pip3 install django'
2. 创建django项目
	- 'django-admin startproject 项目名'
3. 创建一个应用
	- 'python manage.py startapp 应用名'
4. 运行django项目
	- 'python manage.py runserver [[ip:]port]'
	- 默认host：127.0.0.1:8000


Django使用的框架模型是MTV模型加控制，其中控制主要是URl的分发和映射。

<img src="http://chuann.cc/Intermediate_Python/MTV.png" width="500px">

- Django框架下的请求响应流程：
	1. 浏览器向服务器发出请求信息；
	2. 全局环境下的urls.py对请求信息中的URL处理，将URL中指定的路径分发至应用下的url处理文件或直接映射至应用下的视图函数；
	3. 视图函数接收请求数据，并根据请求数据做相应处理；
	4. 根据请求数据访问数据库，并提取数据；
	4. 将数据嵌入模板；
	5. 生成响应信息返回给浏览器。


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


python manage.py makemigrations
python manage.py migrate


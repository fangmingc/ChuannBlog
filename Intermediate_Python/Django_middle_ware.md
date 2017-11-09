## Django中间件

### 什么是中间件
- 中间件是一个钩子框架，介于wsgi协议和Django路由系统之间。它是一个轻量级、底层的“插件”系统，用于在全局批量处理django的请求和响应。
- 每个中间件组件负责完成某个特定的功能。比如django.contrib.sessions.middleware.SessionMiddleware负责给每个请求加上session属性，方便后续的操作

<img src="http://chuann.cc/Intermediate_Python/middleware.png" width="500px">

### 能做什么
- 日志记录
- session
- csrf
- 用户登录
- 权限管理


### 使用
#### 编写中间件
- 位置可以是django项目的任何位置
- 必须继承MiddlewareMixin类(1.10.x之后)，1.4.x-1.9.x只需要继承object类
	- 继承方法一：导入后使用from django.utils.deprecation import MiddlewareMixin
	- 继承方法二：在自定义中间件文件中重写一遍
		- 快速重写：找到设置文件中的任意一个默认中间件，导入该中间件，去该中间件源码的类继承中粘贴复制

	```python
	class MiddlewareMixin(object):
	    def __init__(self, get_response=None):
	        self.get_response = get_response
	        super(MiddlewareMixin, self).__init__()
	
	    def __call__(self, request):
	        response = None
	        if hasattr(self, 'process_request'):
	            response = self.process_request(request)
	        if not response:
	            response = self.get_response(request)
	        if hasattr(self, 'process_response'):
	            response = self.process_response(request, response)
	        return response
	```

- 中间件方法
	- process_request(self, request)
		- 接收来自wsgi的请求需要执行的方法
		- 返回None表示允许通过
	- process_response(self, request, response)
		- 接收来自视图函数的响应需要执行的方法
		- 必须返回response
	- 这两个必须有其中一个

	```python
	class M1(MiddlewareMixin):
	
	    def process_request(self, request):
	        print("M1 process_request")
	
	    def process_response(self, request, response):
	        print("M1 process_response")
	
	        return response
	
	
	class M2(MiddlewareMixin):
	    def process_request(self, request):
	        print("M2 process_request")
	
	    def process_response(self, request, response):
	        print("M2 process_response")
	
	        return response
	```


#### 配置
- 将写好的中间件的路径配置到settings.py的MIDDLEWARE
- 路径必须正确

	```python
	MIDDLEWARE = [
	    'django.middleware.security.SecurityMiddleware',
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	    'manager.my_middle_ware.M1',
	    'manager.my_middle_ware.M2',
	]
	```
- MIDDLEWARE的顺序极其重要，不可随意更改
	- 如django.contrib.sessions.middleware.SessionMiddleware给request增加session属性，如果我们自定义了中间使用了session，就不可以放在SessionMiddleware之前


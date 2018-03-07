## django缓存
- django默认使用内存缓存，原生支持memcache

- [缓存粒度与实现](#2)
- [缓存配置](#2)

### <span id="1">缓存粒度与实现</span>
- 准备数据
	- 视图

	```python
	import time
	
	def index(request):
	
	   t=time.time()      #获取当前时间
	
	   return render(request,"index.html",{"t":t})
	```
	- 模板

	```
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	
	<h3 style="color: red">当前时间:-----{{ t }}</h3>
	
	</body>
	</html>
	```
	- 这是未使用缓存的情况，不停刷新页面，时间也在不停更新

#### 全站缓存
- 利用Django的中间件
	- 用户的请求通过中间件,经过一系列的认证等操作,如果请求的内容在缓存中存在,则使用FetchFromCacheMiddleware获取内容并返回给用户
	- 当返回给用户之前,判断缓存中是否已经存在,如果不存在,则UpdateCacheMiddleware会将缓存保存至Django的缓存之中,以实现全站缓存
	- 配置文件
		- UpdateCacheMiddleware必须在第一位
		- FetchFromCacheMiddleware必须在最后一位

	```python
	MIDDLEWARE_CLASSES = (
	    'django.middleware.cache.UpdateCacheMiddleware',     # 在响应HttpResponse中设置几个headers
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	    'django.middleware.security.SecurityMiddleware',
	    'django.middleware.cache.FetchFromCacheMiddleware',   # 用来缓存通过GET和HEAD方法获取的状态码为200的响应
	)
	
	CACHE_MIDDLEWARE_SECONDS=10		# 设置缓存超时时间
	```
	- 视图函数

	```python
	import time
	
	def index(request):
	
	     t=time.time()      # 获取当前时间
	     return render(request,"index.html",{"t":t})
	
	def foo(request):
	    t=time.time()       # 获取当前时间
	    return HttpResponse("HELLO:"+str(t))
	```

#### 视图缓存
- 使用特定装饰器
- 视图函数

	```python
	import time
	from django.views.decorators.cache import cache_page
	
	@cache_page(15)          #超时时间为15秒
	def index(request):
	
	     t=time.time()      #获取当前时间
	     return render(request,"index.html",{"t":t})
	
	def foo(request):
	    t=time.time()      #获取当前时间
	    return HttpResponse("HELLO:"+str(t))
	```
- 模板不变


#### 局部视图缓存
- 页面部分实现缓存
- 视图函数
	```python
	import time
	
	def index(request):
	
	     t=time.time()      # 获取当前时间
	     return render(request,"index.html",{"t":t})
	
	def foo(request):
	    t=time.time()       # 获取当前时间
	    return HttpResponse("HELLO:"+str(t))
	```
- 模板

	```html
	{&#37; load cache &#37;}
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	 <h3 style="color: green">不缓存:-----{{ t }}</h3>
	<!-- 设置超时时间-->
	{&#37; cache 2 'name' &#37;}	
	 <h3>缓存:-----:{{ t }}</h3>
	{&#37; endcache &#37;}
	
	</body>
	</html> 
	```
### <span id="2">缓存配置</span>
1. 虚拟缓存,开发调试模式,实际上不缓存数据，上线后直接更改引擎即可

	```python
	CACHES = {
	    'default': {
		    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',  # 缓存后台使用的引擎
		    'TIMEOUT': 300,            # 缓存超时时间（默认300秒，None表示永不过期，0表示立即过期）
		    'OPTIONS':{
		        'MAX_ENTRIES': 300,           # 最大缓存记录的数量（默认300）
		        'CULL_FREQUENCY': 3,          # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
		  },
	 }
	}
	```
2. 内存缓存(将缓存内容保存至内存区域中)，默认使用内存缓存，即使不配置

	```python
	CACHES = {
	    'default': {
		    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 指定缓存使用的引擎
		    'LOCATION': 'unique-snowflake',         # 写在内存中的变量的唯一值 
		 }
	}
	```
3. memcached

	```python
	# 'django.core.cache.backends.memcached.MemcachedCache'
	# 'django.core.cache.backends.memcached.PyLibMCCache'
	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	        'LOCATION': [
	            '172.19.26.240:11211',   #服务器1
	            '172.19.26.242:11211',   #服务器2
	        ]
		# 'LOCATION': 'unix:/tmp/memcached.sock',   #unix的socket的方式
	    }
	}
	```
4. 数据库缓存，默认使用数据库配置的数据库
	- 生成数据库表命令:`python manage.py createcachetable my_cache_table`

	```python
	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
	        'LOCATION': 'my_cache_table',
	    }
	```
5. 文件系统缓存
	- 注意是绝对位置（从根目录开始），必须保证服务器对你列出的路径具有读写权限

	```python
	CACHES = {
	    'default': {
	        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
	        'LOCATION': '/var/tmp/django_cache', # 这个是文件夹的路径
	        #'LOCATION': 'c:\foo\bar',#windows下的示例
	    }
	}
	```



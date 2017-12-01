## Django--视图函数
- 视图函数
	- Django项目的核心，绝大部分请求和响应都是在这里完成
	- 项目的业务逻辑就写在这里
	- 分类
		- FBV:函数视图
		- CBV:类视图
- 流程
	- 接收路由系统分发过来的请求数据
	- 使用ORM获取数据
		- 连上数据库读取数据
		- 转换为ORM对象返回
	- python语法处理数据
	- 模板语法渲染模板Templates
	- 生成响应字符串
	- 返回给wsgi

### 请求与响应

#### 请求request
##### request的属性
- request.method
	- 请求方式，GET or POST，字符串
- request.GET
	- GET请求的数据，字典
	- POST请求也可以通过GET发送数据
- request.POST
	- POST请求的数据，字典
	- reqeust.POST.get("xxx")：按照key-value获取对应值
	- request.POST.getlist("xxx"): 获取具有多个值的表单，列表
- request.path/reqeust.path_info
	- URL的路径，字符串
- reqeust.COOKIES
	- cookies,字典
- reqeust.session
	- session，字典
	- 由django.contrib.sessions.middleware.SessionMiddleware中间件添加
	- reqeust.user
		- django自带的用户认证系统的对象
		- 当未使用django自带的用户认证系统，返回值是AnonymousUser，匿名用户
		- 当使用django自带的用户认证系统，返回值是当前用户的用户名
- reqeust.body
	- 获取请求体
	- 无法被django自带的解析语法解析的
- request.FILES
	- 接收的文件
- request.user
	- 一个 AUTH_USER_MODEL 类型的对象，表示当前登录的用户。
	- 如果用户当前没有登录，user 将设置为 django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。
- request.META
	- 一个标准的Python 字典，包含所有的HTTP 首部。具体的头部信息取决于客户端和服务器，下面是一些示例：
		- CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
		- CONTENT_TYPE —— 请求的正文的MIME 类型。
		- HTTP_ACCEPT —— 响应可接收的Content-Type。
		- HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
		- HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。
		- HTTP_HOST —— 客服端发送的HTTP Host 头部。
		- HTTP_REFERER —— Referring 页面。
		- HTTP_USER_AGENT —— 客户端的user-agent 字符串。
		- QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。
		- REMOTE_ADDR —— 客户端的IP 地址。
		- REMOTE_HOST —— 客户端的主机名。
		- REMOTE_USER —— 服务器认证后的用户。
		- REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。
		- SERVER_NAME —— 服务器的主机名。
		- SERVER_PORT —— 服务器的端口（是一个字符串）。
	- 从上面可以看到，除 CONTENT_LENGTH 和 CONTENT_TYPE 之外，请求中的任何 HTTP 首部转换为 META 的键时，都会将所有字母大写并将连接符替换为下划线最后加上 HTTP_  前缀。所以，一个叫做 X-Bender 的头部将转换成 META 中的 HTTP_X_BENDER 键。

##### request的方法
- request.get_host()
	- 获取端口号
- request.get_full_path()
	- 路径加之后的请求数据
- HttpRequest.is_secure()
	- 如果请求时是安全的，则返回True；即请求通是过 HTTPS 发起的。
- HttpRequest.is_ajax()
	- 如果请求是通过XMLHttpRequest 发起的，则返回True，方法是检查 HTTP_X_REQUESTED_WITH 相应的首部是否是字符串'XMLHttpRequest'。
	- 大部分现代的 JavaScript 库都会发送这个头部。如果你编写自己的 XMLHttpRequest 调用（在浏览器端），你必须手工设置这个值来让 is_ajax() 可以工作。
	- 如果一个响应需要根据请求是否是通过AJAX 发起的，并且你正在使用某种形式的缓存例如Django 的 cache middleware，你应该使用 vary_on_headers('HTTP_X_REQUESTED_WITH') 装饰你的视图以让响应能够正确地缓存。


#### 响应
- HttpResponse
	- 只接受字符串
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

### 反向解析

```python
return redirct("/idnex/")

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

return HttpResponseRedirect(reverse('index'))
```



### CBV视图
- 路由分发
	- `url(r'^login_cbv/$', views.Login.as_view())`
- 视图函数

	```python
	from django.views import View
	
	
	class Login(View):
	    
	    def get(self, request):
	        
	        return render(request, "login_cbv.html")
	    
	    def post(self, request):
	        
	        return HttpResponse("cbv_OK")
	```












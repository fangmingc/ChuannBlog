## Django--视图函数
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
## 上下文管理
- 上下文原理

	```python
	# context locals
	_request_ctx_stack = LocalStack()
	_app_ctx_stack = LocalStack()
	current_app = LocalProxy(_find_app)
	request = LocalProxy(partial(_lookup_req_object, 'request'))
	session = LocalProxy(partial(_lookup_req_object, 'session'))
	g = LocalProxy(partial(_lookup_app_object, 'g'))
	```

1. 创建Local类

	```
	{
		线程或协程唯一标识：{'stack': []},
		线程或协程唯一标识：{'stack': []},
		...
	}
	```

2. 流程
	- 当请求进来之后
		- 将请求相关数据封装到RequestContext(self, environ)对象
		- 请求相关数据通过stack添加到local
	- 以后使用时，谁使用谁就通过stack读取local的数据
	- 请求完成之后，将request从列表中移除

3. 关系
	- local对象专门用于存数据
	- stack对象专门负责数据的存、取、删除

4. 数据混淆问题
	- 单线程
	- 多线程
	- 协程
	- 全部由local中实现的get_ident获取的唯一ID标识

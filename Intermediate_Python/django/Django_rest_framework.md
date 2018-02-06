## django_rest_framework

### 预热：基于Django做API
- 视图
	- FBV
	
		```python
		from django.shortcuts import render
		from django.http import JsonResponse, HttpResponse
		
		
		def users(request):
		
		    response = {"code": 1000, "data": None}
		
		    response["data"] = [
		        {"name": "egon", "age": 18},
		        {"name": "wusir", "age": 28},
		        {"name": "yuan", "age": 20}
		    ]
		
		    return JsonResponse(response)
		
		
		def user(request, pk):
		    if request.method == "GET":
		        return JsonResponse({"code": 1000, "data": []})
		    elif request.method == "POST":
		        return HttpResponse("q")
		```
	- CBV
	
		```python
		from django.shortcuts import render
		from django.http import JsonResponse, HttpResponse
		from django.views import View
		
		
		class UsersView(View):
		    def get(self, request):
		
		        response = {"code": 1000, "data": None}
		
		        response["data"] = [
		            {"name": "egon", "age": 18},
		            {"name": "wusir", "age": 28},
		            {"name": "yuan", "age": 20}
		        ]
		
		        return JsonResponse(response)
		
		
		class UserView(View):
		    """
		    单个用户资源
		    """
		
		    def dispatch(self, request, *args, **kwargs):
		
		        # return HttpResponse("asdasd")
		
		        # method = request.method.lower()
		        # func = getattr(self, method)
		        # return func(self, request, *args, **kwargs)
		
		        print("before")
		        response = super(UserView, self).dispatch(request, *args, **kwargs)
		        print("after")
		        return response
		
		    def get(self, request, pk):
		        print(request)
		        return JsonResponse({"code": 1000, "data": []})
		
		    def post(self, request, pk):
		        return HttpResponse("q")
		```
- URL

	```
	urlpatterns = [
	    url(r'^users/', FBV.users),
	    url(r'^user/(\d+)/', FBV.user),
	
	    url(r'^users/', CBV.UsersView.as_view()),
	    url(r'^user/(\d+)/', CBV.UserView.as_view()),
	
	]
	```

### 主要内容
- 安装
	- `pip3 install dajngo-rest-framework`

#### 源码流程
- 路由系统中
	- `APIView.as_view()`
		- `view = super(APIView, cls).as_view(**initkwargs)`
			- 继承自Django的CBV视图类

				```python
				def view(request, *args, **kwargs):
				    self = cls(**initkwargs)
				    if hasattr(self, 'get') and not hasattr(self, 'head'):
				        self.head = self.get
				    self.request = request
				    self.args = args
				    self.kwargs = kwargs
				    return self.dispatch(request, *args, **kwargs)
				```
		- `csrf_exempt(view)`
			- 装饰器，取消Django的CSRF认证
- 请求到来
	1. `self.dispatch(request, *args, **kwargs)`

		```python
		def dispatch(self, request, *args, **kwargs):
		    """
		    `.dispatch()` is pretty much the same as Django's regular dispatch,
		    but with extra hooks for startup, finalize, and exception handling.
		    """
		    self.args = args
		    self.kwargs = kwargs
		
		    # TODO: 1. 对reqeust加工
		    request = self.initialize_request(request, *args, **kwargs)
		    self.request = request
		    self.headers = self.default_response_headers  # deprecate?
		
		    try:
		        # TODO: 2. 对请求进行处理
		        self.initial(request, *args, **kwargs)
		
		        # 根据请求方式执行相应的视图函数
		        if request.method.lower() in self.http_method_names:
		            handler = getattr(self, request.method.lower(),
		                              self.http_method_not_allowed)
		        else:
		            handler = self.http_method_not_allowed
		
		        response = handler(request, *args, **kwargs)
		
		    except Exception as exc:
		        response = self.handle_exception(exc)
		    # TODO: 3. 对响应进一步处理
		    self.response = self.finalize_response(request, response, *args, **kwargs)
		    return self.response
		```
	2. `self.initialize_request(request, *args, **kwargs)`
	 
		```
		def initialize_request(self, request, *args, **kwargs):
		    """
		    Returns the initial request object.
		    """
		    # 字典
		    #     {
		    #       'view': self,
		    #       'args': getattr(self, 'args', ()),
		    #       'kwargs': getattr(self, 'kwargs', {})
		    #    }
		    parser_context = self.get_parser_context(request)
		
		    return Request(
		        request,
		        # TODO: 1.1 获取解析请求的类，eg:JSON格式的，Form格式的。。。
		        parsers=self.get_parsers(),
		        # TODO: 1.2 获取认证相关的类并实例化后传入request对象
		        authenticators=self.get_authenticators(),
		        negotiator=self.get_content_negotiator(),
		        parser_context=parser_context
		    )
		```
	3. `self.initial(request, *args, **kwargs)`

		```python
		def initial(self, request, *args, **kwargs):
		    """
		    Runs anything that needs to occur prior to calling the method handler.
		    """
		    self.format_kwarg = self.get_format_suffix(**kwargs)
		
		    # Perform content negotiation and store the accepted info on the request
		    neg = self.perform_content_negotiation(request)
		    request.accepted_renderer, request.accepted_media_type = neg
		
		    # TODO: 2.1 版本处理
		    # Determine the API version, if versioning is in use.
		    version, scheme = self.determine_version(request, *args, **kwargs)
		    request.version, request.versioning_scheme = version, scheme
		
		    # Ensure that the incoming request is permitted
		    # TODO: 2.2 认证
		    self.perform_authentication(request)
		    # TODO: 2.3 权限
		    self.check_permissions(request)
		    # TODO: 2.4 限制访问频率
		    self.check_throttles(request)
		```
		- `self.perform_authentication(request)`
			- 函数内执行了`request.user`

				```python
				@property
				def user(self):
				    """
				    Returns the user associated with the current request, as authenticated
				    by the authentication classes provided to the request.
				    """
				    if not hasattr(self, '_user'):
				        with wrap_attributeerrors():
				            self._authenticate()
				    return self._user
				```
			- `self._authenticate()`

				```python
				def _authenticate(self):
				    """
				    Attempt to authenticate the request using each authentication instance
				    in turn.
				    """
				    # 循环认证对象列表
				    for authenticator in self.authenticators:
				        try:
				            # 执行每个对象的authenticate
				            user_auth_tuple = authenticator.authenticate(self)
				        except exceptions.APIException:
				            self._not_authenticated()
				            raise
				
				        if user_auth_tuple is not None:
				            self._authenticator = authenticator
				            self.user, self.auth = user_auth_tuple
				            return
				
				    self._not_authenticated()
				```

		- `self.check_permissions(request)`
		- `self.check_throttles(request)`

#### 认证


#### 权限


#### 限流





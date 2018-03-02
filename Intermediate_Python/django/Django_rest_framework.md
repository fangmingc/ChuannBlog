## django_rest_framework
- [介绍](#0)
- [预热](#1)
- [主要内容](#2)
	- [源码流程](#201)
	- [认证](#202)
	- [权限](#203)
	- [限流](#204)
	- [版本](#205)
	- [解析器(paser)](#206)
	- [序列化](#207)
	- [分页](#208)
	- [视图](#209)
	- [路由](#210)
	- [渲染器](211)

### <span id="0">介绍</span>
- restframework是否必需？
	- 不是必需的，基于django也可以做，参考[预热](#1)
- 使用优点
	- 设计很规范、全面，减少重复代码
		- 可以单视图或者全局配置，和django的中间件的配置一样
			- importlib的import_module+反射实现的
			- 动态配置可扩展，CRM的短信、邮件、微信的提醒


### <span id="1">预热：基于Django做API</span>
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

	```python
	urlpatterns = [
	    url(r'^users/', FBV.users),
	    url(r'^user/(\d+)/', FBV.user),
	
	    url(r'^users/', CBV.UsersView.as_view()),
	    url(r'^user/(\d+)/', CBV.UserView.as_view()),
	
	]
	```

### <span id="2">主要内容</span>
- 安装
	- `pip3 install dajngo-rest-framework`

#### <span id="201">源码流程</span>
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
		        # TODO: 1.1 获取解析请求的解析器，eg:JSON格式的，Form格式的。。。
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

#### <span id="202">认证</span>
- 源码剖析
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
- 

#### <span id="203">权限</span>
- 源码剖析
	- `self.check_permissions(request)`


#### <span id="204">限流</span>
- 源码剖析
	- `self.check_throttles(request)`



#### <span id="205">版本</span>
- 源码剖析
	- `version, scheme = self.determine_version(request, *args, **kwargs)`


#### <span id="206">解析器(paser)</span>
- 对请求体的解析
	- 循环APIView.parser_classes，检测每一个class的media_type
	- 当与请求头中Content-Type类型一致则使用该解析器解析请求体
- 单个视图配置使用
	- `from rest_framework.parsers import JSONParser, FormParser`
	- `parser_classes = [JSONParser, FormParser]`
	- 解析的值会存到`request.data`
- 全局生效-配置文件

	```python
	REST_FRAMEWORK = {
	    'DEFAULT_PARSER_CLASSES':[
	        'rest_framework.parsers.JSONParser'
	        'rest_framework.parsers.FormParser'
	        'rest_framework.parsers.MultiPartParser'
	    ]
	}
	```

#### <span id="207">序列化</span>
- 概念
	- 序列化
		- 将对象转换成字符串或将对象转换成字符串后写入文件
	- 反序列化
		- 将字符串转换成对象
- **rest-framework的序列化目的是解决QuerySet的序列化问题**
- **同时也可以进行form数据校验**

##### 定义自己的Serializers类
- 基本使用
	- 序列化普通字段和外键字段

		```python
		from rest_framework.views import APIView
		from rest_framework.response import Response
		from rest_framework import serializers
		
		from . import models
		
		
		class UsersSerializers(serializers.Serializer):
		    # 普通字段
		    username = serializers.CharField()
		    password = serializers.CharField()
		    token = serializers.CharField()
		
		    # 外键
		    gp_id = serializers.CharField(source="group.id")
		    gp_t = serializers.CharField(source="group.title")
		    gp_mu = serializers.CharField(source="group.menu.title")
		
		
		class UsersView(APIView):
		
		    def get(self, request, *args, **kwargs):
		        # QuerySet类型
		        users_list = models.UserInfo.objects.all()
		        ser = UsersSerializers(instance=users_list, many=True)
		
		        # # 单个对象
		        # user = models.UserInfo.objects.all().first()
		        # # ser = UsersSerializers(instance=user)
		        # ser = UsersSerializers(instance=user, many=False)
		
		        return Response(ser.data)
		```
- 多对多字段序列化
	- 方式一:自定义字段写循环对QuerySet处理

		```python
		class MyField(serializers.CharField):
		    def to_representation(self, value):
		        data_list = []
		        for row in value:
		            data_list.append(row.title)
		        return data_list
		
		
		class UsersSerializers(serializers.Serializer):
		    username = serializers.CharField()
		    password = serializers.CharField()
		    token = serializers.CharField()
		    gp_id = serializers.CharField(source="group.id")
		    gp_t = serializers.CharField(source="group.title")
		    gp_mu = serializers.CharField(source="group.menu.title")
		
		    role = MyField(source="roles.all")
		```
	- 方式二：利用ListField做循环，自定义字段只对单个对象处理

		```python
		class MyField(serializers.CharField):
		    def to_representation(self, value):
		        return {"id": value.id, "title": value.title}
		
		
		class UsersSerializers(serializers.Serializer):
		    username = serializers.CharField()
		    password = serializers.CharField()
		    token = serializers.CharField()
		    gp_id = serializers.CharField(source="group.id")
		    gp_t = serializers.CharField(source="group.title")
		    gp_mu = serializers.CharField(source="group.menu.title")
		
		    role = serializers.ListField(child=MyField(), source="roles.all")
		```
	- 方式三：

		```python
		class UsersSerializers(serializers.Serializer):
		    username = serializers.CharField()
		    password = serializers.CharField()
		    token = serializers.CharField()
		    gp_id = serializers.CharField(source="group.id")
		    gp_t = serializers.CharField(source="group.title")
		    gp_mu = serializers.CharField(source="group.menu.title")
		
		    role = serializers.SerializerMethodField()
		
		    def get_role(self, obj):
		        role_list = obj.roles.all()
		        data_list = []
		        for row in role_list:
		            data_list.append(row.title)
		        return data_list
		```

#### <span id="208">分页</span>
- 分页存在的问题
	- 当数据过多，会导致查询速度变得异常慢
	- 解决方案
		1. 记录当前访问页的数据ID
		2. 最多显示120页
		3. 对页码进行加密
- 基于`LimitOffsetPagination`分页
	- 通过URL传参
		- offset，当前第一个数据ID
		- limit，当前页面显示数据数目
	- default_limit，设置默认页面显示数据数量
	- max_limit，设置页面最大显示数量

#### <span id="209">视图</span>
- APIView
- GenericAPIView(APIView)
	- `from rest_framework.generics import GenericAPIView`
- GenericViewSet(ViewSetMixin, GenericAPIView)
	- `from rest_framework.viewsets import ViewSetMixin`
- ModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet)

#### <span id="210">路由</span>


#### <span id="211">渲染器</span>








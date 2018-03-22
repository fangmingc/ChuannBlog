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
- [常用配置](#3)

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
- 概述
	- dispatch之前
		- 路由，视图1/2
	- dispatch
		- 视图函数之前，版本，认证，权限，限流
		- 视图函数中，视图2/2，解析器，序列化（校验、queryset序列化），分页
		- 视图函数结束，渲染器

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
			- 认证列表中只要有一个认证通过即可
	
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
- 定义认证类
	- 必须要定义`authenticate`方法

		```python
		class Auth:
		    def authenticate(self, request):
		        pass
		```
		- 通过返回值代表不同认证结果
			- 抛指定异常，代表认证失败，会触发认证失败的流程
			- 返回None，表示跳过认证，执行后续认证
			- 返回一个两个元素的元组`(user, auth)`，表示认证成功
				- 元组第一个元素会被存放于`request.user`
				- 元组第二个元素会被存放于`request.auth`

- 配置使用
	- 单个视图
		- 在视图类配置`authentication_classes = [认证1, 认证2]`
	- 全局配置
	
		```python
		REST_FRAMEWORK = {
			'DEFAULT_AUTHENTICATION_CLASSES': (
		        'rest_framework.authentication.SessionAuthentication',
		        '认证1的绝对路径',
				'认证2的绝对路径',
		    ),
		}
		```


#### <span id="203">权限</span>
- 源码剖析
	- `self.check_permissions(request)`
		- 函数代码，会执行每一个权限的has_permission方法，

			```python
			def check_permissions(self, request):
			    """
			    Check if the request should be permitted.
			    Raises an appropriate exception if the request is not permitted.
			    """
			    for permission in self.get_permissions():
			        if not permission.has_permission(request, self):
			            self.permission_denied(
			                request, message=getattr(permission, 'message', None)
			            )
			```
		- 权限认证必须每一个都通过
- 定义权限类

	```python
	class Permission:
	    def has_permission(self, request, view)
	        pass
	```
	- 通过返回值表示权限是否通过
		- 返回True表示通过
		- 返回None或者False或者抛异常表示未通过
- 配置使用
	- 单个视图
		- 在视图类配置`permission_classes = [权限1, 权限2]`
	- 全局配置
	
		```python
		REST_FRAMEWORK = {
			'DEFAULT_PERMISSION_CLASSES': (
			    'rest_framework.permissions.AllowAny',
			),
		}
		```

#### <span id="204">限流</span>
- 源码剖析
	- `self.check_throttles(request)`
		- 函数代码，循环每一个限流方式，执行`throttle.allow_request(request, view)`

		```python
		def check_throttles(self, request):
		    """
		    Check if request should be throttled.
		    Raises an appropriate exception if the request is throttled.
		    """
		    for throttle in self.get_throttles():
		        if not throttle.allow_request(request, self):
		            self.throttled(request, throttle.wait())
		```
	- `BaseThrottle类`定义了先限流类的规范
		- allow_request
			- 定义限流规则，检测当前请求是否需要阻止
		- get_ident
			- 获取每一个请求的唯一标识
		- wait
			- 设置距离下一次可以访问还有多长时间

		```python
		class BaseThrottle(object):
		    """
		    Rate throttling of requests.
		    """
		
		    def allow_request(self, request, view):
		        """
		        Return `True` if the request should be allowed, `False` otherwise.
		        """
		        raise NotImplementedError('.allow_request() must be overridden')
		
		    def get_ident(self, request):
		        """
		        Identify the machine making the request by parsing HTTP_X_FORWARDED_FOR
		        if present and number of proxies is > 0. If not use all of
		        HTTP_X_FORWARDED_FOR if it is available, if not use REMOTE_ADDR.
		        """
		        xff = request.META.get('HTTP_X_FORWARDED_FOR')
		        remote_addr = request.META.get('REMOTE_ADDR')
		        num_proxies = api_settings.NUM_PROXIES
		
		        if num_proxies is not None:
		            if num_proxies == 0 or xff is None:
		                return remote_addr
		            addrs = xff.split(',')
		            client_addr = addrs[-min(num_proxies, len(addrs))]
		            return client_addr.strip()
		
		        return ''.join(xff.split()) if xff else remote_addr
		
		    def wait(self):
		        """
		        Optionally, return a recommended number of seconds to wait before
		        the next request.
		        """
		        return None
		```
- 定义示例
	- 对匿名用户进行限制，每个用户一分钟允许访问10次

		```python
		class MyThrottle(BaseThrottle):
		
		    def allow_request(self,request,view):
		        """对匿名用户进行限制，每个用户一分钟访问10次"""
		        ctime = time.time()
		        self.ip =self.get_ident(request)
		        if self.ip not in RECORD:
		            RECORD[self.ip] = [ctime]
		        else:
		            #[152042123,15204212,3152042,123152042123]
		            time_list = RECORD[self.ip]  #获取ip里面的值
		            while True:
		                val = time_list[-1] # 取出最后一个时间，也就是访问最早的时间
		                if (ctime-60)>val:  # 吧时间大于60秒的给剔除
		                    time_list.pop()
		                # 剔除了之后timelist里面就是有效的时间了，在进行判断他的访问次数是不是超过10次
		                else:
		                    break
		            if len(time_list) >10:
		                return False        # 返回False，限制
		            time_list.insert(0, ctime)
		        return True   # 返回True，不限制
		
		    def wait(self):
		        ctime = time.time()
		        first_in_time = RECORD[self.ip][-1]
		        wt = 60-(ctime-first_in_time)
		        return wt
		```
- 配置使用
	- 单个视图
		- 在视图类配置`throttle_classes = [限流1, 限流2]`
	- 全局使用

		```python
		REST_FRAMEWORK = {
			'DEFAULT_THROTTLE_CLASSES': (
			    '限流1的绝对路径',
			),
		}
		```

#### <span id="205">版本</span>
- 源码剖析
	- `version, scheme = self.determine_version(request, *args, **kwargs)`
		- 函数代码，执行指定处理版本的类的`determine_version`方法

		```python
		def determine_version(self, request, *args, **kwargs):
		    """
		    If versioning is being used, then determine any API version for the
		    incoming request. Returns a two-tuple of (version, versioning_scheme)
		    """
		    if self.versioning_class is None:
		        return (None, None)
		    scheme = self.versioning_class()
		    return (scheme.determine_version(request, *args, **kwargs), scheme)
		```
	- 以URL传入版本为例，处理完后可以在request.version获取到当前版本 

		```python
		class URLPathVersioning(BaseVersioning):
		    """
		    To the client this is the same style as `NamespaceVersioning`.
		    The difference is in the backend - this implementation uses
		    Django's URL keyword arguments to determine the version.
		
		    An example URL conf for two views that accept two different versions.
		
		    urlpatterns = [
		        url(r'^(?P<version>[v1|v2]+)/users/$', users_list, name='users-list'),
		        url(r'^(?P<version>[v1|v2]+)/users/(?P<pk>[0-9]+)/$', users_detail, name='users-detail')
		    ]
		
		    GET /1.0/something/ HTTP/1.1
		    Host: example.com
		    Accept: application/json
		    """
		    invalid_version_message = _('Invalid version in URL path.')
		
		    def determine_version(self, request, *args, **kwargs):
		        version = kwargs.get(self.version_param, self.default_version)
		        if not self.is_allowed_version(version):
		            raise exceptions.NotFound(self.invalid_version_message)
		        return version
		
		    def reverse(self, viewname, args=None, kwargs=None, request=None, format=None, **extra):
		        if request.version is not None:
		            kwargs = {} if (kwargs is None) else kwargs
		            kwargs[self.version_param] = request.version
		
		        return super(URLPathVersioning, self).reverse(
		            viewname, args, kwargs, request, format, **extra
		        )
		```
- 配置使用
	- 单个视图
		- 在视图类配置`versioning_class = URLPathVersioning`
	- 全局配置

		```python
		REST_FRAMEWORK = {
		    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
		    'DEFAULT_VERSION': 'v1',
		    'ALLOWED_VERSIONS': ['v1', ],
		    'VERSION_PARAM': 'version',
		}
		```		

#### <span id="206">解析器(paser)</span>
- 对请求体的解析
	- 循环APIView.parser_classes，检测每一个class的media_type
	- 当与请求头中Content-Type类型一致则使用该解析器解析请求体
	- 解析的值会存到`request.data`
- 单个视图配置使用
	- `from rest_framework.parsers import JSONParser, FormParser`
	- `parser_classes = [JSONParser, FormParser]`
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
- 基于Model

	```python
	class UsersSerializer(serializers.ModelSerializer):
	x1 = serializers.CharField(source='name')
	group = serializers.HyperlinkedIdentityField(view_name='detail')
	class Meta:
	    
	    model = models.UserInfo
	    # fields = "__all__"
	    fields = ['name','pwd','group','x1']  # 自定义字段的时候注意要指定source,scource里面的数据必须是数据库有的数据
	    depth = 1 # 表示深度
	
	
	class UsersView(APIView):
	    def get(self,request,*args,**kwargs):
	        user_list = models.UserInfo.objects.all()
	        ser = UsersSerializer(instance=user_list,many=True)
	        return Response(ser.data)
	
	```
- 生成Hyperlinked
	- 在路由配置时，绑定的视图应当定义好别名

		```python
		class UsersSerializer(serializers.ModelSerializer): 
		    group = serializers.HyperlinkedIdentityField(view_name='detail')
		    class Meta:
		        model = models.UserInfo
		        fields = "__all__"
		        fields = ['name', 'pwd','group']
		        depth = 1
		
		
		class UsersView1(APIView):
		    def get(self,request,*args,**kwargs):
		        user_list = models.UserInfo.objects.all()
		        ser = UsersSerializer(instance=user_list,many=True,context={'request':request})
		        return Response(ser.data)
		```
	- URLS

		```python
		from django.conf.urls import url,include
		from django.contrib import admin
		from app01 import views
		urlpatterns = [
		
		    url(r'^users1/$', views.UserView1.as_view(), name='xxx'), # 把users1的group的值反向生成users2的url
		    url(r'^users2/(?P<pk>.*)', views.UserView2.as_view(), name='detail'),  # 组名必须为pk
		
		]
		```
- 全自动生成URL
	- 路由配置时，每个视图类的别名必须按照一定的规则命名
		- `url(r'users/')`, UsersView.as_view(),name='users)'
		- `url(r'userinfo/(?P<pk>\d+)')`, UserInfoView.as_view(),name='userinfo-detail)'
		- `url(r'group/(?P<pk>\d+)')`, GroupView.as_view(),name='group-detail)'
	
	```python
	class UsersSerializer(serializers.HyperlinkedModelSerializer): # 继承他自动生成
	    class Meta:
	        model = models.UserInfo
	        fields = "__all__"
	        # fields = ['id','name','pwd']  
	
	class UsersView(APIView):
	    def get(self,request,*args,**kwargs):
	        user_list = models.UserInfo.objects.all()
	        ser = UsersSerializer(instance=user_list,many=True,context={'request':request})
	        return Response(ser.data)
	```
- 请求数据验证
	- 充当django form组件
	- 完全自定义
		```python
		class PasswordValidator(object):
		    def __init__(self, base):
		        self.base = base
		
		    def __call__(self, value):
		        if value != self.base:
		            message = '用户输入的值必须是 %s.' % self.base
		            raise serializers.ValidationError(message)
		
		    def set_context(self, serializer_field):
		        """
		        This hook is called by the serializer instance,
		        prior to the validation call being made.
		        """
		        # 执行验证之前调用,serializer_fields是当前字段对象
		        pass
			def validate_字段(self,validated_value):
		       # raise ValidationError(detail='xxxxxx')
		       return validated_value
		
		class UsersSerializer(serializers.Serializer):
		        name = serializers.CharField(min_length=6)
		        pwd = serializers.CharField(error_messages={'required': '密码不能为空'}, validators=[PasswordValidator('666')])
		```
	- 基于model
		
		```python
		class PasswordValidator(object):
		    def __init__(self, base):
		        self.base = base
		
		    def __call__(self, value):
		        if value != self.base:
		            message = '用户输入的值必须是 %s.' % self.base
		            raise serializers.ValidationError(message)
		
		    def set_context(self, serializer_field):
		        """
		        This hook is called by the serializer instance,
		        prior to the validation call being made.
		        """
		        # 执行验证之前调用,serializer_fields是当前字段对象
		        pass
		
		class UsersSerializer(serializers.ModelSerializer):
		    class Meta:
		        model = models.UserInfo
		        fields = "__all__"
		        # 自定义验证规则
		        extra_kwargs = {
		            'name': {'min_length': 6},
		            'pwd': {'validators': [PasswordValidator(666), ]}
		        }
		```
	- 使用

		```python
		class UsersView(APIView):
		    def get(self,request,*args,**kwargs):
		        user_list = models.UserInfo.objects.all()
		        ser = UsersSerializer(instance=user_list,many=True,context={'request':request})
		        return Response(ser.data)
		
		    def post(self,request,*args,**kwargs):
		        ser = UsersSerializer(data=request.data)
		        if ser.is_valid():
		            print(ser.validated_data)
		        else:
		            print(ser.errors)
		        return Response('...')
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



### <span id="3">常用配置</span>



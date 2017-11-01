# Django

- [URl的分发和映射](Django_URLconf.md)
- [views视图函数](Django_views.md)
- [template模板](https://github.com/fangmingc/Python/tree/master/Frame/Django/Django_templates.md)
- [model](Django_model.md)

## 开始Django
1. 安装Django
	- 'pip3 install django'
2. 创建django项目
	- 'django-admin startproject 项目名'
3. 创建一个应用
	- 'python manage.py startapp 应用名'
	- 在urls.py添加视图函数
	- 在views.py编写视图函数，使用HttpResponse作为响应
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

## Django命令
- model相关
	- 将models.py中定义的类编译：python manage.py makemigrations
	- 执行编译文件：python manage.py migrate

## settings
### 杂项
#### 区分路径最后的"/"
```python
APPEND_SLASH = True
```

### 模板配置
#### templates配置
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

#### 静态文件相关
- 路径别名，在模板中使用

	```python
	STATIC_URL = '/static/'
	```

- 静态文件路径

	```python
	STATICFILES_DIRS = [
	    os.path.join(BASE_DIR, 'static')
	]
	```


### 数据库相关
#### 使用MySQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ManageBooks',      # 库的名字
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306'
    }
}
```

#### 查看涉及数据库的sql语句，在终端输出
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```

### 用户认证系统
#### 指定登录路径，与login_required搭配
```python
LOGIN_URL = "/login/"
```

#### session存储
- 默认配置

	```python
	SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）,数据源
	SESSION_COOKIE_NAME = "sessionid"  				# Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
	SESSION_COOKIE_PATH = "/"                               # Session的cookie保存的路径（默认）
	SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
	SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
	SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
	SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
	SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
	SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
	```

- 缓存配置

	```python
	SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎,数据源
	SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
	SESSION_COOKIE_NAME = "sessionid"                        # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
	SESSION_COOKIE_PATH = "/"                                # Session的cookie保存的路径
	SESSION_COOKIE_DOMAIN = None                              # Session的cookie保存的域名
	SESSION_COOKIE_SECURE = False                             # 是否Https传输cookie
	SESSION_COOKIE_HTTPONLY = True                            # 是否Session的cookie只支持http传输
	SESSION_COOKIE_AGE = 1209600                              # Session的cookie失效日期（2周）
	SESSION_EXPIRE_AT_BROWSER_CLOSE = False                   # 是否关闭浏览器使得Session过期
	SESSION_SAVE_EVERY_REQUEST = False                        # 是否每次请求都保存Session，默认修改之后才保存
	```

- 文件配置

	```python
	SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎,数据源
	SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()        
	SESSION_COOKIE_NAME ＝ "sessionid"                          # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
	SESSION_COOKIE_PATH ＝ "/"                                  # Session的cookie保存的路径
	SESSION_COOKIE_DOMAIN = None                                # Session的cookie保存的域名
	SESSION_COOKIE_SECURE = False                               # 是否Https传输cookie
	SESSION_COOKIE_HTTPONLY = True                              # 是否Session的cookie只支持http传输
	SESSION_COOKIE_AGE = 1209600                                # Session的cookie失效日期（2周）
	SESSION_EXPIRE_AT_BROWSER_CLOSE = False                     # 是否关闭浏览器使得Session过期
	SESSION_SAVE_EVERY_REQUEST = False                          # 是否每次请求都保存Session，默认修改之后才保存
	```





























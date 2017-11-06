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


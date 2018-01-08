# Flask
轻量级、短小精悍、丰富的第三方组件

## 使用前
- 安装：pip install flask
- 比较：
	- django:无socket、中间件、路由系统、视图(CBV,FBV)、模板、ORM、cookie、session、admin、form、缓存、信号、序列化、.....
	- flask:无socket、中间件(需要扩展)、路由系统、视图(CBV)、第三方模板(jinja2)、cookie、session弱

- 什么是wsgi
	- web服务网关接口，协议
- flask依赖一个实现了WSGI协议的模块：werkzeug模块

## 开始使用
```python
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "jksdhfaj32jhgrfhjgvikhjg32hufgvhxzgv78432hjsvcsgv"

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        if not request.form.get("username") == "wusir" and request.form.get("password") == "123":
            return render_template('login.html', msg="用户名或密码错误")
        session["user_info"] = {"username": "武沛齐"}
        return redirect('/index/')

@app.route("/index/", methods=["GET", ])
def index():
    return render_template('index.html', **{'msg': session.get("user_info")})

if __name__ == '__main__':
    app.run()
```
- flask的使用基于Flask这个类
	- 可配置参数有很多，下面是实例化时的几个参数
		- mport_name，通常使用当前flask项目启动文件名，不固定
		- static_url_path=None，静态文件目录的别名，用于模板中反向指定静态文件，格式'/xxx'
		- static_folder='static'，静态文件目录
		- template_folder='templates'，模板文件目录
		- root_path=None，项目根目录，默认为flask项目启动文件所在目录
	- 额外配置
		- secret_key，当使用了session时需要，flask的session是通过密钥加密session数据发送到浏览器保存
	- 添加路由关系
		- 将URL和视图函数封装成一个Rule对象添加到app.url_map
		- 两种添加路由关系的方式
			- 带参数装饰器，@app.route(url, methods=["GET", ...])
			- 函数，app.add_url_rule(rule, endpoint, f, **options)
	- request
		- values，POST请求数据
		- form，表单数据
		- args，GET请求的数据
	- response
		- 字符串 ---- Httpresponse
		- render_template  -----   render

## 路由系统
- 两种方式都可用，推荐装饰器方式

- url传入参数
	- @app.route('/index/<username>')
	- @app.route('/index/<int:nid>', methods=["GET", "POST"], endpoint="fff")
- 定制参数
	- methods, 可接受请求方式
	- endpoint, 给URL起别名
	- rule, URL规则
	- view_func, 视图函数名称
	- defaults=None, 默认值,当URL中无参数，函数需要参数时，使用defaults={'k':'v'}为函数提供参数
	- endpoint=None, 名称，用于反向生成URL，即： url_for('名称')
	- methods=None,  允许的请求方式，如：["GET","POST"]
	- strict_slashes=None, 对URL最后的 / 符号是否严格要求，
	- redirect_to=None, 重定向到指定地址，旧系统下线了但是部分URL没有改，可以使用重定向跳转到新系统
	- subdomain=None, 子域名访问
		- 域名解析
			- 首先在本地hosts寻找域名对应的IP
			- 本地没有的时候去公网上寻找
		- 修改hosts, C:\Windows\System32\drivers\etc\hosts
- 路由系统中的正则匹配

	```
	from flask import Flask,url_for
	app = Flask(__name__)
	
	# 定义转换的类
	from werkzeug.routing import BaseConverter
	class RegexConverter(BaseConverter):
		"""
		自定义URL匹配正则表达式
		"""
	
		def __init__(self, map, regex):
			super(RegexConverter, self).__init__(map)
			self.regex = regex
	
		def to_python(self, value):
			"""
			路由匹配时，匹配成功后传递给视图函数中参数的值
			:param value: 
			:return: 
			"""
			return int(value)
	
		def to_url(self, value):
			"""
			使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
			:param value: 
			:return: 
			"""
			val = super(RegexConverter, self).to_url(value)
			return val
	
	# 添加到converts中
	app.url_map.converters['xxx'] = RegexConverter
	
	# 进行使用
	@app.route('/index/<xxx("\d+"):nid>',endpoint='xx')
	def index(nid):
		url_for('xx',nid=123)
		return "Index"
	
	if __name__ == '__main__':
		app.run()
	```


## 视图函数
- FBV:

	```
	@app.route('/index',endpoint='xx')
	def index(nid):
		url_for('xx',nid=123)
		return "Index"
	
	def index(nid):
		url_for('xx',nid=123)
		return "Index"
	
	app.add_url_rule('/index',index)
	```

- CBV:
	
	```
	def auth(func):
		def inner(*args, **kwargs):
			result = func(*args, **kwargs)
			return result
		return inner
	
	class IndexView(views.MethodView):
		# methods = ['POST']
		decorators = [auth,]
	
		def get(self):
			v = url_for('index')
			print(v)
			return "GET"
	
		def post(self):
			return "GET"
	
	app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))
	```


## 请求和响应
### 请求
- request.method
- request.args
- request.form
- request.values
- request.cookies
- request.headers
- request.path
- request.full_path
- request.script_root
- request.url
- request.base_url
- request.url_root
- request.host_url
- request.host
- request.files
- obj = request.files['the_file_name']
- obj.save('/var/www/uploads/' + secure_filename(f.filename))


### 响应
- jsonfy

- return "字符串"
- return render_template('html模板路径',**{})
- return redirect('/index.html')
- response = make_response(render_template('index.html'))
- response是flask.wrappers.Response类型
- response.delete_cookie('key')
- response.set_cookie('key', 'value')
- response.headers['X-Something'] = 'A value'
- return response

## 模板语言
- app.template_global
- app.template_filter
- 宏
	- macro func_name(arg)
	- func_name(arg)



## 第三方session模块
- 设置：session['username'] ＝ 'xxx'
- 删除：session.pop('username', None)

```python
from flask import Flask, session, redirect, url_for, escape, request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''
 
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
 
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
```

## 闪现
基于Session实现的用于保存数据的集合，其特点是：使用一次就删除
- flash("msg")
- msg = get_flashed_messages()


## 扩展
### 模拟中间件
```python
@app.before_first_request
def before_first_request1():
    print('before_first_request1')


@app.before_first_request
def before_first_request2():
    print('before_first_request2')

@app.before_request
def before_request1():
    Request.nnn = 123
    print('before_request1')

@app.before_request
def before_request2():
    print('before_request2')


@app.after_request
def after_request1(response):
    print('before_request1', response)
    return response


@app.after_request
def after_request2(response):
    print('before_request2', response)
    return response


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.template_global()
def sb(a1, a2):
    return a1 + a2


@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3
```

- 源码

```python
def full_dispatch_request(self):
    """Dispatches the request and on top of that performs request
    pre and postprocessing as well as HTTP exception catching and
    error handling.

    .. versionadded:: 0.7
    """
    self.try_trigger_before_first_request_functions()
    try:
        request_started.send(self)
        rv = self.preprocess_request()
        if rv is None:
            rv = self.dispatch_request()
    except Exception as e:
        rv = self.handle_user_exception(e)
    return self.finalize_request(rv)
```
## 配置文件
```
# 方式一
app.config["NNN"] = 123

# 方式二
app.config.from_pyfile("settings.py")

# 方式三
import os
os.environ["FLASK_SETTINGS"] = "settings.py"
app.config.from_envvar("FLASK_SETTINGS")

# 方式四
app.config.from_object("settings2.DevConfig")
```

## blueprint 蓝图
- 对应用程序目录结构

## 数据库连接池
- 每次操作都要连接
- 公用一个链接，多线程会出问题
	- 加锁可以解决
	- 但是加锁后就变成串行

- DBUtils数据库连接池
	- 模式一
		- 基于threding.local实现为每个线程创建一个连接，关闭非关闭，当前线程可以重复使用本线程中的链接，线程终止时链接才关闭
	- 模式二
		- 连接池原理
		- 设置连接池中最大连接数
		- 启动时，连接池中默认可以创建指定数目的链接
		- 如果有三个线程来连接池获取连接
			- 1个连接时，另外两个排着队等着使用
			- 2个连接时，另外一个排着队使用
			- 3个连接时，一对一使用
		- maxshared设置的最大共享连接数是无效的
			- 除非设置pymysql中threadsafety>1

## 上下文
- 本地线程
- 上下文原理




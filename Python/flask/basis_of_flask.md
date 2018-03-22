## flask基础
- [创建FLask对象](#1)
- [配置文件](#2)
- [路由系统](#3)
- [视图函数](#4)
	- [请求](#41)
	- [响应](#42)
	- [session](#43)
	- [闪现](#44)
- [模板](#5)
- [blueprint](#6)
- [特殊装饰器](#7)


### <span id='1'>创建FLask对象</span>
- import_name，通常使用当前flask项目启动文件名，不固定
- static_url_path=None，静态文件目录的别名，用于模板中反向指定静态文件，格式'/xxx'
- static_folder='static'，静态文件目录
- template_folder='templates'，模板文件目录
- root_path=None，项目根目录，默认为flask项目启动文件所在目录
- instance_path=None,
- instance_relative_config=False

### <span id='2'>配置文件</span>
```python
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

### <span id='3'>路由系统</span>
- 流程
	- 将函数和url封装到Rule对象
	- 将Rule对象添加到app.url_map(Map对象)
- 添加路由有两种方式，推荐装饰器方式
	- 在视图函数上方加装饰器@app.route(url)
	- 在视图函数后使用app.add_url_rule(url, view_func)
- url传入参数
	- @app.route('/index/<username>')
	- @app.route('/index/<int:nid>', methods=["GET", "POST"], endpoint="fff")
- 定制参数
	- rule, URL规则
	- view_func, 视图函数名称
	- methods, 可接受请求方式
	- endpoint, 给URL起别名
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
	- URL中不可直接使用正则表达式，需定义类
	- URL自带部分正则匹配
		- <int:var_name>
		- <path:var_name>

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

### <span id='4'>视图函数</span>
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

#### <span id='41'>请求</span>
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


#### <span id='42'>响应</span>
- "字符串"
- jsonfy
- render_template('html模板路径',**{})
- redirect('/index.html')
- response = make_response(render_template('index.html'))
	- 可设置响应头
- response是flask.wrappers.Response类型
- response.delete_cookie('key')
- response.set_cookie('key', 'value')
- response.headers['X-Something'] = 'A value'
- return response

#### <span id='43'>session</span>
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

#### <span id='44'>闪现</span>
基于Session实现的用于保存数据的集合，其特点是：使用一次就删除
- flash("msg")
- msg = get_flashed_messages()


### <span id='5'>模板</span>
- 基本语法
	- django有的基本都有
	- 宏
		- macro func_name(arg)
		- func_name(arg)
- 自定义函数
	- app.template_global
	- app.template_filter

	```python
	@app.template_global()
	def sb(a1, a2):
	    return a1 + a2
	
	
	@app.template_filter()
	def db(a1, a2, a3):
	    return a1 + a2 + a3
	```

### <span id='6'>blueprint 蓝图</span>
- 对项目目录结构规则化

	```
	manage.py
	fcrm
	│  __init__.py
	├─static
	├─templates
	│      login.html
	└─views
	   │  account.py
	   └─ order.py
	```
- manage.py

	```python
	import fcrm		# 项目文件包
	
	if __name__ == '__main__':
	    fcrm.app.run(port=8001)
	```

- \_\_init__.py

	```python
	from flask import Flask
	from .views import account
	from .views import order
	
	app = Flask(__name__)
	print(app.root_path)
	app.register_blueprint(account.account)
	app.register_blueprint(order.order)
	```

- order.py
	```python
	from flask import Blueprint
	
	order = Blueprint('order',__name__)
	
	@order.route('/order')
	def login():
	    return 'Order'
	```

### <span id='7'>特殊装饰器</span>
#### 模拟中间件
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
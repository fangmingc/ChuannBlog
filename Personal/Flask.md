# Flask学习
教程：
- Flask Web开发：基于Python的Web应用开发实战
- Flask Web Development:Developing Web Applications with Python
- [美] Miguel Grinberg 著
- 安道 译

## 遇到的问题
- 栈跟踪？





## 了解Flask
### 使用前的知识储备
- python
	- 理解：包/模块/函数/修饰器/面向对象编程
	- 熟悉：异常处理
- 命令行的操作（win OR linux）
- html/css/javascript
- git
	- 教程实例代码：：https://github.com/miguelgrinberg/flasky

### 为何用Flask
- 在 Flask 中，你可以自主选择程序的组件，如果找不到合适的，还可以自己开发。例如选择数据库，可以使用关系数据库，也可以使用非关系数据库，甚至使用自己写的数据库
- Flask 提供了一个强健的核心，其中包含每个 Web 程序都需要的基本功能，而其他功能则交给行业系统中的众多第三方扩展，当然，你也可以自行开发。
- Flask是小型框架，自开发就被设计为可扩展的框架，包含有一个基本服务的强健核心，其他功能通过拓展实现，可以自行挑选所需拓展包，组成一个没有附加功能的精益组合，满足所需


### 主要依赖
- 路由
- 调试
- web服务器网关接口
- 子系统由werkzeug提供（http://werkzeug.pocoo.org）
- 模板系统由jinja2提供（http://jinja.pocoo.org）
- Flask 并不原生支持数据库访问、Web 表单验证和用户认证等高级功能。这些功能以及其他大多数 Web 程序中需要的核心服务都以扩展的形式实现，然后再与核心包集成。


## 1起步
### 1.1 安装和设置Flask框架
#### 使用虚拟环境
>虚拟环境是 Python 解释器的一个私有副本，在这个环境中你可以安装私有包，而且不会影响系统中安装的全局 Python 解释器。     
>用于避免包的混乱和版本的冲突

- 检测是否安装了virtualenv<code>$ virtualenv --version</code>

#### 跟踪教程的程序版本
- 下载git源码
	-  <code>git clone https://github.com/miguelgrinberg/flasky.git</code>
- 切换历史版本
	-  <code>git checkout 1a</code>

#### 创建 Python 虚拟环境
- 使用 virtualenv 命令在 flasky 文件夹中创建 Python 虚拟环境，该命令有一个必需的参数，即虚拟环境的名字。一般虚拟环境会被命名为 venv
- <code>$ virtualenv venv</code>

#### 激活环境
- linux/mac 的bash命令行：<code>$ source venv/bin/activate</code>
- windows：<code>$ venv\Scripts\activate</code>
- 解除环境:<code>deactivate</code>

#### 使用pip安装Python包
- <code>$ pip install flask</code>
- 检测是否成功安装:

	```
	(venv) $ python
	>>> import flask
	>>>
	```

### 1.2 程序的基本结构
#### 初始化
- 所有 Flask 程序都必须创建一个程序实例。
- Web 服务器使用一种名为 Web 服务器网关接口（Web Server Gateway Interface，WSGI）的协议，把接收自客户端的所有请求都转交给这个对象处理。
- 程序实例是 Flask 类的对象，经常使用下述代码创建

	```python
	from flask import Flask
	app = Flask(__name__)
	```

- Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python 的 __name__ 变量就是所需的值。

#### 路由和视图函数
- 路由 
	- 客户端（例如 Web 浏览器）把请求发送给 Web 服务器，
	- Web 服务器再把请求发送给 Flask程序实例。
	- 程序实例需要知道对每个 URL 请求运行哪些代码，所以保存了一个 URL 到Python 函数的映射关系。
	- 处理 URL 和函数之间关系的程序称为路由
- 定义路由
	- 使用程序实例提供的 app.route 修饰器把修饰的函数注册为路由

	```python
	@app.route('/')
	def index():
	    return '<h1>Hello World!</h1>'
	```

- 这里把index() 函数注册为程序根地址的处理程序，如果部署程序的服务器域名为 www.example.com，在浏览器中访问 http://www.example.com 后，会触发服务器执行 index() 函数
- 这个函数的返回值称为响应，是客户端接收到的内容。如果客户端是 Web 浏览器，响应就是显示给用户查看的文档。
- 像 index() 这样的函数称为视图函数（view function）。视图函数返回的响应可以是包含HTML 的简单字符串，也可以是复杂的表单

>在 Python 代码中嵌入响应字符串会导致代码难以维护，此处这么做只是为了介绍响应的概念

##### 动态路由
- 日常所用服务的URL地址中都包含可变部分，如http://www.facebook.com/<your-name>

	```python
	@app.route('/user/<name>')
	def user(name):
	    return '<h1>Hello, %s</h1>'%name
	```

- 尖括号中的内容就是动态部分，任何能匹配静态部分的 URL 都会映射到这个路由上。调用视图函数时，Flask 会将动态部分作为参数传入函数。在这个视图函数中，参数用于生成针对个人的欢迎消息。
- 路由中的动态部分默认使用字符串，不过也可使用类型定义。例如，路由 /user/<int:id>只会匹配动态片段 id 为整数的 URL。Flask 支持在路由中使用 int、float 和 path 类型。path 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。

#### 启动服务器
```python
if __name__ == '__main__':
    app.run(debug=True)
```
- __name__=='__main__' 是 Python 的惯常用法，在这里确保直接执行这个脚本时才启动开发Web 服务器。如果这个脚本由其他脚本引入，程序假定父级脚本会启动不同的服务器，因此不会执行 app.run()。
- 启用调试模式会带来一些便利，比如说激活调试器和重载程序。要想启用调试模式，我们可以把 debug 参数设为 True

#### first flask
```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(debug=True)
```
- 在命令行虚拟环境下使用<code>python hello.py</code>建立服务器
- 在浏览器输入http://127.0.0.1:5000/即可链接上服务器

>使用pycharm    
创建新项目，选择flask，选择虚拟环境，其他相同

#### 包含动态路由的flask
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def uesr(name):
    return '<h1>Hello %s!</h1>'%name


if __name__ == '__main__':
    app.run(debug=True)
```
- 启动服务器：<code>python hello.py</code>
- 访问动态路由：http://127.0.0.1:5000/user/chuck


#### 请求−响应循环
##### 程序和请求上下文
>Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。请求对象就是一个很好的例子，它封装了客户端发送的 HTTP 请求。为了让视图可以访问对象，会使用将对象作为参数传入视图函数，但是这会让程序每个视图函数都增加参数，如果视图函数访问对象较多，情况就非常复杂。

为避免大量这样的参数把函数弄得混乱，flask使用上下文临时把某些对象变成全局可访问，有了上下文就可以写出下面的视图函数：

```python
from flask import request
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
```

>User Agent(用户代理)，是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。

- Flask上下文全局变量

<table><tr><td>current_app</td><td>程序上下文</td><td>当前激活程序的程序实例</td></tr><tr><td>g</td><td>程序上下文</td><td>处理请求时用作临时存储的对象。每次请求都会重设这个变量</td></tr><tr><td>request</td><td>请求上下文</td><td>请求对象，封装了客户端发出的 HTTP 请求中的内容</td></tr><tr><td>session</td><td>请求上下文</td><td>用户会话，用于存储请求之间需要“记住”的值的词典</td></tr></table>

- Flask 在分发请求之前激活（或推送）程序和请求上下文，请求处理完成后再将其删除。
- 程序上下文被推送后，就可以在线程中使用 current_app 和 g 变量。
- 类似地，请求上下文被推送后，就可以使用 request 和 session 变量。
- 如果使用这些变量时我们没有激活程序上下文或请求上下文，就会导致错误。

	```python
	>>> from hello import app
	>>> from flask import current_app
	>>> current_app.name
	>Traceback (most recent call last):
	...
	RuntimeError: working outside of application context
	>>> app_ctx = app.app_context()
	>>> app_ctx.push()
	>>> current_app.name
	'hello'
	>>> app_ctx.pop()
	```

- 调用 app.app_context() 可获得一个程序上下文。

##### 请求调度
- 程序收到客户端发来的请求时，要找到处理该请求的视图函数。
- 为了完成这个任务，Flask会在程序的 URL 映射中查找请求的 URL。URL 映射是 URL 和视图函数之间的对应关系。
- Flask 使用 app.route 修饰器或者非修饰器形式的 app.add_url_rule() 生成映射。
- 测试hello.py的映射

	```python
	>>> from hello import app
	>>> app.url_map
	Map([<Rule '/' (OPTIONS, HEAD, GET) -> index>,
	    <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>,
	    <Rule '/user/<name>' (OPTIONS, HEAD, GET) -> uesr>])
	```

- / 和 /user/<name> 路由在程序中使用 app.route 修饰器定义。/static/<filename> 路由是Flask 添加的特殊路由，用于访问静态文件。
- URL 映射中的 HEAD、Options、GET 是请求方法，由路由进行处理。
- Flask 为每个路由都指定了请求方法，这样不同的请求方法发送到相同的 URL 上时，会使用不同的视图函数进行处理。
- HEAD 和 OPTIONS 方法由 Flask 自动处理，因此可以这么说，在这个程序中，URL映射中的 3 个路由都使用 GET 方法。

##### 请求钩子
- 为了避免在每个视图函数中都使用重复的代码，Flask 提供了注册通用函数的功能，注册的函数可在请求被分发到视图函数之前或之后调用。
- 请求钩子使用修饰器实现。Flask 支持以下 4 种钩子。
	- before_first_request：注册一个函数，在处理第一个请求之前运行。
	- before_request：注册一个函数，在每次请求之前运行。
	- after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
	- teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。
- 在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g。
- 例如，before_request 处理程序可以从数据库中加载已登录用户，并将其保存到 g.user 中。随后调用视图函数时，视图函数再使用 g.user 获取用户。

##### 响应
- Flask 调用视图函数后，会将其返回值作为响应的内容。
	- 大多数情况下，响应就是一个简单的字符串，作为 HTML 页面回送客户端。       
	- 但 HTTP 协议需要的不仅是作为请求响应的字符串。HTTP 响应中一个很重要的部分是状态码，Flask 默认设为 200，这个代码表明请求已经被成功处理。       
	- 如果视图函数返回的响应需要使用不同的状态码，那么可以把数字代码作为第二个返回值，添加到响应文本之后。例如，下述视图函数返回一个 400 状态码，表示请求无效：        

	```python
	@app.route('/')
	def index():
	    return '<h1>Bad Request</h1>', 400
	```
	- 视图函数返回的响应还可接受第三个参数，这是一个由首部（header）组成的字典，可以添加到 HTTP 响应中。一般情况下并不需要这么做，

- 如果不想返回由 1 个、2 个或 3 个值组成的元组，Flask 视图函数还可以返回 Response 对象
	- make_response() 函数可接受 1 个、2 个或 3 个参数（和视图函数的返回值一样），并返回一个 Response 对象。
	- 有时我们需要在视图函数中进行这种转换，然后在响应对象上调用各种方法，进一步设置响应。
	- 下例创建了一个响应对象，然后设置了 cookie：

	```python
	from flask import make_response
	@app.route('/')
	def index():
	    response = make_response('<h1>This document carries a cookie!</h1>')
	    response.set_cookie('answer', '42')
	    return response
	```

- 有一种名为重定向的特殊响应类型。这种响应没有页面文档，只告诉浏览器一个新地址用以加载新页面。重定向经常在 Web 表单中使用.
	- 重定向经常使用 302 状态码表示，指向的地址由 Location 首部提供。
	- 重定向响应可以使用3 个值形式的返回值生成，也可在 Response 对象中设定。
	- 不过，由于使用频繁，Flask 提供了 redirect() 辅助函数，

	```python
	from flask import redirect
	@app.route('/')
	def index():
	    return redirect('http://www.example.com')
	```

- 还有一种特殊的响应由 abort 函数生成，用于处理错误。在下面这个例子中，如果 URL 中动态参数 id 对应的用户不存在，就返回状态码 404：

	```python
	from flask import abort
	@app.route('/user/<id>')
	def get_user(id):
	    user = load_user(id)
	    if not user:
	    abort(404)
	    return '<h1>Hello, %s</h1>' % user.name
	```

#### Flask扩展
Flask 被设计为可扩展形式，故而没有提供一些重要的功能，例如数据库和用户认证，所以开发者可以自由选择最适合程序的包，或者按需求自行开发。
社区成员开发了大量不同用途的扩展，如果这还不能满足需求，你还可使用所有 Python 标准包或代码库。为了让你知道如何把扩展整合到程序中，接下来我们将在 hello.py 中添加一个扩展，使用命令行参数增强程序的功能。

- 使用Flask-Script支持命令行选项
	- Flask 的开发 Web 服务器支持很多启动设置选项，但只能在脚本中作为参数传给 app.run()函数。这种方式并不十分方便，传递设置选项的理想方式是使用命令行参数。
	- Flask-Script 是一个 Flask 扩展，为 Flask 程序添加了一个命令行解析器。Flask-Script 自带了一组常用选项，而且还支持自定义命令。
	- Flask-Script 扩展使用 pip 安装：<code>(venv) $ pip install flask-script</code>

	```python
	from flask.ext.script import Manager
	manager = Manager(app)
	# ...
	if __name__ == '__main__':
	    manager.run()
	```

	- 专为 Flask 开发的扩展都暴漏在 flask.ext 命名空间下。Flask-Script 输出了一个名为Manager 的类，可从 flask.ext.script 中引入。
- 这个扩展的初始化方法也适用于其他很多扩展：把程序实例作为参数传给构造函数，初始化主类的实例。创建的对象可以在各个扩展中使用。在这里，服务器由 manager.run() 启动，启动后就能解析命令行了。
	- 现在可以在命令行使用<code>(venv) $ python hello.py 命令</code>
	- shell
		- 令用于在程序的上下文中启动 Python shell 会话。你可以使用这个会话中运行维护任务或测试，还可调试异常。
	- runserver
		- 用来启动 Web 服务器。运行<code>python hello.py runserver</code>将以调试模式启动 Web 服务器
		- 使用<code>(venv) $ python hello.py runserver --help</code>查看命令参数
		- --host 参数是个很有用的选项，它告诉 Web 服务器在哪个网络接口上监听来自客户端的连接。默认情况下，Flask 开发 Web 服务器监听 localhost 上的连接，所以只接受来自服务器所在计算机发起的连接。下述命令让 Web 服务器监听公共网络接口上的连接，允许同网中的其他计算机连接服务器：

		```
		(venv) $ python hello.py runserver --host 0.0.0.0
		 * Running on http://0.0.0.0:5000/
		 * Restarting with reloader
		```

		- 现在，Web 服务器可使用 http://a.b.c.d:5000/ 网络中的任一台电脑进行访问，其中“a.b.c.d”是服务器所在计算机的外网 IP 地址。

### 1.3 flask中的模板
#### 业务逻辑和表现逻辑
- 例如，用户在网站中注册了一个新账户。用户在表单中输入电子邮件地址和密码，然后点击提交按钮。
- 服务器接收到包含用户输入数据的请求，然后 Flask 把请求分发到处理注册请求的视图函数。
	- 这个视图函数需要访问数据库，添加新用户，
	- 然后生成响应回送浏览器。
	- 这两个过程分别称为业务逻辑和表现逻辑。
- 把业务逻辑和表现逻辑混在一起会导致代码难以理解和维护。在现在的简单示例程序还看不出来，但是在生产中必定会考虑这个问题。
- 假设要为一个大型表格构建HTML 代码，表格中的数据由数据库中读取的数据以及必要的 HTML 字符串连接在一起。
- 把表现逻辑移到模板中能够提升程序的可维护性。模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染。
- 为了渲染模板，Flask 使用了一个名为 Jinja2 的强大模板引擎。

#### Jinja2模板引擎
- 默认模板存放于与程序文件同目录下templates文件夹下
- 生成两个模板文件：
	- index.html：<code>&lt;h1>Hello World!</h1&gt;</code>
	- uaer.html:<code>&lt;h1>Hello, {{ name }}!</h1&gt;</code>

##### 渲染模板
新的hello.py，3.1版本：        
```python
from flask import Flask
from flask import render_template
from flask.ext.script import Manager

app = Flask(__name__)

manger = Manager(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manger.run()
```
- Flask 提供的 render_template 函数把 Jinja2 模板引擎集成到了程序中。
- render_template 函数的第一个参数是模板的文件名。
- 随后的参数都是键值对，表示模板中变量对应的真实值。在这段代码中，第二个模板收到一个名为 name 的变量。
- 左边的“name”表示参数名，就是模板中使用的占位符；右边的“name”是当前作用域中的变量，表示同名参数的值

##### 变量
- 在模板中使用的 {{ name }} 结构表示一个变量，它是一种特殊的占位符，告诉模板引擎这个位置的值从渲染模板时使用的数据中获取。
- Jinja2 能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。
- 示例

	```html
	<p>A value from a dictionary: {{ mydict['key'] }}.</p>
	<p>A value from a list: {{ mylist[3] }}.</p>
	<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
	<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
	```
- 可以使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔。例如，下述模板以首字母大写形式显示变量 name 的值：<code>Hello, {{ name|capitalize }}</code>
- Jinja2 提供的部分常用过滤器

<table><tr><td>过滤器名</td><td>说　　明</td></tr><tr><td>safe</td><td>渲染值时不转义</td></tr><tr><td>capitalize</td><td>把值的首字母转换成大写，其他字母转换成小写</td></tr><tr><td>lower</td><td>把值转换成小写形式</td></tr><tr><td>upper</td><td>把值转换成大写形式</td></tr><tr><td>title</td><td>把值中每个单词的首字母都转换成大写</td></tr><tr><td>trim</td><td>把值的首尾空格去掉</td></tr><tr><td>striptags</td><td>渲染之前把值中所有的 HTML 标签都删掉</td></tr></table>


>safe 过滤器值得特别说明一下。默认情况下，出于安全考虑，Jinja2 会转义所有变量。例如，如果一个变量的值为 '\<h1\>Hello\</h1\>'，Jinja2 会将其渲染成 '\&lt;h1\&gt;Hello\&lt;/h1\&gt;'，浏览器能显示这个 h1 元素，但不会进行解释。很多情况下需要显示变量中存储的 HTML 代码，这时就可使用 safe 过滤器。       
[完整的过滤器列表](http://jinja.pocoo.org/docs/templates/#builtin-filters)

##### 控制结构
- 可用来改变模板的渲染流程
1. 条件控制

	```
	{% id user%}
	    Hello, {{ user }}!
	{% else %}
	    Hello, Stranger!
	{% endif%}
	```

2. for循环

	```
	<ul>
	    {% for comment in comments %}
	    <li>{{ comment }}</li>
	    {% endfor %}
	</ul>
	```

3. 宏（类似函数）
	- 直接定义


	```
	{% macro render_comment(comment) %}
	    <li>{{ comment }}</li>
	{% endmacro %}
	<ul>
	    {% for comment in comments %}
	    {{ render_comment(comment) }}
	    {% endfor %}
	</ul>
	```

	- 保存使用

	```
	{% import 'macros.html' as macros %}
	<ul>
	    {% for comment in comments %}
	    {{ macros.render_comment(comment) }}
	    {% endfor %}
	</ul>
	```

4. 将多出重复使用的模板代码写入文件，再包含在所有模板

	```
	{% include 'common.html' %}
	```

5. 模板继承
	- 基模板  block 标签定义的元素可在衍生模板中修改

	```html
	<html>
	<head>
	    {% block head %}
	    <title>{% block title %}{% endblock %} - My Application</title>
	    {% endblock %}
	</head>
	<body>
	    {% block body %}
	    {% endblock %}
	</body>
	</html>
	```

	- 衍生模板  extends 指令声明这个模板衍生自 base.html。在 extends 指令之后，基模板中的 3 个块被重新定义，模板引擎会将其插入适当的位置。注意新定义的 head 块，在基模板中其内容不是空的，所以使用 super() 获取原来的内容。

	```
	{% extends "base.html" %}
	{% block title %}Index{% endblock %}
	{% block head %}
	    {{ super() }}
	    <style>
	    </style>
	{% endblock %}
	{% block body %}
	<h1>Hello, World!</h1>
	{% endblock %}
	```

##### 使用Flask-Bootstrap集成Twitter Bootstrap
Bootstrap（http://getbootstrap.com/）是 Twitter 开发的一个开源框架，它提供的用户界面组件可用于创建整洁且具有吸引力的网页，而且这些网页还能兼容所有现代 Web 浏览器。       
Bootstrap 是客户端框架，因此不会直接涉及服务器。服务器需要做的只是提供引用了Bootstrap 层叠样式表（CSS） 和 JavaScript 文件的 HTML 响 应， 并 在 HTML、CSS 和JavaScript 代码中实例化所需组件。这些操作最理想的执行场所就是模板。              
要想在程序中集成 Bootstrap，显然要对模板做所有必要的改动。不过，更简单的方法是使用一个名为 Flask-Bootstrap 的 Flask 扩展，简化集成的过程。
Flask-Bootstrap 使用 pip安装：<code>(venv) $ pip install flask-bootstrap</code>     
Flask 扩展一般都在创建程序实例时初始化:       

```python
from flask.ext.bootstrap import Bootstrap
# ...
bootstrap = Bootstrap(app)
```
初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。这个模板利用 Jinja2 的模板继承机制，让程序扩展一个具有基本页面结构的基模板，其中就有用来引入 Bootstrap 的元素。
示例 3-5 是把 user.html 改写为衍生模板后的新版本。

```html
{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle"
                    data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}
{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
```
基模板中定义了可在衍生模板中重定义的块。block 和 endblock 指令定义的块中的内容可添加到基模板中。       
上面这个 user.html 模板定义了 3 个块，分别名为 title、navbar 和 content。这些块都是基模板提供的，可在衍生模板中重新定义。title 块的作用很明显，其中的内容会出现在渲染后的 HTML 文档头部，放在 <title> 标签中。navbar 和 content 这两个块分别表示页面中的导航条和主体内容。

新的hello.py，3.2版本     
```python
from flask import Flask
from flask import render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

manger = Manager(app)
bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manger.run()
```

### web 表单
### 数据库
### 实现电子邮件
### 适用于大中型程序的结构


## 实例：社交博客程序





















<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
<script>$("code").css('color', '#D05');$("code").css('padding','0 4px');$("code").css('background','#fafafa');$("code").css('border','1px solid #ddd');</script>
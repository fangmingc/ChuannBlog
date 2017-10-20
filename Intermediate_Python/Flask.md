# Flask学习
教程：
- Flask Web开发：基于Python的Web应用开发实战
- Flask Web Development:Developing Web Applications with Python
- [美] Miguel Grinberg 著
- 安道 译

## 目录
- [了解Flask](#1.0)
- [1 起步](#2.0)
	- [1.1 安装和设置Flask框架](#2.1)
	- [1.2 程序的基本结构](#2.2)
		- [\* 路由和视图函数](#2.2.2)
		- [\* 请求−响应循环](#2.2.6)
	- [1.3 flask中的模板](#2.3)
		- [\* Jinja2模板引擎](#2.3.2)
	- [1.4 Web表单](#2.4)
	- [1.5 数据库](#2.5)
- []()
- []()
- []()
- 







## 遇到的问题
- 栈跟踪？





## <span id="1.0">了解Flask</span>
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


## <span id="2.0">1 起步</span>
### <span id="2.1">1.1 安装和设置Flask框架</span>
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

### <span id="2.2">1.2 程序的基本结构</span>
#### 初始化
- 所有 Flask 程序都必须创建一个程序实例。
- Web 服务器使用一种名为 Web 服务器网关接口（Web Server Gateway Interface，WSGI）的协议，把接收自客户端的所有请求都转交给这个对象处理。
- 程序实例是 Flask 类的对象，经常使用下述代码创建

	```python
	from flask import Flask
	app = Flask(__name__)
	```

- Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python 的 __name__ 变量就是所需的值。

#### <span id="2.2.2">路由和视图函数
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


#### <span id="2.2.6">请求−响应循环</span>
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
	from flask_script import Manager
	manager = Manager(app)
	# ...
	if __name__ == '__main__':
	    manager.run()
	```

	- 专为 Flask 开发的扩展都暴漏在 flask.ext 命名空间下。Flask-Script 输出了一个名为Manager 的类，可从 flask_script 中引入。
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

### <span id="2.3">1.3 flask中的模板</span>
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

#### <span id="2.3.2">Jinja2模板引擎</span>
- 默认模板存放于与程序文件同目录下templates文件夹下
- 生成两个模板文件：
	- index.html：<code>&lt;h1>Hello World!</h1&gt;</code>
	- uaer.html:<code>&lt;h1>Hello, {{ name }}!</h1&gt;</code>

##### 渲染模板
新的hello.py，3.1版本：        
```python
from flask import Flask
from flask import render_template
from flask_script import Manager

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

5. **模板继承**
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

	- **衍生模板**  extends 指令声明这个模板衍生自 base.html。在 extends 指令之后，基模板中的 3 个块被重新定义，模板引擎会将其插入适当的位置。注意新定义的 head 块，在基模板中其内容不是空的，所以使用 super() 获取原来的内容。

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
from flask_bootstrap import Bootstrap
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
from flask_script import Manager
from flask_bootstrap import Bootstrap

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
Flask-Bootstrap 的 base.html 模板还定义了很多其他块，都可在衍生模板中使用。表3-2列出了所有可用的块。      
表3-2 Flask-Bootstrap基模板中定义的块        
<table><tr><th>块　　名</th><th>说　　明</th></tr><tr><td>doc</td><td>整个 HTML 文档</td></tr><tr><td>html_attribs</td><td>&lt;html> 标签的属性</td></tr><tr><td>html</td><td>&lt;html> 标签中的内容</td></tr><tr><td>head</td><td>&lt;head> 标签中的内容</td></tr><tr><td>title</td><td>&lt;title> 标签中的内容</td></tr><tr><td>metas</td><td>一组 &lt;meta> 标签</td></tr><tr><td>styles</td><td>层叠样式表定义</td></tr><tr><td>body_attribs</td><td>&lt;body> 标签的属性</td></tr><tr><td>body</td><td>&lt;body> 标签中的内容</td></tr><tr><td>navbar</td><td>用户定义的导航条</td></tr><tr><td>content</td><td>用户定义的页面内容</td></tr><tr><td>scripts</td><td>文档底部的 JavaScript 声明</td></tr></table>

大部分是bootstrap自用的，如果程序需要向已经有内容的块中添加新内容，必须使用 Jinja2 提供的 super() 函数。例如，如果要在衍生模板中添加新的 JavaScript 文件，需要这么定义 scripts 块：       
```html
{% block scripts %}
{{ super() }}
<script type="text/javascript" src="my-script.js"></script>
{% endblock %}
```

#### 自定义错误页面
如果你在浏览器的地址栏中输入了不可用的路由，那么会显示一个状态码为 404 的错误页面。现在这个错误页面太简陋、平庸，而且样式和使用了 Bootstrap 的页面不一致。     
像常规路由一样，Flask 允许程序使用基于模板的自定义错误页面。最常见的错误代码有两个：404，客户端请求未知页面或路由时显示；500，有未处理的异常时显示。     

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def internal_sever_error(e):
    return render_template('500.html'),500
```
和视图函数一样，错误处理程序也会返回响应。它们还返回与该错误对应的数字状态码。
错误处理程序中引用的模板也需要编写。这些模板应该和常规页面使用相同的布局，因此要有一个导航条和显示错误消息的页面头部。

- 编写这些模板最直观的方法是复制 templates/user.html,分别创建 templates/404.html, templates/500.html，然后把这两个文件中的页面头部元素改为相应的错误消息。但这种方法会带来很多重复劳动。


Jinja2 的模板继承机制可以帮助我们解决这一问题。Flask-Bootstrap 提供了一个具有页面基本布局的基模板，同样，程序可以**自定义**一个具有**更完整页面布局**的**基模板**，其中包含导航条，而页面内容则可留到衍生模板中定义。示例 3-7 展示了 templates/base.html 的内容，这是一个继承自 bootstrap/base.html 的新模板，其中定义了导航条。这个模板本身也可作为其他模板的基模板，例如 templates/user.html、templates/404.html 和 templates/500.html。

- 示例 3-7 templates/base.html：包含导航条的程序基模板：

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
	    {% block page_content %}{% endblock %}
	</div>
	{% endblock %}
	```

- 示例 3-8 templates/404.html：使用模板继承机制自定义 404 错误页面
	
	```html
	{% extends "base.html" %}
	{% block title %}Flasky - Page Not Found{% endblock %}
	{% block page_content %}
	<div class="page-header">
	    <h2>Page Not Found!</h2>
	    <a href="">Click to diagnose network.</a>
	</div>
	{% endblock %}
	```

- 示例 3-9 templates/user.html：使用模板继承机制简化页面模板

	```html
	{% extends "base.html" %}
	{% block title %}Flasky{% endblock %}
	{% block page_content %}
	<div class="page-header">
	    <h1>Hello, {{ name }}!</h1>
	    <h2>Welcome to your space!</h2>
	</div>
	{% endblock %}
	```

- 使用模板简化修改首页

	```html
	{% extends "base.html" %}
	{% block title %}Flasky{% endblock %}
	{% block page_content %}
	<div class="page-header">
	    <h1>Welcome to Flasky Blog.</h1>
	    <h3>Blog is under construction...</h3>
	    <h3>Please look forward to.</h3>
	</div>
	{% endblock %}
	```

#### 链接
任何具有多个路由的程序都需要可以连接不同页面的链接，例如导航条。

在模板中直接编写简单路由的 URL 链接不难，但对于包含可变部分的动态路由，在模板中构建正确的 URL 就很困难。而且，直接编写 URL 会对代码中定义的路由产生不必要的依赖关系。如果重新定义路由，模板中的链接可能会失效。

为了避免这些问题，Flask 提供了 url_for() 辅助函数，它可以使用程序 URL 映射中保存的信息生成 URL。

url_for() 函数最简单的用法是以视图函数名（或者 app.add_url_route() 定义路由时使用的端点名）作为参数，返回对应的 URL。例如，在当前版本的 hello.py 程序中调用 url_for('index') 得到的结果是 /。调用 url_for('index', _external=True) 返回的则是绝对地址，在这个示例中是 http://localhost:5000/。

>生成连接程序内不同路由的链接时，使用相对地址就足够了。如果要生成在浏览器之外使用的链接，则必须使用绝对地址，例如在电子邮件中发送的链接。

使用 url_for() 生成动态地址时，将动态部分作为关键字参数传入。例如，url_for('user', name='john', _external=True) 的返回结果是 http://localhost:5000/user/john。

>此处经过约一小时尝试，可以通过衍生base模板的scripts，利用JS，寻找a标签，通过设置a标签的href属性值来添加链接。commit信息chapter3.4

```python
# hello.py 修改代码
@app.route("/user/<name>")
def user(name):
    a_dict = {
        'a_home': url_for('index'),
        'a_me': url_for('user', name="World", _external=True),
    }
    return render_template('user.html', name=name, a_dict=a_dict)
```
```html
<!--base.html增加代码-->
{% block scripts %}
{{ super() }}
{% endblock %}
<!--user.html增加代码-->
{{ super() }}
<script>
    var a_arrs = document.getElementsByClassName('menu')[0].children;
    a_arrs[0].firstChild.setAttribute('href', '{{ a_dict["a_home"] }}');
    a_arrs[1].firstChild.setAttribute('href', '{{ a_dict["a_me"] }}');
</script>
{% endblock %}
```

#### 静态文件
Web 程序不是仅由 Python 代码和模板组成。大多数程序还会使用静态文件，例如 HTML代码中引用的图片、JavaScript 源码文件和 CSS。
你可能还记得在第 2 章中检查 hello.py 程序的 URL 映射时，其中有一个 static 路由。这是因为对静态文件的引用被当成一个特殊的路由，即 /static/<lename>。例如，调用url_for('static', filename='css/styles.css', _external=True) 得到的结果是 http://localhost:5000/static/css/styles.css。
默认设置下，Flask 在程序根目录中名为 static 的子目录中寻找静态文件。如果需要，可在static 文件夹中使用子文件夹存放文件。服务器收到前面那个 URL 后，会生成一个响应，包含文件系统中 static/css/styles.css 文件的内容。
- 示例 3-10 templates/base.html：定义收藏夹图标

	```html
	{% block head %}
	{{ super() }}
	<link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
	    type="image/x-icon">
	<link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}"
	    type="image/x-icon">
	{% endblock %}
	```

#### 使用Flask-Moment本地化日期和时间
如果 Web 程序的用户来自世界各地，那么处理日期和时间可不是一个简单的任务。     
服务器需要统一时间单位，这和用户所在的地理位置无关，所以一般使用协调世界时（Coordinated Universal Time，UTC）。不过用户看到 UTC 格式的时间会感到困惑，他们更希望看到当地时间，而且采用当地惯用的格式。        
要想在服务器上只使用 UTC 时间，一个优雅的解决方案是，把时间单位发送给 Web 浏览器，转换成当地时间，然后渲染。Web 浏览器可以更好地完成这一任务，因为它能获取用户电脑中的时区和区域设置。        
有一个使用 JavaScript 开发的优秀客户端开源代码库，名为 moment.js（http://momentjs.com/），它可以在浏览器中渲染日期和时间。Flask-Moment 是一个 Flask 程序扩展，能把moment.js 集成到 Jinja2 模板中。Flask-Moment 可以使用 pip 安装：<code>(venv) $ pip install flask-moment</code>  

- 示例 3-11 hello.py：初始化 Flask-Moment:

	```python
	from flask_moment import Moment
	moment = Moment(app)
	```

除了 moment.js，Flask-Moment 还依赖 jquery.js。要在 HTML 文档的某个地方引入这两个库，可以直接引入，这样可以选择使用哪个版本，也可使用扩展提供的辅助函数，从内容分发网络（Content Delivery Network，CDN）中引入通过测试的版本。Bootstrap 已经引入了 jquery.js，因此只需引入 moment.js 即可。示例 3-12 展示了如何在基模板的 scripts 块中引入这个库。
- 示例 3-12 templates/base.html：引入 moment.js 库

```html
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```
为了处理时间戳，Flask-Moment 向模板开放了 moment 类。示例 3-13 中的代码把变量current_time 传入模板进行渲染.
- 示例 3-13 hello.py：加入一个 datetime 变量

	```python
	from datetime import datetime
	@app.route('/')
	def index():
	    return render_template('index.html', current_time=datetime.utcnow())
	```

- 3-14 templates/index.html：使用 Flask-Moment 渲染时间戳

```html
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```
format('LLL') 根据客户端电脑中的时区和区域设置渲染日期和时间。参数决定了渲染的方式，'L' 到 'LLLL' 分别对应不同的复杂度。format() 函数还可接受自定义的格式说明符。         
第二行中的 fromNow() 渲染相对时间戳，而且会随着时间的推移自动刷新显示的时间。这个时间戳最开始显示为“a few seconds ago”，但指定 refresh 参数后，其内容会随着时间的推移而更新。如果一直待在这个页面，几分钟后，会看到显示的文本变成“a minute ago”“2 minutes ago”等。      
Flask-Moment 实现了 moment.js 中的 format()、fromNow()、fromTime()、calendar()、valueOf()和 unix() 方法。你可查阅文档（http://momentjs.com/docs/#/displaying/）学习 moment.js 提供的全部格式化选项。      
Flask-Moment 渲染的时间戳可实现多种语言的本地化。语言可在模板中选择，把语言代码传给 lang() 函数即可：{{ moment.lang('es') }}

### <span id="2.4">web 表单</span>
1.2中介绍的请求对象包含客户端发出的所有请求信息。其中，request.form 能获取POST 请求中提交的表单数据。         
尽管 Flask 的请求对象提供的信息足够用于处理 Web 表单，但有些任务很单调，而且要重复操作。比如，生成表单的 HTML 代码和验证提交的表单数据。           
Flask-WTF（http://pythonhosted.org/Flask-WTF/）扩展可以把处理 Web 表单的过程变成一种愉悦的体验。这个扩展对独立的 WTForms（http://wtforms.simplecodes.com）包进行了包装，方便集成到 Flask 程序中。
Flask-WTF 及其依赖可使用 pip 安装：<code>(venv) $ pip install flask-wtf</code>            

#### 　跨站请求伪造保护
默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造（Cross-Site Request Forgery，CSRF）的攻击。恶意网站把请求发送到被攻击者已登录的其他网站时就会引发 CSRF 攻击。      
为了实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成加密令牌，再用令牌验证请求中表单数据的真伪。    
- 示例 4-1 hello.py：设置 Flask-WTF:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
```
app.config 字典可用来存储框架、扩展和程序本身的配置变量。使用标准的字典句法就能把配置值添加到 app.config 对象中。这个对象还提供了一些方法，可以从文件或环境中导入配置值。

SECRET_KEY 配置变量是通用密钥，可在 Flask 和多个第三方扩展中使用。如其名所示，加密的强度取决于变量值的机密程度。不同的程序要使用不同的密钥，而且要保证其他人不知道你所用的字符串。

>为了增强安全性，密钥不应该直接写入代码，而要保存在环境变量中。

#### 表单类
使用 Flask-WTF 时，每个 Web 表单都由一个继承自 Form 的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。

- 示例 4-2 hello.py：定义表单类

```python
class NameForm(Form):
    """表单类"""
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
```

这个表单中的字段都定义为类变量，类变量的值是相应字段类型的对象。在这个示例中，NameForm 表单中有一个名为 name 的文本字段和一个名为 submit 的提交按钮。StringField类表示属性为 type="text" 的 <input> 元素。SubmitField 类表示属性为 type="submit" 的<input> 元素。字段构造函数的第一个参数是把表单渲染成 HTML 时使用的标号。

StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据。验证函数 Required() 确保提交的字段不为空。

>Form 基类由 Flask-WTF 扩展定义，所以从 flask_wtf 中导入。字段和验证函数却可以直接从 WTForms 包中导入。

- 表4-1 WTForms支持的HTML标准字段
<table><tr><th>字段类型</th><th>说　　明</th></tr><tr><td>StringField</td><td>文本字段</td></tr><tr><td>TextAreaField</td><td>多行文本字段</td></tr><tr><td>PasswordField</td><td>密码文本字段</td></tr><tr><td>HiddenField</td><td>隐藏文本字段</td></tr><tr><td>DateField</td><td>文本字段，值为 datetime.date 格式</td></tr><tr><td>DateTimeField</td><td>文本字段，值为 datetime.datetime 格式</td></tr><tr><td>IntegerField</td><td>文本字段，值为整数</td></tr><tr><td>DecimalField</td><td>文本字段，值为 decimal.Decimal</td></tr><tr><td>FloatField</td><td>文本字段，值为浮点数</td></tr><tr><td>BooleanField</td><td>复选框，值为 True 和 False</td></tr><tr><td>RadioField</td><td>一组单选框</td></tr><tr><td>SelectField</td><td>下拉列表</td></tr><tr><td>SelectMultipleField</td><td>下拉列表，可选择多个值</td></tr><tr><td>FileField</td><td>文件上传字段</td></tr><tr><td>SubmitField</td><td>表单提交按钮</td></tr><tr><td>FormField</td><td>把表单作为字段嵌入另一个表单</td></tr><tr><td>FieldList</td><td>一组指定类型的字段</td></tr></table>

- 表4-2 WTForms验证函数
<table><tr><th>验证函数</th><th>说　　明</th></tr><tr><td>Email</td><td>验证电子邮件地址</td></tr><tr><td>EqualTo</td><td>比较两个字段的值；常用于要求输入两次密码进行确认的情况</td></tr><tr><td>IPAddress</td><td>验证 IPv4 网络地址</td></tr><tr><td>Length</td><td>验证输入字符串的长度</td></tr><tr><td>NumberRange</td><td>验证输入的值在数字范围内</td></tr><tr><td>Optional</td><td>无输入值时跳过其他验证函数</td></tr><tr><td>Required</td><td>确保字段中有数据</td></tr><tr><td>Regexp</td><td>使用正则表达式验证输入值</td></tr><tr><td>URL</td><td>验证 URL</td></tr><tr><td>AnyOf</td><td>确保输入值在可选值列表中</td></tr><tr><td>NoneOf</td><td>确保输入值不在可选值列表中</td></tr></table>

#### 把表单渲染成HTML
表单字段是可调用的，在模板中调用后会渲染成 HTML。假设视图函数把一个 NameForm 实例通过参数 form 传入模板，在模板中可以生成一个简单的表单，如下所示

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>
```
当然，这个表单还很简陋。要想改进表单的外观，可以把参数传入渲染字段的函数，传入的参数会被转换成字段的 HTML 属性。例如，可以为字段指定 id 或 class 属性，然后定义 CSS 样式：

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```

即便能指定 HTML 属性，但按照这种方式渲染表单的工作量还是很大，所以在条件允许的情况下最好能使用 Bootstrap 中的表单样式。Flask-Bootstrap 提供了一个非常高端的辅助函数，可以使用 Bootstrap 中预先定义好的表单样式渲染整个 Flask-WTF 表单，而这些操作只需一次调用即可完成。使用 Flask-Bootstrap，上述表单可使用下面的方式渲染：

```html
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

import 指令的使用方法和普通 Python 代码一样，允许导入模板中的元素并用在多个模板中。导入的 bootstrap/wtf.html 文件中定义了一个使用 Bootstrap 渲染 Falsk-WTF 表单对象的辅助函数。wtf.quick_form() 函数的参数为 Flask-WTF 表单对象，使用 Bootstrap 的默认样式渲染传入的表单。

- 示例 4-3 templates/index.html：使用 Flask-WTF 和 Flask-Bootstrap 渲染表单

```html
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky{% endblock %}
{% block page_content %}
<div class="page-header">
    <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
</div>
{{ wtf.quick_form(form) }}
{% endblock %}
```

#### 在视图函数中处理表单
在新版 hello.py 中，视图函数 index() 不仅要渲染表单，还要接收表单中的数据。

- 示例 4-4 hello.py：路由方法

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
    form.name.data = ''
    return render_template('index.html', form=form, name=name)
```

app.route 修饰器中添加的 methods 参数告诉 Flask 在 URL 映射中把这个视图函数注册为GET 和 POST 请求的处理程序。如果没指定 methods 参数，就只把视图函数注册为 GET 请求的处理程序。

把 POST 加入方法列表很有必要，因为将提交表单作为 POST 请求进行处理更加便利。表单也可作为 GET 请求提交，不过 GET 请求没有主体，提交的数据以查询字符串的形式附加到URL 中，可在浏览器的地址栏中看到。基于这个以及其他多个原因，提交表单大都作为POST 请求进行处理。

局部变量 name 用来存放表单中输入的有效名字，如果没有输入，其值为 None。如上述代码所示，在视图函数中创建一个 NameForm 类实例用于表示表单。提交表单后，如果数据能被所有验证函数接受，那么validate_on_submit() 方法的返回值为 True，否则返回 False。这个函数的返回值决定是重新渲染表单还是处理表单提交的数据。

用户第一次访问程序时，服务器会收到一个没有表单数据的 GET 请求，所以 validate_on_submit() 将返回 False。if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对象和值为 None 的 name 变量作为参数。用户会看到浏览器中显示了一个表单。

用户提交表单后，服务器收到一个包含数据的 POST 请求。validate_on_submit() 会调用name 字段上附属的 Required() 验证函数。如果名字不为空，就能通过验证，validate_on_submit() 返回 True。现在，用户输入的名字可通过字段的 data 属性获取。在 if 语句中，把名字赋值给局部变量 name，然后再把 data 属性设为空字符串，从而清空表单字段。最后一行调用 render_template() 函数渲染模板，但这一次参数 name 的值为表单中输入的名字，因此会显示一个针对该用户的欢迎消息。

#### 重定向和用户会话
最新版的 hello.py 存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。如果这个请求是一个包含表单数据的 POST 请求，刷新页面后会再次提交表单。大多数情况下，这并不是理想的处理方式。

很多用户都不理解浏览器发出的这个警告。基于这个原因，最好别让 Web 程序把 POST 请求作为浏览器发送的最后一个请求。

这种需求的实现方式是，使用重定向作为 POST 请求的响应，而不是使用常规响应。重定向是一种特殊的响应，响应内容是 URL，而不是包含 HTML 代码的字符串。浏览器收到这种响应时，会向重定向的 URL 发起 GET 请求，显示页面的内容。这个页面的加载可能要多花几微秒，因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，最后一个请求是 GET 请求，所以刷新命令能像预期的那样正常使用了。这个技巧称为 Post/ 重定向 /Get 模式。

但这种方法会带来另一个问题。程序处理 POST 请求时，使用 form.name.data 获取用户输入的名字，可是一旦这个请求结束，数据也就丢失了。因为这个 POST 请求使用重定向处理，所以程序需要保存输入的名字，这样重定向后的请求才能获得并使用这个名字，从而构建真正的响应。

程序可以把数据存储在用户会话中，在请求之间“记住”数据。用户会话是一种私有存储，存在于每个连接到服务器的客户端中。我们在第 2 章介绍过用户会话，它是请求上下文中的变量，名为 session，像标准的 Python 字典一样操作。

默认情况下，用户会话保存在客户端 cookie 中，使用设置的 SECRET_KEY 进行加密签名。如果篡改了 cookie 中的内容，签名就会失效，会话也会随之失效。

- 示例 4-5 hello.py：重定向和用户会话

```python
from flask import Flask, render_template, redirect, session, url_for
# 将视图函数注册为GET和POST请求的处理函数，默认为GET
@app.route("/", methods=['GET', 'POST'])
def index():
    """起始页面"""
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    form.name.data = ''
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
```

在程序的前一个版本中，局部变量 name 被用于存储用户在表单中输入的名字。这个变量现在保存在用户会话中，即 session['name']，所以在两次请求之间也能记住输入的值。

>现在，包含合法表单数据的请求最后会调用 redirect() 函数。redirect() 是个辅助函数，用来生成 HTTP 重定向响应。redirect() 函数的参数是重定向的 URL，这里使用的重定向URL 是程序的根地址，因此重定向响应本可以写得更简单一些，写成 redirect('/')，但却会使用 Flask 提供的 URL 生成函数 url_for()。推荐使用 url_for() 生成 URL，因为这个函数使用 URL 映射生成 URL，从而保证 URL 和定义的路由兼容，而且修改路由名字后依然可用。

url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。默认情况下，路由的端点是相应视图函数的名字。在这个示例中，处理根地址的视图函数是index()，因此传给 url_for() 函数的名字是 index。

最后一处改动位于 render_function() 函数中，使用 session.get('name') 直接从会话中读取 name 参数的值。和普通的字典一样，这里使用 get() 获取字典中键对应的值以避免未找到键的异常情况，因为对于不存在的键，get() 会返回默认值 None。

#### Flash消息
请求完成后，有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错误提醒。一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新渲染了登录表单，并在表单上面显示一个消息，提示用户用户名或密码错误。**这种功能是 Flask 的核心特性**。

- 示例 4-6 hello.py：Flash 消息

```python
from flask import Flask, render_template, redirect, session, url_for, flash
# 将视图函数注册为GET和POST请求的处理函数，默认为GET
@app.route("/", methods=['GET', 'POST'])
def index():
    """起始页面"""
    form = NameForm()
    old_name = ''
    if form.validate_on_submit():
        old_name = session.get('name')
    if old_name is not None and old_name != form.name.data:
        flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
```

在这个示例中，每次提交的名字都会和存储在用户会话中的名字进行比较，而会话中存储的名字是前一次在这个表单中提交的数据。如果两个名字不一样，就会调用 flash() 函数，在发给客户端的下一个响应中显示一个消息。仅调用 flash() 函数并不能把消息显示出来，程序使用的模板要渲染这些消息。最好在基模板中渲染 Flash 消息，因为这样所有页面都能使用这些消息。Flask 把 get_flashed_messages() 函数开放给模板，用来获取并渲染消息，如示例 4-7 所示。

- 示例 4-7 templates/base.html：渲染 Flash 消息

```html
{% block content %}
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-warning">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        {{ message }}
    </div>
    {% endfor %}
    {% block page_content %}{% endblock %}
</div>
{% endblock %}
```

在模板中使用循环是因为在之前的请求循环中每次调用 flash() 函数时都会生成一个消息，所以可能有多个消息在排队等待显示。get_flashed_messages() 函数获取的消息在下次调用时不会再次返回，因此 Flash 消息只显示一次，然后就消失了。

### 数据库
### 实现电子邮件
### 适用于大中型程序的结构


## 实例：社交博客程序





















<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>
<script>$("code").css('color', '#D05');$("code").css('padding','0 4px');$("code").css('background','#fafafa');$("code").css('border','1px solid #ddd');</script>
# Flask
轻量级、短小精悍、丰富的第三方组件

## 使用前
- 安装：pip install flask
- flask和django区别：
	- django:无socket、中间件、路由系统、视图(CBV,FBV)、模板、ORM、cookie、session、admin、form、缓存、信号、序列化、.....
	- flask:无socket、中间件(需要扩展)、路由系统、视图(CBV)、第三方模板(jinja2)、cookie、session弱
	- 请求相关数据传递方式
		- Django传参
		- flask基于Local和LocalStack的上下文管理(详细见下文)

- 什么是wsgi
	- web服务网关接口，协议
- flask依赖一个实现了WSGI协议的模块：werkzeug模块


- [开始使用](fisrt_flask.md)
- [flask基础](basis_of_flask.md)
- [wtforms快速使用和源码分析](wtforms.md)
	- [自定义一个form组件](diy_form.md)
- 数据库选择
	- 原生SQL，借助[数据库连接池](database_connection_pool.md)
	- ORM，借助[flask-sqlalchemy](flask-sqlalchemy.md)
- [flask-script](flask-script.md)

- flask原理剖析
	- 请求如何达到flask？[源码理解：从app.run到app.\_\_call__](analyze_principle_of_flask.md)
	- 处理请求的准备工作
		- [上下文管理](context_management.md)
			- 本地线程
		- [flask信号](singal_of_flask.md)
			- blinker
			- 对比Django信号
		- [session](session.md)
			- flask-session
	- [处理请求的过程]()
		- 中间件
		- 视图函数
		- 模板渲染
	- [返回响应]()
	- flask扩展点

flask最难的就是local和stack完成上下文管理

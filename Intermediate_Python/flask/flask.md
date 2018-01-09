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


- [开始使用](Intermediate_Python/flask/fisrt_flask.md)
- [flask基础](Intermediate_Python/flask/flask基础.md)
- [上下文管理(重要)](Intermediate_Python/flask/上下文管理.md)
- [数据库连接池](Intermediate_Python/flask/数据库连接池.md)
- [flask原理剖析](Intermediate_Python/flask/Flask原理剖析.md)






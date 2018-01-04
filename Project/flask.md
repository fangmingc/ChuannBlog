# Flask
轻量级、短小精悍、丰富的第三方组件

## 使用前
- 安装：pip install flask
- 比较：
	- django:无socket、中间件、路由系统、视图(CBV,FBV)、模板、ORM、cookie、session、admin、form、缓存、信号、序列化、.....
	- flask:无socket、中间件(需要扩展)、路由系统、视图(CBV)、第三方模板(jinja2)、cookie、session弱

- 什么是wsgi
	- web服务网关接口，协议
- flask依赖一个实现了WSGI协议的模块：werken模块

## 开始使用
```
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
		- mport_name，当前flask项目启动文件
		- static_url_path=None，静态文件目录的别名，用于模板中反向指定静态文件
		- static_folder='static'，静态文件目录
		- template_folder='templates'，模板文件目录
		- root_path=None，项目根目录，默认为flask项目启动文件所在目录
	- 额外配置
		- secret_key，当使用了session时需要，flask的session是通过密钥加密session数据发送到浏览器保存
	- route

## 路由系统

## 视图函数

## 请求和响应

## 



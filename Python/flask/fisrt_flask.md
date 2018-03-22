## fisrt FLask
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
		- import_name，通常使用当前flask项目启动文件名，不固定
		- static_url_path=None，静态文件目录的别名，用于模板中反向指定静态文件，格式'/xxx'
		- static_folder='static'，静态文件目录
		- template_folder='templates'，模板文件目录
		- root_path=None，项目根目录，默认为flask项目启动文件所在目录
		- instance_path=None,
		- instance_relative_config=False
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
## 自定义Form组件
- 为深入理解wtforms组件，参考其源码制作的简陋from组件。
- 可实现form自动生成html标签，自动校验，获取校验成功值。

### 组件代码
```python
from flask import Markup


# Form
class BaseForm(object):
    """
    表单类，所有自定义form必须至少继承该类。
    """

    def __init__(self, data=None, init_data=None):
        # 获取当前所有字段
        _fields = {}
        for name, field in self.__class__.__dict__.items():
            if isinstance(field, Field):
                field.name = name
                field.input_type = field.widgt.input_type
                _fields[name] = field
        self._fields = _fields

        # 当有预设值
        if init_data:
            self.init_data = dict(init_data)
        else:
            self.init_data = None

        # 当有校验值
        if data:
            temp = {}
            for item in data:
                temp.setdefault(item, data.getlist(item))
            self.data = temp
            self.init_data = dict(temp)

        # 校验成功值
        self.safe_data = {}

        if self.init_data:
            for k1, v1 in self.init_data.items():
                for k2, v2 in self._fields.items():
                    if k1 == k2:
                        if isinstance(v1, list):
                            v2.value = v1[0]
                        else:
                            v2.value = v1
        else:
            for field in self._fields.values():
                field.value = ""

    def validate(self):
        """找到所有字段，执行每个自带你的validate方法"""
        flag = True
        for name, field in self._fields.items():
            input_val = self.data.get(name)
            result = field.validate(input_val)
            if not result:
                flag = False
            else:
                self.safe_data.setdefault(name, input_val[0])
            print(name, field, input_val, result)
        return flag


# 插件
class Widget(object):
    """
    插件类，所有插件类必须至少继承该类。
    """

    def __call__(self, field, **kwargs):
        """生成input标签"""
        return Markup("<input type='{0}' name='{1}' value='{2}'>".format(field.input_type, field.name, field.value))


class TextInput(Widget):
    input_type = "text"


class EmailInput(Widget):
    input_type = "email"


class PasswordInput(Widget):
    input_type = "password"


# 字段
class Field(object):
    """
    字段类，所有字段必须至少继承该类。
    """
    widgt = None

    def __str__(self):
        return self()

    def __call__(self, *args, **kwargs):
        raise Exception("未重写")

    def validate(self, value):
        raise Exception("未实现")


class CharField(Field):
    widgt = TextInput()

    def __call__(self, *args, **kwargs):
        return self.widgt(self)

    def validate(self, value):
        if value:
            return True


class EmailField(Field):
    widgt = TextInput()
    regex = ".*@.*"

    def __call__(self, *args, **kwargs):
        return self.widgt(self)

    def validate(self, value):
        import re
        if re.match(self.regex, value):
            return True


class PasswordField(Field):
    widgt = PasswordInput()

    def __call__(self, *args, **kwargs):
        return self.widgt(self)

    def validate(self, value):
        if value:
            return True
```

### 使用
#### python代码
```python
from flask import request, session, render_template, redirect

import myforms

class MyLoginForm(myforms.BaseForm):
    """
    登录表单
    """
    username = myforms.CharField()
    password = myforms.PasswordField()


@auth.route("/login", methods=['GET', "POST"])
def login():
    if request.method == "GET":
        form = forms.MyLoginForm()
        return render_template("auth/login.html", form=form)
    else:
        form = forms.MyLoginForm(data=request.form)
        if form.validate():
            if form.safe_data["username"] == "alex" and form.safe_data["password"] == "123456":
                print(form.safe_data)
                session["user"] = {
                    "username": form.safe_data['username'],
                }
                return redirect("/index")
            else:
                return render_template("auth/login.html", form=form)
        else:
            return render_template("auth/login.html", form=form)
```

#### 模板代码
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
    <h1>登录页面</h1>
    <div class="col-md-4">
        <form action="" method="post">
            <p>{{form.username.label}}{{form.username}}</p>
            <p>{{form.password.label}}{{form.password}}</p>
            <p><input type="submit" class="btn"></p>
        </form>
    </div>
</div>
</body>
</html>
``` 


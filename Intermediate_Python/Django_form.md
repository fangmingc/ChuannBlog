## Django表单组件
### 什么是form组件

### 功能有什么
- 用户请求验证
- 自动生成HTML标签（保留上次输入）
- 集成错误信息

### 使用流程
#### 基本使用
1. 定义类
	- 需要继承django.forms.Form
2. 设置字段
	- 从django.forms.fields获取字段类型，应当和和models中定义的类相似
	- 其中的参数为校验类型
		- required:是否为空
		- min_length:最小长度
		- max_length:最大长度
	- error_messages
		- 校验不通过显示的错误信息，不设置则使用django自带的错误信息
		- 格式为字典，key为错误类型，value为错误信息
			- required:为空
			- invalid：值无效
	- widget
		- 设置在模板中使用的html样式
		- 必须通过django.forms.widgets调用

	```python
	from django.forms import Form
	from django.forms import fields
	from django.forms import widgets
	class LoginForm(Form):
	    username = fields.CharField(
	        required=True,
	        error_messages={
	            "required": "用户名不能为空！"
	        },
	        widget=widgets.TextInput(attrs={
	            "placeholder": "Username"
	        }))
	    password = fields.CharField(
	        required=True,
	        error_messages={
	            "required": "密码不能为空！"
	        },
	        widget=widgets.PasswordInput(attrs={
	            "placeholder": "Password"
	        }))
	```
3. 在模板中使用
	- 直接{{ form }}将全部
	- form.errors.username 错误信息有可能不止一条，这里选择获取第一条

	```html
	<p>用户名:{{ form.username }}{{ form.errors.username.0 }}</p>
	<p>密码:{{ form.password }}{{ form.errors.password.0 }}</p>
	```

4. 实例化
	- 全参数：form = LoginForm(data=None, files=None, auto_id='id_%s', prefix=None,initial=None, error_class=ErrorList, label_suffix=None,empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None)
	- data,传入的数据用于校验，
	- initial，给表单中的input便签赋初始值，通常和模板一起渲染返回需要初始值的页面（编辑页面）

5. is_valid()
	- 校验函数，返回校验结果，布尔值

6. cleaned_data&errors
	- cleaned_data，存储校验成功的值
	- errors，存储校验失败的值

#### 扩展
1. 定义form组件字段中的值传入的参数，可以使用：
	- validators=[RegexVlidator("xxx")]
	- 通常用于自定义的一些正则表达式校验
	- from django.core.validators import RegexValidator, ValidationError
2. 局部钩子函数
	- 定义form组件时，可以额外定义的函数，用于form组件校验流程完毕之后自定义的校验
	- 不通过则主动抛异常ValidationError("xxx")
	- 定义格式
		- clean_字段名
	- 注意事项
		- 必须有返回值，
		- 只能取当前字段，不能跨字段取值
	- djago源码支持:django.forms.BaseForm

	```python
	def _clean_fields(self):
	    for name, field in self.fields.items():
	        # value_from_datadict() gets the data from the data dictionaries.
	        # Each widget type knows how to retrieve its own data, because some
	        # widgets split data over several HTML fields.
	        if field.disabled:
	            value = self.get_initial_for_field(field, name)
	        else:
	            value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
	        try:
	            if isinstance(field, FileField):
	                initial = self.get_initial_for_field(field, name)
	                value = field.clean(value, initial)
	            else:
	                value = field.clean(value)
	            self.cleaned_data[name] = value
	            # ##############################
	            if hasattr(self, 'clean_%s' % name):
	                value = getattr(self, 'clean_%s' % name)()
	                self.cleaned_data[name] = value
	            # ##############################
	        except ValidationError as e:
	            self.add_error(name, e)
	```
	- 使用示例

	```python
	def clean_username(self):
	    """钩子函数"""
	    user = self.cleaned_data["username"]
	    is_exist = models.User.objects.filter(username=user).count()
	    if not is_exist:
	        raise ValidationError("用户名不存在！")
	    return user
	```
3. 全局钩子函数
	- 局部钩子函数验证结束后进行全局的校验，在这里可以从cleaned_data取到所有已经验证过的数据进行多项联合校验，如注册时验证两次密码是否一致
	- 务必返回clean_data

```python
def clean(self):
    """全局校验"""
    if self.cleaned_data.get("password") != self.cleaned_data.get("repeat_password"):
        self.add_error("repeat_password", "两次密码不一致！")
    return self.cleaned_data
```

4. 数据源实时更新
	1. 重写构造方法（\_\_init__）
		- 注意继承父类的构造方法
		- 推荐使用此方法，因为数据源可以与不直接操作数据库

	```python
	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields["目标字段"].choices = [(1,111),(2,222)...]或ORM的values_list返回值
	```

	2. ModelChoiceField，在定义form组件时使用

	```python
	from django.forms.models import ModelChoiceField
	    cls = ModelChoiceField(
	        queryset=models.Classes.objects.all(),
	        widget=widgets.Select()
	    )
	```

### 模板中使用
- 生成单个input框
	- form.字段
- 生成所有标签
	- form
	- form.as_p
	- form.as_ul
	- form.as_table


### 实例：博客项目的注册
```python
class RegisterForm(Form):
    """
    注册表单
    """
    email = fields.EmailField(
        required=True,
        error_messages={
            "required": "邮箱不能为空！",
            "invalid": "邮箱格式错误！",
        },
        widget=widgets.TextInput(attrs={
            "class": "form-control",
            "placeholder": "请输入您的邮箱地址",
            "id": "email",
        }),
    )
    username = fields.CharField(
        required=True,
        max_length=32,
        min_length=3,
        error_messages={
            "required": "用户名不能为空！",
            "max_length": "用户名过长!",
            "min_length": "用户名过短！"
        },
        widget=widgets.TextInput(attrs={
            "class": "form-control",
            "placeholder": "请输入用户名，必须是字母、数字、下划线、'-'组成",
            "id": "username",
        }),
    )
    password = fields.CharField(
        required=True,
        max_length=32,
        min_length=6,
        error_messages={
            "required": "密码不能为空！",
            "max_length": "密码过长!",
            "min_length": "密码过短！"
        },
        widget=widgets.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "请输入密码",
            "id": "password",
        }),
    )
    repeat_password = fields.CharField(
        required=True,
        max_length=32,
        min_length=6,
        error_messages={
            "required": "密码不能为空！",
            "max_length": "密码过长!",
            "min_length": "密码过短！"
        },
        widget=widgets.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "请再次输入密码",
            "id": "repeat_password",
        })
    )
    nickname = fields.CharField(
        required=True,
        min_length=2,
        error_messages={
            "required": "昵称不能为空！",
            "min_length": "昵称过短！"
        },
        widget=widgets.TextInput(attrs={
            "class": "form-control",
            "placeholder": "请输入昵称",
            "id": "nickname",
        }),
    )
    phone = fields.CharField(
        required=True,
        error_messages={
            "required": "手机号不能为空！",
        },
        widget=widgets.TextInput(attrs={
            "class": "form-control",
            "placeholder": "请输入手机号",
            "id": "phone",
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from app01.models import User
        self.user = User

    def clean(self):
        """全局校验"""
        # 校验两次密码是否一致
        if not self.cleaned_data.get("password") == self.cleaned_data.get("repeat_password"):
            self.add_error("repeat_password", "两次密码不一致")

        return self.cleaned_data

    def clean_email(self):
        """邮箱验证"""
        email = self.cleaned_data.get("email")
        if self.user.objects.filter(userinfo__email=email):
            raise ValidationError("该邮箱已注册！")
        else:
            return email

    def clean_username(self):
        """校验用户名"""
        username = self.cleaned_data.get("username")
        user = self.user.objects.filter(username=username)
        if user:
            raise ValidationError("用户名已存在！")
        from re import search
        if len(search("[\w-]*", username).group()) != len(username):
            raise ValidationError("用户名只能是数字、字母、下划线和'-'组成！")
        return username

    def clean_password(self):
        """校验密码"""
        from re import findall
        password = self.cleaned_data.get("password")
        if findall("\d+", password) and findall("[a-zA-Z]+", password):
            return password
        raise ValidationError("密码必须包含数字和字母")

    def clean_phone(self):
        """校验手机号"""
        from re import findall
        phone = self.cleaned_data.get("phone")
        if phone and len(phone) == 11:
            if findall("^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$", phone):
                if self.user.objects.filter(userinfo__phone=phone):
                    raise ValidationError("该手机号已注册！")
                else:
                    return phone
            else:
                raise ValidationError("请输入正确的手机号！")
        else:
            raise ValidationError("手机号必须是11位！")
```


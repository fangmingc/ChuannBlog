## wtforms
- [开始使用](#1)
- [源码分析](#2)
	- [项目加载form类所在模块](#21)
	- [在视图函数中实例化form类](#22)
	- [模板渲染调用form的字段](#23)
	- [前端填好数据，返回后端校验](#24)

- 和django的form组件大同小异，下面给出一个应用举例以便快速查询。

### <span id='1'>开始使用</span>
```python
from flask import Flask, render_template, request, redirect

from wtforms import Form

from wtforms.fields import core
from wtforms.fields import html5
from wtforms.fields import simple

from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder='templates')
app.debug = True

class MyValidator(object):
    def __init__(self,message):
        self.message = message
    def __call__(self, form, field):
        print(field.data)
        if field.data == '王浩':
            return None
        raise validators.StopValidation(self.message)


class LoginForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            # MyValidator(message='用户名必须等于王浩')
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'}
    )
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('login.html', form=form)


# ########################### 用户注册 ##########################
class RegisterForm(Form):
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired()
        ],
        widget=widgets.TextInput(),
        render_kw={'class': 'form-control'},
        default='alex'
    )

    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('pwd', message="两次密码输入不一致")
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )

    email = html5.EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label='性别',
        choices=(
            (1, '男'),
            (2, '女'),
        ),
        coerce=int
    )
    city = core.SelectField(
        label='城市',
        choices=(
            ('bj', '北京'),
            ('sh', '上海'),
        )
    )

    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )

    favor = core.SelectMultipleField(
        label='喜好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))

    def validate_pwd_confirm(self, field):
        """
        自定义pwd_confirm字段规则，例：与pwd字段是否一致
        :param field: 
        :return: 
        """
        # 最开始初始化时，self.data中已经有所有的值

        if field.data != self.data['pwd']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        # 设置默认值
        form = RegisterForm(data={'gender': 1})
        return render_template('register.html', form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():
            print('用户提交数据通过格式验证，提交的值为：', form.data)
        else:
            print(form.errors)
        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
```


### <span id='2'>源码分析</span>
- 高级用法
	- metaclass的另类使用
- 切入点：
	- 当定义好一个自定义的form类，项目加载form类所在模块，代码都做了什么？
	- 在视图函数中实例化form类，代码都做了什么？
		- 模板渲染调用form的字段时，代码做了什么？
	- 前端填好数据，返回后端校验时，代码做了什么？

#### 详细分析
1. <span id='21'>项目加载form类所在模块</span>
	- form类
		- 这是声明Form的代码：`class Form(with_metaclass(FormMeta, BaseForm))`
		- 可见这里调用一个函数with_metaclass
			
			```python
			def with_metaclass(meta, base=object):
			    return meta("NewBase", (base,), {})
			```
		- 该函数返回了一个FormMeta元类创建的NewBase类作为Form类的基类
		- 元类创建类会执行元类的\_\_init__方法
	
			```python
			def __init__(cls, name, bases, attrs):
			    type.__init__(cls, name, bases, attrs)
			    cls._unbound_fields = None
			    cls._wtforms_meta = None
			```
		- 此处为Form类定义了_unbound_fields和_wtforms_meta两个静态字段
	- 类的字段
		- 拿一个字段举例：`username = simple.StringField()`
		- 可见是实例化了一个StringField类
			- StringField类定义了一个静态字段：`widget = widgets.TextInput()`
				- 这里是实例化了一个插件类TextInput
					- TextInput类定义了一个静态字段：`input_type = 'text'`指定生成html标签时的type
					- 基类中的\_\_init__方法只是将检测了一下input_type
			- StringField类没有\_\_init__方法，\_\_new__方法，显然要从基类中寻找
				- 基类中的\_\_new__方法返回的是：`UnboundField(cls, *args, **kwargs)`实例化了一个UnboundField类的对象

					```python
					creation_counter = 0
					def __init__(self, field_class, *args, **kwargs):
					    UnboundField.creation_counter += 1
					    self.field_class = field_class
					    self.args = args
					    self.kwargs = kwargs
					    self.creation_counter = UnboundField.creation_counter
					```
					- 可见UnboundField类封装了字段的类StringField，并给了字段一个编号，看来wtforms应该就是通过这个编号来识别字段的顺序
				- 基类中的\_\_init__方法
					- 有意思的是此时\_\_init__的接收的self已经不是Field类的实例，而是UnboundField类的实例
					- init这里大部分操作都是常规的赋值操作，不过也有个值得关注的地方
						- `if _translations is not None: self._translations = _translations`
							- 通过这两行代码可以看出，wtforms内部还实现了实现了多语言的提示信息
		- 最后得出结论，form类的静态字段如username此时存储的是UnboundField类的实例
2. <span id='22'>在视图函数中实例化form类</span>
	- 首先执行元类的\_\_call__方法

		```python
		def __call__(cls, *args, **kwargs):
		    """
		    Construct a new `Form` instance.
		
		    Creates the `_unbound_fields` list and the internal `_wtforms_meta`
		    subclass of the class Meta in order to allow a proper inheritance
		    hierarchy.
		    """
		    if cls._unbound_fields is None:
		        fields = []
		        for name in dir(cls):
		            if not name.startswith('_'):
		                unbound_field = getattr(cls, name)
		                if hasattr(unbound_field, '_formfield'):
		                    fields.append((name, unbound_field))
		        # We keep the name as the second element of the sort
		        # to ensure a stable sort.
		        fields.sort(key=lambda x: (x[1].creation_counter, x[0]))
		        cls._unbound_fields = fields
		
		    # Create a subclass of the 'class Meta' using all the ancestors.
		    if cls._wtforms_meta is None:
		        bases = []
		        for mro_class in cls.__mro__:
		            if 'Meta' in mro_class.__dict__:
		                bases.append(mro_class.Meta)
		        cls._wtforms_meta = type('Meta', tuple(bases), {})
		    return type.__call__(cls, *args, **kwargs)
		```
		- 这里就是给form类的_unbound_fields和_wtforms_meta赋值
			- 使用`dir(cls)`获取form类的所有变量字符串，当其不为'_'开头时说明是自定义form的字段，获取字段的对应的对象，根据字段的编号排序后加入_unbound_fields列表
				- 此处的判断做的还不够好，或许通过`cls.__dict__.items()`获取到所有的变量名和值，判断值是否为UnboundField的实例，若为UnboundField的实例则加入列表
			- 使用\_\_mro__获取form类所有的继承关系，挨个寻找这些类中的Meta字段对应的类计入bases列表，最后通过type一次型创建一个继承了所有bases列表中的类的Meta类，并存入_wtforms_meta字段
	- 接着应该执行类的\_\_new__方法，不过这里没有定义，忽略此步骤
	- 然后执行类的\_\_init__方法
		
		```python
		def __init__(self, formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
		    meta_obj = self._wtforms_meta()
		    if meta is not None and isinstance(meta, dict):
		        meta_obj.update_values(meta)
		    super(Form, self).__init__(self._unbound_fields, meta=meta_obj, prefix=prefix)
		
		    for name, field in iteritems(self._fields):
		        setattr(self, name, field)
		    self.process(formdata, obj, data=data, **kwargs)
		```
		- 这里首先实例化了_wtforms_meta字段对应的Meta类然后传入了基类的\_\_init__方法
	
			```python
			def __init__(self, fields, prefix='', meta=DefaultMeta()):
			    if prefix and prefix[-1] not in '-_;:/.':
			        prefix += '-'
			
			    self.meta = meta
			    self._prefix = prefix
			    self._errors = None
			    self._fields = OrderedDict()
			
			    if hasattr(fields, 'items'):
			        fields = fields.items()
			
			    translations = self._get_translations()
			    extra_fields = []
			    if meta.csrf:
			        self._csrf = meta.build_csrf(self)
			        extra_fields.extend(self._csrf.setup_form(self))
			
			    for name, unbound_field in itertools.chain(fields, extra_fields):
			        options = dict(name=name, prefix=prefix, translations=translations)
			        field = meta.bind_field(self, unbound_field, options)
			        self._fields[name] = field
			```
			- prefix是设置生成html标签的name属性的值的前缀
			- meta是一个继承了form类以及所有form类继承的类中的Meta类的实例
				- 这里检测了是否启用了csrf字段
				- 并将meta中额外定义的有关csrf的字段加入extra_fields
			- 最后将fields和extra_fields中所有的字段全部放置在form类实例的_fields字段中
				- 这里通过`field = meta.bind_field(self, unbound_field, options)`对所有的UnboundField类实例做了处理，找回了原有的Field
		- 然后将类中的_fields表中的字段设置为form类实例的属性
			- 注意：此时的字段已经变回了原来的Field，尚不明确为何要多进行这样的操作
		- 这行代码主要是针对有数据传入时的操作`self.process(formdata, obj, data=data, **kwargs)`
			- 在第4点详细查看
3. <span id='23'>模板渲染调用form的字段</span>
	- 此时本质上就是调用了字段的\_\_str__方法，把返回的字符串放置在模板

		```python
		def __str__(self):
		    """
		    Returns a HTML representation of the field. For more powerful rendering,
		    see the `__call__` method.
		    """
		    return self()
		```
	- 转为调用字段的__call__方法

		```python
		def __call__(self, **kwargs):
		    """
		    Render this field as HTML, using keyword args as additional attributes.
		
		    This delegates rendering to
		    :meth:`meta.render_field <wtforms.meta.DefaultMeta.render_field>`
		    whose default behavior is to call the field's widget, passing any
		    keyword arguments from this call along to the widget.
		
		    In all of the WTForms HTML widgets, keyword arguments are turned to
		    HTML attributes, though in theory a widget is free to do anything it
		    wants with the supplied keyword arguments, and widgets don't have to
		    even do anything related to HTML.
		    """
		    return self.meta.render_field(self, kwargs)
		```
	- 继续调用Meta类的render_field方法,这个方法在DefaultMeta类

		```python
		def render_field(self, field, render_kw):
		    """
		    render_field allows customization of how widget rendering is done.
		
		    The default implementation calls ``field.widget(field, **render_kw)``
		    """
		    other_kw = getattr(field, 'render_kw', None)
		    if other_kw is not None:
		        render_kw = dict(other_kw, **render_kw)
		    return field.widget(field, **render_kw)
		```
	- 这里调用了字段的插件对象的\_\_call__方法

		```python
		def __call__(self, field, **kwargs):
		    kwargs.setdefault('id', field.id)
		    kwargs.setdefault('type', self.input_type)
		    if 'value' not in kwargs:
		        kwargs['value'] = field._value()
		    return HTMLString('<input %s>' % self.html_params(name=field.name, **kwargs))
		```
	- 至此，完成了Form类实例的\_\_str__方法，返回了一个HTML的input标签的字符串
4. <span id='24'>前端填好数据，返回后端校验</span>
	- 依然是实例化一个Form类的对象，大部分流程和第2点讨论的一致，不过在执行到Form类的\_\_init__方法的最后一行时开始不同
		- `self.process(formdata, obj, data=data, **kwargs)`
	
			```python
			def process(self, formdata=None, obj=None, data=None, **kwargs):
			    formdata = self.meta.wrap_formdata(self, formdata)
			
			    if data is not None:
			        kwargs = dict(data, **kwargs)
			
			    for name, field, in iteritems(self._fields):
			        if obj is not None and hasattr(obj, name):
			            field.process(formdata, getattr(obj, name))
			        elif name in kwargs:
			            field.process(formdata, kwargs[name])
			        else:
			            field.process(formdata)
			```
		- 这里根据传入的数据不同做不同的操作
			- `formdata = self.meta.wrap_formdata(self, formdata)`是将不具有getlist方法的formdata的对象封装一个getlist对象
			- field.process函数就是将数据封装进self.data和self.row_data
				```python
				def process(self, formdata, data=unset_value):
				    self.process_errors = []
				    if data is unset_value:
				        try:
				            data = self.default()
				        except TypeError:
				            data = self.default
				
				    self.object_data = data
				
				    try:
				        self.process_data(data)
				    except ValueError as e:
				        self.process_errors.append(e.args[0])
				
				    if formdata:
				        try:
				            if self.name in formdata:
				                self.raw_data = formdata.getlist(self.name)
				            else:
				                self.raw_data = []
				            self.process_formdata(self.raw_data)
				        except ValueError as e:
				            self.process_errors.append(e.args[0])
				
				    try:
				        for filter in self.filters:
				            self.data = filter(self.data)
				    except ValueError as e:
				            self.process_errors.append(e.args[0])
				```
	- 然后调用form.validate方法
		
		```python
		def validate(self):
		    extra = {}
		    for name in self._fields:
		        inline = getattr(self.__class__, 'validate_%s' % name, None)
		        if inline is not None:
		            extra[name] = [inline]
		    return super(Form, self).validate(extra)
		```
		- 把每个字段的校验规则封装进extra
	- 然后调用BaseForm的validate()

		```python
		def validate(self, extra_validators=None):
		    self._errors = None
		    success = True
		    for name, field in iteritems(self._fields):
		        if extra_validators is not None and name in extra_validators:
		            extra = extra_validators[name]
		        else:
		            extra = tuple()
		        if not field.validate(self, extra):
		            success = False
		    return success
		```
	- 然后挨个调用字段的校验方法完成校验





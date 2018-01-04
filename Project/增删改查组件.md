## ORM增删改查组件
- 参考django admin源码
- 启动django项目的流程
- 路由系统
- 单例模式

### django admin
- 路由系统
	- /admin/app01/role/
	- /admin/app01/add/
	- /admin/app01/1/change/
	- /admin/app01/1/delete/
- 如何使用：
	- http://www.cnblogs.com/wupeiqi/articles/7444717.html
- 原理
	- 路由关系
	- 对应视图函数


### 启动django项目的流程
1. 运行每一个app下的admin.py并加载
	- app01.admin.py
		- 创建admin.site中的对象
		- 执行对象的registry方法，目的:将注册的类添加到_registry
	- app02.admin.py
		- 用app01.admin中已经创建的admin.site对象
		- 执行对象的registry方法，目的:将注册的类添加到_registry
	- admin.site是一个对象（单例模式创建），其中封装了：
		- _registry = {xxx,bbb,...}


### 
#### 启动项目时自定义需要执行的文件
- 在组件app下的apps.py的AppConfig类中定义ready方法

	```python
	def ready(self):
	    from django.utils.module_loading import autodiscover_modules
	    autodiscover_modules('stark')
	```

#### 路由系统


#### 定制展示


#### 编辑和删除定制


#### 添加/删除按钮


#### 分页


#### 组合搜索


#### popUp
- 功能简述
	- 在添加或修改页面，当有外键或多对多字段时，可以通过按钮，弹出一个小的窗口，该窗口为该字段所外键的表新增url，在小窗口增加完毕可以直接自行关闭回到主页面，并在该字段自动选中新增选项
- 实现流程
	- 主页面可以点击弹出新的窗口
		- 后端
			- 当为选项字段时生成可点击按钮，url为该字段所外键的表的新增url
			- 此处使用了templaetags
		
			```python
			from django.shortcuts import reverse
			from django.template import Library
			from django.forms.models import ModelChoiceField
			
			from automodel.services.automodel import site
			
			register = Library()
			
			
			@register.inclusion_tag("automodel/form.html")
			def add_change_form(model_form):
			    new_form = []
			    for bfield in model_form:
			        temp = {"field": bfield, "is_popup": False}
			        # 判断是否是有外键的字段
			        if isinstance(bfield.field, ModelChoiceField):
			            model_class = bfield.field.queryset.model
			            # 确保外键的表已注册
			            if model_class in site._registry:
			                temp["is_popup"] = True
			                app_model_name = model_class.model._meta.app_label, model_class._meta.model_name
			                temp["pop_url"] = reverse("automodel:{0[0]}_{0[1]}_add".format(app_model_name))
			        new_form.append(temp)
			    return {"form": new_form}
			```

		- 前端
			- window.open(URL,name,features,replace)
			- js
			
			```javascript
			function popUpCallback(data) {
			    var aim_obj = document.getElementById(data.popup_id);
			    var new_option = document.createElement("option");
			    new_option.innerHTML = data.text;
			    new_option.setAttribute("value", data.pk);
			    new_option.setAttribute("selected", "selected");
			    aim_obj.appendChild(new_option)
			}
			function popUp(url) {
			    window.open(url, "popup", "status=1, width=700, height=500, left=400, top=150")
			}
			```

	- 在新的窗口可以新增数据并保存
		- 新增数据流程不变
		- 新增完毕需要返回新增数据
			- 后端

			```python
			if request.GET.get("_popupkey"):
			    data = {"pk": new_obj.pk, "text": str(new_obj), "popup_id": request.GET.get("_popupkey")}
			
			    return render(request, "automodel/pop_response.html", {"json_data": json.dumps(data)})
			```

			- html+js

			```html
			<!DOCTYPE html>
			<html lang="en">
			<head>
			    <title>正在关闭...</title>
			</head>
			<body>
			<script>
			    (function () {
			        opener.popUpCallback({{ json_data|safe }});
			        window.close()
			    })()
			</script>
			</body>
			</html>
			```


	- 保存完毕自动关闭新窗口，将新增数据返回到主页面并展示

##### 补充
- window.open(URL,name,features,replace)
	- URL，可选字符串，生命要在新窗口中显示的文档的URL
	- name，可选字符串，声明新窗口的名称，若窗口已存在，则返回对指定窗口的引用， features会被忽略
	- features，可选字符串，声明了新窗口要显示的标准浏览器的特征，如果省略，新窗口将具有所有标准的特征

	<table class="dataintable"><tr>
	<td>channelmode=yes|no|1|0</td>
	<td>是否使用剧院模式显示窗口。默认为 no。</td>
	</tr><tr>
	<td>directories=yes|no|1|0</td>
	<td>是否添加目录按钮。默认为 yes。</td>
	</tr><tr>
	<td>fullscreen=yes|no|1|0</td>
	<td>是否使用全屏模式显示浏览器。默认是 no。处于全屏模式的窗口必须同时处于剧院模式。</td>
	</tr><tr><td>height=pixels</td>
	<td>窗口文档显示区的高度。以像素计。</td>
	</tr><tr><td>left=pixels</td>
	<td>窗口的 x 坐标。以像素计。</td>
	</tr><tr><td>location=yes|no|1|0</td>
	<td>是否显示地址字段。默认是 yes。</td>
	</tr><tr><td>menubar=yes|no|1|0</td>
	<td>是否显示菜单栏。默认是 yes。</td>
	</tr><tr><td>resizable=yes|no|1|0</td>
	<td>窗口是否可调节尺寸。默认是 yes。</td>
	</tr><tr><td>scrollbars=yes|no|1|0</td>
	<td>是否显示滚动条。默认是 yes。</td>
	</tr><tr><td>status=yes|no|1|0</td>
	<td>是否添加状态栏。默认是 yes。</td>
	</tr><tr><td>titlebar=yes|no|1|0</td>
	<td>是否显示标题栏。默认是 yes。</td>
	</tr><tr><td>toolbar=yes|no|1|0</td>
	<td>是否显示浏览器的工具栏。默认是 yes。</td>
	</tr><tr><td>top=pixels</td><td>窗口的 y 坐标。</td>
	</tr><tr><td>width=pixels</td>
	<td>窗口的文档显示区的宽度。以像素计。</td></tr></table>

	- replace，可选布尔值
		- true-替换浏览历史中的当前条目
		- false-在浏览历史中创建信封条目
- opener.func_name(...)
	- 此语句应运行
	- func_name为主页面的回调函数


### 总结
- 单例
	- 文件导入
	- 类
- 面向对象
	- 遇到封装数据：使用字典，对象
	- 遇到循环数据：使用字典，元组，列表，可迭代对象
	- 遇到后台对数据加工再在页面中循环展示：处理再循环，生成器构造边循环边生产
- request.GET
	- s
- 类
	- 组件
		- AutomodelSite
		- AutomodelConfig
		- ShowList
		- FilterOption
		- FilterRow
	- 使用
		- 定义好model类
			- class UserInfo(models.Modal):...
		- 在app中新建automodel.py
			- class UserModelForm(forms.ModelForm):...
			- class UserInfoConfig(AutomodelConfig):
				- model_class




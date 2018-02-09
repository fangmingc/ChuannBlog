## Django路由系统--URL的分发和映射(urls.py)

- 路由系统
	- 主要解析URl的路径，并将请求送往相应的视图函数
	- 结构：
	```
	urlpatterns = {
		url("^blog/", views.bolg)
	}
	```
- url(regex, view, kwargs=None, name=None)
	- 建立起URL与视图函数的映射关系
	- 正则表达式：匹配url中的路径
	- 视图函数：view
	- 别名name:正则匹配的路径的别名
- 注意
	- 出现覆盖URL，只匹配第一个视图函数
	- 无名分组
		- 正则表达式中使用分组^blog/(\d{4})/(\d{2})
		- 将匹配到的分组数据按位置传参给视图函数
	- 有名分组
		- 正则表达式中使用命名分组^blog/(?P<year>\d{4})/(?P<month>\d{2})
		- 将匹配到的分组数据按关键字传参给视图函数
	- URL分发
		- url(r'^blog/', include('blog.urls'))
		- urls为blog应用文件夹下的urls.py
	- 反向查询
		- 在模板中使用<code>{百分号 url "别名" [[参数1] ...] 百分号}</code>，表示此处为指定别名代表的路径
			- 参数可以是值(1)或键值对(a=1)
		- 当修改路径时可以自动同步
		- 在视图函数中，反向指定url，使用reverse
			- from django.shortcuts import reverse
			- reverse("别名")
			- reverse("别名",args=(11,))
			- reverse("别名",kwargs={'nid':11})
	- [练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/URLconf)
- 特殊路由
	- media配置

		```python
		from django.views.static import serve
		from django.conf import settings
		urlpatterns = [
		    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
		]
		```

### django2.0特性
- django.urls下的re_path代替了url
- 但原url仍然可用


### 进阶：url分发
- include



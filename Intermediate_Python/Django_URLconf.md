## Django--URL的分发和映射(urls.py)
结构：
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
		- 在模板中使用<code>{% url "别名" %}</code>，表示此处为指定别名代表的路径
		- 当修改路径时可以自动同步

[练习文件](https://github.com/fangmingc/Python/tree/master/Frame/Django/URLconf)
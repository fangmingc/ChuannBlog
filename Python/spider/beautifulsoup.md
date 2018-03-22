## beautifulsoup
```python
pip3 install beautifulsoup4
```
- [官方文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

### 语法
- soup = BeautifulSoup(markup="", features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, **kwargs)
	- markup,可以是html字符串，也可以是文件句柄
	- features，指定解析格式，官方推荐lxml(需要安装)，默认html5
- soup.prettify()
	- 自动补全未闭合标签，并美化格式
- soup.tag_name
	- 寻找第一个tag_name标签
	- soup.tag_name.text， 标签文本内容
	- soup.tag_name.atts["attr_name"], 标签属性内容
	- soup.tag_name.tag_name2....，深入层级
	- soup.tag_name.children，标签子节点
	- soup.tag_name.descendants
	- soup.tag_name.parent
	- soup.tag_name.parents

#### 搜索文档树
- 搜索方法
	- find_all(name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)，找所有符合条件的
		- name，指定标签名
		- attrs，指定标签属性
		- text,指定文本内容
		- kwargs,可以使用class_,id....等属性
	- find()，找一个符合条件的
- 过滤器，指搜索方法时的条件内容
	- 字符串
		- 完全匹配
		- soup.find_all(name="a", attrs={"class": "link"})，寻找类为link的a标签
	- 正则
		- re.compile('正则表达式')
		- soup.find_all(name=re.compile('^b')),寻找标签名以b开头的标签	
	- 列表
		- 列表为其他过滤器的组合，逻辑条件为或，即满足列表中一个条件即可
		- soup.find_all(name=['a', re.compile('^b')]), 寻找a标签或b开头的标签
	- True
		- soup.find_all(name=True),找到所有的标签
		- soup.find_all(attr={"id": True}),找到有id属性的标签
	- 方法
		- 需求：找到有class属性但是没有id属性的a标签

		```python
		def has_class_not_id(tag):
		    return tag.name == "a" and tag.has_attr('class') and not tag.has_attr("id")
		soup.find_all(name=has_class_not_id)
		```
#### CSS选择器
- soup=BeautifulSoup(html_doc,'lxml')
- soup.select("CSS选择器语法")
	- 层叠使用，soup.select(".c1").select(".c2")
	- 获取属性，attrs
	- 获取文本内容，get_text()






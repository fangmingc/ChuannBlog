## CRM项目问答
- 为什么开发CRM(客户关系管理系统)
	- 给自己公司用
		- 原来人少通过excel保存各种资料
		- 人员和部门增加之后，主要目的是直接给销售使用，将部分逻辑自动化处理
			- 销售管理
				- 分配订单
				- 订单失效(3天，15天)
				- 销售数据
				- 数据留存--回访、跟踪调查--为了二次销售
			- 学校管理
				- 以前保留作业之类的都是用的excel，一个sheet算一天，
				- 学校
				- 课程
				- 班级
				- 上课
				- 作业/作业成绩
				- 题库
			- 会议室预定
			- 满意度调查（调查问卷）
- 开发周期
	- 公司接到任务需要评估开发周期
		- 大概需要多久多久，具体的日期还需要进一步评估，后面确定了再回复
		- eg:预计2周，技术点有些不太确定，先进行评估然后再给老大明确答案
	- CRM:开发用了2个月，又2个月持续还在做修复bug和新功能的开发
	- 一般都要两个阶段
		- 开发阶段，只开发业务
		- 项目维护和扩展，抽离组件以后便于其他系统快速应用
- 技术点
	- 你的业务有多少张表？有哪些字段？
		- 权限
		- CRM业务
		- 满意度调查
		- 会议室预订
	- 有没有遇到坑？令你印象深刻的事情？你觉得写的比较吊的功能？
		- 组合搜索时，生成URL
			- request.GET
			- 深拷贝
			- 可迭代对象
			- yield
			- 面向对象封装
		- popup
			- window.open("", 'name')
				- popup打开一个窗口
			- opener.xxxxx()
				- 回调popup之前的页面的函数
			- FK时，可以使用limit_choice_to
				- 引用另外一张表的时候添加条件，可以是字典或Q对象
			- 生成popup时把related_name和model_name写进url
			- popup新增成功后，通过新增对象获取所有的方向关联字段，获取limit_choice_to字段
			- 判断新增对象是否满足条件
		- excel批量导入
		- 路由系统
			- 动态生成URL
			- 看的Django-admin的源码，参考着写的
			- 路由生成时，URL对应的就是一个元组
				- URL列表，namespace, app_name
				- URL列表又是一个个的URL，可以继续嵌套来完成路由系统的分发
		- 开发组件时，不明白为什么源码里配置时，总是使用了get，后来才知道要和权限管理配合着使用


### 知识点总结
1. 通过ShowList封装数据
2. 销售中公共资源：Q查询实现的3天15天的查询
3. 使用yield
	- 生成器函数实现数据的二次加工，前端使用时少循环一次
	- \_\_iter__和yield配合
4. 获取model类的字段对应的对象
	- Models.UserInfo.get_field("username")
5. 模糊搜索
	- 实例化Q
	- 设置Q.connector = 'OR'
	- 使用Q.children.append()添加搜索条件
6. Type创建类
	- 动态生成ModelForm
7. 自动派单
	- 内存中实现时，重启和多进程都有问题
	- redis
		- 状态
		- 原来数据，数据库销售权重表取来的数据(权重和个数)
		- pop数据
8. 使用list_display配置
	- 可以使用字段，函数
	- list_display = [dispaly_username, "eamil"]
9. reverse方向生成URL
	- "namespace1:namespace2:别名"
10. 模板的继承
11. ready方法定制起始文件
	- 文件导入实现单例模式
12. inclusion_tag
	- 可以生成html代码
13. 中间件的使用
	- 中间件类
		- 常用process_request，process_response
		- 
14. importlib + getattr
	- 获取字符串，通过切割，使用import_module导入模块
	- 使用getattr获取模块内的类
15. FileterOption，接受lambda表达式的函数
	- text_func_name
16. QueryDict的使用
	- 保留原搜索条件
	- 组合搜索时filter
17. ModelForm
18. 面向对象:
	- property
		- @property
		- property(get_func,set_func)
	- classmethod
		- 实现单例模式
19. mark_safe
	- XSS攻击
20. 接口类
	- 抽象方法/抽象类
	- 基类定义方法，抛出异常
21. 组件中的装饰器，使self.request = request
22. JS自执行函数
	- (function func(arg))('arg')
23. URL的钩子函数
24. 多继承
25. 批量导入/批量保存，xlrd
26. redis连接池
27. 工厂模式，importlib+反射

	```
	settings.py
		MSG_PATH = "path.Email"
	class XXFactory(object):
		@classmethod
		def get_obj(cls):
			settings.MSG_PATH
			# rsplit
			# importlib.import_module
			# return obj
	/path/
		class Email(object):
			def send ...
	/path2/
		class WeChat(object):
			def send ...
	```
28. Models类中重写save方法
	- 为每个新创建用户分配ID
29. admin装饰器注册model类
30. 深浅拷贝
	- 深拷贝
	- 浅拷贝
	- copy.copy()
	- copy.deepcopy()





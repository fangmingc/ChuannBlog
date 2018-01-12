## Python 进阶
本部分为Python进阶知识。

- [模块进阶](Advanced_Module.md)
- [网络编程](Network_Programming.md)
- [并发编程](Concurrent_Programming.md)

### 版本控制工具
- [Git](Git.md)

### 框架
#### Web应用框架(Web application framework)
- [Django](django/Django.md)
- [Flask](flask/flask.md)
- Tornado

#### 什么是框架？
1. DRY原则
	- Don't Repeat Yourself，不要重复你的代码。
	- 顺序结构->循环结构->函数->类型->组合类
2. 设计模式
	- 设计模式是经过长时间编码之后，经过系统性的总结所提出的针对某一类问题的最佳解决方案，又称之为最佳实践
	- 小规模的编码工作中，其实并不需要什么设计模式，只有大型程序才有设计模式发挥的空间 
	- 框架是设计模式的集大成者，将大型程序中的大量重复性代码精简封装，仅提供接口(API)，使程序员专注于业务逻辑，仅写不同于其他程序的代码
3. 框架需要对基础知识有足够的了解才能使用，否则遇到问题不清楚细节，无法自行排查解决。 
4. [写一个Web框架](DIY_Frame.md)

#### 数据库的使用
- 操作数据库的两种方式
	- [原生SQL](http://chuann.cc/Database/MySQL.html)
	- ORM
		- Django这个框架有自带的ORM：[Django模型层](http://chuann.cc/Intermediate_Python/django/Django_model.html)
		- [SQLAlchemy](SQLAlchemy.md)比较通用，适用于多个框架
		- 优点
			- 使用方便
			- 省却大量的sql语句
		- 缺点
			- 可能有速度上的缺陷
			- 难以构造复杂的sql语句




## Django Content-Type
- django提供的一种优化表结构的解决方案

- 问题，以路飞学城项目为例：
	- 学位课程表
		- id,name,period,scholarship,special_teacher
	- 普通课程表
		- id,name,period,level,order,status
	- 现在为两种课程制定价格策略，通常的思路是新建两张表
		- 学位课程价格策略
			- id,学位课程id,时长,价格
		- 普通课程价格策略
			- id,普通课程id,时长,价格
	- 需求总结：
		- 多张不同表都有相同的额外需求
- 



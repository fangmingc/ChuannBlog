# 权限管理系统

## tips
- python所有项目名都应该是小写
- 

## 需求
### 初稿
- 老男孩员工管理
	- 设计表描述四个角色：学生，老师（用户名和密码），班主任（用户名和密码），班级关系
	- 创建表
	- 具体功能：
		- 不登录不能访问（除login页面），session，不能用auth模块
		- 老师列表，把所有老师列出来，
			- 添加老师，
			- 查看老师详细（年龄，姓名，电话，薪资）- 任教班级
			- 删除老师
			- 修改老师
		- 班级列表
			- 增删改查
		- 学生列表
			- 添加学生
			- 查看学生详细（班级，）
- 时间
	- 2：00~3：00整理知识点
	- 3：30~4：30设计表
	- 5：00~5：30models，老师列表页面
	- 6：30~写功能
	- 不使用bootstrap
	- 睡觉前回顾学习内容

#### 设计表
- 用户表
	- id
	- username,16字符，用户民
	- password，32字符，密码
	- identity，8字符，身份
	- realname，8字符，姓名
	- age，整数，年龄
	- phone_num，11字符，手机号
	- salary，8位数，两位小数，薪水
	- create_time，时间
- 学生表
	- id
	- name,16字符，姓名
	- education,8字符，学历
	- qq，12位字符，qq号
	- phone_num，11位字符，手机号
	- class，外键，班级
- 班级表Class
	- id
	- name，16字符，班级名
	- teachers，M2M,关联老师
	- classteacher,外键，班主任


- 数据库设计
	- 属性相同归类到一张表
	- 联表有性能消耗
		- 联表设计
			- a
		- 单表设计
			- b
	- 一张表中对同一个其他表做FK,M2M时，需要使用related name

## 

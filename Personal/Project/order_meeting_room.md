## 会议室预定
### 需求分析

### 知识点

### 功能分析
#### 用户登录
- session
- 签名cookie
- 主动设置超时时间

#### 判断用户是否登陆
- 装饰器
- 中间件

#### 功能分析
- 获取并显示数据
	- 模板数据
	- 返回页面，ajax获取数据
- 发送数据
	- Form表单提交
	- Ajax提交

#### 数据库设计
- 用户表User
	- username
	- password
- 会议室表Room
	- title
	- container
- 记录表Record
	- owner
	- date	日期（精确到天）
	- room_id
	- block (每天时间块)
		- choice=((1, "08:00-09:00"), (2, "09:00-10:00"),...)
	- date、room_id、block联合唯一

#### 功能设计
- 页面
- 数据提交



- [代码]()


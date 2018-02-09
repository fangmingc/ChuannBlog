# 实战项目
## 知识梗概
### 前置知识
- 基本数据类型
- 函数（装饰器，迭代器，生成器）
- 面向对象（封装、继承、多态）
- 网络编程（socket）
	- 本质上就是在操纵(发送/接收)字节
	- 为什么不是字符串？
		- python3中字符串是Unicode，压缩后发送效率更高，字节对是通过某种编码格式编码后的bytes类型
		- python2中字符串是就是字节，字符串前面加上u之后就成了Unicode类型
		- python2中直接就是发送的字符串（字节）
		- python2和python3的字符串/字节的表现形式不一样

- 进程/线程/协程

- 数据库，必会ORM，必会设计表，知道sql查询语句
	- 设计表：
		- 单表
		- ForeignKey
		- ManyToMany

- 前端（会用bootstrap）

- Django知识
	- 参考

## 权限管理系统
- [总览](ManageAuthority.md)

## 博客系统
- [总览](blog/README.md)
- [表设计](blog/表设计.md)
- [验证码](blog/验证码.md)
- [优化查询](blog/优化查询.md)

- [email](email.md)


## crm
- [CRM](CRM/README.md)

### 问卷调查
- [总览](questionnaire.md)

### 会议室预定
- [总览](order_meeting_room.md)






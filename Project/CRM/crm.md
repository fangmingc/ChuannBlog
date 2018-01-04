# CRM
## 表结构

- 部门表
- 用户表
- 销售相关
	- 客户表（分配时间，最后跟进时间，当前正在沟通的销售）
		- 跟进记录表
	- 客户分配表
	- 销售量和权重表
- 教学相关
	- 上课记录表

- 学校表
	- 课程表
		- 班级表

	- 支付记录表
	- 学生表
		- 学习记录表





- 部门表Department
	- title 部门表
	- code 部门编号
- 用户表Userinfo
	- name 员工姓名
	- username 用户名
	- password 密码
	- email 邮箱
	- depart 部门 外键部门表
- 课程表Course
	- name
- 学校表School
	- title
- 班级表ClassList
	- school
	- course
	- semester
	- price
	- start_date
	- graduate_date
	- memo
	- teachers
	- tutor
- 客户表Customer
	- qq
	- name
	- gender
	- education
	- graduation_school
	- major
	- experience
	- work_status
	- company
	- salary
	- source
	- referral
	- course
	- status
	- consultant
	- recv_data
	- last_consult_date
	- date
- 客户分配表CustomerDistribution
	- user
	- customer
	- ctime
	- status
	- memo
- 销售权重和数量SaleRank
	- user
	- num
	- weight
- 跟进记录表ConsultRecord
	- customer
	- consultant
	- date
	- note
- 支付记录表PaymentRecord
	- customer
	- class_list
	- pay_type
	- paid_fee
	- turnover
	- quote
	- note
	- date
	- consultant
- 学生表Student
	- customer
	- username
	- password
	- emergency_contract
	- class_list
	- company
	- location
	- salary
	- location
	- position
	- salary
	- welfare
	- date
	- memo
- 上课记录表CourseRecord
	- class_obj
	- day_num
	- teacher
	- date
	- course_title
	- course_memo
	- has_homework
	- homework_memo
	- exam
- 学习记录表StudyRecord
	- course_Record
	- student
	- record
	- score
	- homework_note
	- note
	- homework
	- stu_memo
	- date




##

- 对象，找到反向关联的所有字段
	- obj.related_objects 返回对象的外键关系对象
	

- models.Userinfo._meta
	- app_label
	- model_name
	- get_field('字段名') 根据字段名获取字段对象
	- fields 获取类中所有的字段
	- _get_fields() 获取类中所有的字段(包含反向关联的字段)
	- many_to_many 获取M2M字段


## 学习记录



##






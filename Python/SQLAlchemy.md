## SQLAlchemy
- [SQLAlchemy结构](#1)
- [借助SQLAlchemy执行原生SQL](#2)
- [ORM](#3)
	- [表操作](#31)
	- [记录操作](#32)
- [扩展](#4)
	- [sqlalchemy_utils](#41)


### <span id="1">SQLAlchemy结构</span>
- 上层的是对象关系模型(Object Relational Mapper)
	- 类对应表，对象对应记录，对象属性对应记录值
- 下层是SQLAlchemy的核心，分三块
	- 模式(Schema/Type)
	- SQL语句翻译(SQl Expression Language)
	- 框架引擎(Engine),这里又分为两部分
		- Connection Pooling 数据库连接池
		- Dialect,选择DB API种类
- SQLAlchemy自身无法操作数据库，需要借助DB API，如pymysql，mysqldb，cx_oracle等

<img src="http://chuann.cc/Intermediate_Python/sqlalchemy.png">
- 使用不同DB API连接数据库

	```python
	from sqlalchemy import create_engine
	
	engine = create_engine(name_or_url)
	```
	- MySQL-Python
		- mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
	- pymysql
		- mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
	- MySQL-Connector
		- mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
	- cx_Oracle
		- oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
	- [更多](http://docs.sqlalchemy.org/en/latest/dialects/index.html)

### <span id='2'>借助SQLAlchemy执行原生SQL</span>
```python 
import threading
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:@127.0.0.1:3306/db5?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

def task():
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from t1"
    )
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()

for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()
```

### <span id='3'>ORM</span>
#### <span id='31'>表操作</span>
- 定义表
	- 实例化出模型基类
	- 定义模型类
 		- 双下划线字段指定特殊属性
			- \_\_tablename__,定义表名，类名不会自动生成表名
			- \_\_table_args__,定义表的特殊参数，如指定联合唯一字段
		- 定义静态字段
			- 普通静态字段均为Column对象
			- Column第一个参数为字段类型，可指定长度的类型需要传入最大长度
			- primary_key指定是否为主键
			- autoincrement指定是否自增
			- unique指定是否为唯一索引
			- default指定默认值
			- nullable指定是否可以为空
			- comment指定字段描述
			- ForeignKey对象指定外键表名以及字段
- 创建与删除
	- 默认不支持修改字段，只有新建与删除
		- Base.metadata.drop_all(engine)
		- Base.metadata.create_all(engine)

	```python
	import datetime
	
	from sqlalchemy import create_engine
	from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
	
	from sqlalchemy.orm import relationship
	from sqlalchemy.ext.declarative import declarative_base
	
	
	Base = declarative_base()
	
	
	class Department(Base):
	    """
	    部门表
	    """
	    __tablename__ = "department"
	
	    id = Column(Integer, primary_key=True, autoincrement=True)
	    title = Column(String(32), comment="部门名称")
	    code = Column(Integer, unique=True, comment="部门编号")
	    ctime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
	
	
	class UserInfo(Base):
	    """
	    用户表
	    """
	    __tablename__ = "userinfo"
	
	    id = Column(Integer, primary_key=True, autoincrement=True)
	    username = Column(String(16), unique=True, comment="用户名")
	    password = Column(String(32), comment="密码")
	    email = Column(String(64), unique=True, comment="邮箱")
	    ctime = Column(DateTime, default=datetime.datetime.now, comment="创建日期")
	    extra = Column(Text, nullable=True)
	    department_id = Column(Integer, ForeignKey("department.code"), comment="部门编号", nullable=True)
	
	    department = relationship("Department", backref="users")
	
	    __table_args__ = (
	        UniqueConstraint("id", "username", name="id_username"),
	    )
	
	
	class Department2Hosts(Base):
	    """
	    部门主机关系表
	    """
	    __tablename__ = "department2hosts"
	
	    id = Column(Integer, primary_key=True, autoincrement=True)
	    dep_code = Column(Integer, ForeignKey("department.code"))
	    host_id = Column(Integer, ForeignKey("hosts.id"))
	
	    __table_args__ = (
	        UniqueConstraint("dep_code", "host_id", name="dep_host"),
	    )
	
	
	class Hosts(Base):
	    """
	    主机表
	    """
	    __tablename__ = "hosts"
	
	    id = Column(Integer, primary_key=True, autoincrement=True)
	    addr = Column(String(32), unique=True, comment="主机地址")
	    name = Column(String(32), nullable=True, default="未命名", comment="主机名称")
	    ctime = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
	
	    departments = relationship("Department", secondary="department2hosts", backref="hosts")
	
	
	def init_db(_engine):
	    """
	    根据类创建数据库表
	    :return:
	    """
	    Base.metadata.create_all(_engine)
	
	
	def drop_db(_engine):
	    """
	    根据类删除数据库表
	    :return:
	    """
	    Base.metadata.drop_all(_engine)
	
	
	if __name__ == '__main__':
	    engine = create_engine(
	        "mysql+pymysql://root:@127.0.0.1:3306/cmdb1?charset=utf8",
	        max_overflow=0,  # 超过连接池大小外最多创建的连接
	        pool_size=5,  # 连接池大小
	        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
	        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
	    )
	
	    drop_db(engine)
	    init_db(engine)
	```

#### <span id='32'>记录操作</span>
- 创建操作记录的session
	- 直接使用SessionFactory实例化的对象
		- 具有qeury、add、close....等方法
		- 结束使用session，close()
		- 非线程安全
	- 使用scoped_session间接实例化的对象
		- 内部封装了session应该具有的所有方法
		- 结束使用session.remove()
		- 内部使用了本地线程确保线程安全

	```python
	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker, scoped_session
	
	engine = create_engine(
	    "mysql+pymysql://root@127.0.0.1:3306/cmdb1?charset=utf8",
	    max_overflow=0,
	    pool_size=5,
	    pool_timeout=30,  
	    pool_recycle=-1
	)
	
	SessionFactory = sessionmaker(bind=engine)
	
	# session = SessionFactory()
	# session.close()
	session = scoped_session(SessionFactory)
	session.remove()
	```

- 插入表记录
	- 实例化模型类
	- 添加到表
	- 提交
	
	```python
	# 基本创建方式
	obj = UserInfo(username="alex", password="123", email="alex@live.com")
	obj2 = UserInfo(username="egon", password="123", email="egon@live.com")
	obj3 = UserInfo(username="wusir", password="123", email="wusir@live.com")
	session.add(obj)
	session.add_all([obj2, obj3])
	session.commit()
	
	# 多对多关系创建
	obj4 = Hosts(addr="45.68.6.15", name="深蓝")
	obj4.departments = [
	    Department(title="市场部", code=1000),
	    Department(title="销售部", code=1001),
	    Department(title="技术部", code=1002),
	    Department(title="运维部", code=1003),
	]
	session.add(obj4)
	session.commit()
	
	session.add_all([
	    Hosts(addr="79.222.6.89", name="阿波罗"),
	    Hosts(addr="99.7.6.5", name="荧惑"),
	    Hosts(addr="185.48.121.198", name="饕餮"),
	])
	session.commit()
	
	session.add_all([
	    Department2Hosts(dep_code=1000, host_id=2),
	    Department2Hosts(dep_code=1002, host_id=2),
	    Department2Hosts(dep_code=1001, host_id=3),
	    Department2Hosts(dep_code=1003, host_id=4),
	])
	session.commit()
	```
- 删除表记录

	```python
	# 删除查到的数据
	session.query(UserInfo).delete()
	session.commit()
	```

- 修改表记录

	```python
	session.query(UserInfo).filter(UserInfo.id == 1).update({"username": "alex_yy", "department_code": 1002})
	session.query(UserInfo).filter(UserInfo.id == 2).update({"department_code": 1003})
	session.query(UserInfo).filter(UserInfo.id == 3).update(
	    {UserInfo.username: UserInfo.username + "_xy", "department_code": 1002},
	    synchronize_session=False)
	
	session.query(Department).filter(Department.id == 4).update(
	    {"id": Department.id + 1}, synchronize_session="evaluate")
	
	session.commit()
	```

- 查询表记录
	- 基本操作示例
		- all,获取所有结果
		- first，获取第一个结果
		- label，给映射字段命令
		- filter，相当于sql的where，接收各种条件，条件用python表达式传入
		- filter_by，接收各种条件，条件用关键字传参传入
	
		```python
		from sqlalchemy.sql import text
		
		r1 = session.query(UserInfo).all()
		r2 = session.query(UserInfo.username.label('xx'), UserInfo.email).all()
		r3 = session.query(UserInfo).filter(UserInfo.username == "egon").all()
		r4 = session.query(UserInfo).filter_by(username='egon').all()
		r5 = session.query(UserInfo).filter_by(username='egon').first()
		r6 = session.query(UserInfo).filter(
		    text("id<:value and username=:username")).params(value=224, username='egon').order_by(UserInfo.id).all()
		r7 = session.query(UserInfo).from_statement(
		    text("SELECT * FROM userinfo where username=:username")).params(username='egon').all()
		```
	- 条件查询
		- 大于小于等于和python语法一样
		- between，传入两个值查询介于两个值之间的
		- in_，传入列表/元组，查询满足在序列中的值的
		- ~，取反
		- and_,构造多个且的条件
		- or_，构造多个或的条件
	
		```python
		ret1 = session.query(UserInfo).filter_by(username='alex').all()
		ret2 = session.query(UserInfo).filter(UserInfo.id > 1, UserInfo.username == 'alex').all()
		ret3 = session.query(UserInfo).filter(UserInfo.id.between(1, 3), UserInfo.username == 'egon').all()
		ret4 = session.query(UserInfo).filter(UserInfo.id.in_([1, 2, 3])).all()
		ret5 = session.query(UserInfo).filter(~UserInfo.id.in_([1, 2, 3])).all()
		ret6 = session.query(UserInfo).filter(UserInfo.id.in_(session.query(UserInfo.id).filter_by(username='egon'))).all()
		from sqlalchemy import and_, or_
		ret7 = session.query(UserInfo).filter(and_(UserInfo.id > 3, UserInfo.username == 'egon')).all()
		ret8 = session.query(UserInfo).filter(or_(UserInfo.id < 2, UserInfo.username == 'alex')).all()
		ret9 = session.query(UserInfo).filter(
		    or_(
		        UserInfo.id < 3,
		        and_(UserInfo.username == 'egon', UserInfo.id > 0),
		        UserInfo.extra != ""
		    )).all()
		```
	- 通配符
		- like,模糊搜索
		- %
		
		```python
		ret1 = session.query(UserInfo).filter(UserInfo.username.like('e%')).all()
		ret2 = session.query(UserInfo).filter(~UserInfo.username.like('e%')).all()
		```
	- 限制/结果切片

		```python
		ret = session.query(UserInfo)[1:2]
		```
	- 排序
		- asc,正序
		- desc，倒序
		- 多个排序则在前一个排序无法区分时使用下一个排序

		```python
		ret1 = session.query(UserInfo).order_by(UserInfo.username.desc()).all()
		ret2 = session.query(UserInfo).order_by(UserInfo.username.desc(), UserInfo.id.asc()).all()
		```
	- 分组

		```python
		from sqlalchemy.sql import func
		ret1 = session.query(
		    func.max(UserInfo.id),
		    func.sum(UserInfo.id),
		    func.min(UserInfo.id)).group_by(UserInfo.department_code).having(func.min(UserInfo.id) > 0).all()
		```
	- 联表
		- join
		- union
		- concat

		```
		ret1 = session.query(UserInfo, Department).filter(UserInfo.department_code == Department.id).all()
		ret2 = session.query(UserInfo).join(Department).all()
		ret3 = session.query(UserInfo).join(Department, isouter=True).all()
		
		
		# 组合
		q1 = session.query(UserInfo.username).filter(UserInfo.id > 2)
		q2 = session.query(Department.title).filter(Department.id < 2)
		ret4 = q1.union(q2).all()
		
		q1 = session.query(Department.title).filter(UserInfo.id > 2)
		q2 = session.query(Hosts.addr.concat(Hosts.name)).filter(UserInfo.id < 2)
		ret5 = q1.union_all(q2).all()
		```

### <span id='4'>扩展</span>
#### <span id='41'>sqlalchemy_utils</span>
```
pip install sqlalchemy_utils
```

```python
from sqlalchemy_utils import ChoiceType


class Test(Base):
	type_choices = ((1, "北京"),(2, "上海"),(3, "广州"),(4, "深圳"))
	id = Column(Intger, primary_key=True, autoincrement=True)
	name = Column(String(32))
	type = Column(ChoiceType(type_choice, Intger()))
```

```python
session = Session()
obj = Test(name="alex",type=1)
session.add(obj)
session.commit()

result = session.query(Test).first()
print(result.type)
print(result.type.value)
```


## SQLAlchemy

### SQLAlchemy结构
- 上层的是对象关系模型(Object Relational Mapper)
	- 类对应表，对象对应记录，对象属性对应记录值
- 下层是SQLAlchemy的核心，分三块
	- 模式(Schema/Type)
	- SQL语句翻译(SQl Expression Language)
	- 框架引擎(Engine),这里又分为两部分
		- Connection Pooling 数据库连接池
		- Dialect,选择DB API种类
- SQLAlchemy自身无法操作数据库，需要借助DB API，如pymysql，mysqldb，cx_oracle等
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

### 借助SQLAlchemy执行原生SQL
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

### ORM
#### 表操作
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

#### 记录操作
- 插入表记录
	- 实例化模型类
	- 添加到表
	- 提交
- 删除表记录
- 查询表记录
	- 



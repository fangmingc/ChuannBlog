# <span id='0'>MySQL</span>
- [数据库基础](#1.0)
- [MySQL准备使用](#2.0)
	- [Liunx环境](#2.1)
	- [Windows环境](#2.2)
	- [MySQL软件基本管理](#2.3)
	- [MySQL数据库导入导出](#2.4)
	- [为其他人创建mysql用户](#2.5)
- [SQL语句(Structured Query Language)](#3.0)
	- [库操作](#3.1)
	- [表操作](#3.2)
	- [记录操作](#3.3)
	- [授权](#3.4)
	- [数据类型](#3.5)
	- [完整性约束](#3.6)
- [查询语句](#4.0)
	- [单表查询](#4.1)
	- [多表查询](#4.2)
- [索引](#5.0)
- [Pymysql](#6.0)


## <span id='1.0'>数据库基础</span>
数据库服务器，数据管理系统，数据库，表和记录      
装文件的电脑，MySQL软件，文件夹，文件和文件的每一行内容     

### 为什么不用文件？
- 难以共享给多用户，非常影响效率
- 当文件比较多，非常依赖硬件性能，成本过高

### 什么是数据    
描述事物的符号记录（特征）称为数据，描述事物的符号既可以是数字，也可以是文字、图片，图像、声音、语言等，数据由多种表现形式，它们都可以经过数字化后存入计算机

### 什么是数据库（DataBase，简称DB）  
数据库即存放数据的仓库，只不过这个仓库是在计算机存储设备上，而且数据是按一定的格式存放的   
过去人们将数据存放在文件柜里，现在数据量庞大，已经不再适用   
数据库是长期存放在计算机内、有组织、可共享的数据即可。   
数据库中的数据按一定的数据模型组织、描述和储存，具有较小的冗余度、较高的数据独立性和易扩展性，并可为各种 用户共享

#### 数据库分类
分两大类：
- 关系型：sqllite，db2，oracle，access，sql server，MySQL，MariaDB，注意：sql语句通用
- 非关系型：mongodb，redis，memcache

### 什么是数据库管理系统（DataBase Management System 简称DBMS）
在了解了Data与DB的概念后，如何科学地组织和存储数据，如何高效获取和维护数据成了关键   
这就用到了一个系统软件---数据库管理系统    
如MySQL、Oracle、SQLite、Access、MS SQL Server   
- mysql主要用于大型门户，例如搜狗、新浪等，它主要的优势就是开放源代码，因为开放源代码这个数据库是免费的，他现在是甲骨文公司的产品。    
- oracle主要用于银行、铁路、飞机场等。该数据库功能强大，软件费用高。也是甲骨文公司的产品。
- sql server是微软公司的产品，主要应用于大中型企业，如联想、方正等。

<p align="right">[回到顶部](#0)</p>
<span style="right">[回到顶部](#0)</span>
<li style="right">[回到顶部](#0)</li>
## <span id='2.0'>MySQL准备使用</span>
### <span id='2.1'>Liunx环境</span>
### <span id='2.2'>Windows环境</span>
#### 下载
在官网下载相应版本。  
官网链接：https://dev.mysql.com/downloads/mysql

#### 解压
如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64   

#### 初始化
- MySQL解压后的 bin 目录下有一大堆的可执行文件，执行如下命令初始化数据    
	
	```cmd
	cd c:\mysql-5.7.16-winx64\bin
	mysqld --initialize-insecure
	```

#### 启动MySQL服务
- 执行命令从而启动MySQL服务     

	```cmd
	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	 
	# 启动MySQL服务
	mysqld
	```

#### 启动MySQL客户端连接到MySQL服务
- 由于初始化时使用的【mysqld --initialize-insecure】命令，其默认未给root账户设置密码    

	```cmd
	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	 
	# 连接MySQL服务器
	mysql -u root -p
	 
	# 提示请输入密码，直接回车
	```

#### 优化MySQL启动
##### 添加环境变量       
【右键计算机】-->【属性】-->【高级系统设置】-->【高级】-->【环境变量】-->    
【在第二个内容框中找到 变量名为Path 的一行，双击】 -->    
【将MySQL的bin目录路径追加到变值值中，用；分割】   
- 当再次启动服务仅需        

	```cmd
	# 启动MySQL服务，在终端任意目录输入
	mysqld
	# 连接MySQL服务，在终端任意目录输入：
	mysql -u root -p
	```

##### 将MySQL服务制作成windows服务

```cmd
# 制作MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --install
 
# 移除MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --remove
```

- 注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令(管理员权限下)      

	```cmd
	# 启动MySQL服务
	net start mysql
	 
	# 关闭MySQL服务
	net stop mysql
	```

#### 扩展windows命令
- 命令之后接/?获取帮助
- findstr
	- 在文件中寻找字符串(必须包括在双引号内)
	- 如findstr "hello" test.txt
	- 可以在一些命令后接 \| 在命令的结果中查找
- tasklist
	- 该工具显示在本地或远程机器上当前运行的进程列表
	- 显示结果由5部分组成：图像名(进程名)、PID、会话名、会话和内存使用
	- tasklist \|findstr explorer
- taskkill
	- 使用该工具按照进程 ID (PID) 或映像名称终止任务
	- /T 删除指定进程及子进程
	- /F 强制删除进程
	- /PID 以PID形式删除进程

<p align=right>[回到顶部](#0)</p>
### <span id='2.3'>MySQL软件基本管理</span>
#### 第一次登录后设置密码
- 初始状态下，管理员root，密码为空，默认只允许从本机登录localhost
- 设置密码        
	
	```cmd
	mysqladmin -uroot password "123"        
	# 设置初始密码 由于原密码为空，因此-p可以不用
	mysqladmin -uroot -p"123" password "456"        
	# 修改mysql密码,因为已经有密码了，所以必须输入原密码才能设置新密码
	``` 
- 登录命令格式       
	
	```cmd
	mysql -h172.31.0.2 -uroot -p456
	mysql -uroot -p
	mysql 以root用户登录本机，密码为空
	```

#### 忘记密码
##### linux
- 方法一：删除授权库mysql，重新初始化         
	
	```linux
	# rm -rf /var/lib/mysql/mysql #所有授权信息全部丢失！！！
	# systemctl restart mariadb
	# mysql
	```

- 方法二：启动时跳过授权库，修改密码后重新登录    
	
	```linux
	# vim /etc/my.cnf    #mysql主配置文件
	[mysqld]
	skip-grant-table
	# systemctl restart mariadb
	# mysql
	MariaDB [(none)]> update mysql.user set password=password("123") where user="root" and host="localhost";
	MariaDB [(none)]> flush privileges;
	MariaDB [(none)]> \q
	# #打开/etc/my.cnf去掉skip-grant-table,然后重启
	# systemctl restart mariadb
	# mysql -u root -p123 #以新密码登录
	```
   
##### windows
基本方法，跳过授权表登录
- 方法一     
	
	```cmd
	#1 关闭mysql
	#2 在cmd中执行：
	mysqld --skip-grant-tables
	#3 在cmd中执行：
	mysql
	#4 执行如下sql：
	```
	
	```sql
	update mysql.user set authentication_string=password('') where user = 'root';
	flush privileges;
	```	
	
	```cmd
	#5 tskill mysqld(tskill无法使用时先用tasklist寻找mysqld的PID再用taskkill杀死进程)
	#6 重新启动mysql
	```

- 方法二      
	
	```cmd
	#1. 关闭mysql，可以用tskill将其杀死(tskill无法使用时先用tasklist寻找mysqld的PID再用taskkill杀死进程)
	#2. 在解压目录下，新建mysql配置文件my.ini
	#3. my.ini内容,指定
	[mysqld]
	skip-grant-tables
	#4.启动mysqld
	#5.在cmd里直接输入mysql登录，然后操作
	update mysql.user set authentication_string=password('') where user='root and host='localhost';
	flush privileges;
	#6.注释my.ini中的skip-grant-tables，然后重新启动myqsld，然后就可以以新密码登录了
	```

#### windows下为mysql服务指定配置文件
```ini
#在mysql的解压目录下，新建my.ini,然后配置
#1. 在执行mysqld命令时，下列配置会生效，即mysql服务启动时生效
[mysqld]
;skip-grant-tables
port=3306
character_set_server=utf8
#解压的目录
basedir=E:\mysql-5.7.19-winx64
#data目录
datadir=E:\my_data #在mysqld --initialize时，就会将初始数据存入此处指定的目录，在初始化之后，启动mysql时，就会去这个目录里找数据

#2. 针对客户端命令的全局配置，当mysql客户端命令执行时，下列配置生效
[client]
port=3306
default-character-set=utf8
user=root
password=123

#3. 只针对mysql这个客户端的配置，2中的是全局配置，而此处的则是只针对mysql这个命令的局部配置
[mysql]
;port=3306
;default-character-set=utf8
user=egon
password=4573

#！！！如果没有[mysql],则用户在执行mysql命令时的配置以[client]为准
```

#### mac上MySQL出现error
> mac mysql error You must reset your password using ALTER USER statement before executing this statement.

- 解决方法     
	
	```
	step 1: SET PASSWORD = PASSWORD('your new password');
	step 2: ALTER USER 'root'@'localhost' PASSWORD EXPIRE NEVER;
	step 3: flush privileges;
	```

<p align=right>[回到顶部](#0)</p>
### <span id='2.4'>MySQL数据库导入导出</span>
#### 导出
- 导出数据和结构
	- mysqldump -h IP -u用户名 -p 数据库 > [.sql文件路径]
- 导出结构
	- mysqldump -h IP -u用户名 -p -d 数据库 > [.sql文件路径]
- 导出多个数据库
	- mysqldump -h IP -u用户名 -p --databases 数据库1 数据库2... > [.sql文件路径]
- 导出所有数据库
	- mysqldump -h IP -u用户名 -p --all-databases > [.sql文件路径]

#### 导入
在mysql内use数据库时：
- source [.sql文件路径]

在mysql外部：
- mysql -uroot -p 数据库 < [.sql文件路径]
- 在外部查看是否导入成功：mysql -uroot -e "use tmp;show tables;"

导入多个数据库
- mysql -u用户名 -p < [.sql存有多个库的文件]

#### 数据库迁移
mysqldump -h 源IP -uroot -p --databases db1 | mysql -h -目标IP -u用户名 -p密码


#### 导出其他格式文件
- select [列名称] from tablename [where] into outfile '目标文件路径' [option]

### <span id='2.5'>为其他人创建mysql用户</span>
- 创建账号
	- `create user 'username'@'允许ip来源' identified by 'password'`
		- 允许ip来源为%表示任意来源
		- 允许ip来源为localhost或127.0.0.1表示只允许本机访问
		- 允许ip来源为192.168.20.%表示只允许局域网192.168.20网段访问
			- 192.168.所在局域网子网段.%
- 授权
	- 参考[授权](#3.4)
	- 对所有数据库所有表的所有权限
		- `grant all privileges on *.* to 'username'@'允许ip来源';`
	- 对某个数据库某个表的所有权限
		- `grant all privileges on 数据库名.表名 to 'username'@'允许ip来源';`
	- 对某个数据所有表的增、查[改、删]权限
		- `grant insert,select[,update,delete] on 数据库名.* to 'username'@'允许ip来源';`
- 记得flush privileges更新权限



<p align=right>[回到顶部](#0)</p>
## <span id='3.0'>SQL语句（Structured Query Language）</span>
- 查看当前用户信息   
	
	```sql
	select user();
	```
- 分类
	1. DDL语句	数据库定义语言： 数据库、表、视图、索引、存储过程，例如CREATE DROP ALTER
	2. DML语句	数据库操纵语言： 插入数据INSERT、删除数据DELETE、更新数据UPDATE、查询数据SELECT
	3. DCL语句	数据库控制语言： 例如控制用户的访问权限GRANT、REVOKE
- 系统数据库     
	- information_schema：	虚拟库，不占用磁盘空间，存储的是数据库启动后的一些参数，如用户表信息、列信息、权限信息、字符信息等
	- performance_schema： MySQL 5.5开始新增一个数据库：主要用于收集数据库服务器性能参数，记录处理查询请求时发生的各种事件、锁等现象 
	- mysql：	授权库，主要存储系统用户的权限信息
	- test：	MySQL 数据库系统自动创建的测试数据库

<p align=right>[回到顶部](#0)</p>
### <span id='3.1'>库（文件夹）操作</span>
#### 增
- **CREATE** **{DATABASE \| SCHEMA}** [IF NOT EXISTS] **db_name** [create_specification] ... 
	- **create_specification**: [DEFAULT] CHARACTER SET [=] charset_name \| [DEFAULT] COLLATE [=] collation_name     

	```sql
	create database db1 charset utf8;
	```

#### 查   
- **SHOW** **DATABASES** [like_or_where]    
- **SHOW** **CREATE** **DATABASE** **db_name**     

	```sql
	show databases;
	show create database db1;
	```

#### 改  
- **ALTER** **{DATABASE \| SCHEMA}** [db_name] alter_specification ...
	- **alter_specification**: [DEFAULT] CHARACTER SET [=] charset_name \| [DEFAULT] COLLATE [=] collation_name
- **ALTER** **{DATABASE \| SCHEMA}** **db_name** **UPGRADE** **DATA DIRECTORY NAME**    
	
	```sql
	alter database db1 charset gbk;
	```

#### 删   
- **DROP** **{DATABASE \| SCHEMA}** [IF EXISTS] **db_name**      

	```sql
	drop database db1;
	```

<p align=right>[回到顶部](#0)</p>
### <span id='3.2'>表（文件）操作</span>
切换到文件夹下：   

```sql
use db1;
```
#### 增   
**简易例子**：        

```sql
create table t1(id int, name char(10)) engine=innodb;
create table t2(id int, name char(10)) engine=innodb;
create table t4 select * from t1 where 1=2;

```

**完整命令**：       
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name(create_definition,...)**  [table_options] [partition_options]
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name**[(create_definition,...)]  [table_options] [partition_options] [IGNORE \| REPLACE] [AS] **query_expression**
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name{ LIKE old_tbl_name \| (LIKE old_tbl_name) }**
	- **create_definition**:
		- **col_name** 
		- **column_definition** 
		- \| [CONSTRAINT [symbol]] **PRIMARY KEY** [index_type] (index_col_name,...)  [index_option] ...
		- \| **{INDEX\|KEY}** [index_name] [index_type] (index_col_name,...) [index_option] ...
		- \| [CONSTRAINT [symbol]] **UNIQUE** [INDEX\|KEY] [index_name] [index_type] (index_col_name,...) [index_option] ... 
		- \| **{FULLTEXT\|SPATIAL}** [INDEX\|KEY] [index_name] (index_col_name,...)  [index_option] ...
		- \| [CONSTRAINT [symbol]] **FOREIGN KEY** [index_name] (index_col_name,...) **reference_definition**
		- \| **CHECK(expr)**
			- **column_definition**:
		    	- **data_type** [NOT NULL \| NULL] [DEFAULT default_value] [AUTO_INCREMENT] [UNIQUE [KEY] \| [PRIMARY] KEY] [COMMENT 'string'] [COLUMN_FORMAT {FIXED\|DYNAMIC\|DEFAULT}] [STORAGE {DISK\|MEMORY\|DEFAULT}] [reference_definition]
		    	- \| **data_type** [GENERATED ALWAYS] **AS** **(expression)** [VIRTUAL \| STORED] [UNIQUE [KEY]] [COMMENT comment] [NOT NULL \| NULL] [[PRIMARY] KEY]
					- **data_type**:
						- **BIT**[(length)]
						- \| **TINYINT**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **SMALLINT**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **MEDIUMINT**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **INT**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **INTEGER**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **BIGINT**[(length)] [UNSIGNED] [ZEROFILL]
						- \| **REAL**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- \| **DOUBLE**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- \| **FLOAT**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- \| **DECIMAL**[(length[,decimals])] [UNSIGNED] [ZEROFILL]
						- \| **NUMERIC**[(length[,decimals])] [UNSIGNED] [ZEROFILL]
						- \| **DATE**
						- \| **TIME**[(fsp)]
						- \| **TIMESTAMP**[(fsp)]
						- \| **DATETIME**[(fsp)]
						- \| **YEAR**
						- \| **CHAR**[(length)] [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **VARCHAR(length)** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **BINARY**[(length)]
						- \| **VARBINARY(length)**
						- \| **TINYBLOB**
						- \| **BLOB**
						- \| **MEDIUMBLOB**
						- \| **LONGBLOB**
						- \| **TINYTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **TEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **MEDIUMTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **LONGTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name] 
						- \| **ENUM(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **SET(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
						- \| **JSON**
						- \| **spatial_type**
			- **index_col_name**:
		    	- **col_name** [(length)] [ASC \| DESC]
			- **index_type**:
			    - **USING {BTREE \| HASH}**
			- **index_option**:
				- **KEY_BLOCK_SIZE** [=] **value**
				- \| **index_type**
				- \| **WITH PARSER parser_name**
				- \| **COMMENT 'string'**
			- **reference_definition**:
				- **REFERENCES tbl_name(index_col_name,...)** [MATCH FULL \| MATCH PARTIAL \| MATCH SIMPLE] [ON DELETE reference_option] [ON UPDATE reference_option]
			- **reference_option**: 
				- **RESTRICT** \| **CASCADE** \| **SET NULL** \| **NO ACTION** \| **SET DEFAULT**
	- **table_options**:
		- **table_option** [[,] table_option] ...
			- **table_option**:
				- **ENGINE** [=] **engine_name**
				- \| **AUTO_INCREMENT** [=] **value**
				- \| **AVG_ROW_LENGTH** [=] **value**
				- \| [DEFAULT] **CHARACTER SET** [=] **charset_name**
				- \| **CHECKSUM** [=] **{0 \| 1}**
				- \| [DEFAULT] **COLLATE** [=] **collation_name**
				- \| **COMMENT** [=] **'string'**
				- \| **COMPRESSION** [=] **{'ZLIB'\|'LZ4'\|'NONE'}**
				- \| **CONNECTION** [=] **'connect_string'**
				- \| **DATA DIRECTORY** [=] **'absolute path to directory'**
				- \| **DELAY_KEY_WRITE** [=] **{0 \| 1}**
				- \| **ENCRYPTION** [=] **{'Y' \| 'N'}**
				- \| **INDEX DIRECTORY** [=] **'absolute path to directory'**
				- \| **INSERT_METHOD** [=] **{ NO \| FIRST \| LAST }**
				- \| **KEY_BLOCK_SIZE** [=] **value**
				- \| **MAX_ROWS** [=] **value**
				- \| **MIN_ROWS** [=] **value**
				- \| **PACK_KEYS** [=] **{0 \| 1 \| DEFAULT}**
				- \| **PASSWORD** [=] **'string'**
				- \| **ROW_FORMAT** [=] **{DEFAULT\|DYNAMIC\|FIXED\|COMPRESSED\|REDUNDANT\|COMPACT}**
				- \| **STATS_AUTO_RECALC** [=] **{DEFAULT\|0\|1}**
				- \| **STATS_PERSISTENT** [=] **{DEFAULT\|0\|1}**
				- \| **STATS_SAMPLE_PAGES** [=] **value**
				- \| **TABLESPACE tablespace_name** [STORAGE {DISK\|MEMORY\|DEFAULT}]
				- \| **UNION** [=] **(tbl_name[,tbl_name]...)**
	- **partition_options**:
		- **PARTITION BY** { [LINEAR] **HASH(expr)** \| [LINEAR] **KEY** [ALGORITHM={1\|2}](column_list) \| **RANGE{(expr)** \| **COLUMNS(column_list)**} \| **LIST{(expr)** \| **COLUMNS(column_list)**} }
		- [PARTITIONS num]
		- [SUBPARTITION BY { [LINEAR] **HASH(expr)** \| [LINEAR] **KEY** [ALGORITHM={1\|2}] (column_list) } [SUBPARTITIONS num]]
		- [(partition_definition [, partition_definition] ...)]
			- **partition_definition**:
				- **PARTITION** **partition_name**
					- [VALUES {LESS THAN {(expr \| value_list) \| MAXVALUE} \| IN (value_list)}]
					- [[STORAGE] **ENGINE** [=] engine_name]
					- [COMMENT [=] 'comment_text' ]
					- [DATA DIRECTORY [=] 'data_dir']
					- [INDEX DIRECTORY [=] 'index_dir']
					- [MAX_ROWS [=] max_number_of_rows]
					- [MIN_ROWS [=] min_number_of_rows]
					- [TABLESPACE [=] tablespace_name]
					- [(subpartition_definition [, subpartition_definition] ...)]
						- **subpartition_definition**:
							- **SUBPARTITION** **logical_name**
								- [[STORAGE] **ENGINE** [=] engine_name]
								- [COMMENT [=] 'comment_text' ]
								- [DATA DIRECTORY [=] 'data_dir']
								- [INDEX DIRECTORY [=] 'index_dir']
								- [MAX_ROWS [=] max_number_of_rows]
								- [MIN_ROWS [=] min_number_of_rows]
								- [TABLESPACE [=] tablespace_name]
	- **query_expression**:
		- SELECT ...   (Some valid select or union statement)

#### 查   
- **SHOW** [FULL] **TABLES** [{FROM \| IN} db_name] [LIKE 'pattern' \| WHERE expr]     
- **SHOW** **CREATE TABLE tbl_name**     

	```sql
	show tables;
	show create table t1;
	
	# 查看表结构
	desc/describe t1;
	```

#### 改   

```sql
alter table t1 add age int;
alter table t1 modify name char(12);
```
**完整命令**
- **ALTER** **TABLE tbl_name** [alter_specification [, alter_specification] ...] [partition_options]
	- **alter_specification**:
		- **table_options** 
		- \| **ADD** [COLUMN] **col_name column_definition** [FIRST \| AFTER col_name ]
		- \| **ADD** [COLUMN] **(col_name column_definition,...)**
		- \| **ADD** **{INDEX\|KEY}** [index_name] [index_type] **(index_col_name,...)** [index_option] ...
		- \| **ADD** [CONSTRAINT [symbol]] **PRIMARY KEY** [index_type] **(index_col_name,...)** [index_option] ...
		- \| **ADD** [CONSTRAINT [symbol]] **UNIQUE** [INDEX\|KEY] [index_name] [index_type] **(index_col_name,...)** [index_option] ...
		- \| **ADD FULLTEXT** [INDEX\|KEY] [index_name] **(index_col_name,...)** [index_option] ...
		- \| **ADD SPATIAL** [INDEX\|KEY] [index_name] **(index_col_name,...)** [index_option] ...
		- \| **ADD** [CONSTRAINT [symbol]] **FOREIGN KEY** [index_name] **(index_col_name,...) reference_definition**
		- \| **ALGORITHM** [=] **{DEFAULT\|INPLACE\|COPY}**
		- \| **ALTER** [COLUMN] **col_name {SET DEFAULT literal \| DROP DEFAULT}**
		- \| **CHANGE** [COLUMN] **old_col_name new_col_name column_definition** [FIRST\|AFTER col_name]
		- \| **LOCK** [=] **{DEFAULT\|NONE\|SHARED\|EXCLUSIVE}**
		- \| **MODIFY** [COLUMN] **col_name column_definition** [FIRST \| AFTER col_name]
		- \| **DROP** [COLUMN] **col_name**
		- \| **DROP PRIMARY KEY**
		- \| **DROP {INDEX\|KEY} index_name**
		- \| **DROP FOREIGN KEY fk_symbol**
		- \| **DISABLE KEYS**
		- \| **ENABLE KEYS**
		- \| **RENAME** [TO\|AS] **new_tbl_name**
		- \| **RENAME {INDEX\|KEY} old_index_name TO new_index_name**
		- \| **ORDER BY col_name** [, col_name] ...
		- \| **CONVERT TO CHARACTER SET charset_name** [COLLATE collation_name]
		- \| [DEFAULT] **CHARACTER SET** [=] **charset_name** [COLLATE [=] collation_name]
		- \| **DISCARD TABLESPACE**
		- \| **IMPORT TABLESPACE**
		- \| **FORCE**
		- \| **{WITHOUT\|WITH} VALIDATION**
		- \| **ADD PARTITION (partition_definition)**
		- \| **DROP PARTITION partition_names**
		- \| **DISCARD PARTITION {partition_names \| ALL} TABLESPACE**
		- \| **IMPORT PARTITION {partition_names \| ALL} TABLESPACE**
		- \| **TRUNCATE PARTITION {partition_names \| ALL}**
		- \| **COALESCE PARTITION number**
		- \| **REORGANIZE PARTITION partition_names INTO (partition_definitions)**
		- \| **EXCHANGE PARTITION partition_name WITH TABLE tbl_name** [{WITH\|WITHOUT} VALIDTION]
		- \| **ANALYZE PARTITION {partition_names \| ALL}**
		- \| **CHECK PARTITION {partition_names \| ALL}**
		- \| **OPTIMIZE PARTITION {partition_names \| ALL}**
		- \| **REBUILD PARTITION {partition_names \| ALL}**
		- \| **REPAIR PARTITION {partition_names \| ALL}**
		- \| **REMOVE PARTITIONING**
		- \| **UPGRADE PARTITIONING**
			- **index_col_name**:
				- **col_name** [(length)] [ASC \| DESC]
			- **index_type**:
				- **USING {BTREE \| HASH}**
			- **index_option**:
				- **KEY_BLOCK_SIZE** [=] **value**
				- \| **index_type**
				- \| **WITH PARSER parser_name**
				- \| **COMMENT 'string'**
			- **table_options**:
				- **table_option** [[,] table_option] ...
					- **table_option**:
						- **ENGINE** [=] **engine_name**
						- \| **AUTO_INCREMENT** [=] **value**
						- \| **AVG_ROW_LENGTH** [=] **value**
						- \| [DEFAULT] **CHARACTER SET** [=] **charset_name**
						- \| **CHECKSUM** [=] **{0 \| 1}**
						- \| [DEFAULT] **COLLATE** [=] **collation_name**
						- \| **COMMENT** [=] **'string'**
						- \| **COMPRESSION** [=] **{'ZLIB'\|'LZ4'\|'NONE'}**
						- \| **CONNECTION** [=] **'connect_string'**
						- \| **DATA DIRECTORY** [=] **'absolute path to directory'**
						- \| **DELAY_KEY_WRITE** [=] **{0 \| 1}**
						- \| **ENCRYPTION** [=] **{'Y' \| 'N'}**
						- \| **INDEX DIRECTORY** [=] **'absolute path to directory'**
						- \| **INSERT_METHOD** [=] **{ NO \| FIRST \| LAST }**
						- \| **KEY_BLOCK_SIZE** [=] **value**
						- \| **MAX_ROWS** [=] **value**
						- \| **MIN_ROWS** [=] **value**
						- \| **PACK_KEYS** [=] **{0 \| 1 \| DEFAULT}**
						- \| **PASSWORD** [=] **'string'**
						- \| **ROW_FORMAT** [=] **{DEFAULT\|DYNAMIC\|FIXED\|COMPRESSED\|REDUNDANT\|COMPACT}**
						- \| **STATS_AUTO_RECALC** [=] **{DEFAULT\|0\|1}**
						- \| **STATS_PERSISTENT** [=] **{DEFAULT\|0\|1}**
						- \| **STATS_SAMPLE_PAGES** [=] **value**
						- \| **TABLESPACE tablespace_name** [STORAGE {DISK\|MEMORY\|DEFAULT}]
						- \| **UNION** [=] **(tbl_name[,tbl_name]...)**
	- **partition_options**:(see CREATE TABLE options)
#### 删  
- **DROP** [TEMPORARY] **TABLE** [IF EXISTS] **tbl_name** [, tbl_name] ... [RESTRICT \| CASCADE]

	```sql
	drop table t2;
	```

<p align=right>[回到顶部](#0)</p>
### <span id='3.3'>记录（文件内容）操作</span>
#### 增   
```sql
insert into db1.t1 values(1,'chuck',19),(2,'chuck2',20),(3,'chuck3',21);
insert into t1 value(4,'chuck4',20);
insert into t1(name) value('chuck5');

```
- **INSERT** [LOW_PRIORITY \| DELAYED \| HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] [(col_name,...)] **{VALUES \| VALUE}({expr \| DEFAULT},...)**,(...),... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
- **INSERT** [LOW_PRIORITY \| DELAYED \| HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] **SET col_name={expr \| DEFAULT}**, ... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
- **INSERT** [LOW_PRIORITY \| HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] [(col_name,...)] **SELECT** ... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
#### 查   
```sql
select \* from t1;
select name from t1;
select name,id from t1;
```

- **SELECT** 
	- [ALL \| DISTINCT \| DISTINCTROW ]
	- [HIGH_PRIORITY] 
	- [STRAIGHT_JOIN] 
	- [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT] 
	- [SQL_CACHE \| SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    - **select_expr** [, select_expr ...]
    - [**FROM** **table_references** 
	    - [**PARTITION** partition_list]
	    - [**WHERE** where_condition]
	    - [**GROUP BY** {col_name \| expr \| position} [ASC \| DESC], ... [WITH ROLLUP]]
	    - [**HAVING** where_condition]
	    - [**ORDER BY** {col_name \| expr \| position} [ASC \| DESC], ...]
	    - [**LIMIT** {[offset,] row_count \| row_count OFFSET offset}]
	    - [**PROCEDURE** procedure_name(argument_list)]
	    - [**INTO OUTFILE** 'file_name' [CHARACTER SET charset_name] export_options
		    - \| **INTO DUMPFILE** 'file_name'
		    - \| **INTO** var_name [, var_name]]
		- [**FOR UPDATE** \| **LOCK IN SHARE MODE**]]

- select \* from mysql.user\G; 

#### 改   
```sql
update t1 set name='NOBODY' where id=4;
update t1 set name='None' where name=chuck;
update t1 set id=12 where name='None';
```
**Single-table syntax**
- UPDATE [LOW_PRIORITY] [IGNORE] table_reference SET col_name1={expr1\|DEFAULT} [, col_name2={expr2\|DEFAULT}] ... [WHERE where_condition] [ORDER BY ...] [LIMIT row_count]        

**Multiple-table syntax**
- UPDATE [LOW_PRIORITY] [IGNORE] table_references SET col_name1={expr1\|DEFAULT} [, col_name2={expr2\|DEFAULT}] ... [WHERE where_condition]

#### 删     
```sql
delete from t1 where id=4;
delete from t1; # 清空表

truncate # :截断，比delete删除快         
truncate t1; # 清空表      
```

#### 自增id 
```sql
create table t1(id int not null, name char(10));
```
- primary key为主键，不为空，且唯一，等同not null unique     

	```sql
	create table t4(id int not null unique, name char(10));
	```
- auto_increment：自增        

	```sql
	create table t5(id int primary key auto_increment, name char(10));
	insert into t5(name) values('chuck'),('chuck2'),('chuck3'),('chuck4'),('chuck5');
	```
- 自增的字段需要用truncate清空表后才可以从1开始自增

#### 拷贝表
- 表结构和记录   

	```sql
	create table t6 select * from t5;
	create table t3 like t1;
	```
- 表结构    

	```sql
	create table t7 select * from t5 where 1=2; 
	alter table t7 modify id int primary key auto_increment;
	
	create table t8 like t5;
	```

<p align=right>[回到顶部](#0)</p>
### <span id='3.4'>授权</span>
```sql
# 创建用户
create user 'temp'@'localhost' identified by '123';

# insert delete update select
# 级别1：所有库，所有表，所有字段
grant select on *.* to 'temp'@'localhost' identified by '123';

# 级别2：对db1下的所有表，所有字段
grant select on db1.* to 'temp2'@'localhost' identified by '123';

# 级别3：对db下的t1表的所有字段
grant select on db1.t1 to 'temp3'@'localhost' identified by '123';

# 级别4：对db下的t1表的id字段
grant select (id) on db1.t1 to 'temp4'@'localhost' identified by '123';

# 修改完毕后
flush privileges;
```

**完整命令**
- **GRANT** **priv_type** [(column_list)] [, priv_type [(column_list)]] ... **ON** [object_type] **priv_level** **TO** **user** [auth_option] [, user [auth_option]] ... [REQUIRE {NONE \| tls_option [[AND] tls_option] ...}] [WITH {GRANT OPTION \| resource_option} ...]   
- **GRANT** **PROXY** **ON** **user** **TO** **user** [, user] ... [WITH GRANT OPTION]
	- **object_type**: {TABLE \| FUNCTION \| PROCEDURE }
	- **priv_level**: { \* \| \*.\* \| db_name.\* \| db_name.tbl_name \| tbl_name \| db_name.routine_name }
	- **user**:(see http://dev.mysql.com/doc/refman/5.7/en/account-names.html)
	- **auth_option**:{ **# Before MySQL 5.7.6** IDENTIFIED BY 'auth_string' \| IDENTIFIED BY PASSWORD 'hash_string' \| IDENTIFIED WITH auth_plugin \| IDENTIFIED WITH auth_plugin AS 'hash_string'}
	- **auth_option**: { **# As of MySQL 5.7.6** IDENTIFIED BY 'auth_string' \| IDENTIFIED BY PASSWORD 'hash_string' \| IDENTIFIED WITH auth_plugin \| IDENTIFIED WITH auth_plugin BY 'auth_string' \| IDENTIFIED WITH auth_plugin AS 'hash_string'}
	- **tls_option**: { SSL \| X509 \| CIPHER 'cipher' \| ISSUER 'issuer' \| SUBJECT 'subject' }
	- **resource_option**: { \| MAX_QUERIES_PER_HOUR count \| MAX_UPDATES_PER_HOUR count \| MAX_CONNECTIONS_PER_HOUR count \| MAX_USER_CONNECTIONS count }

<p align=right>[回到顶部](#0)</p>
### <span id='3.5'>数据类型</span>
#### 数值类型
##### 整数
整数的length表示显示的长度（在zerofill启用时有效）    
- **TINYINT**[(length)] [UNSIGNED] [ZEROFILL]
	- 1字节，小整数，保存一些小范围的整数数值
	- 有符号，范围（-128，127）
	- 无符号，范围（0，255）
	- MySQL中无布尔值，使用tinyint(1)构造。
- **INT**[(length)] [UNSIGNED] [ZEROFILL]
	- 4字节，整数，数据类型用于保存一些中等范围的整数数值
	- 有符号： -2147483648 ～ 2147483647
	- 无符号： 0 ～ 4294967295
- **BIGINT**[(length)] [UNSIGNED] [ZEROFILL]
	- 8字节，大整数，数据类型用于保存一些大范围的整数数值
	- 有符号：-9223372036854775808 ～ 9223372036854775807
	- 无符号：0  ～  18446744073709551615

##### 浮点数
- **DECIMAL**[(length[,decimals])] [UNSIGNED] [ZEROFILL]
	- 准确的小数值，length是数字总个数（负号不算），decimals是小数点后个数。 length最大值为65，decimals最大值为30。
	- 特别的：对于精确数值计算时需要用此类型，decaimal能够存储精确值的原因在于其内部按照字符串存储。
- **DOUBLE**[(length,decimals)] [UNSIGNED] [ZEROFILL]
	- 单精度浮点数（非准确小数值），length是数字总个数，decimals是小数点后个数。
	- 有符号：
		- -3.402823466E+38 to -1.175494351E-38
		- 0
		- 1.175494351E-38 3.402823466E+38
	- 无符号：
		- 0
		- 1.175494351E-38 to 3.402823466E+38
- **FLOAT**[(length,decimals)] [UNSIGNED] [ZEROFILL]
	- 双精度浮点数（非准确小数值），length是数字总个数，decimals是小数点后个数。
	- 有符号：
		- -1.7976931348623157E+308 to -2.2250738585072014E-308
		- 0
		- 2.2250738585072014E-308 to 1.7976931348623157E+308
	- 无符号：
		- 0
		- 2.2250738585072014E-308 to 1.7976931348623157E+308

##### 位类型
- **BIT**[(length)]
	- 可以用来存放多位二进制数，length范围从1~64，如果不写默认为1位。
	- 注意：对于位字段需要使用函数读取
		- bin()显示为二进制
		- hex()显示为十六进制

#### 字符串类型
- **CHAR**[(length)] [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
	- 定长，简单粗暴，浪费空间，存取速度快
	- 字符长度范围：0-255（一个中文是一个字符，是utf8编码的3个字节）
	- 存储：
	    - 存储char类型的值时，会往右填充空格来满足长度
	    - 例如：指定长度为10，存>10个字符则报错，存<10个字符则用空格填充直到凑够10个字符存储
    - 检索：
	    - 在检索或者说查询时，查出的结果会自动删除尾部的空格，除非我们打开pad_char_to_full_length SQL模式（SET sql_mode = 'PAD_CHAR_TO_FULL_LENGTH';）
- **VARCHAR(length)** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
	- 变长，精准，节省空间，存取速度慢
	- 字符长度范围：0-65535（如果大于21845会提示用其他类型 。mysql行最大限制为65535字节，字符编码为utf-8：https://dev.mysql.com/doc/refman/5.7/en/column-count-limit.html）
	- 存储：
		- varchar类型存储数据的真实内容，不会用空格填充，如果'ab  ',尾部的空格也会被存起来
		- 强调：varchar类型会在真实数据前加1-2Bytes的前缀，该前缀用来表示真实数据的bytes字节数（1-2Bytes最大表示65535个数字，正好符合mysql对row的最大字节限制，即已经足够使用）
		- 如果真实的数据<255bytes则需要1Bytes的前缀（1Bytes=8bit 2**8最大表示的数字为255）
		- 如果真实的数据>255bytes则需要2Bytes的前缀（2Bytes=16bit 2**16最大表示的数字为65535）
	- 检索：
		- 尾部有空格会保存下来，在检索或者说查询时，也会正常显示包含空格在内的内容

#### 日期
- **DATE**
	- YYYY-MM-DD（1000-01-01/9999-12-31）
- **YEAR**
	- YYYY（1901/2155）
- **TIME**[(fsp)]
	- HH:MM:SS（'-838:59:59'/'838:59:59'）
- **DATETIME**[(fsp)]
	- YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）
- TIMESTAMP
	- YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）         

	```sql
	create table student(id int,name char(5),born_date date,born_year year,reg_time datetime,class_time time);
	
	mysql> desc student;
	+------------+----------+------+-----+---------+-------+
	| Field      | Type     | Null | Key | Default | Extra |
	+------------+----------+------+-----+---------+-------+
	| id         | int(11)  | YES  |     | NULL    |       |
	| name       | char(5)  | YES  |     | NULL    |       |
	| born_date  | date     | YES  |     | NULL    |       |
	| born_year  | year(4)  | YES  |     | NULL    |       |
	| reg_time   | datetime | YES  |     | NULL    |       |
	| class_time | time     | YES  |     | NULL    |       |
	+------------+----------+------+-----+---------+-------+
	
	insert into student values(1,'chuck',now(),now(),now(),now());
	
	mysql> select * from student;
	+------+-------+------------+-----------+---------------------+------------+
	| id   | name  | born_date  | born_year | reg_time            | class_time |
	+------+-------+------------+-----------+---------------------+------------+
	|    1 | chuck | 2017-09-06 |      2017 | 2017-09-06 10:52:12 | 10:52:12   |
	+------+-------+------------+-----------+---------------------+------------+
	1 row in set (0.00 sec)
	```

#### 枚举与集合
- **ENUM(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
	- 规定一个范围，赋值时只能取其中一个
- **SET(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
	- 规定一个范围，赋值时可以取其中一个或多个           

	```sql
	create table student(
		id int primary key auto_increment,
		name char(5),
		sex enum('male','female'),
		hobbies set('coding','read','music','study')
		);
	
	mysql> desc student;
	+---------+--------------------------------------+------+-----+---------+----------------+
	| Field   | Type                                 | Null | Key | Default | Extra          |
	+---------+--------------------------------------+------+-----+---------+----------------+
	| id      | int(11)                              | NO   | PRI | NULL    | auto_increment |
	| name    | char(5)                              | YES  |     | NULL    |                |
	| sex     | enum('male','female')                | YES  |     | NULL    |                |
	| hobbies | set('coding','read','music','study') | YES  |     | NULL    |                |
	+---------+--------------------------------------+------+-----+---------+----------------+
	
	insert into student(name,sex,hobbies) values('chuck','male','coding,read,music');
	
	mysql> select * from student;
	+----+-------+------+-------------------+
	| id | name  | sex  | hobbies           |
	+----+-------+------+-------------------+
	|  1 | chuck | male | coding,read,music |
	+----+-------+------+-------------------+
	```

<p align=right>[回到顶部](#0)</p>
### <span id='3.6'>完整性约束</span>
#### 其他约束条件
- UNSIGNED 无符号
- ZEROFILL 使用0填充  

- NOT NULL    标识该字段不能为空
- DEFAULT    为该字段设置默认值       

	```sql
	[not null]
	create table student2(
		id int primary key auto_increment,
		name char(5),
		sex enum('male','female') not null,
		hobbies set('coding','read','music','study')
		);
	
	
	[default]
	insert into student2(name,sex,hobbies) values('chuck',null,'coding,read,music');
	insert into student2(name,hobbies) values('chuck2','coding,read,music');
	
	create table student3(
		id int primary key auto_increment,
		name char(5),
		age int not null default 18
		);
	```

#### 唯一、主键
- PRIMARY KEY (PK)    标识该字段为该表的主键，不为空且唯一
- UNIQUE KEY (UK)    标识该字段的值是唯一的，若为空则不限
- 单列唯一     

	```sql
	create table teacher(
		id int not null unique,
		name char(5)
		);
	```
- 多列唯一         

	```sql
	create table services(
		name char(10),
		host char(15),
		port int,
		unique(host,port)	
		);
	
	mysql> desc services;
	+-------+----------+------+-----+---------+-------+
	| Field | Type     | Null | Key | Default | Extra |
	+-------+----------+------+-----+---------+-------+
	| name  | char(10) | YES  |     | NULL    |       |
	| host  | char(15) | YES  | MUL | NULL    |       |
	| port  | int(11)  | YES  |     | NULL    |       |
	+-------+----------+------+-----+---------+-------+
	
	mysql> show create table services;
	+----------+-----------------------------------------------------------------+
	| Table    | Create Table                                                    |
	+----------+-----------------------------------------------------------------+
	| services | CREATE TABLE `services` (                                       |
	|          |  `name` char(10) DEFAULT NULL,                                  |
	|          |  `host` char(15) DEFAULT NULL,                                  |
	|          |  `port` int(11) DEFAULT NULL,                                   |
	|          |  UNIQUE KEY `host` (`host`,`port`)                              |
	|          |  ) ENGINE=InnoDB DEFAULT CHARSET=utf8                           |
	+----------+-----------------------------------------------------------------+
	
	insert into services values('ftp','127.0.0.1',8080);
	insert into services values('ftp','127.0.0.1',8080);
	insert into services values('ftp','127.0.0.1',8081);
	```

#### 自增长
- AUTO_INCREMENT    标识该字段的值自动增长（整数类型，而且为主键）
	- auto_increment_offset 偏移量
	- auto_increment_increment 步长          

	```sql
	create table dep(
		id int primary key auto_increment,
		name char(10)
		);
	
	insert into dep(name) values('IT'),('Boss'),('HR'),('Sale');
	select * from dep;
	+----+------+
	| id | name |
	+----+------+
	|  1 | IT   |
	|  2 | Boss |
	|  3 | HR   |
	|  4 | Sale |
	+----+------+
	
	show create table dep;
	+-------+---------------------------------------------------------+
	| Table | Create Table                                            |
	+-------+---------------------------------------------------------+
	| dep   | CREATE TABLE `dep` (
	          `id` int(11) NOT NULL AUTO_INCREMENT,
	          `name` char(10) DEFAULT NULL,
	           PRIMARY KEY (`id`)
	           ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8  |
	+-------+---------------------------------------------------------+
	
	# 可以看到AUTO_INCREMENT就是自增的偏移量，可以在建表的时候通过alter修改
	
	create table dep1(
		id int primary key auto_increment,
		name char(10)
		)auto_increment=10;
	
	show create table dep1;
	+-------+-------------------------------------------------------+
	| Table | Create Table                                          |
	+-------+-------------------------------------------------------+
	| dep1  | CREATE TABLE `dep1` (
	          `id` int(11) NOT NULL AUTO_INCREMENT,
	          `name` char(10) DEFAULT NULL,
	          PRIMARY KEY (`id`)
	         ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 |
	+-------+-------------------------------------------------------+
	
	insert into dep1(name) values('IT'),('Boss'),('HR'),('Sale');
	select * from dep1;
	+----+------+
	| id | name |
	+----+------+
	| 10 | IT   |
	| 11 | Boss |
	| 12 | HR   |
	| 13 | Sale |
	+----+------+
	
	create table dep2(
		id int primary key auto_increment,
		name char(10)
		);
	
	# 对单次会话修改
	# 设置步长
	set session auto_increment_increment=2;
	# 设置初始偏移量
	set session auto_increment_offset=2;
	# 全局修改，所有会话都有效
	# set global auto_increment_increment=2;
	
	insert into dep(name) values('IT'),('Boss'),('HR'),('Sale');
	
	# mysql 特性:初始偏移量不能比步长小，否则初始偏移量会失效
	```

#### 外键
- FOREIGN KEY (FK)    标识该字段为该表的外键     
	
	```sql
	# 表类型必须是innodb存储引擎，且被关联的字段，即references指定的另外一个表的字段，必须保证唯一
	# 必须先创建被关联的父表
	create table dep(
		id int primary key auto_increment,
		name varchar(20) not null
		)engine=innodb;
	
	# dep_id外键，关联父表（dep主键id），同步更新，同步删除
	create table emp(
		id int primary key auto_increselment,
		name varchar(20) not null,
		dpt_id int,
		constraint fk_name foreign key(dpt_id) references dep(id)
		on delete cascade
		on update cascade 
		)engine=innodb;
	
	# 先往父表dep中插入记录
	insert into dep values
		(1,'欧德博爱技术有限事业部'),
		(2,'艾利克斯人力资源部'),
		(3,'销售部');
	
	# 再往子表emp插入记录
	insert into emp values
		(1,'egon',1),
		(2,'alex',2),
		(3,'alex2',2),
		(4,'alex3',2),
		(5,'jack',3),
		(6,'jack2',3),
		(7,'jack3',3),
		(8,'tom',3),
		(9,'tom2',3)
		;
	
	# 删父表dep，子表emp中对应的记录跟着删
	delete from dep where id=2;
	select * from emp;
	+----+-------+--------+
	| id | name  | dpt_id |
	+----+-------+--------+
	|  1 | egon  |      1 |
	|  5 | jack  |      3 |
	|  6 | jack2 |      3 |
	|  7 | jack3 |      3 |
	|  8 | tom   |      3 |
	|  9 | tom2  |      3 |
	+----+-------+--------+
	
	# 更新父表dep，子表emp中对应的记录跟着改
	update dep set id=303 where id =3;
	select * from emp;
	+----+-------+--------+
	| id | name  | dpt_id |
	+----+-------+--------+
	|  1 | egon  |      1 |
	|  5 | jack  |    303 |
	|  6 | jack2 |    303 |
	|  7 | jack3 |    303 |
	|  8 | tom   |    303 |
	|  9 | tom2  |    303 |
	+----+-------+--------+
	```

- 多对一或一对多
	- 被关联的表称父表，外键关联父表的称字表，父表必须比子表先建立
	- 字表多条记录的相同外键值对应父表具有唯一性的一个字段值，称多对一
	- 父表具有唯一性的一个字段值对应字表多条记录的相同外键值，称一对多
- 一对一
	- 子表唯一一条记录对应父表唯一一条记录
- 多对多
	- 子表多条记录对应父表一条记录，父表多条记录对应字表一条记录
	- 专门使用一张新的表记录子表和父表的对应关系

	```sql
	create table author(
	id int primary key auto_increment,
	name varchar(20)
	);
	create table book(
	id int primary key auto_increment,
	name varchar(20)
	);
	
	#这张表就存放作者表与书表的关系，即查询二者的关系查这表就可以了
	create table author2book(
		id int not null unique auto_increment,
		author_id int not null,
		book_id int not null,
		constraint fk_author foreign key(author_id) references author(id)
		on delete cascade on update cascade,
		constraint fk_book foreign key(book_id) references book(id)
		on delete cascade on update cascade,
		primary key(author_id,book_id)
	);
	```

<p align=right>[回到顶部](#0)</p>
## <span id='4.0'>查询语句</span>
### <span id='4.1'>单表查询</span>
- **SELECT** 
	- [DISTINCT] 
    - **select_expr** [, select_expr ...]
    - [**FROM** **table_references** 
	    - [**WHERE** where_condition]
	    - [**GROUP BY** {col_name \| expr \| position} [ASC \| DESC], ... [WITH ROLLUP]]
	    - [**HAVING** where_condition]
	    - [**ORDER BY** {col_name \| expr \| position} [ASC \| DESC], ...]
	    - [**LIMIT** {[offset,] row_count \| row_count OFFSET offset}]

#### 关键字的执行优先级及详细用法
- from  导入表
- where  约束条件取出记录
	1. 比较运算符：> < >= <= <> !=
	2. between 80 and 100 值在10到20之间
	3. in(80,90,100) 值是10或20或30
	4. like '_egon%'  
		- %表示任意多字符
		- _表示一个字符 
	5. 逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not
	6. 正则表达式 
		- REGEXP '^ale'
		- REGEXP 'on$'
		- REGEXP 'm{2}'

- group by  将取出的记录按照条件分组
	- 按照指定字段分组，那么select查询的字段只能是指定分组的字段，想要获取组内的其他相关信息，需要借助聚合函数

- 聚合函数  对分好组的记录按照指定字段聚合
	- GROUP_CONCAT() 将分组内指定字段组合成一条字符串
	- COUNT() 将分组内指定字段统计计数
	- MAX() 从分组内指定字段取出最大值
	- MIN() 从分组内指定字段取出最小值
	- SUM() 将分组内指定字段求和
	- AVG() 将分组内指定字段求平均数

- having  按照筛选条件筛选记录
	- 筛选条件同where
	- 如果有分组，还可以使用聚合函数

- select  按照给出字段名组合成虚拟表
- distinct  字段去重
- order by  将结果按照条件排序
	- ASC 从小到大排序
	- DESC 从大到小排序
	- 多列排序
		- 跟多个字段和排序顺序，对前一个排序后结果有相同的时候继续排序
		- SELECT * from employee ORDER BY age, salary DESC;
		- 按照年龄从小到大排序，当年龄相同按照薪资从大到小排序

- limit  限制结果的显示条数
	- limit n  默认从0开始，排到n
	- limit n,m  从n开始，显示m条 

### <span id='4.2'>多表查询</span>
- SELECT [DISTINCT] <select_list>
	- FROM <left_table>
	- <join_type> JOIN <right_table> ON <join_condition>
	- WHERE <where_condition>
	- GROUP BY <group_by_list>
	- HAVING <having_condition>
	- ORDER BY <order_by_condition>
	- LIMIT <limit_number>

#### 连接查询
- 交叉连接
	- 使用逗号隔开表，不增加查询条件，生成笛卡尔积，不推荐使用
	- select \* from t1,t2; 

- 内连接
	- 找两张表共有的部分，相当于利用条件从笛卡尔积结果中筛选出了正确的结果
	- select t1.field,t2.field from t1 inner join t2 on t1.filed1=t2.filed2

- 外链接-优先左连接
	- 在内连接的基础上增加左边有右边没有的结果
	- select t1.field,t2.field from t1 left join t2 on t1.filed1=t2.filed2

- 外链接-优先右链接
	- 在内连接的基础上增加右边有左边没有的结果
	- select t1.field,t2.field from t1 right join t2 on t1.filed1=t2.filed2

- 外链接-全连接
	- 在内连接的基础上增加左边有右边没有的和右边有左边没有的结果
	- select t1.field,t2.field from t1 left join t2 on t1.filed1=t2.filed2
	- union
	- select t1.field,t2.field from t1 right join t2 on t1.filed1=t2.filed2

#### 子查询(嵌套查询)
- 子查询是将一个查询语句嵌套在另一个查询语句中
- 内层查询语句的查询结果，可以为外层查询语句提供查询条件或者表
- 可用关键字IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS
- 还可以包含比较运算符：= 、 !=、> 、<等
- select \* from t1 where field=(select field2 from t2 where id>5);

查询练习：


<p align=right>[回到顶部](#0)</p>
## <span id='5.0'>索引</span>
- 索引的目的在于提高查询效率
- 通过不断地缩小想要获取数据的范围来筛选出最终想要的结果，同时把随机的事件变成顺序的事件，也就是说，有了这种索引机制，我们可以总是用同一种查找方式来锁定数据。

详细参阅http://www.cnblogs.com/linhaifeng/articles/7274563.html#_label2

- 普通索引
- 主键索引
- 唯一索引
- 联合索引
	- 最左前缀原则，匹配时只匹配最左边的
	- 如name,email,pwd，只有包括name的条件才能命中索引
- 命中索引，创建索引也未命中，需要了解如何命中索引


<p align=right>[回到顶部](#0)</p>
## <span id='6.0'>Pymysql</span>
### 用法示例
#### 查询
```python
import pymysql

# 链接mysql，使用数据库
conn = pymysql.connect(host='localhost', user='root', password='', database='day47', charset='utf8')
# 拿到mysql的游标（可接收输入命令的）
cursor = conn.cursor()
# 编写sql语句
sql = 'select * from user;'
# 拿到受影响的行数
res = cursor.execute(sql)
print('%s rows in set (0.00sec)'%res)

cursor.close()
conn.close()
```

##### 实现用户登录
```python
import pymysql

user = input('username: ').strip()
pwd = input('password: ').strip()

# 链接mysql，使用数据库
conn = pymysql.connect(host='localhost', user='root', password='', database='day47', charset='utf8')
# 拿到mysql的游标（可接收输入命令的）
cursor = conn.cursor()

sql = 'select * from user where name="%s" and pwd="%s";' % (user, pwd)
print(sql)
# 拿到受影响的行数
res = cursor.execute(sql)
# 当查询有结果说明用户名和密码是正确的则登录成功
if res:
    print('Login success')
else:
    print('Login failure')

cursor.close()
conn.close()
```

##### sql注入
在上面的例子中，按照给定的标准输入用户名和密码可以正常登陆，但是如果非正常输入呢？
对于上面的例子，登录时输入：
```python
username: xxx" or 1=1 #
password: 
select * from user where name="xxx" or 1=1 #" and pwd="";
Login success
```
- 明显用户名和密码不是正确的但是依然登陆成功，可以复制第三行生成的sql语句在终端里面输入一下，看看是什么情况：

	```sql
	mysql> select * from user where name="xxx" or 1=1 #" and pwd="";
	    -> ;
	+----+-------+------+
	| id | name  | pwd  |
	+----+-------+------+
	|  1 | egon  | 123  |
	|  2 | alex  | 123  |
	|  3 | chuan | 123  |
	+----+-------+------+
	3 rows in set (0.00 sec)
	```
- 可以发现or语句后面1=1是成立的，所以where总是true，其次'#'号在sql语句中是注释，将后面的语句都注释掉了。这种非正常的用户输入导致的问题就是sql注入。
- 解决办法就是对用户的输入进行语法检查（但要知道，这并不总是有效的），对于pymysql来说提供了检查服务：

	```python
	import pymysql
	
	user = input('username: ').strip()
	pwd = input('password: ').strip()
	
	# 链接mysql，使用数据库
	conn = pymysql.connect(host='localhost', user='root', password='', database='day47')
	# 拿到mysql的游标（可接收输入命令的）
	cursor = conn.cursor()
	
	sql = 'select * from user where name=%s and pwd=%s;'
	
	# 拿到受影响的行数
	res = cursor.execute(sql, (user, pwd))
	
	if res:
	    print('Login success')
	else:
	    print('Login failure')
	
	cursor.close()
	conn.close()
	```

#### 增加、删除、修改
```python
import pymysql

# 链接mysql，使用数据库
# conn = pymysql.connect(host='localhost', user='root', password='', database='day47')
# conn.set_charset('utf8')
conn = pymysql.connect(host='localhost', user='root', password='', database='day47', charset='utf8')


# 拿到mysql的游标（可接收输入命令的）
cursor = conn.cursor()

sql = 'insert into user(name, pwd) values(%s, %s);'

# 拿到受影响的行数
# 插入单条记录
# res = cursor.execute(sql, ('哈大', '123'))
# 插入多条记录
res = cursor.executemany(sql, [('哈大', '123'), ('sada', '123')])

print('%s rows in set (0.00sec)' % res)

# 提交到mysql才算修改了
conn.commit()

cursor.close()
conn.close()
```

#### 读取查询记录   
```python

import pymysql


# 链接mysql，使用数据库
conn = pymysql.connect(host='localhost', user='root', password='', database='day47')
conn.set_charset('utf8')
# 拿到mysql的游标（可接收输入命令的）
cursor = conn.cursor()

sql = 'select * from user;'

# 执行sql语句
cursor.execute(sql)
```
- 逐条取出

	```python
	rows = cursor.fetchone()
	rows2 = cursor.fetchone()
	rows3 = cursor.fetchone()
	print(rows)
	print(rows2)
	print(rows3)
	```
- 多条取出
	
	```python
	print(cursor.fetchmany(3))
	print(cursor.fetchone())
	```
- 全部取出

	```python
	print(cursor.fetchall())
	print(cursor.fetchone())
	```
- 光标移动-绝对位置

	```python
	print(cursor.fetchall())
	cursor.scroll(2, mode='absolute')   # 绝对位置，以文件开头为目标，数字表示移动次数
	print(cursor.fetchall())
	```
- 光标移动相对位位置

	```python
	print(cursor.fetchone())
	print(cursor.fetchone())
	cursor.scroll(-1, mode='relative')   # 相对位置，以当前光标为目标，数字表示移动次数
	print(cursor.fetchall())
	
	cursor.close()
	conn.close()
	```

<p align=right>[回到顶部](#0)</p>
## other
在MySQL内查看所有配置信息          

LAMP

Apache MySQL PHP
Linux


LNMP
Nginx MySQL PHP/Python
Linux 

MySQL --> MariaDB 
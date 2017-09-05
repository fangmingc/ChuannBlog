# MySQL

## 数据库基础
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

## MySQL准备使用
### Liunx环境
### Windows环境
#### 下载
在官网下载相应版本。  
官网链接：https://dev.mysql.com/downloads/mysql

#### 解压
如果想要让MySQL安装在指定目录，那么就将解压后的文件夹移动到指定目录，如：C:\mysql-5.7.16-winx64   

#### 初始化
- MySQL解压后的 bin 目录下有一大堆的可执行文件，执行如下命令初始化数据   
	```
	cd c:\mysql-5.7.16-winx64\bin
	mysqld --initialize-insecure
	```

#### 启动MySQL服务
- 执行命令从而启动MySQL服务     
	```
	# 进入可执行文件目录
	cd c:\mysql-5.7.16-winx64\bin
	 
	# 启动MySQL服务
	mysqld
	```

#### 启动MySQL客户端连接到MySQL服务
- 由于初始化时使用的【mysqld --initialize-insecure】命令，其默认未给root账户设置密码
	```python
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
	```python
	# 启动MySQL服务，在终端任意目录输入
	mysqld
	# 连接MySQL服务，在终端任意目录输入：
	mysql -u root -p
	```

##### 将MySQL服务制作成windows服务
```python
# 制作MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --install
 
# 移除MySQL的Windows服务，在终端执行此命令：
"c:\mysql-5.7.16-winx64\bin\mysqld" --remove
```

- 注册成服务之后，以后再启动和关闭MySQL服务时，仅需执行如下命令(管理员权限下)
	```python
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
	- 可以在一些命令后接 | 在命令的结果中查找
- tasklist
	- 该工具显示在本地或远程机器上当前运行的进程列表
	- 显示结果由5部分组成：图像名(进程名)、PID、会话名、会话和内存使用
	- tasklist |findstr explorer
- taskkill
	- 使用该工具按照进程 ID (PID) 或映像名称终止任务
	- /T 删除指定进程及子进程
	- /F 强制删除进程
	- /PID 以PID形式删除进程

### MySQL软件基本管理
#### 第一次登录后设置密码
- 初始状态下，管理员root，密码为空，默认只允许从本机登录localhost
- 设置密码       
	```python
	mysqladmin -uroot password "123"        
	# 设置初始密码 由于原密码为空，因此-p可以不用
	mysqladmin -uroot -p"123" password "456"        
	# 修改mysql密码,因为已经有密码了，所以必须输入原密码才能设置新密码
	``` 
- 登录命令格式      
	```python
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
	```python
	step 1: SET PASSWORD = PASSWORD('your new password');
	step 2: ALTER USER 'root'@'localhost' PASSWORD EXPIRE NEVER;
	step 3: flush privileges;
	```

## SQL语句（Structured Query Language）
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

### 库（文件夹）操作
#### 增
- **CREATE** **{DATABASE | SCHEMA}** [IF NOT EXISTS] **db_name** [create_specification] ... 
	- **create_specification**: [DEFAULT] CHARACTER SET [=] charset_name | [DEFAULT] COLLATE [=] collation_name     
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
- **ALTER** **{DATABASE | SCHEMA}** [db_name] alter_specification ...
	- **alter_specification**: [DEFAULT] CHARACTER SET [=] charset_name | [DEFAULT] COLLATE [=] collation_name
- **ALTER** **{DATABASE | SCHEMA}** **db_name** **UPGRADE** **DATA DIRECTORY NAME**    
```sql
alter database db1 charset gbk;
```

#### 删   
- **DROP** **{DATABASE | SCHEMA}** [IF EXISTS] **db_name**      
```sql
drop database db1;
```

### 表（文件）操作
切换到文件夹下：   
#### 增   
**简易例子**：        
```sql
create table t1(id int, name char(10)) engine=innodb;
create table t2(id int, name char(10)) engine=innodb;
create table t4 select * from t1 where 1=2;
```

**完整命令**：       
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name(create_definition,...)**  [table_options] [partition_options]
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name**[(create_definition,...)]  [table_options] [partition_options] [IGNORE | REPLACE] [AS] **query_expression**
- **CREATE** [TEMPORARY] **TABLE** [IF NOT EXISTS] **tbl_name{ LIKE old_tbl_name | (LIKE old_tbl_name) }**
	- **create_definition**:
		- **col_name** 
		- **column_definition** 
		- | [CONSTRAINT [symbol]] **PRIMARY KEY** [index_type] (index_col_name,...)  [index_option] ...
		- | **{INDEX|KEY}** [index_name] [index_type] (index_col_name,...) [index_option] ...
		- | [CONSTRAINT [symbol]] **UNIQUE** [INDEX|KEY] [index_name] [index_type] (index_col_name,...) [index_option] ... 
		- | **{FULLTEXT|SPATIAL}** [INDEX|KEY] [index_name] (index_col_name,...)  [index_option] ...
		- | [CONSTRAINT [symbol]] **FOREIGN KEY** [index_name] (index_col_name,...) **reference_definition**
		- | **CHECK(expr)**
			- **column_definition**:
		    	- **data_type** [NOT NULL | NULL] [DEFAULT default_value] [AUTO_INCREMENT] [UNIQUE [KEY] | [PRIMARY] KEY] [COMMENT 'string'] [COLUMN_FORMAT {FIXED|DYNAMIC|DEFAULT}] [STORAGE {DISK|MEMORY|DEFAULT}] [reference_definition]
		    	- | **data_type** [GENERATED ALWAYS] **AS** **(expression)** [VIRTUAL | STORED] [UNIQUE [KEY]] [COMMENT comment] [NOT NULL | NULL] [[PRIMARY] KEY]
					- **data_type**:
						- **BIT**[(length)]
						- | **TINYINT**[(length)] [UNSIGNED] [ZEROFILL]
						- | **SMALLINT**[(length)] [UNSIGNED] [ZEROFILL]
						- | **MEDIUMINT**[(length)] [UNSIGNED] [ZEROFILL]
						- | **INT**[(length)] [UNSIGNED] [ZEROFILL]
						- | **INTEGER**[(length)] [UNSIGNED] [ZEROFILL]
						- | **BIGINT**[(length)] [UNSIGNED] [ZEROFILL]
						- | **REAL**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- | **DOUBLE**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- | **FLOAT**[(length,decimals)] [UNSIGNED] [ZEROFILL]
						- | **DECIMAL**[(length[,decimals])] [UNSIGNED] [ZEROFILL]
						- | **NUMERIC**[(length[,decimals])] [UNSIGNED] [ZEROFILL]
						- | **DATE**
						- | **TIME**[(fsp)]
						- | **TIMESTAMP**[(fsp)]
						- | **DATETIME**[(fsp)]
						- | **YEAR**
						- | **CHAR**[(length)] [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **VARCHAR(length)** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **BINARY**[(length)]
						- | **VARBINARY(length)**
						- | **TINYBLOB**
						- | **BLOB**
						- | **MEDIUMBLOB**
						- | **LONGBLOB**
						- | **TINYTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **TEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **MEDIUMTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **LONGTEXT** [BINARY] [CHARACTER SET charset_name] [COLLATE collation_name] 
						- | **ENUM(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **SET(value1,value2,value3,...)** [CHARACTER SET charset_name] [COLLATE collation_name]
						- | **JSON**
						- | **spatial_type**
			- **index_col_name**:
		    	- **col_name** [(length)] [ASC | DESC]
			- **index_type**:
			    - **USING {BTREE | HASH}**
			- **index_option**:
				- **KEY_BLOCK_SIZE** [=] **value**
				- | **index_type**
				- | **WITH PARSER parser_name**
				- | **COMMENT 'string'**
			- **reference_definition**:
				- **REFERENCES tbl_name(index_col_name,...)** [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE] [ON DELETE reference_option] [ON UPDATE reference_option]
			- **reference_option**: 
				- **RESTRICT** | **CASCADE** | **SET NULL** | **NO ACTION** | **SET DEFAULT**
	- **table_options**:
		- **table_option** [[,] table_option] ...
			- **table_option**:
				- **ENGINE** [=] **engine_name**
				- | **AUTO_INCREMENT** [=] **value**
				- | **AVG_ROW_LENGTH** [=] **value**
				- | [DEFAULT] **CHARACTER SET** [=] **charset_name**
				- | **CHECKSUM** [=] **{0 | 1}**
				- | [DEFAULT] **COLLATE** [=] **collation_name**
				- | **COMMENT** [=] **'string'**
				- | **COMPRESSION** [=] **{'ZLIB'|'LZ4'|'NONE'}**
				- | **CONNECTION** [=] **'connect_string'**
				- | **DATA DIRECTORY** [=] **'absolute path to directory'**
				- | **DELAY_KEY_WRITE** [=] **{0 | 1}**
				- | **ENCRYPTION** [=] **{'Y' | 'N'}**
				- | **INDEX DIRECTORY** [=] **'absolute path to directory'**
				- | **INSERT_METHOD** [=] **{ NO | FIRST | LAST }**
				- | **KEY_BLOCK_SIZE** [=] **value**
				- | **MAX_ROWS** [=] **value**
				- | **MIN_ROWS** [=] **value**
				- | **PACK_KEYS** [=] **{0 | 1 | DEFAULT}**
				- | **PASSWORD** [=] **'string'**
				- | **ROW_FORMAT** [=] **{DEFAULT|DYNAMIC|FIXED|COMPRESSED|REDUNDANT|COMPACT}**
				- | **STATS_AUTO_RECALC** [=] **{DEFAULT|0|1}**
				- | **STATS_PERSISTENT** [=] **{DEFAULT|0|1}**
				- | **STATS_SAMPLE_PAGES** [=] **value**
				- | **TABLESPACE tablespace_name** [STORAGE {DISK|MEMORY|DEFAULT}]
				- | **UNION** [=] **(tbl_name[,tbl_name]...)**
	- **partition_options**:
		- **PARTITION BY** { [LINEAR] **HASH(expr)** | [LINEAR] **KEY** [ALGORITHM={1|2}](column_list) | **RANGE{(expr)** | **COLUMNS(column_list)**} | **LIST{(expr)** | **COLUMNS(column_list)**} }
		- [PARTITIONS num]
		- [SUBPARTITION BY { [LINEAR] **HASH(expr)** | [LINEAR] **KEY** [ALGORITHM={1|2}] (column_list) } [SUBPARTITIONS num]]
		- [(partition_definition [, partition_definition] ...)]
			- **partition_definition**:
				- **PARTITION** **partition_name**
					- [VALUES {LESS THAN {(expr | value_list) | MAXVALUE} | IN (value_list)}]
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
- **SHOW** [FULL] **TABLES** [{FROM | IN} db_name] [LIKE 'pattern' | WHERE expr]     
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
		- | **ADD** [COLUMN] **col_name column_definition** [FIRST | AFTER col_name ]
		- | **ADD** [COLUMN] **(col_name column_definition,...)**
		- | **ADD** **{INDEX|KEY}** [index_name] [index_type] **(index_col_name,...)** [index_option] ...
		- | **ADD** [CONSTRAINT [symbol]] **PRIMARY KEY** [index_type] **(index_col_name,...)** [index_option] ...
		- | **ADD** [CONSTRAINT [symbol]] **UNIQUE** [INDEX|KEY] [index_name] [index_type] **(index_col_name,...)** [index_option] ...
		- | **ADD FULLTEXT** [INDEX|KEY] [index_name] **(index_col_name,...)** [index_option] ...
		- | **ADD SPATIAL** [INDEX|KEY] [index_name] **(index_col_name,...)** [index_option] ...
		- | **ADD** [CONSTRAINT [symbol]] **FOREIGN KEY** [index_name] **(index_col_name,...) reference_definition**
		- | **ALGORITHM** [=] **{DEFAULT|INPLACE|COPY}**
		- | **ALTER** [COLUMN] **col_name {SET DEFAULT literal | DROP DEFAULT}**
		- | **CHANGE** [COLUMN] **old_col_name new_col_name column_definition** [FIRST|AFTER col_name]
		- | **LOCK** [=] **{DEFAULT|NONE|SHARED|EXCLUSIVE}**
		- | **MODIFY** [COLUMN] **col_name column_definition** [FIRST | AFTER col_name]
		- | **DROP** [COLUMN] **col_name**
		- | **DROP PRIMARY KEY**
		- | **DROP {INDEX|KEY} index_name**
		- | **DROP FOREIGN KEY fk_symbol**
		- | **DISABLE KEYS**
		- | **ENABLE KEYS**
		- | **RENAME** [TO|AS] **new_tbl_name**
		- | **RENAME {INDEX|KEY} old_index_name TO new_index_name**
		- | **ORDER BY col_name** [, col_name] ...
		- | **CONVERT TO CHARACTER SET charset_name** [COLLATE collation_name]
		- | [DEFAULT] **CHARACTER SET** [=] **charset_name** [COLLATE [=] collation_name]
		- | **DISCARD TABLESPACE**
		- | **IMPORT TABLESPACE**
		- | **FORCE**
		- | **{WITHOUT|WITH} VALIDATION**
		- | **ADD PARTITION (partition_definition)**
		- | **DROP PARTITION partition_names**
		- | **DISCARD PARTITION {partition_names | ALL} TABLESPACE**
		- | **IMPORT PARTITION {partition_names | ALL} TABLESPACE**
		- | **TRUNCATE PARTITION {partition_names | ALL}**
		- | **COALESCE PARTITION number**
		- | **REORGANIZE PARTITION partition_names INTO (partition_definitions)**
		- | **EXCHANGE PARTITION partition_name WITH TABLE tbl_name** [{WITH|WITHOUT} VALIDTION]
		- | **ANALYZE PARTITION {partition_names | ALL}**
		- | **CHECK PARTITION {partition_names | ALL}**
		- | **OPTIMIZE PARTITION {partition_names | ALL}**
		- | **REBUILD PARTITION {partition_names | ALL}**
		- | **REPAIR PARTITION {partition_names | ALL}**
		- | **REMOVE PARTITIONING**
		- | **UPGRADE PARTITIONING**
			- **index_col_name**:
				- **col_name** [(length)] [ASC | DESC]
			- **index_type**:
				- **USING {BTREE | HASH}**
			- **index_option**:
				- **KEY_BLOCK_SIZE** [=] **value**
				- | **index_type**
				- | **WITH PARSER parser_name**
				- | **COMMENT 'string'**
			- **table_options**:
				- **table_option** [[,] table_option] ...
					- **table_option**:
						- **ENGINE** [=] **engine_name**
						- | **AUTO_INCREMENT** [=] **value**
						- | **AVG_ROW_LENGTH** [=] **value**
						- | [DEFAULT] **CHARACTER SET** [=] **charset_name**
						- | **CHECKSUM** [=] **{0 | 1}**
						- | [DEFAULT] **COLLATE** [=] **collation_name**
						- | **COMMENT** [=] **'string'**
						- | **COMPRESSION** [=] **{'ZLIB'|'LZ4'|'NONE'}**
						- | **CONNECTION** [=] **'connect_string'**
						- | **DATA DIRECTORY** [=] **'absolute path to directory'**
						- | **DELAY_KEY_WRITE** [=] **{0 | 1}**
						- | **ENCRYPTION** [=] **{'Y' | 'N'}**
						- | **INDEX DIRECTORY** [=] **'absolute path to directory'**
						- | **INSERT_METHOD** [=] **{ NO | FIRST | LAST }**
						- | **KEY_BLOCK_SIZE** [=] **value**
						- | **MAX_ROWS** [=] **value**
						- | **MIN_ROWS** [=] **value**
						- | **PACK_KEYS** [=] **{0 | 1 | DEFAULT}**
						- | **PASSWORD** [=] **'string'**
						- | **ROW_FORMAT** [=] **{DEFAULT|DYNAMIC|FIXED|COMPRESSED|REDUNDANT|COMPACT}**
						- | **STATS_AUTO_RECALC** [=] **{DEFAULT|0|1}**
						- | **STATS_PERSISTENT** [=] **{DEFAULT|0|1}**
						- | **STATS_SAMPLE_PAGES** [=] **value**
						- | **TABLESPACE tablespace_name** [STORAGE {DISK|MEMORY|DEFAULT}]
						- | **UNION** [=] **(tbl_name[,tbl_name]...)**
	- **partition_options**:(see CREATE TABLE options)
#### 删  
- **DROP** [TEMPORARY] **TABLE** [IF EXISTS] **tbl_name** [, tbl_name] ... [RESTRICT | CASCADE]
```sql
drop table t2;
```

### 记录（文件内容）操作
#### 增   
```sql
insert into db1.t1 values(1,'chuck',19),(2,'chuck2',20),(3,'chuck3',21);
insert into t1 value(4,'chuck4',20);
insert into t1(name) value('chuck5');
```
- **INSERT** [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] [(col_name,...)] **{VALUES | VALUE}({expr | DEFAULT},...)**,(...),... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
- **INSERT** [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] **SET col_name={expr | DEFAULT}**, ... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
- **INSERT** [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE] [INTO] **tbl_name** [PARTITION (partition_name,...)] [(col_name,...)] **SELECT** ... [ ON DUPLICATE KEY UPDATE col_name=expr [, col_name=expr] ... ]
#### 查   
```sql
select \* from t1;
select name from t1;
select name,id from t1;
```

- **SELECT** 
	- [ALL | DISTINCT | DISTINCTROW ]
	- [HIGH_PRIORITY] 
	- [STRAIGHT_JOIN] 
	- [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT] 
	- [SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    - **select_expr** [, select_expr ...]
    - [**FROM** **table_references** 
	    - [**PARTITION** partition_list]
	    - [**WHERE** where_condition]
	    - [**GROUP BY** {col_name | expr | position} [ASC | DESC], ... [WITH ROLLUP]]
	    - [**HAVING** where_condition]
	    - [**ORDER BY** {col_name | expr | position} [ASC | DESC], ...]
	    - [**LIMIT** {[offset,] row_count | row_count OFFSET offset}]
	    - [**PROCEDURE** procedure_name(argument_list)]
	    - [**INTO OUTFILE** 'file_name' [CHARACTER SET charset_name] export_options
		    - | **INTO DUMPFILE** 'file_name'
		    - | **INTO** var_name [, var_name]]
		- [**FOR UPDATE** | **LOCK IN SHARE MODE**]]

#### 改   
```sql
update t1 set name='NOBODY' where id=4;
update t1 set name='None' where name=chuck;
update t1 set id=12 where name='None';
```

#### 删     
```sql
delete from t1 where id=4;
delete from t1; # 清空表

truncate # :截断，比delete删除快         
truncate t1; # 清空表      
```
**Single-table syntax**
- UPDATE [LOW_PRIORITY] [IGNORE] table_reference SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ... [WHERE where_condition] [ORDER BY ...] [LIMIT row_count]        

**Multiple-table syntax**
- UPDATE [LOW_PRIORITY] [IGNORE] table_references SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ... [WHERE where_condition]

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
```

### 清空记录
```sql

```

## 授权
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
- **GRANT** **priv_type** [(column_list)] [, priv_type [(column_list)]] ... **ON** [object_type] **priv_level** **TO** **user** [auth_option] [, user [auth_option]] ... [REQUIRE {NONE | tls_option [[AND] tls_option] ...}] [WITH {GRANT OPTION | resource_option} ...]   
- **GRANT** **PROXY** **ON** **user** **TO** **user** [, user] ... [WITH GRANT OPTION]
	- **object_type**: {TABLE | FUNCTION | PROCEDURE }
	- **priv_level**: { \* | \*.\* | db_name.\* | db_name.tbl_name | tbl_name | db_name.routine_name }
	- **user**:(see http://dev.mysql.com/doc/refman/5.7/en/account-names.html)
	- **auth_option**:{ **# Before MySQL 5.7.6** IDENTIFIED BY 'auth_string' | IDENTIFIED BY PASSWORD 'hash_string' | IDENTIFIED WITH auth_plugin | IDENTIFIED WITH auth_plugin AS 'hash_string'}
	- **auth_option**: { **# As of MySQL 5.7.6** IDENTIFIED BY 'auth_string' | IDENTIFIED BY PASSWORD 'hash_string' | IDENTIFIED WITH auth_plugin | IDENTIFIED WITH auth_plugin BY 'auth_string' | IDENTIFIED WITH auth_plugin AS 'hash_string'}
	- **tls_option**: { SSL | X509 | CIPHER 'cipher' | ISSUER 'issuer' | SUBJECT 'subject' }
	- **resource_option**: { | MAX_QUERIES_PER_HOUR count | MAX_UPDATES_PER_HOUR count | MAX_CONNECTIONS_PER_HOUR count | MAX_USER_CONNECTIONS count }

## other
在MySQL内查看所有配置信息          
```sql
\s
```
LAMP

Apache MySQL PHP
Linux


LNMP
Nginx MySQL PHP/Python
Linux 

MySQL --> MariaDB 
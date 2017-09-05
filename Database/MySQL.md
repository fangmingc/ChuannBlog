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

## SQL语句
查看当前用户信息
```sql
select user();
```

### 库（文件夹）操作
- 增   
```sql
create database db1 charset utf8;
```
- 查   
```sql
show databases;
show create database db1;
```
- 改  
```sql
alter database db1 charset gbk;
```
- 删   
```sql
drop database db1;
```
### 表（文件）操作
切换到文件夹下：   
- 增   
```sql
create table t1(id int, name char(10)) engine=innodb;
create table t2(id int, name char(10)) engine=innodb;
```
- 查   
```sql
show tables;
show create table t1;

# 查看表结构
desc/describe t1;
```
- 改   
```sql
alter table t1 add age int;
alter table t1 modify name char(12);
```
- 删  
```sql
drop table t2;
```
### 记录（文件内容）操作
- 增   
```sql
insert into db1.t1 values(1,'chuck',19),(2,'chuck2',20),(3,'chuck3',21);
insert into t1 value(4,'chuck4',20);
insert into t1(name) value('chuck5');
```
- 查   
```sql
select \* from t1;
select name from t1;
select name,id from t1;
```
- 改   
```sql
update t1 set name='NOBODY' where id=4;
update t1 set name='None' where name=chuck;
update t1 set id=12 where name='None';
```
- 删     
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

## other
LAMP

Apache MySQL PHP
Linux


LNMP
Nginx MySQL PHP/Python
Linux 

MySQL --> MariaDB 
# MySQL

## 数据库基础
数据库服务器，数据管理系统，数据库，表和记录
装文件的电脑，MySQL软件，文件夹，文件和文件的每一行内容

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
- 方法一     
```windows
#1 关闭mysql
#2 在cmd中执行：mysqld --skip-grant-tables
#3 在cmd中执行：mysql
#4 执行如下sql：
update mysql.user set authentication_string=password('') where user = 'root';
flush privileges;

#5 tskill mysqld(tskill无法使用时先用tasklist寻找mysqld的PID再用taskkill杀死进程)
#6 重新启动mysql
```
- 方法二      
```
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
```
#在mysql的解压目录下，新建my.ini,然后配置
[mysqld]
;skip-grant-tables
port=3306
character_set_server=utf8
#解压的目录
basedir=E:\mysql-5.7.19-winx64
#data目录
datadir=E:\my_data #在mysqld --initialize时，就会将初始数据存入此处指定的目录，在初始化之后，启动mysql时，就会去这个目录里找数据

[client]
port=3306
default-character-set=utf8
```

#### mac上MySQL出现error
> mac mysql error You must reset your password using ALTER USER statement before executing this statement.

- 解决方法     
	```python
	step 1: SET PASSWORD = PASSWORD('your new password');
	step 2: ALTER USER 'root'@'localhost' PASSWORD EXPIRE NEVER;
	step 3: flush privileges;
	```

## other
LAMP

Apache MySQL PHP
Linux


LNMP
Nginx MySQL PHP/Python
Linux 

MySQL --> MariaDB 
## bug及解决方案合集

- centos安装gcc
	- yum -y install gcc gcc-c++ kernel-devel //安装gcc、c++编译器以及内核文件

- python安装mysql-python失败
	- 报错关键词`EnvironmentError: mysql_config not found`
	- ubuntu：
		- `sudo apt install libmysqlclient-dev python-dev`
	- centos
		- `yum install python-devel`
		- `yum install mysql-devel`
- centos7以上安装mysql
	- `yum install mysql-community-server`

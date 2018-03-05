## rabbitmq 安装使用
- [安装Erlang](#1)
- [安装RabbitMQ](#2)


### </span id="1">安装Erlang</span>
- 安装erlang的依赖环境
	- `yum -y install make gcc gcc-c++ kernel-devel m4 ncurses-devel openssl-devel unixODBC-devel`
- 下载最新 Erlang 19.0
	- `wget http://erlang.org/download/otp_src_19.3.tar.gz`
- 解压
	- `tar -xvzf otp_src_19.3.tar.gz`
- 编译配置
	- `cd otp_src_19.3`
	- `./configure --prefix=/usr/local/erlang --with-ssl -enable-threads -enable-smmp-support -enable-kernel-poll --enable-hipe --without-javac`
- 编译
	- `make`
	- `make install`
- 配置Erlang
	- `vim /etc/profile`
	- 添加如下

		```shell
		ERLANG_HOME=/usr/local/erlang
		PATH=$PATH:$ERLANG_HOME/bin
		export PATH ERLANG_HOME
		```
- 配置生效
	- `source /etc/profile`
- 检验erl
	- `erl`
	- ctrl+z退出
- *若修改`/etc/profile`导致无法使用命令
	- 指定编辑文件目录对文件进行修改回原来的代码，并重启虚拟机
		- `/bin/vim /etc/profile`

### </span id="2">安装RabbitMQ</span>
- 下载
	- `wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.6.3/rabbitmq-server-generic-unix-3.6.3.tar.xz`
- 解压
	- `tar -xvf rabbitmq-server-generic-unix-3.6.3.tar.xz`
- 配置使用
	- 切换目录
		- `cd rabbitmq_server-3.6.3/sbin/`
	- 启用web管理界面
		- `./rabbitmq-plugins enable rabbitmq_management`
	- 启动rabbitmq服务
		- `./rabbitmq-server -detached`
	- 新增用户
		- `./rabbitmqctl add_user admin 123456`
	- 设置权限
		- `./rabbitmqctl set_user_tags admin administrator`
	- 设置远程连接权限
		- `./rabbitmqctl set_permissions -p "/" admin ".*" ".*" ".*"`
- 关闭&启动rabbitmq
	- `./rabbitmqctl stop_app`
	- `./rabbitmqctl start_app`
- 浏览器访问
	- 服务器ip:15672



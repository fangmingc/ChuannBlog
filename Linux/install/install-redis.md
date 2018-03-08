## linux安装redis

- 通过wget方式直接在linux上下载Redis
	- `wget http://download.redis.io/releases/redis-4.0.2.tar.gz`
- 解压下载的redis-2.6.17.tar.gz 文件
	- `tar -xvf redis-4.0.2.tar.gz`
- 进入解压后的文件夹
	- `cd redis-4.0.2`
- 编译安装
	- `make`

### 启用与配置
- 启动服务
	- `src/redis-server [指定配置文件]`
		- redis默认监听6379端口，通过配置可以更改监听端口
	- 查看redis是否开始监听
		- `netstat -lnpt |grep redis`
- 启动客户端
	- `src/redis-cli [-p 服务监听的端口]`

- 自定义redis6380.conf，仅供参考
	- 详细的可以打开redis.conf，里面有官方完整的配置及说明

	```conf
	daemonize yes
	pidfile /var/run/redis6380.pid
	port 6380	# 端口
	timeout 0
	tcp-keepalive 0
	loglevel notice
	logfile stdout
	databases 16
	save 900 1
	save 300 10
	save 60 10000
	stop-writes-on-bgsave-error yes
	protected-mode no
	rdbcompression yes
	rdbchecksum yes
	dbfilename dump.rdb
	dir /data/redis/redis6380	# 持久化目录，应当实现创建好这个路径
	slave-serve-stale-data yes
	slave-read-only yes
	repl-disable-tcp-nodelay no
	slave-priority 100
	appendonly no
	appendfsync everysec
	no-appendfsync-on-rewrite no
	auto-aof-rewrite-percentage 100
	auto-aof-rewrite-min-size 64mb
	lua-time-limit 5000
	slowlog-log-slower-than 10000
	slowlog-max-len 128
	hash-max-ziplist-entries 512
	hash-max-ziplist-value 64
	list-max-ziplist-entries 512
	list-max-ziplist-value 64
	set-max-intset-entries 512
	zset-max-ziplist-entries 128
	zset-max-ziplist-value 64
	activerehashing yes
	client-output-buffer-limit normal 0 0 0
	client-output-buffer-limit slave 256mb 64mb 60
	client-output-buffer-limit pubsub 32mb 8mb 60
	hz 10
	```

### 可能遇到的问题
1. 报如下错，是gcc没有安装

	```
	cd src && make all
	make[1]: Entering directory `/root/redis-4.0.2/src'
	    CC Makefile.dep
	make[1]: Leaving directory `/root/redis-4.0.2/src'
	make[1]: Entering directory `/root/redis-4.0.2/src'
	    CC adlist.o
	/bin/sh: cc: command not found
	make[1]: *** [adlist.o] Error 127
	make[1]: Leaving directory `/root/redis-4.0.2/src'
	make: *** [all] Error 2
	```
	- 使用yum安装：
		- `yum -y install gcc`
2. make时报如下错误：

	```
	zmalloc.h:50:31: error: jemalloc/jemalloc.h: No such file or directory
	zmalloc.h:55:2: error: #error "Newer version of jemalloc required"
	make[1]: *** [adlist.o] Error 1
	make[1]: Leaving directory `/data0/src/redis-2.6.2/src'
	make: *** [all] Error 2
	```		
	- 原因是jemalloc重载了Linux下的ANSI C的malloc和free函数。解决办法：make时添加参数。
		- `make MALLOC=libc`
3. make之后，会出现一句提示
	- `Hint: To run 'make test' is a good idea ;)` 
	- 但是不测试，通常是可以使用的。若我们运行make test ，会有如下提示
	
		```
		[devnote@devnote src]$ make test
		You need tcl 8.5 or newer in order to run the Redis test
		make: ***[test] Error_1
		```
	- 解决办法是用yum安装tcl8.5（或去tcl的官方网站http://www.tcl.tk/下载8.5版本，并参考官网介绍进行安装）
		- yum install tcl



## MemCache
- Memcached 是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。
- 它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提高动态、数据库驱动网站的速度。
- Memcached基于一个存储键/值对的hashmap。其守护进程（daemon ）是用C写的，但是客户端可以用任何语言来编写，并通过memcached协议与守护进程通信。

### Memcached安装和基本使用
- linux安装

	```linux
	wget http://memcached.org/latest
	tar -zxvf memcached-1.x.x.tar.gz
	cd memcached-1.x.x
	./configure && make && make test && sudo make install
	 
	PS：依赖libevent
	       yum install libevent-devel
	       apt-get install libevent-dev
	```
- 启动Memcached

	```linux
	memcached -d -m 10    -u root -l 10.211.55.4 -p 12000 -c 256 -P /tmp/memcached.pid
	 
	参数说明:
	    -d 是启动一个守护进程
	    -m 是分配给Memcache使用的内存数量，单位是MB
	    -u 是运行Memcache的用户
	    -l 是监听的服务器IP地址
	    -p 是设置Memcache监听的端口,最好是1024以上的端口
	    -c 选项是最大运行的并发连接数，默认是1024，按照你服务器的负载量来设定
	    -P 是设置保存Memcache的pid文件
	```
- Memcached命令

	```
	存储命令: set/add/replace/append/prepend/cas
	获取命令: get/gets
	其他命令: delete/stats..
	```
### Python操作Memcached
- `pip3 install python-memcached`

- 简单使用

	```python
	import memcache
	 
	mc = memcache.Client(['10.211.55.4:12000'], debug=True)	# debug = True 表示运行出现错误时，现实错误信息，上线后移除该参数。
	mc.set("foo", "bar")
	ret = mc.get('foo')
	print(ret)
	```
- 天生支持集群
	- python-memcached模块原生支持集群操作，其原理是在内存维护一个主机列表，且集群中主机的权重值和主机在列表中重复出现的次数成正比

		```
		     主机    权重
		    1.1.1.1   1
		    1.1.1.2   2
		    1.1.1.3   1
		 
		那么在内存中主机列表为：
		    host_list = ["1.1.1.1", "1.1.1.2", "1.1.1.2", "1.1.1.3", ]
		```
	- 如果用户根据如果要在内存中创建一个键值对（如：k1 = "v1"），那么要执行一下步骤：
		- 根据算法将 k1 转换成一个数字
		- 将数字和主机列表长度求余数，得到一个值 N（ 0 <= N < 列表长度 ）
		- 在主机列表中根据 第2步得到的值为索引获取主机，例如：host_list[N]
		- 连接 将第3步中获取的主机，将 k1 = "v1" 放置在该服务器的内存中
	
		```python
		import memcache
		mc = memcache.Client([('1.1.1.1:12000', 1), ('1.1.1.2:12000', 2), ('1.1.1.3:12000', 1)], debug=True)
		 
		mc.set('k1', 'v1'
		```
- 命令方法
	1. 	add，添加一条键值对，如果已经存在的 key，重复执行add会操作异常

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		mc.add('k1', 'v1')
		# mc.add('k1', 'v2') # 报错，对已经存在的key重复添加，失败
		```
	2. replace,修改某个key的值，如果key不存在，则异常

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		# 如果memcache中存在kkkk，则替换成功，否则异常
		mc.replace('kkkk','999')
		```
	3. set 和 set_multi
		- set            设置一个键值对，如果key不存在，则创建，如果key存在，则修改
		- set_multi   设置多个键值对，如果key不存在，则创建，如果key存在，则修改

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		 
		mc.set('key0', 'wupeiqi')
		 
		mc.set_multi({'key1': 'val1', 'key2': 'val2'})
		```
	4. delete 和 delete_multi
		- delete             在Memcached中删除指定的一个键值对
		- delete_multi    在Memcached中删除指定的多个键值对

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		 
		mc.delete('key0')
		mc.delete_multi(['key1', 'key2'])
		```
	5. get 和 get_multi
		- get            获取一个键值对
		- get_multi   获取多一个键值对
	
		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		 
		val = mc.get('key0')
		item_dict = mc.get_multi(["key1", "key2", "key3"])
		```
	6. append 和 prepend
		- append    修改指定key的值，在该值 后面 追加内容
		- prepend   修改指定key的值，在该值 前面 插入内容

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		# k1 = "v1"
		 
		mc.append('k1', 'after')
		# k1 = "v1after"
		 
		mc.prepend('k1', 'before')
		# k1 = "beforev1after"
		```
	7. decr 和 incr　　
		- incr  自增，将Memcached中的某一个值增加 N （ N默认为1 ）
		- decr 自减，将Memcached中的某一个值减少 N （ N默认为1 ）

		```python
		import memcache
		 
		mc = memcache.Client(['10.211.55.4:12000'], debug=True)
		mc.set('k1', '777')
		 
		mc.incr('k1')
		# k1 = 778
		 
		mc.incr('k1', 10)
		# k1 = 788
		 
		mc.decr('k1')
		# k1 = 787
		 
		mc.decr('k1', 10)
		# k1 = 777
		```
	8. gets 和 cas
		- gets和cas之间，如果有其他连接对去的数据进行了操作就会报异常

		```python
		import memcache
		mc = memcache.Client(['10.211.55.4:12000'], debug=True, cache_cas=True)
		 
		v = mc.gets('product_count')
		# ...
		# 如果有人在gets之后和cas之前修改了product_count，那么，下面的设置将会执行失败，剖出异常，从而避免非正常数据的产生
		mc.cas('product_count', "899")
		```
		- Ps：本质上每次执行gets时，会从memcache中获取一个自增的数字，通过cas去修改gets的值时，会携带之前获取的自增值和memcache中的自增值进行比较，如果相等，则可以提交，如果不想等，那表示在gets和cas执行之间，又有其他人执行了gets（获取了缓冲的指定值）， 如此一来有可能出现非正常数据，则不允许修改。


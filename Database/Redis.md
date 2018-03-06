## Redis
- redis是一个key-value存储系统。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。
- 这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。
- 在此基础上，redis支持各种不同方式的排序。
- 与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。

- [安装及配置](#1)
- [python操作redis](#2)
	- [操作模式](#21)
	- [连接池](#22)
	- [操作](#23)
		- [String操作](#231)
		- [Hash操作](#232)
		- [List操作](#233)
		- [Set操作](#234)
		- [SortSet操作](#235)
	- [管道](#24)
	- [基于redis的“发布”和“订阅”](#25)
- [为什么选择redis](#3)

### <span id="1">安装及配置</span>
- 安装
	- yum一键安装
		- `yum install redis`
	- 下载安装
		- `wget http://download.redis.io/releases/redis-4.0.2.tar.gz`
		- `tar -xvf redis-4.0.2.tar.gz`
		- `cd redis-4.0.2`
		- `make test`
	- 启动服务
		- `src/redis-server [指定配置文件]`
		- redis默认监听6379端口，通过配置可以更改监听端口
	- 启动客户端
		- `src/redis-cli [-p 服务监听的端口]`

### <span id="2">python操作redis</span>
- `pip3 install redis`

- redis-py 的API的使用可以分类为：
	- 操作模式
	- 连接池
	- 操作
		- String 操作
		- Hash 操作
		- List 操作
		- Set 操作
		- Sort Set 操作
	- 管道
	- 发布订阅

#### <span id="21">操作模式</span>
- redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py

	```python
	import redis
	 
	r = redis.Redis(host='192.168.20.180', port=6380)
	r.set('foo', 'Bar')
	print r.get('foo')
	```

#### <span id="22">连接池</span>
- redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
- 默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
	
	```python
	import redis
	 
	pool = redis.ConnectionPool(host='192.168.20.180', port=6380)
	 
	r = redis.Redis(connection_pool=pool)
	r.set('foo', 'Bar')
	print r.get('foo')
	```

#### <span id="23">操作</span>
##### <span id="231">String操作</span>
- redis中在内存中按照一个name对应一个value来存储
- 指令方法
	1. r.set(name, value, ex=None, px=None, nx=False, xx=False)
	2. r.setnx(name, value)
	3. r.setex(name, value, time)
	4. r.psetex(name, time_ms, value)
	5. r.mset(*args, **kwargs)
	6. r.get(name)
	7. r.mget(keys, *args)
	8. r.getset(name, value)
	9. r.getrange(key, start, end)
	10. r.setrange(name, offset, value)
	11. r.setbit(name, offset, value)
	12. r.getbit(name, offset)
	13. r.bitcount(key, start=None, end=None)
	14. r.bitop(operation, dest, *keys)
	15. r.strlen(name)
	16. r.incr(self, name, amount=1)
	17. r.incrbyfloat(self, name, amount=1.0)
	18. r.decr(self, name, amount=1)
	19. r.append(key, value)

##### <span id="232">Hash操作</span>
- redis中按照一个name对应一张哈希表，哈希表类似字典
- 指令方法
	1. r.hset(name, key, value)
	2. r.hmset(name, mapping)
	3. r.hget(name,key)
	4. r.hmget(name, keys, *args)
	5. r.hgetall(name)
	6. r.hlen(name)
	7. r.hkeys(name)
	8. r.hvals(name)
	9. r.hexists(name, key)
	10. r.hdel(name,*keys)
	11. r.hincrby(name, key, amount=1)
	12. r.hincrbyfloat(name, key, amount=1.0)
	13. r.hscan(name, cursor=0, match=None, count=None)
	14. r.hscan_iter(name, match=None, count=None)

##### <span id="233">List操作</span>
- redis中的List在在内存中按照一个name对应一个数组来存储
- 指令方法
	1. r.lpush(name,values)
	2. r.lpushx(name,value)
	3. r.llen(name)
	4. r.linsert(name, where, refvalue, value))
	5. r.lset(name, index, value)
	6. r.lrem(name, value, num)
	7. r.lpop(name)
	8. r.lindex(name, index)
	9. r.lrange(name, start, end)
	10. r.ltrim(name, start, end)
	11. r.rpoplpush(src, dst)
	12. r.blpop(keys, timeout)
	13. r.brpoplpush(src, dst, timeout=0)
	14. 自定义增量迭代

		```python
		# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
		    # 1、获取name对应的所有列表
		    # 2、循环列表
		# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内存撑爆，所有有必要自定义一个增量迭代的功能：
		 
		def list_iter(name):
		    """
		    自定义redis列表增量迭代
		    :param name: redis中的name，即：迭代name对应的列表
		    :return: yield 返回 列表元素
		    """
		    list_count = r.llen(name)
		    for index in xrange(list_count):
		        yield r.lindex(name, index)
		 
		# 使用
		for item in list_iter('pp'):
		    print(item)
		```

##### <span id="234">Set操作</span>
- redis中的Set在在内存中按照一个name对应一个集合来存储，Set就是不允许重复的列表
- 指令方法
	1. r.sadd(name,values)
	2. r.scard(name)
	3. r.sdiff(keys, *args)
	4. r.sdiffstore(dest, keys, *args)
	5. r.sinter(keys, *args)
	6. r.sinterstore(dest, keys, *args)
	7. r.sismember(name, value)
	8. r.smembers(name)
	9. r.smove(src, dst, value)
	10. r.spop(name)
	11. r.srandmember(name, numbers)
	12. r.srem(name, values)
	13. r.sunion(keys, *args)
	14. r.sunionstore(dest,keys, *args)
	15. r.sscan(name, cursor=0, match=None, count=None)
	16. r.sscan_iter(name, match=None, count=None)

##### <span id="235">SortSet操作</span>
- SortSet,有序集合，在集合的基础上，为每元素排序
	- 元素的排序需要根据另外一个值来进行比较，
	- 所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
- 指令方法
	1. r.zadd(name, *args, **kwargs)
	2. r.zcard(name)
	3. r.zcount(name, min, max)
	4. r.zincrby(name, value, amount)
	5. r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
	6. r.zrank(name, value)
	7. r.zrangebylex(name, min, max, start=None, num=None)
	8. r.zrem(name, values)
	9. r.zremrangebyrank(name, min, max)
	10. r.zremrangebyscore(name, min, max)
	11. r.zremrangebylex(name, min, max)
	12. r.zscore(name, value)
	13. r.zinterstore(dest, keys, aggregate=None)
	14. r.zunionstore(dest, keys, aggregate=None)
	15. r.zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
	16. r.zscan_iter(name, match=None, count=None,score_cast_func=float)

##### <span id="236">其他常用操作</span> 
- 指令方法
	1. r.delete(*names)
	2. r.exists(name)
	3. r.keys(pattern='*')
	4. r.expire(name ,time)
	5. r.rename(src, dst)
	6. r.move(name, db))
	7. r.randomkey()
	8. r.type(name)
	9. r.scan(cursor=0, match=None, count=None)
	10. r.scan_iter(match=None, count=None)

#### <span id="24">管道</span>
- redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

	```python
	import redis
	 
	pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
	 
	r = redis.Redis(connection_pool=pool)
	 
	# pipe = r.pipeline(transaction=False)
	pipe = r.pipeline(transaction=True)
	 
	pipe.set('name', 'alex')
	pipe.set('role', 'sb')
	 
	pipe.execute()
	```

#### <span id="25">基于redis的“发布”和“订阅”</span>
- 发布方为多个，订阅方也为多个，发布方可以向redis推送各种数据，订阅方可以在redis取所有的数据
- RedisHelper

	```python
	import redis
	
	class RedisHelper:
	
	    def __init__(self):
	        self.__conn = redis.Redis(host='10.211.55.4')
	        self.chan_sub = 'fm104.5'
	        self.chan_pub = 'fm104.5'
	
	    def public(self, msg):
	        self.__conn.publish(self.chan_pub, msg)
	        return True
	
	    def subscribe(self):
	        pub = self.__conn.pubsub()
	        pub.subscribe(self.chan_sub)
	        pub.parse_response()
	        return pub
	```
- 订阅者：

	```python
	from monitor.RedisHelper import RedisHelper
	 
	obj = RedisHelper()
	redis_sub = obj.subscribe()
	 
	while True:
	    msg= redis_sub.parse_response()
	    print msg
	```

- 发布者

	```python
	from monitor.RedisHelper import RedisHelper
	 
	obj = RedisHelper()
	obj.public('hello')
	```


### <span id="3">为什么选择redis</span>
1. 使用Redis有哪些好处？
	1. 速度快，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1)
	2. 支持丰富数据类型，支持string，list，set，sorted set，hash
	3. 支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行
	4. 丰富的特性：可用于缓存，消息，按key设置过期时间，过期后将会自动删除
2. redis相比memcached有哪些优势？
	1. memcached所有的值均是简单的字符串，redis作为其替代者，支持更为丰富的数据类型
	2. redis的速度比memcached快很多
	3. redis可以持久化其数据
3. redis常见性能问题和解决方案：
	1. Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件
	2. 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次
	3. 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内
	4. 尽量避免在压力很大的主库上增加从库
	5. 主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <- Slave3...
		- 这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变。
4. MySQL里有2000w数据，redis中只存20w的数据，如何保证redis中的数据都是热点数据

	>相关知识：redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。redis 提供 6种数据淘汰策略：      
	>voltile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰      
	volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰    
	volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰      
	allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰    
	allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰      
	no-enviction（驱逐）：禁止驱逐数据      
5. Memcache与Redis的区别都有哪些？
	1. 存储方式
		- Memecache把数据全部存在内存之中，断电后会挂掉，数据不能超过内存大小。
		- Redis有部份存在硬盘上，这样能保证数据的持久性。
	2. 数据支持类型
		- Memcache对数据类型支持相对简单。
		- Redis有复杂的数据类型。
	3. value大小
		- redis最大可以达到1GB，而memcache只有1MB
6. Redis 常见的性能问题都有哪些？如何解决？
	1. Master写内存快照，save命令调度rdbSave函数，会阻塞主线程的工作，当快照比较大时对性能影响是非常大的，会间断性暂停服务，所以Master最好不要写内存快照。
	2. Master AOF持久化，如果不重写AOF文件，这个持久化方式对性能的影响是最小的，但是AOF文件会不断增大，AOF文件过大会影响Master重启的恢复速度。Master最好不要做任何持久化工作，包括内存快照和AOF日志文件，特别是不要启用内存快照做持久化,如果数据比较关键，某个Slave开启AOF备份数据，策略为每秒同步一次。
	3. Master调用BGREWRITEAOF重写AOF文件，AOF在重写的时候会占大量的CPU和内存资源，导致服务load过高，出现短暂服务暂停现象。
	4. Redis主从复制的性能问题，为了主从复制的速度和连接的稳定性，Slave和Master最好在同一个局域网内
7. redis 最适合的场景
	- Redis最适合所有数据in-momory的场景，虽然Redis也提供持久化功能，但实际更多的是一个disk-backed的功能，跟传统意义上的持久化有比较大的差别，那么可能大家就会有疑问，似乎Redis更像一个加强版的Memcached，那么何时使用Memcached,何时使用Redis呢?
	- 如果简单地比较Redis与Memcached的区别，大多数都会得到以下观点：
		1. Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
		2. Redis支持数据的备份，即master-slave模式的数据备份。
		3. Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
	1. 会话缓存（Session Cache）
		- 最常用的一种使用Redis的情景是会话缓存（session cache）。用Redis缓存会话比其他存储（如Memcached）的优势在于：Redis提供持久化。当维护一个不是严格要求一致性的缓存时，如果用户的购物车信息全部丢失，大部分人都会不高兴的，现在，他们还会这样吗？
		- 幸运的是，随着 Redis 这些年的改进，很容易找到怎么恰当的使用Redis来缓存会话的文档。甚至广为人知的商业平台Magento也提供Redis的插件。
	2. 全页缓存（FPC）
		- 除基本的会话token之外，Redis还提供很简便的FPC平台。回到一致性问题，即使重启了Redis实例，因为有磁盘的持久化，用户也不会看到页面加载速度的下降，这是一个极大改进，类似PHP本地FPC。
		- 再次以Magento为例，Magento提供一个插件来使用Redis作为全页缓存后端。
		- 此外，对WordPress的用户来说，Pantheon有一个非常好的插件  wp-redis，这个插件能帮助你以最快速度加载你曾浏览过的页面。
	3. 队列
		- Reids在内存存储引擎领域的一大优点是提供 list 和 set 操作，这使得Redis能作为一个很好的消息队列平台来使用。Redis作为队列使用的操作，就类似于本地程序语言（如Python）对 list 的 push/pop 操作。
		- 如果你快速的在Google中搜索“Redis queues”，你马上就能找到大量的开源项目，这些项目的目的就是利用Redis创建非常好的后端工具，以满足各种队列需求。例如，Celery有一个后台就是使用Redis作为broker，你可以从这里去查看。
	4. 排行榜/计数器
		- Redis在内存中对数字进行递增或递减的操作实现的非常好。集合（Set）和有序集合（Sorted Set）也使得我们在执行这些操作的时候变的非常简单，Redis只是正好提供了这两种数据结构。所以，我们要从排序集合中获取到排名最靠前的10个用户–我们称之为“user_scores”，我们只需要像下面一样执行即可：
		- 当然，这是假定你是根据你用户的分数做递增的排序。如果你想返回用户及用户的分数，你需要这样执行：
			- `ZRANGE user_scores 0 10 WITHSCORES`
		- Agora Games就是一个很好的例子，用Ruby实现的，它的排行榜就是使用Redis来存储数据的，你可以在这里看到。
	5. 发布/订阅
		- 最后（但肯定不是最不重要的）是Redis的发布/订阅功能。发布/订阅的使用场景确实非常多。我已看见人们在社交网络连接中使用，还可作为基于发布/订阅的脚本触发器，甚至用Redis的发布/订阅功能来建立聊天系统！（不，这是真的，你可以去核实）。
		- Redis提供的所有特性中，我感觉这个是喜欢的人最少的一个，虽然它为用户提供如果此多功能。



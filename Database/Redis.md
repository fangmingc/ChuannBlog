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
	- [如何在redis对数据加锁](#26)
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
		- 直接设置单个键值对
		- ex，过期时间，单位秒
		- px，过去时间，单位毫秒
		- nx，True表示当前name不存在才执行操作
		- xx，True表示当前name存在时才执行操作
	2. r.setnx(name, value)
		- 当前name不存在才执行操作
	3. r.setex(name, value, time)
		- time，过期时间，数字秒或timedeleta对象
	4. r.psetex(name, time_ms, value)
		- time_ms，过期时间，追秒或timedelta对象
	5. r.mset(*args, **kwargs)
		- 批量设置，如r.mset(k1='v1', k2='v2')或r.mget({'k1': 'v1', 'k2': 'v2'})
	6. r.get(name)
		- 获取值
	7. r.mget(keys, *args)
		- 批量获取值，传入多个键，或一个包含键的列表
	8. r.getset(name, value)
		- 设置新值并获取原来的值
	9. r.getrange(key, start, end)
		- 获取子序列（根据字节获取，非字符）
		- name，Redis 的 name
		- start，起始位置（字节）
		- end，结束位置（字节）
	10. r.setrange(name, offset, value)
		- 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
		- offset，字符串的索引，字节（一个汉字三个字节）
		- value，要设置的值
	11. r.setbit(name, offset, value)
		- 对name对应值的二进制表示的位进行操作
		- name，redis的name
		- offset，位的索引（将值变换成二进制后再进行索引）
		- value，值只能是 1 或 0
	12. r.getbit(name, offset)
		- 获取name对应的值的二进制表示中的某位的值 （0或1）
	13. r.bitcount(key, start=None, end=None)
		- 获取name对应的值的二进制表示中 1 的个数
	14. r.bitop(operation, dest, *keys)
		- key，Redis的name
		- start，位起始位置
		- end，位结束位置
	15. r.strlen(name)
		- 获取多个值，并将值做位运算，将最后的结果保存至新的name对应的值
	16. r.incr(self, name, amount=1)
		- 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
		- name,Redis的name
		- amount,自增数（必须是整数）
	17. r.incrbyfloat(self, name, amount=1.0)
		- 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
		- name,Redis的name
		- amount,自增数（浮点型）
	18. r.decr(self, name, amount=1)
		- 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。
		- name,Redis的name
		- amount,自减数（整数）
	19. r.append(key, value)
		- 在redis name对应的值后面追加内容
		- key, redis的name
		- value, 要追加的字符串

##### <span id="232">Hash操作</span>
- redis中按照一个name对应一张哈希表，哈希表类似字典
- 指令方法
	1. r.hset(name, key, value)
		- name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
		- name，redis的name
		- key，name对应的hash中的key
		- value，name对应的hash中的value
	2. r.hmset(name, mapping)
		- 在name对应的hash中批量设置键值对
		- name，redis的name
		- mapping，字典，如：{'k1':'v1', 'k2': 'v2'}
	3. r.hget(name,key)
		- 在name对应的hash中获取根据key获取value
	4. r.hmget(name, keys, *args)
		- 在name对应的hash中获取多个key的值
		- name，reids对应的name
		- keys，要获取key集合，如：['k1', 'k2', 'k3']
		- *args，要获取的key，如：k1,k2,k3
	5. r.hgetall(name)
		- 获取name对应hash的所有键值
	6. r.hlen(name)
		- 获取name对应的hash中键值对的个数
	7. r.hkeys(name)
		- 获取name对应的hash中所有的key的值
	8. r.hvals(name)
		- 获取name对应的hash中所有的value的值
	9. r.hexists(name, key)
		- 检查name对应的hash是否存在当前传入的key
	10. r.hdel(name,*keys)
		- 将name对应的hash中指定key的键值对删除
	11. r.hincrby(name, key, amount=1)
		- 自增name对应的hash中的指定key的值，不存在则创建key=amount
		- name，redis中的name
		- key， hash对应的key
		- amount，自增数（整数）
	12. r.hincrbyfloat(name, key, amount=1.0)
		- 自增name对应的hash中的指定key的值，不存在则创建key=amount
		- name，redis中的name
		- key， hash对应的key
		- amount，自增数（浮点数）
	13. r.hscan(name, cursor=0, match=None, count=None)
		- 增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而防止内存被撑爆
		- name，redis的name
		- cursor，游标（基于游标分批取获取数据）
		- match，匹配指定key，默认None 表示所有的key
		- count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数
	14. r.hscan_iter(name, match=None, count=None)
		- 利用yield封装hscan创建生成器，实现分批去redis中获取数据
		- match，匹配指定key，默认None 表示所有的key
		- count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数

##### <span id="233">List操作</span>
- redis中的List在在内存中按照一个name对应一个数组来存储
- 指令方法
	1. r.lpush(name,values)
		- 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
		- r.rpush(name, values) 表示从右向左操作
	2. r.lpushx(name,value)
		- 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
		- rpushx(name, value) 表示从右向左操作
	3. r.llen(name)
		- name对应的list元素的个数
	4. r.linsert(name, where, refvalue, value))
		- 在name对应的列表的某一个值前或后插入一个新值
		- name，redis的name
		- where，BEFORE或AFTER
		- refvalue，标杆值，即：在它前后插入数据
		- value，要插入的数据
	5. r.lset(name, index, value)
		- 对name对应的list中的某一个索引位置重新赋值
		- name，redis的name
		- index，list的索引位置
		- value，要设置的值
	6. r.lrem(name, value, num)
		- 在name对应的list中删除指定的值
		- name，redis的name
		- value，要删除的值
		- num，  
			- num=0，删除列表中所有的指定值；
			- num=2,从前到后，删除2个；
			- num=-2,从后向前，删除2个
	7. r.lpop(name)
		- 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
		- rpop(name) 表示从右向左操作
	8. r.lindex(name, index)
		- 在name对应的列表中根据索引获取列表元素
	9. r.lrange(name, start, end)
		- 在name对应的列表分片获取数据
		- name，redis的name
		- start，索引的起始位置
		- end，索引结束位置
	10. r.ltrim(name, start, end)
		- 在name对应的列表中移除没有在start-end索引之间的值
		- name，redis的name
		- start，索引的起始位置
		- end，索引结束位置
	11. r.rpoplpush(src, dst)
		- 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
		- src，要取数据的列表的name
		- dst，要添加数据的列表的name
	12. r.blpop(keys, timeout)
		- 将多个列表排列，按照从左到右去pop对应列表的元素
		- keys，redis的name的集合
		- timeout，超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞
		- r.brpop(keys, timeout)，从右向左获取数据
	13. r.brpoplpush(src, dst, timeout=0)
		- 从一个列表的右侧移除一个元素并将其添加到另一个列表的左侧
		- src，取出并要移除元素的列表对应的name
		- dst，要插入元素的列表对应的name
		- timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞

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
		- name对应的集合中添加元素
	2. r.scard(name)
		- 获取name对应的集合中元素个数
	3. r.sdiff(keys, *args)
		- 在第一个name对应的集合中且不在其他name对应的集合的元素集合
	4. r.sdiffstore(dest, keys, *args)
		- 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中
	5. r.sinter(keys, *args)
		- 获取多一个name对应集合的并集
	6. r.sinterstore(dest, keys, *args)
		- 获取多一个name对应集合的并集，再讲其加入到dest对应的集合中
	7. r.sismember(name, value)
		- 检查value是否是name对应的集合的成员
	8. r.smembers(name)
		- 获取name对应的集合的所有成员
	9. r.smove(src, dst, value)
		- 将某个成员从一个集合中移动到另外一个集合
	10. r.spop(name)
		- 从集合的右侧（尾部）移除一个成员，并将其返回
	11. r.srandmember(name, numbers)
		- 从name对应的集合中随机获取 numbers 个元素
	12. r.srem(name, values)
		- 在name对应的集合中删除某些值
	13. r.sunion(keys, *args)
		- 获取多一个name对应的集合的并集
	14. r.sunionstore(dest,keys, *args)
		- 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中
	15. r.sscan(name, cursor=0, match=None, count=None)
	16. r.sscan_iter(name, match=None, count=None)
		- 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大

##### <span id="235">SortSet操作</span>
- SortSet,有序集合，在集合的基础上，为每元素排序
	- 元素的排序需要根据另外一个值来进行比较，
	- 所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。
- 指令方法
	1. r.zadd(name, *args, **kwargs)
		- 在name对应的有序集合中添加元素
		- `zadd('zz', 'n1', 1, 'n2', 2)`
	2. r.zcard(name)
		- 获取name对应的有序集合元素的数量
	3. r.zcount(name, min, max)
		- 获取name对应的有序集合中分数 在 [min,max] 之间的个数
	4. r.zincrby(name, value, amount)
		- 自增name对应的有序集合的 name 对应的分数
	5. r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)
		- 按照索引范围获取name对应的有序集合的元素
		- name，redis的name
		- start，有序集合索引起始位置（非分数）
		- end，有序集合索引结束位置（非分数）
		- desc，排序规则，默认按照分数从小到大排序
		- withscores，是否获取元素的分数，默认只获取元素的值
		- score_cast_func，对分数进行数据转换的函数
			- 从大到小排序
				- zrevrange(name, start, end, withscores=False, score_cast_func=float)
			- 按照分数范围获取name对应的有序集合的元素
				- zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
			- 从大到小排序
				- zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
	6. r.zrank(name, value)
		- 获取某个值在 name对应的有序集合中的排行（从 0 开始）
		- zrevrank(name, value)，从大到小排序
	7. r.zrangebylex(name, min, max, start=None, num=None)
		- 当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员
		- 对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大
		- name，redis的name
		- min，左区间（值）。 + 表示正无限； - 表示负无限； ( 表示开区间； [ 则表示闭区间
		- min，右区间（值）
		- start，对结果进行分片处理，索引位置
		- num，对结果进行分片处理，索引后面的num个元素
			- 从大到小排序
				- zrevrangebylex(name, max, min, start=None, num=None)
	8. r.zrem(name, values)
		- 删除name对应的有序集合中值是values的成员
	9. r.zremrangebyrank(name, min, max)
		- 根据排行范围删除
	10. r.zremrangebyscore(name, min, max)
		- 根据分数范围删除
	11. r.zremrangebylex(name, min, max)
		- 根据值返回删除
	12. r.zscore(name, value)
		- 获取name对应有序集合中 value 对应的分数
	13. r.zinterstore(dest, keys, aggregate=None)
		- 获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作
	14. r.zunionstore(dest, keys, aggregate=None)
		- 获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作
	15. r.zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
	16. r.zscan_iter(name, match=None, count=None,score_cast_func=float)
		- 同字符串相似，相较于字符串新增score_cast_func，用来对分数进行操作

##### <span id="236">其他常用操作</span> 
- 指令方法
	1. r.delete(*names)
		- 根据删除redis中的任意数据类型
	2. r.exists(name)
		- 检测redis的name是否存在
	3. r.keys(pattern='*')
		- 根据模型获取redis的name
	4. r.expire(name ,time)
		- 为某个redis的某个name设置超时时间
	5. r.rename(src, dst)
		- 对redis的name重命名为
	6. r.move(name, db))
		- 将redis的某个值移动到指定的db下
	7. r.randomkey()
		- 随机获取一个redis的name（不删除）
	8. r.type(name)
		- 获取name对应值的类型
	9. r.scan(cursor=0, match=None, count=None)
	10. r.scan_iter(match=None, count=None)
		- 同字符串操作，用于增量迭代获取key

#### <span id="24">管道</span>
- redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

	```python
	import redis
	 
	pool = redis.ConnectionPool(host='192.168.20.180', port=6380)
	 
	r = redis.Redis(connection_pool=pool)
	 
	# pipe = r.pipeline(transaction=False)
	pipe = r.pipeline(transaction=True)
	 
	pipe.set('name', 'xiaoming')
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
	        self.__conn = redis.Redis(host='192.168.20.180', port=6380)
	        self.chan_sub = 'fm104.5'
	        self.chan_pub = 'fm104.5'
	
	    def public(self, msg):
	        self.__conn.publish(self.chan_pub, msg)
	        return True
	
	    def subscribe(self):
	        pub = self.__conn.pubsub()
	        pub.subscribe(self.chan_sub)
	        return pub
	```
- 订阅者：

	```python
	from monitor.RedisHelper import RedisHelper
	 
	obj = RedisHelper()
	redis_sub = obj.subscribe()
	 
	while True:
	    msg = redis_sub.parse_response()
	    print(msg)
	```

- 发布者

	```python
	from monitor.RedisHelper import RedisHelper
	 
	obj = RedisHelper()
	obj.public('hello')
	```

#### <span id="26">如何在redis对数据加锁</span>
- 手动写锁
	- 为需要加锁的数据绑定一个标记值（不是真的绑定）
	- 取值时为标记值存入随机字符串
	- 操作完数据，读取这个标记值，如果和取值时的随机字符串不一样，则表示已有其他人操作了数据，抛出异常
	

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
	1. Redis最适合所有数据in-momory的场景，虽然Redis也提供持久化功能，但实际更多的是一个disk-backed的功能，跟传统意义上的持久化有比较大的差别，那么可能大家就会有疑问，似乎Redis更像一个加强版的Memcached，那么何时使用Memcached,何时使用Redis呢?
	2. 如果简单地比较Redis与Memcached的区别，大多数都会得到以下观点：
		1. Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
		2. Redis支持数据的备份，即master-slave模式的数据备份。
		3. Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。
	3. 会话缓存（Session Cache）
		- 最常用的一种使用Redis的情景是会话缓存（session cache）。用Redis缓存会话比其他存储（如Memcached）的优势在于：Redis提供持久化。当维护一个不是严格要求一致性的缓存时，如果用户的购物车信息全部丢失，大部分人都会不高兴的，现在，他们还会这样吗？
		- 幸运的是，随着 Redis 这些年的改进，很容易找到怎么恰当的使用Redis来缓存会话的文档。甚至广为人知的商业平台Magento也提供Redis的插件。
	4. 全页缓存（FPC）
		- 除基本的会话token之外，Redis还提供很简便的FPC平台。回到一致性问题，即使重启了Redis实例，因为有磁盘的持久化，用户也不会看到页面加载速度的下降，这是一个极大改进，类似PHP本地FPC。
		- 再次以Magento为例，Magento提供一个插件来使用Redis作为全页缓存后端。
		- 此外，对WordPress的用户来说，Pantheon有一个非常好的插件  wp-redis，这个插件能帮助你以最快速度加载你曾浏览过的页面。
	5. 队列
		- Reids在内存存储引擎领域的一大优点是提供 list 和 set 操作，这使得Redis能作为一个很好的消息队列平台来使用。Redis作为队列使用的操作，就类似于本地程序语言（如Python）对 list 的 push/pop 操作。
		- 如果你快速的在Google中搜索“Redis queues”，你马上就能找到大量的开源项目，这些项目的目的就是利用Redis创建非常好的后端工具，以满足各种队列需求。例如，Celery有一个后台就是使用Redis作为broker，你可以从这里去查看。
	6. 排行榜/计数器
		- Redis在内存中对数字进行递增或递减的操作实现的非常好。集合（Set）和有序集合（Sorted Set）也使得我们在执行这些操作的时候变的非常简单，Redis只是正好提供了这两种数据结构。所以，我们要从排序集合中获取到排名最靠前的10个用户–我们称之为“user_scores”，我们只需要像下面一样执行即可：
		- 当然，这是假定你是根据你用户的分数做递增的排序。如果你想返回用户及用户的分数，你需要这样执行：
			- `ZRANGE user_scores 0 10 WITHSCORES`
		- Agora Games就是一个很好的例子，用Ruby实现的，它的排行榜就是使用Redis来存储数据的，你可以在这里看到。
	7. 发布/订阅
		- 最后（但肯定不是最不重要的）是Redis的发布/订阅功能。发布/订阅的使用场景确实非常多。可以用在社交网络连接中，还可作为基于发布/订阅的脚本触发器，甚至用Redis的发布/订阅功能来建立聊天系统。




## RabbitMQ
- [介绍与安装](#1)
- [RabbitMQ工作模型](#2)
- [基于RabbitMQ的RPC](#3)

### <span id="1">介绍与安装</span>
- 一种增强型消息队列的解决方案，可支持不同软件应用之间的通信
- [linux下rabbitmq安装](http://chuann.cc/linux/install/install-rabbitmq.html)

### <span id="2">基本用法流程</span>
- 生产者
	- 建立socket连接上rabbitmq
		- `connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))`
		- `pika.ConnectionParameters(host=_DEFAULT, port=_DEFAULT, virtual_host=_DEFAULT, credentials=_DEFAULT, channel_max=_DEFAULT, frame_max=_DEFAULT, heartbeat=_DEFAULT, ssl=_DEFAULT, ssl_options=_DEFAULT, connection_attempts=_DEFAULT, retry_delay=_DEFAULT, socket_timeout=_DEFAULT, locale=_DEFAULT, backpressure_detection=_DEFAULT, blocked_connection_timeout=_DEFAULT, client_properties=_DEFAULT, tcp_options=_DEFAULT, **kwargs)`
		- 常用参数
			- host
			- port
			- credentials
				- 用户认证，使用如`pika.credentials.PlainCredentials`进行认证
	- 建立通信通道
		- `channel = connection.channel()`
	- 建立队列/建立交换机
		- 简单模式建立队列
			- `result = channel.queue_declare(self, queue='', passive=False, durable=False, exclusive=False, auto_delete=False, arguments=None)`
			- 常用参数
				- queue，队列名
				- durable，消息是放在队列由消费者取走，该参数表示取走时是否备份一份
				- exclusive，队列是否本连接独占
			- 建立的队列
				- `queue = result.method.queue`
		- 其他模式建立交换机
			- `channel.exchange_declare(exchange=None, exchange_type='direct', passive=False, durable=False, auto_delete=False, internal=False, arguments=None)`
			- 常用参数
				- exchange，交换机名称
				- exchange_type，*重点*，交换机的模式，有三种:fanout,direct,topic，详细见[exchange模式](#exchange)
				- durable，该参数表示消费者取走时是否备份一份
	- 传输数据
		- `channel.basic_publish(exchange, routing_key, body, properties=None, mandatory=False, immediate=False)`
		- 常用参数
			- exchange，传输到交换机的名，可为''，表示不传输到交换机
			- routing_key，传输到队列的名，可为''，表示不传输到队列
			- body，传输的数据
			- properties，额外参数，必须是pika.BasicProperties的实例
				- `pika.BasicProperties(content_type=None, content_encoding=None, headers=None, delivery_mode=None, priority=None, correlation_id=None, reply_to=None, expiration=None, message_id=None, timestamp=None, type=None, user_id=None, app_id=None, cluster_id=None)`
				- delivery_mode,传输模式
					- 设置为2，表示对消息进行持久化
				- reply_to,传递队列，可用于RPC回调队列
				- correlation_id,关联ID，可用于RPC回调时识别身份
	- 结束
		- `connection.close()`
- 消费者
	- 建立socket连接上rabbitmq
		- 同上生产者
	- 建立通信通道
		- `channel = connection.channel()`
	- 建立交换机[可选]
		- 同上生产者
	- 建立队列
		- 
	- 定制消息处理规则
		- 定义回调函数
	- 监听队列，当有消息，则按照规则处理


- 主要命令
	- channel.basic_publish(self, exchange, routing_key, body, properties=None, mandatory=False, immediate=False)
		- exchange
			- 工作模式选择
		- routing_key
			- 队列名
		- body
			- 传输的数据
		- properties
			- 如果有值，必须是pika.BasicProperties对象
		- mandatory
		- immediate
	- channel.basic_consume(self, consumer_callback, queue, no_ack=False, exclusive=False, consumer_tag=None, arguments=None)
		- consumer_callback
			- 指定消息回调函数
		- queue
			- 队列名
		- no_ack
			- 应答模式，True为无应答，Flase为有应答
		- exclusive
		- consumer_tag
		- arguments


### <span id="2">RabbitMQ工作模型</span>
- 工作模型指的是生产者和消费者之间使用不同规则通信使用的RabbitMQ的模式

#### 主要参数
- 是否应答
- 持久化
- 数据获取方式


#### 简单模式
- 示例
	- 生产者

		```python
		import pika
		
		# 封装socket通信，建立连接
		connection = pika.BlockingConnection(
		    pika.ConnectionParameters(
		        host='192.168.40.128',
		        port=5672,
		        credentials=pika.credentials.PlainCredentials(
		            username='admin',
		            password='123456'
		        )
		    ))
		
		# 创建通道对象
		channel = connection.channel()
		
		# 创建一个队列，名字为hello
		channel.queue_declare(queue='hello')
		
		# 直接向队列推送消息
		msg = "兔子"
		num = 10
		for i in range(num):
		    channel.basic_publish(
		        exchange='',				# 值为空表示简单模式
		        routing_key='hello',		# 队列名
		        body=''.join([msg, str(i)])	# 发送数据
		    )
		
		print("Sent '%s' * %s" % (msg, num))
		connection.close()
		```
	- 消费者
	
		```python
		import pika
		
		# 封装socket通信，建立连接
		connection = pika.BlockingConnection(
		    pika.ConnectionParameters(
		        host='192.168.40.128',
		        port=5672,
		        credentials=pika.credentials.PlainCredentials(
		            username='admin',
		            password='123456'
		        )
		    ))
		
		# 创建通道对象
		channel = connection.channel()
		
		# 创建一个叫hello的队列，有则连接该队列
		channel.queue_declare(queue='hello')
		
		# 定义回调函数
		def callback(ch, method, properties, body):
		    print(" [x] Received %r" % body.decode("utf-8"))
		
		# 设置执行命令
		channel.basic_consume(
		    callback,
		    queue='hello',
		    no_ack=True
		)
		
		print(' [*] Waiting for messages. To exit press CTRL+C')
		# 执行命令
		channel.start_consuming()
		```

#### <span id="exchange">exchange模式(三种)</span>
##### fanout


##### direct


##### topic



### <span id="3">基于RabbitMQ的RPC</span>

## 通过pika模块使用RabbitMQ
- [RabbitMQ介绍与安装](#1)
- [RabbitMQ工作模型](#2)
- [基于RabbitMQ的RPC](#3)

### <span id="1">RabbitMQ介绍与安装</span>
- 一种增强型消息队列的解决方案，可支持不同软件应用之间的通信
- [linux下rabbitmq安装](http://chuann.cc/linux/install/install-rabbitmq.html)

### <span id="2">基本用法流程</span>
- 生产者
	- 建立socket连接上rabbitmq
		- `connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))`
		- `pika.ConnectionParameters(host=_DEFAULT, port=_DEFAULT, virtual_host=_DEFAULT, credentials=_DEFAULT, channel_max=_DEFAULT, frame_max=_DEFAULT, heartbeat=_DEFAULT, ssl=_DEFAULT, ssl_options=_DEFAULT, connection_attempts=_DEFAULT, retry_delay=_DEFAULT, socket_timeout=_DEFAULT, locale=_DEFAULT, backpressure_detection=_DEFAULT, blocked_connection_timeout=_DEFAULT, client_properties=_DEFAULT, tcp_options=_DEFAULT, **kwargs)`
		- 常用参数
			- host，与rabbitmq服务器连接
				- 设置为localhost表示与本机的rabbitmq建立连接，通常程序与rabbitmq服务需要在统一环境方可使用
			- port，默认5672
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
		- 同上生产者
	- 定制消息处理规则
		- 定义回调函数
			- `def callback(ch, method, properties, body): pass`
		- 定制规则
			- `channel.basic_consume(consumer_callback, queue, no_ack=False, exclusive=False, consumer_tag=None, arguments=None)`
			- consumer_callback，回调函数
			- queue，接收消息队列
			- no_ack，是否不应答，True表示不应答，False表示应答
				- 是否给rabbitmq返回，已收到并处理消息
	- 阻塞监听队列，当有消息，则按照规则处理
		- `channel.start_consuming()`

### <span id="2">RabbitMQ工作模型</span>
- 工作模型指的是生产者和消费者之间使用不同规则通信使用的RabbitMQ的模式

#### 简单模式
<img src="http//chuann.cc/Intermediate_Python/base/rabbitmq-simple-mode.png">

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
- 分发模式，报纸订阅模式，生产者生产一份数据，交换机为每个消费者绑定的队列发送一样的数据

<img src="http//chuann.cc/Intermediate_Python/base/rabbitmq-fanout-mode.png">

- 生产者

	```python
	import pika
	import sys
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='logs',
	                         exchange_type='fanout')
	
	message = ' '.join(sys.argv[1:]) or "info: Hello World!"
	channel.basic_publish(exchange='logs',
	                      routing_key='',
	                      body=message)
	print(" [x] Sent %r" % message)
	connection.close()
	```

- 消费者

	```python
	import pika
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='logs',
	                         exchange_type='fanout')
	
	result = channel.queue_declare(exclusive=True)
	queue_name = result.method.queue
	
	channel.queue_bind(exchange='logs',
	                   queue=queue_name)
	
	print(' [*] Waiting for logs. To exit press CTRL+C')
	
	def callback(ch, method, properties, body):
	    print(" [x] %r" % body)
	
	channel.basic_consume(callback,
	                      queue=queue_name,
	                      no_ack=True)
	
	channel.start_consuming()
	```

##### direct
- 关键字指定发送，

<img src="http//chuann.cc/Intermediate_Python/base/rabbitmq-direct-mode.png">
- 生产者

	```python
	import pika
	import sys
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='direct_logs',
	                         exchange_type='direct')
	
	severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
	message = ' '.join(sys.argv[2:]) or 'Hello World!'
	channel.basic_publish(exchange='direct_logs',
	                      routing_key=severity,
	                      body=message)
	print(" [x] Sent %r:%r" % (severity, message))
	connection.close()
	```

- 消费者

	```python
	import pika
	import sys
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='direct_logs',
	                         exchange_type='direct')
	
	result = channel.queue_declare(exclusive=True)
	queue_name = result.method.queue
	
	severities = sys.argv[1:]
	if not severities:
	    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
	    sys.exit(1)
	
	for severity in severities:
	    channel.queue_bind(exchange='direct_logs',
	                       queue=queue_name,
	                       routing_key=severity)
	
	print(' [*] Waiting for logs. To exit press CTRL+C')
	
	def callback(ch, method, properties, body):
	    print(" [x] %r:%r" % (method.routing_key, body))
	
	channel.basic_consume(callback,
	                      queue=queue_name,
	                      no_ack=True)
	
	channel.start_consuming()
	```
- 测试
	- `python producer.py warning error > logs_from_rabbit.log`
	- `python comsumer.py info warning error`

##### topic


<img src="http//chuann.cc/Intermediate_Python/base/rabbitmq-topic-mode.png">

- 生产者

	```python
	import pika
	import sys
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='topic_logs',
	                         exchange_type='topic')
	
	routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
	message = ' '.join(sys.argv[2:]) or 'Hello World!'
	channel.basic_publish(exchange='topic_logs',
	                      routing_key=routing_key,
	                      body=message)
	print(" [x] Sent %r:%r" % (routing_key, message))
	connection.close()
	```

- 消费者

	```python
	import pika
	import sys
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare(exchange='topic_logs',
	                         exchange_type='topic')
	
	result = channel.queue_declare(exclusive=True)
	queue_name = result.method.queue
	
	binding_keys = sys.argv[1:]
	if not binding_keys:
	    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
	    sys.exit(1)
	
	for binding_key in binding_keys:
	    channel.queue_bind(exchange='topic_logs',
	                       queue=queue_name,
	                       routing_key=binding_key)
	
	print(' [*] Waiting for logs. To exit press CTRL+C')
	
	def callback(ch, method, properties, body):
	    print(" [x] %r:%r" % (method.routing_key, body))
	
	channel.basic_consume(callback,
	                      queue=queue_name,
	                      no_ack=True)
	
	channel.start_consuming()
	```
- 测试
	- 接收所有日志
		- `python comsumer.py "#"`
	- 接收包含kern开头的
		- `python comsumer.py "kern.*"`
	- 接收critical结尾的
		- `python comsumer.py "*.critical"`
	- 发送kern.critical、A critical kernel error	
		- `python producer.py "kern.critical" "A critical kernel error"`

### <span id="3">基于RabbitMQ的RPC</span>
- 何为RPC
	- 客户端通过消息队列向服务端发送数据
	- 服务端处理完数据，将数据通过回调队列返回给客户端
- 客户端可能回同时发起多个任务，在服务端回调后应当根据唯一标识为每一个任务返回值的指定数据

<img src="http//chuann.cc/Intermediate_Python/base/rabbitmq-RPC.png">

- 服务端

	```python
	import pika
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	
	channel = connection.channel()
	
	channel.queue_declare(queue='rpc_queue')
	
	def fib(n):
	    if n == 0:
	        return 0
	    elif n == 1:
	        return 1
	    else:
	        return fib(n-1) + fib(n-2)
	
	def on_request(ch, method, props, body):
	    n = int(body)
	
	    print(" [.] fib(%s)" % n)
	    response = fib(n)
	
	    ch.basic_publish(exchange='',
	                     routing_key=props.reply_to,
	                     properties=pika.BasicProperties(correlation_id = \
	                                                         props.correlation_id),
	                     body=str(response))
	    ch.basic_ack(delivery_tag = method.delivery_tag)
	
	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(on_request, queue='rpc_queue')
	
	print(" [x] Awaiting RPC requests")
	channel.start_consuming()
	```

- 客户端

	```python
	import pika
	import uuid
	
	class FibonacciRpcClient(object):
	    def __init__(self):
	        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	
	        self.channel = self.connection.channel()
	
	        result = self.channel.queue_declare(exclusive=True)
	        self.callback_queue = result.method.queue
	
	        self.channel.basic_consume(self.on_response, no_ack=True,
	                                   queue=self.callback_queue)
	
	    def on_response(self, ch, method, props, body):
	        if self.corr_id == props.correlation_id:
	            self.response = body
	
	    def call(self, n):
	        self.response = None
	        self.corr_id = str(uuid.uuid4())
	        self.channel.basic_publish(exchange='',
	                                   routing_key='rpc_queue',
	                                   properties=pika.BasicProperties(
	                                         reply_to = self.callback_queue,
	                                         correlation_id = self.corr_id,
	                                         ),
	                                   body=str(n))
	        while self.response is None:
	            self.connection.process_data_events()
	        return int(self.response)
	
	fibonacci_rpc = FibonacciRpcClient()
	
	print(" [x] Requesting fib(30)")
	response = fibonacci_rpc.call(30)
	print(" [.] Got %r" % response)
	```

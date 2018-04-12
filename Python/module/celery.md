## Celery
- 简单、灵活、可靠的分布式系统，用于处理大量的消息，同时为提供用于维护系统的工具。
- 这是一个专注于实时处理的任务队列，同时也支持任务调度。

### 开始
- 什么是任务队列
	- 任务队列用作跨线程或机器分配工作的机制。
	- 任务队列的输入是统称为task的工作单元。 专用工作进程不断监视任务队列以执行新工作。
	- Celery通过消息进行沟通，通常使用broker在客户端和处理端之间进行协调。 
	- 要启动任务，客户端会向队列中添加消息，然后broker会将该消息传递给处理端。
	- Celery系统可以由多个工人和经纪人组成，让位于高可用性和水平缩放。
	- Celery是用Python编写的，但协议可以用任何语言实现。 除了Python之外，还有Node.js的node-celery和PHP client。
- celery的组成
	- brokers
		- RabbitMQ,Redis
		- Amazon SQS
		- ...
	- concurrency
		- prefork/multiprocessing
		- Eventlet,gevent
		- solo(single threaded)
	- result stores
		- AMQP,Redis
		- Memcached
		- SQLAlchemy,Django ORM
		- Apache Cassandra,Elasticesearch
	- serialization
		- pickle,json,yaml,msgpack
		- zlib,bzip2 compression
		- Crytographic message signing

- 安装celery 
	- 安装主体：`pip install -U Celery`
	- 安装相关包
		- 单个安装：`pip install "celery[librabbitmq]"`
		- 多个安装：`pip install "celery[librabbitmq,redis,auth,msgpack]"`
		- [完整包列表](http://docs.celeryproject.org/en/master/getting-started/introduction.html#bundles)
- 准备broker
	- 使用RabbitMQ
		- 安装：`sudo apt install rabbitmq-server`
	- 使用Redis

- 使用
	- 首先要有生成一个celery对象，通常称之为celery app
	- 写一个tasks.py

		```python
		from celery import Celery
		
		app = Celery('tasks', backend='rpc://', broker='pyamqp://')
		
		@app.task
		def add(x, y):
		    return x + y
		```
	- 启动celery服务
		- `celery -A tasks worker --loglevel=info`
	- 打开python console

		```python
		>>> from tasks import add
		>>> res = add.delay(4, 4)
		>>> res.ready()
		True
		>>> res.get()
		8
		```




## Celery
- 简单、灵活、可靠的分布式系统，用于处理大量的消息，同时为提供用于维护系统的工具。
- 这是一个专注于实时处理的任务队列，同时也支持任务调度。

- [介绍与准备](#介绍与准备)
- [简单示例](#简单示例)
	- [示例1](#示例1)
	- [示例2](#示例2)
	- [示例3：指定任务队列](#示例3：指定任务队列)
	- [示例4：任务调度](#示例4：任务调度)
	- [示例5：任务绑定、记录日志和重试](#示例5：任务绑定、记录日志和重试)
- [django-celery](django-celery)

### 介绍与准备
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
- celery工作模式
	- <img src="http://chuann.cc/Python/module/celery_work_mode.jpg">
- 安装celery 
	- 安装主体：`pip install -U Celery`
	- 安装相关包
		- 单个安装：`pip install "celery[librabbitmq]"`
		- 多个安装：`pip install "celery[librabbitmq,redis,auth,msgpack]"`
		- [完整包列表](http://docs.celeryproject.org/en/master/getting-started/introduction.html#bundles)
- 准备broker
	- 使用RabbitMQ
		- [rabbitmq 安装使用](http://chuann.cc/Linux/install/install-rabbitmq.html)
	- 使用Redis
		- [redis 安装使用](http://chuann.cc/Linux/install/install-redis.html)

### 简单示例
#### 示例1
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
	>>> res.get(timeout=2)
	8
	```

#### 示例2
- 文件结构

	```python
	study_celery
	└── proj
	    ├── celeryconfig.py
	    ├── celery.py
	    ├── __init__.py
	    └── tasks.py
	```
- celery.py

	```python
	# -*- coding: UTF-8 -*-
	
	# 拒绝隐式引入，因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
	from __future__ import absolute_import
	
	from celery import Celery
	
	# app是Celery类的实例，创建的时候添加了proj.tasks这个模块，也就是包含了proj/tasks.py这个文件
	app = Celery('proj', include=['proj.tasks'])
	
	# 把Celery配置存放进proj/celeryconfig.py文件，使用app.config_from_object加载配置
	app.config_from_object('proj.celeryconfig')
	
	if __name__ == '__main__':
	    app.start()
	```
- tasks.py

	```python
	# -*- coding: UTF-8 -*-
	
	from __future__ import absolute_import
	
	from proj.celery import app
	
	@app.task
	def add(x, y):
	    return x + y
	```
- celeryconfig.py

	```python
	# -*- coding: UTF-8 -*-
	
	# 使用RabbitMQ作为消息代理
	BROKER_URL = 'pyamqp://admin:123456@localhost:5672'
	
	# 把任务结果存在Redis
	CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
	
	# 任务序列化和反序列化使用msgpack方案
	CELERY_TASK_SERIALIZER = 'msgpack'
	
	# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
	CELERY_RESULT_SERIALIZER = 'json'
	
	# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
	CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
	
	# 指定接受的内容类型
	CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
	```
- 启动服务
	- 在study_celery目录下：`celery -A proj worker -l info`
	- 提示信息中会提供一些有帮助的内容，如消息代理和存储结果的地址、并发数量、任务列表、交换类型等，可以通过如上信息判断设置和修改是否已生效。
- 在study_celery目录下启动python终端
	
	```python
	>>> from proj.tasks import add
	>>> r = add.delay(4,5)
	>>> r.successful()
	True
	>>> r.result
	9
	```

#### 示例3：指定任务队列
- 文件结构
	- 建立proj_q目录，复制示例2中的代码，将其中proj都改成proj_q
	- 更改celeryconfig.py

		```python
		# -*- coding: UTF-8 -*-
		from kombu import Queue
		
		# 使用RabbitMQ作为消息代理
		BROKER_URL = 'pyamqp://admin:123456@localhost:5672'
		
		# 把任务结果存在Redis
		CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
		
		# 任务序列化和反序列化使用msgpack方案
		CELERY_TASK_SERIALIZER = 'msgpack'
		
		# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
		CELERY_RESULT_SERIALIZER = 'json'
		
		# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
		CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
		
		# 指定接受的内容类型
		CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
		
		# 定义任务队列
		CELERY_QUEUES = (
		    Queue('default', routing_key='task.#'),   # 路由键以“task.”开头的消息都进default队列
		    Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列
		)
		
		# 默认的交换机名字为tasks
		CELERY_DEFAULT_EXCHANGE = 'tasks'
		
		# 默认的交换类型是topic
		CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
		
		# 默认的路由键是task.default，这个路由键符合上面的default队列
		CELERY_DEFAULT_ROUTING_KEY = 'task.default'
		
		CELERY_ROUTES = {
		    'proj_q.tasks.add': {  # tasks.add的消息会进入web_tasks队列
		        'queue': 'web_tasks',
		        'routing_key': 'web.add',
		    }
		}
		```
- 指定队列的方式启动消费者进程
	- `celery -A proj_q worker -Q web_tasks -l info`
- 在study_celery目录下启动python终端
	
	```python
	>>> from proj_q.tasks import add
	>>> r = add.delay(4,5)
	>>> r.successful()
	True
	>>> r.result
	9
	```

#### 示例4：任务调度
- 文件结构
	- 建立proj_b目录，复制示例2中的代码，将其中proj都改成proj_b
	- 更改celeryconfig.py

		```python
		# -*- coding: UTF-8 -*-
		from datetime import timedelta
		
		# 使用RabbitMQ作为消息代理
		BROKER_URL = 'pyamqp://admin:123456@localhost:5672'
		
		# 把任务结果存在Redis
		CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
		
		# 任务序列化和反序列化使用msgpack方案
		CELERY_TASK_SERIALIZER = 'msgpack'
		
		# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
		CELERY_RESULT_SERIALIZER = 'json'
		
		# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
		CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
		
		# 指定接受的内容类型
		CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
		
		CELERYBEAT_SCHEDULE = {
		    'add': {
		        'task': 'proj_b.tasks.add',
		        'schedule': timedelta(seconds=3),  # 指定了tasks.add这个任务每3秒跑一次
		        'args': (73, 84)                    # 执行的时候的参数是73和84
		    }
		}
		```
- 启动worker
	- `celery -A proj_b worker -l info`
- 启动beat
	- `celery beat -A proj_b`
- 然后在worker执行的终端即可看见任务每3秒执行一次
	- 一起启动beat和worker:`celery -B -A projb worker -l info`

#### 示例5：任务绑定、记录日志和重试
- 文件结构
	- 建立proj_log目录，复制示例2中的代码，将其中proj都改成proj_log
	- 更改tasks.py

		```python
		# -*- coding: UTF-8 -*-
		
		from __future__ import absolute_import
		
		from proj_log.celery import app
		from celery.utils.log import get_task_logger
		
		logger = get_task_logger(__name__)
		
		
		@app.task
		def add(x, y):
		    return x + y
		
		
		@app.task(bind=True)
		def div(self, x, y):
		    # 打印日志信息
		    logger.info(('Executing task id {0.id}, args: {0.args!r} '
		                 'kwargs: {0.kwargs!r}').format(self.request))
		    try:
		        result = x / y
		    except ZeroDivisionError as e:
		        # 每五秒尝试一次，最多尝试三次
		        raise self.retry(exc=e, countdown=5, max_retries=3)
		    return result
		```
- 启动worker
	- `celery -A proj_log worker -l info`
- 在study_celery目录下启动python终端
	
	```python
	>>> from proj_log.tasks import add, div
	>>> r = div(2,1)
	>>> r = div.delay(2,1)
	>>> r.successful()
	True
	>>> r.result
	2
	>>> r2 = div.delay(2,0)
	>>> r2.successful()
	False
	>>> r2.result
	ZeroDivisionError(u'integer division or modulo by zero',)
	>>> r3 = add.delay(3,4)
	>>> r3.successful()
	True
	>>> r3.result
	7
	>>> r2.successful()
	False
	>>> r2.result
	ZeroDivisionError(u'integer division or modulo by zero',)
	```

### django-celery
- Demo：加法运算
	- 项目结构

```python

```








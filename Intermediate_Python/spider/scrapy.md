## scrapy
基于twisted、整合其他模块的框架

- [安装](#1)
- [命令行工具](#2)
- [爬虫项目结构](#3)
- [Spiders](#4)
- [Items&Pipeline](#5)
- [Middeware](#6)
- [selectors](#7)

### <span id="1">安装</span>
- 先装twisted
	- [详细参考](http://chuann.cc/Intermediate_Python/high-performance/twisted.md)
	- 在这里下载相应版本的twisted的whl文件：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
	- 然后在whl文件目录使用`pip3 install whl文件`即可
- 然后
	- pip3 install scrapy

#### 介绍
- Scrapy一个开源和协作的框架，其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的，使用它可以以快速、简单、可扩展的方式从网站中提取所需的数据。
- 但目前Scrapy的用途十分广泛，可用于如数据挖掘、监测和自动化测试等领域，也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。
- Scrapy 是基于twisted框架开发而来，twisted是一个流行的事件驱动的python网络框架。因此Scrapy使用了一种非阻塞（又名异步）的代码来实现并发。整体架构大致如下

<img src="http://chuann.cc/Intermediate_Python/spider/scrapy.png">

- 组成介绍
	1. 引擎(EGINE)，引擎负责控制系统所有组件之间的数据流，并在某些动作发生时触发事件。有关详细信息，请参见上面的数据流部分。
	2. 调度器(SCHEDULER)，用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL的优先级队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
	3. 下载器(DOWLOADER)，用于下载网页内容, 并将网页内容返回给EGINE，下载器是建立在twisted这个高效的异步模型上的
	4. 爬虫(SPIDERS)，SPIDERS是开发人员自定义的类，用来解析responses，并且提取items，或者发送新的请求
	5. 项目管道(ITEM PIPLINES)，在items被提取后负责处理它们，主要包括清理、验证、持久化（比如存到数据库）等操作
	6. 下载器中间件(Downloader Middlewares)，位于Scrapy引擎和下载器之间，主要用来处理从EGINE传到DOWLOADER的请求request，已经从DOWNLOADER传到EGINE的响应response
	7. 爬虫中间件(Spider Middlewares)，位于EGINE和SPIDERS之间，主要工作是处理SPIDERS的输入（即responses）和输出（即requests）

### <span id="2">命令行工具</span>
#### 查看帮助
- scrapy -h
- scrapy <command> -h

- 有两种命令
	- 其中Project-only必须切到项目文件夹下才能执行，
	- 而Global的命令则不需要
- Global commands:
	- startproject # 创建项目
	- genspider    # 创建爬虫程序
	- settings     # 如果是在项目目录下，则得到的是该项目的配置
	- runspider    # 运行一个独立的python文件，不必创建项目
	- shell        # scrapy shell url地址  在交互式调试，如选择器规则正确与否
	- fetch        # 独立于程单纯地爬取一个页面，可以拿到请求头
	- view         # 下载完毕后直接弹出浏览器，以此可以分辨出哪些数据是ajax请求
	- version      # scrapy version 查看scrapy的版本，scrapy version -v查看scrapy依赖库的版本
- Project-only commands:
	- crawl        # 运行爬虫，必须创建项目才行，确保配置文件中ROBOTSTXT_OBEY = False
	- check        # 检测项目中有无语法错误
	- list         # 列出项目中所包含的爬虫名
	- edit         # 编辑器，一般不用
	- parse        # scrapy parse url地址 --callback 回调函数  #以此可以验证我们的回调函数是否正确
	- bench        # scrapy bentch压力测试
- 示例

	```cmd
	#1、执行全局命令：请确保不在某个项目的目录下，排除受该项目配置的影响
	scrapy startproject MyProject
	
	scrapy genspider baidu www.baidu.com # 创建爬虫
	scrapy settings --get XXX #如果切换到项目目录下，看到的则是该项目的配置
	scrapy runspider baidu.py	# 运行爬虫
	scrapy shell https://www.baidu.com
	    response
	    response.status
	    response.body
	    view(response)
	    
	scrapy view https://www.taobao.com #如果页面显示内容不全，不全的内容则是ajax请求实现的，以此快速定位问题
	
	scrapy fetch --nolog --headers https://www.taobao.com
	
	scrapy version #scrapy的版本
	
	scrapy version -v #依赖库的版本
	
	
	#2、执行项目命令：切到项目目录下
	scrapy crawl baidu
	scrapy check
	scrapy list
	scrapy parse http://quotes.toscrape.com/ --callback parse
	scrapy bench
	```

#### 官网链接
[官方文档](https://docs.scrapy.org/en/latest/topics/commands.html)


###  <span id="3">项目结构</span>
- 图形化显示
	```
	项目根目录
	│  entrypoint.py		# 启动文件
	│  scrapy.cfg			# 项目部署文件
	└─AMAZON
	    │  items.py			
	    │  middlewares.py	
	    │  pipelines.py		# 数据存储模板，用于结构化数据
	    │  settings.py		# 项目配置文件,如：递归的层数、并发数，延迟下载等
	    │  __init__.py
	    └─spiders			# 爬虫目录，如：创建文件，编写爬虫规则
	       │  amazon.py			# 爬虫程序
	       └─ __init__.py
	```

#### entrypoint.py
- 运行该文件即可启动项目
	- 通常在命令行即可启动文件

	```python
	from scrapy.cmdline import execute
	
	# execute(["scrapy", "crawl", "amazon"])
	execute(["scrapy", "crawl", "amazon", "--nolog"])

	keyword = input("请输入搜索内容>>>")
	execute(["scrapy", "crawl", "amazon", "-a", "keyword=%s"%keyword])
	```

###  <span id="4">Spiders</span>
- 封装请求
	- 发送一个请求必须绑定一个回调函数
- 解析响应
	- 必须封装成items对象

- spider流程
	1. 生成初始的Requests来爬取第一个URLS，并且标识一个回调函数
		- 第一个请求定义在start_requests()方法内默认从start_urls列表中获得url地址来生成Request请求，默认的回调函数是parse方法。回调函数在下载完成返回response时自动触发
	2. 在回调函数中，解析response并且返回值
		- 返回值可以4种：
			- 包含解析数据的字典
			- Item对象
			- 新的Request对象（新的Requests也需要指定一个回调函数）
			- 或者是可迭代对象（包含Items或Request）
	3. 在回调函数中解析页面内容
		- 通常使用Scrapy自带的Selectors，但很明显你也可以使用Beutifulsoup，lxml或其他你爱用啥用啥。
	4. 最后，针对返回的Items对象将会被持久化到数据库
		- 通过Item Pipeline组件存到数据库：https://docs.scrapy.org/en/latest/topics/item-pipeline.html#topics-item-pipeline）
		- 或者导出到不同的文件（通过Feed exports：https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-exports）
- 静态字段
	- name，爬虫名
	- allowed_domains，定义允许爬取的域名，如果OffsiteMiddleware启动（默认启动），那么不属于该列表的域名及其子域名都不允许爬取
	- start_urls，如果没有指定url，就从该列表中读取url来生成第一个请求
	- custom_settings，值为一个字典，定义一些配置信息，在运行爬虫程序时，这些配置会覆盖项目级别的配置
- 方法
	- start_requests，该方法用来发起第一个Requests请求，且必须返回一个可迭代的对象。它在爬虫程序打开时就被Scrapy调用，Scrapy只调用它一次
	- parse，默认的回调函数，并不必须，主要靠请求中指定的回调函数
	- closed，爬虫结束时调用

#### 示例：amazon.py
- 爬取亚马逊iphone8商品列表页面
	```python
	# -*- coding: utf-8 -*-
	import scrapy
	from urllib.parse import urlencode
	
	# 调度器
	from scrapy.core.scheduler import Scheduler
	# 默认去重规则
	# from scrapy.dupefilter import RFPDupeFilter
	
	
	class AmazonSpider(scrapy.Spider):
	    name = 'amazon'		# 爬虫名
	    allowed_domains = ['www.amazon.com']	# 该爬虫可以爬的域
	    start_urls = ['http://www.amazon.com/']		# 需要爬取的url
		
		# 自定义设置
	    custom_settings = {
	        "BOT_NAME": "chuck",
	        "REQUEST_HEADERS": {}
	    }
	
	    def __init__(self, keyword="iphone8", *args, **kwargs):
	        scrapy.Spider.__init__(self, *args, **kwargs)
	        self.keyword = keyword
		
		# 开始请求的视图函数，生成请求
	    def start_requests(self):
	        # scrapy.Request()
	        # yield scrapy.Request(
	        #     "https://www.amazon.com/b/ref=unrec_bubbler_2/136-4368269-0847354?_encoding=UTF8&node=12847721&ref=unrec_bubbler_2&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=B8D3YND7QYX4393P8SXD&pf_rd_t=36701&pf_rd_p=e00909ac-c77c-445a-9c6c-9c021da40fa3&pf_rd_i=desktop",
	        #     self.parse,
	        #     # dont_filter=True
	        # )
	        # yield scrapy.Request(
	        #     "https://www.amazon.com/b/ref=unrec_bubbler_2/136-4368269-0847354?_encoding=UTF8&node=12847721&ref=unrec_bubbler_2&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=B8D3YND7QYX4393P8SXD&pf_rd_t=36701&pf_rd_p=e00909ac-c77c-445a-9c6c-9c021da40fa3&pf_rd_i=desktop",
	        #     self.parse,
	        #     # dont_filter=True
	        # )
	        # yield scrapy.Request(
	        #     "https://www.amazon.com/b/ref=unrec_bubbler_2/136-4368269-0847354?_encoding=UTF8&node=12847721&ref=unrec_bubbler_2&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=B8D3YND7QYX4393P8SXD&pf_rd_t=36701&pf_rd_p=e00909ac-c77c-445a-9c6c-9c021da40fa3&pf_rd_i=desktop",
	        #     self.parse,
	        #     # dont_filter=True
	        # )
	
	        yield scrapy.Request(
	            "https://www.amazon.com/s/ref=nb_sb_noss_1?{0}".format(urlencode({"field-keywords": self.keyword})),
	            callback=self.parse,
	        )
		
		# 请求返回的响应处理
	    def parse(self, response):
	        # import hashlib
	        # import time
	        # md = hashlib.md5()
	        # md.update(str(time.time()).encode("utf-8"))
	        # with open("%s.html" % md.hexdigest(), "w", encoding="utf-8") as wf:
	        #     wf.write(response.text)
	        print("=========>", len(response.text))
	
	    def close(spider, reason):
	        print("结束")
	```

#### 去重
- 去重规则应该多个爬虫共享，但凡一个爬虫爬取了，其他都不应该再爬
- 方法一：
	1. 新增类属性
		- visited=set() #类属性
	2. 回调函数parse方法内：

		```python
		def parse(self, response):
		    if response.url in self.visited:
		        return None
		    .......
		
		    self.visited.add(response.url) 
		```
	- 方法一改进：
		- 针对url可能过长，所以我们存放url的hash值
			
			```python
			def parse(self, response):
			        url=md5(response.request.url)
			    if url in self.visited:
			        return None
			    .......
			
			    self.visited.add(url) 
			```
- 方法二：启用Scrapy自带去重功能
	- 配置文件：

		```python
		DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter' #默认的去重规则帮我们去重，去重规则在内存中
		DUPEFILTER_DEBUG = False
		JOBDIR = "保存范文记录的日志路径，如：/root/"  # 最终路径为 /root/requests.seen，去重规则放文件中
		```
	- scrapy自带去重规则默认为RFPDupeFilter，只需要我们指定
	- Request(...,dont_filter=False) ，如果dont_filter=True则告诉Scrapy这个URL不参与去重。

- 方法三：
	- 我们也可以仿照RFPDupeFilter自定义去重规则，
	- 看源码，仿照BaseDupeFilter
		- `from scrapy.dupefilter import RFPDupeFilter`
	- 步骤一：在项目目录下自定义去重文件dup.py

		```python
		class UrlFilter(object):
		    def __init__(self):
		        self.visited = set() #或者放到数据库
		
		    @classmethod
		    def from_settings(cls, settings):
		        return cls()
		
		    def request_seen(self, request):
		        if request.url in self.visited:
		            return True
		        self.visited.add(request.url)
		
		    def open(self):  # can return deferred
		        pass
		
		    def close(self, reason):  # can return a deferred
		        pass
		
		    def log(self, request, spider):  # log that a request has been filtered
		        pass
		```

	- 步骤二：配置文件settings.py：

		```python
		DUPEFILTER_CLASS = '项目名.dup.UrlFilter'
		```

###  <span id="5">Items，pipeline</span>
- 配置文件
	- 可以写多个Pipeline类,数字越大优先级越低
	- 如果优先级高的Pipeline的process_item返回一个值或者None，会自动传给下一个pipline的process_item
	- 如果只想让第一个Pipeline执行，那得让第一个pipline的process_item抛出异常raise DropItem()
	- 可以用spider.name == '爬虫名' 来控制哪些爬虫用哪些pipeline
	
	```python
	ITEM_PIPELINES = {
	   'Amazon.pipelines.CustomPipeline': 200,
	   'Amazon.pipelines.CustomPipeline2': 300,
	}
	```

- pipeline类

	```python 
	class CustomPipeline(object):
	    def __init__(self,host,port,user,pwd,db,table):
	        self.host=host
	        self.port=port
	        self.user=user
	        self.pwd=pwd
	        self.db=db
	        self.table=table
	
	    @classmethod
	    def from_crawler(cls, crawler):
	        """
	        Scrapy会先通过getattr判断我们是否自定义了from_crawler,有则调它来完
	        成实例化
	        """
	        HOST = crawler.settings.get('HOST')
	        PORT = crawler.settings.get('PORT')
	        USER = crawler.settings.get('USER')
	        PWD = crawler.settings.get('PWD')
	        DB = crawler.settings.get('DB')
	        TABLE = crawler.settings.get('TABLE')
	        return cls(HOST,PORT,USER,PWD,DB,TABLE)
	
	    def open_spider(self,spider):
	        """
	        爬虫刚启动时执行一次
	        """
	        self.client = MongoClient('mongodb://%s:%s@%s:%s' %(self.user,self.pwd,self.host,self.port))
	
	    def close_spider(self,spider):
	        """
	        爬虫关闭时执行一次
	        """
	        self.client.close()
	
	
	    def process_item(self, item, spider):
	        # 操作并进行持久化
	
	        self.client[self.db][self.table].save(dict(item))
	```

###  <span id="6">Middeware</span>
- scrapy的中间件相当于django1.6左右版本以及之前的中间件
- eg:有三层中间件
	- A进，A出
	- B进，B出
	- C进，C出
	- 执行顺序A进->B进->C进----C出->B出->A出
	- 当在A进终止(异常或退出中间件)，从C出开始执行

#### 爬虫中间件
- 基本使用
	- from_crawler
		- 类方法，用于实例化中间件
	- process_spider_input(self,response, spider)
		- 路过此处表示已经获取到下载内容
		- 必须返回None或抛出一个异常
			- 返回None，继续执行response(下一个中间件的process_input)，抵达spider，然后逆序中间件执行process_output
			- 抛出异常，不再执行其他中间件，抵达Request的errback参数指定的异常处理函数，然后逆序中间件执行process_exception
				- 在start_reqeust中定义的Request(url,callback=right_parse,errback=error_handle_func)
	- process_spider_output(self,response, result, spider)
		- 已经经过spider的解析，准备传送到pipline
		- result为来自异常处理机制的数据，为生成器
		- 返回值必须是可迭代对象
	- process_spider_exception(self,response, exception, spider)
		- 爬虫中间件执行过程中出现异常，首先由sipder中生成Request时指定的异常处理函数处理
		- 若spider没有处理，则由本函数处理
		- 返回值为None表示本函数不处理，交由下一个中间件执行，若所有中间件都没有处理，由engine抛出异常
		- 返回值应该是Response对象、字典、items对象，结果会被送到管道，然后开始中间件的output流程
	- process_start_requests(self,start_requests, spider)
		- 处理第一个request的函数，可用来添加请求头
	- spider_opened
		- 中间件启用后，到爬虫打开时调用

	```python
	class AmazonSpiderMiddleware(object):
	    # Not all methods need to be defined. If a method is not defined,
	    # scrapy acts as if the spider middleware does not modify the
	    # passed objects.
	
	    @classmethod
	    def from_crawler(cls, crawler):
	        # This method is used by Scrapy to create your spiders.
	        s = cls()
	        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
	        return s
	
	    def process_spider_input(self, response, spider):
	        # Called for each response that goes through the spider
	        # middleware and into the spider.
	
	        # Should return None or raise an exception.
	        return None
	
	    def process_spider_output(self, response, result, spider):
	        # Called with the results returned from the Spider, after
	        # it has processed the response.
	
	        # Must return an iterable of Request, dict or Item objects.
	        for i in result:
	            yield i
	
	    def process_spider_exception(self, response, exception, spider):
	        # Called when a spider or process_spider_input() method
	        # (from other spider middleware) raises an exception.
	
	        # Should return either None or an iterable of Response, dict
	        # or Item objects.
	        pass
	
	    def process_start_requests(self, start_requests, spider):
	        # Called with the start requests of the spider, and works
	        # similarly to the process_spider_output() method, except
	        # that it doesn’t have a response associated.
	
	        # Must return only requests (not items).
	        for r in start_requests:
	            yield r
	
	    def spider_opened(self, spider):
	        spider.logger.info('Spider opened: %s' % spider.name)
	```

#### 下载中间件
- 基本使用
	- from_crawler
		- 类方法，用于实例化中间件
	- process_request(self, request, spider)
		- 请求即将被doenloader执行之前
		- 常用来添加请求头、更换代理IP、设置超时时间等
		- 返回None表示正常
		- 返回Response对象，停止process_request的执行，开始执行process_response
		- 返回Request对象，停止中间件的执行，将Request重新调度器
		- 抛出异常，执行中间件的异常流程，然后交给sipder生成Request时errback指定的异常处理函数
	- process_response(self, request, response, spider)
		- downloader已经得到请求的响应之后
		- 常用来检测响应的状态、是否成功等
		- 返回Response对象,转交给其他中间件process_response,最后交给engine
		- 返回Request 对象，停止中间件，request会被重新调度下载
		- 抛出异常，执行中间件的异常流程，然后交给sipder生成Request时errback指定的异常处理函数
	- process_exception(self, request, exception, spider)
		- 处理下载中间件出现的异常
		- 返回None表示不处理异常，交由后续函数处理
		- 返回response对象表示已处理异常，执行output流程
		- 返回request对象表示已处理异常，执行input流程
	- spider_opened
		- 中间件启用后，到爬虫打开时调用
- 使用代理
	- TODO

	```python
	#1、与middlewares.py同级目录下新建proxy_handle.py
	import requests
	
	def get_proxy():
	    return requests.get("http://127.0.0.1:5010/get/").text
	
	def delete_proxy(proxy):
	    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
	    
	
	#2、middlewares.py
	from Amazon.proxy_handle import get_proxy,delete_proxy
	
	class DownMiddleware1(object):
	    def process_request(self, request, spider):
	        """
	        请求需要被下载时，经过所有下载器中间件的process_request调用
	        :param request:
	        :param spider:
	        :return:
	            None,继续后续中间件去下载；
	            Response对象，停止process_request的执行，开始执行process_response
	            Request对象，停止中间件的执行，将Request重新调度器
	            raise IgnoreRequest异常，停止process_request的执行，开始执行process_exception
	        """
	        proxy="http://" + get_proxy()
	        request.meta['download_timeout']=20
	        request.meta["proxy"] = proxy
	        print('为%s 添加代理%s ' % (request.url, proxy),end='')
	        print('元数据为',request.meta)
	
	    def process_response(self, request, response, spider):
	        """
	        spider处理完成，返回时调用
	        :param response:
	        :param result:
	        :param spider:
	        :return:
	            Response 对象：转交给其他中间件process_response
	            Request 对象：停止中间件，request会被重新调度下载
	            raise IgnoreRequest 异常：调用Request.errback
	        """
	        print('返回状态吗',response.status)
	        return response
	
	
	    def process_exception(self, request, exception, spider):
	        """
	        当下载处理器(download handler)或 process_request() (下载中间件)抛出异常
	        :param response:
	        :param exception:
	        :param spider:
	        :return:
	            None：继续交给后续中间件处理异常；
	            Response对象：停止后续process_exception方法
	            Request对象：停止中间件，request将会被重新调用下载
	        """
	        print('代理%s，访问%s出现异常:%s' %(request.meta['proxy'],request.url,exception))
	        import time
	        time.sleep(5)
	        delete_proxy(request.meta['proxy'].split("//")[-1])
	        request.meta['proxy']='http://'+get_proxy()
	
	        return request
	```

### <span id="7">Selectors</span>
- scrapy提供的方便的对文档元素的查询
	- xpath,按照文档树结构的查询
	- css，按照css选择器的方式查询
	- re,按照正则表达式查询
		- 查询结构通用方法
			- from scrapy.selector.unified import Selector
			- extract,查询结果都是列表，列表元素都是seletors对象，此方法取对象保存的文档数据
			- extract_first,只取列表第一个元素
			- 嵌套查找,查询结果还可以继续使用xpath、css、re
- xpath
	- "//"与"/"
	- text
	- 属性加前缀"@"
	- 相对路径
		- 在"/"或"//"前加"."，表示从查询结果中搜索
- css
- re

- 测试
	- `scrapy shell https://doc.scrapy.org/en/latest/_static/selectors-sample1.html`

	```python
	#1 //与/
	>>> response.xpath('//body/a') #开头的//代表从整篇文档中寻找,body之后的/代表body的儿子
	[]
	>>> response.xpath('//body//a') #开头的//代表从整篇文档中寻找,body之后的//代表body的子子孙孙
	[<Selector xpath='//body//a' data='<a href="image1.html">Name: My image 1 <'>, <Selector xpath='//body//a' data='<a href="image2.html">Name: My image 2 <'>, <Selector xpath='//body//a' data='<a href="
	image3.html">Name: My image 3 <'>, <Selector xpath='//body//a' data='<a href="image4.html">Name: My image 4 <'>, <Selector xpath='//body//a' data='<a href="image5.html">Name: My image 5 <'>]
	
	#2 text
	>>> response.xpath('//body//a/text()')
	>>> response.css('body a::text')
	
	#3、extract与extract_first:从selector对象中解出内容
	>>> response.xpath('//div/a/text()').extract()
	['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']
	>>> response.css('div a::text').extract()
	['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']
	
	>>> response.xpath('//div/a/text()').extract_first()
	'Name: My image 1 '
	>>> response.css('div a::text').extract_first()
	'Name: My image 1 '
	
	#4、属性：xpath的属性加前缀@
	>>> response.xpath('//div/a/@href').extract_first()
	'image1.html'
	>>> response.css('div a::attr(href)').extract_first()
	'image1.html'
	
	#4、嵌套查找
	>>> response.xpath('//div').css('a').xpath('@href').extract_first()
	'image1.html'
	
	#5、设置默认值
	>>> response.xpath('//div[@id="xxx"]').extract_first(default="not found")
	'not found'
	
	#4、按照属性查找
	response.xpath('//div[@id="images"]/a[@href="image3.html"]/text()').extract()
	response.css('#images a[@href="image3.html"]/text()').extract()
	
	#5、按照属性模糊查找
	response.xpath('//a[contains(@href,"image")]/@href').extract()
	response.css('a[href*="image"]::attr(href)').extract()
	
	response.xpath('//a[contains(@href,"image")]/img/@src').extract()
	response.css('a[href*="imag"] img::attr(src)').extract()
	
	response.xpath('//*[@href="image1.html"]')
	response.css('*[href="image1.html"]')
	
	#6、正则表达式
	response.xpath('//a/text()').re(r'Name: (.*)')
	response.xpath('//a/text()').re_first(r'Name: (.*)')
	
	#7、xpath相对路径
	>>> res=response.xpath('//a[contains(@href,"3")]')[0]
	>>> res.xpath('img')
	[<Selector xpath='img' data='<img src="image3_thumb.jpg">'>]
	>>> res.xpath('./img')
	[<Selector xpath='./img' data='<img src="image3_thumb.jpg">'>]
	>>> res.xpath('.//img')
	[<Selector xpath='.//img' data='<img src="image3_thumb.jpg">'>]
	>>> res.xpath('//img') #这就是从头开始扫描
	[<Selector xpath='//img' data='<img src="image1_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image2_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image3_thumb.jpg">'>, <Selector xpa
	th='//img' data='<img src="image4_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image5_thumb.jpg">'>]
	
	#8、带变量的xpath
	>>> response.xpath('//div[@id=$xxx]/a/text()',xxx='images').extract_first()
	'Name: My image 1 '
	>>> response.xpath('//div[count(a)=$yyy]/@id',yyy=5).extract_first() #求有5个a标签的div的id
	'images'
	```

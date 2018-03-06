## Flask原理剖析

### 图解源码
<img src="http://chuann.cc/Intermediate_Python/flask/from_app.runtoapp.__call__.png">

### 详细
1. Flask的实例app.run()
2. 执行werkzeug.serving中的run_simple函数，这里传入了Flask类的实例app
3. 执行run_simple中的inner函数，得到一个socket
	- 执行werkzeug.serving中的make_server函数
	- 在make_server函数根据设置调用线程、进程、或基础WSGI服务
		- 在WSGI服务实例化过程中
			1. 给handler绑定WSGIRequestHandler处理类，用于处理客户端请求到来
			2. 将flask指定的ip和端口、handler传递给python的http.HTTPSerer，生成一个socket，即flask所使用的套接字
			3. 给这个scoket服务的RequestHandlerClass属性，绑定上了WSGIRequestHandler处理类
			4. 给这个socket服务的app水星，绑定了Flask的实例app
4. 在inner函数中，socket启动，开始监听请求
	- `socket.serve_forever()`，这便是flask框架建立的服务器的根本，通过这段代码可以监听请求，然后处理请求
	
	```python
	def serve_forever(self, poll_interval=0.5):
	    """Handle one request at a time until shutdown.
	
	    Polls for shutdown every poll_interval seconds. Ignores
	    self.timeout. If you need to do periodic tasks, do them in
	    another thread.
	    """
	    self.__is_shut_down.clear()
	    try:
	        # XXX: Consider using another file descriptor or connecting to the
	        # socket to wake this up instead of polling. Polling reduces our
	        # responsiveness to a shutdown request and wastes cpu at all other
	        # times.
	        with _ServerSelector() as selector:
	            selector.register(self, selectors.EVENT_READ)
	
	            while not self.__shutdown_request:
	                ready = selector.select(poll_interval)
	                if ready:
	                    self._handle_request_noblock()
	
	                self.service_actions()
	    finally:
	        self.__shutdown_request = False
	        self.__is_shut_down.set()
	```
5. 当有请求到来会执行self._handle_request_noblock()
	- 这里可以看到执行了处理请求函数，以及最后的结束请求，展现了http协议无连接的特性，一次请求建立了一次连接，处理完就断开
	
	```python
	def _handle_request_noblock(self):
	    """Handle one request, without blocking.
	
	    I assume that selector.select() has returned that the socket is
	    readable before this function was called, so there should be no risk of
	    blocking in get_request().
	    """
	    try:
	        request, client_address = self.get_request()
	    except OSError:
	        return
	    if self.verify_request(request, client_address):
	        try:
	            self.process_request(request, client_address)
	        except Exception:
	            self.handle_error(request, client_address)
	            self.shutdown_request(request)
	        except:
	            self.shutdown_request(request)
	            raise
	    else:
	        self.shutdown_request(request)	
	```
6. 上面执行`self.process_request(request, client_address)`，会根据之前设定的多线程或者多进程或者其他处理，这里以线程举例

	```python
	class ThreadingMixIn:
	    """Mix-in class to handle each request in a new thread."""
	
	    # Decides how threads will act upon termination of the
	    # main process
	    daemon_threads = False
	
	    def process_request_thread(self, request, client_address):
	        """Same as in BaseServer but as a thread.
	
	        In addition, exception handling is done here.
	
	        """
	        try:
	            self.finish_request(request, client_address)
	        except Exception:
	            self.handle_error(request, client_address)
	        finally:
	            self.shutdown_request(request)
	
	    def process_request(self, request, client_address):
	        """Start a new thread to process the request."""
	        t = threading.Thread(target = self.process_request_thread,
	                             args = (request, client_address))
	        t.daemon = self.daemon_threads
	        t.start()
	```
7. 上面主要是根据选择应对并发的策略，最终执行的是`self.finish_request(request, client_address)`

	```python
	def finish_request(self, request, client_address):
	    """Finish one request by instantiating RequestHandlerClass."""
	    self.RequestHandlerClass(request, client_address, self)
	```
	- 这里触发werkzeug.serving.WSGIRequestHandler的构造方法，可见最终处理请求的就是RequestHandler类的handle方法

	```python
	def __init__(self, request, client_address, server):
	    self.request = request
	    self.client_address = client_address
	    self.server = server
	    self.setup()
	    try:
	        self.handle()
	    finally:
	        self.finish()
	```
8. 执行handler的目的是调用werkzeug.serving.WSGIRequestHandler的handle_one_request方法:

	```python
	def handle_one_request(self):
	    """Handle a single HTTP request."""
	    self.raw_requestline = self.rfile.readline()
	    if not self.raw_requestline:
	        self.close_connection = 1
	    elif self.parse_request():
	        return self.run_wsgi()
	```
9. 这里run_wsgi的代码较多，着重关注两行代码
	- 调用方法内定义的execute函数，把Flask的实例app传入`execute(self.server.app)`
	- 调用app的\_\_call__方法，把环境变量和定义的开始响应的函数传入`application_iter = app(environ, start_response)`
	- 至此，从flask启动项目到请求抵达flask服务，终于开始了flask的流程

10. app的\_\_call__方法并没有开始处理请求，而是转交给self.wsgi_app，在这里包含了请求在flask的生命周期
	1. 开启上下文管理，并将请求加入上下文
	2. 处理请求
	3. 返回响应
	4. 关闭上下文管理

	```python
	def wsgi_app(self, environ, start_response):
	    """The actual WSGI application.  This is not implemented in
	    `__call__` so that middlewares can be applied without losing a
	    reference to the class.  So instead of doing this::
	
	        app = MyMiddleware(app)
	
	    It's a better idea to do this instead::
	
	        app.wsgi_app = MyMiddleware(app.wsgi_app)
	
	    Then you still have the original application object around and
	    can continue to call methods on it.
	
	    .. versionchanged:: 0.7
	       The behavior of the before and after request callbacks was changed
	       under error conditions and a new callback was added that will
	       always execute at the end of the request, independent on if an
	       error occurred or not.  See :ref:`callbacks-and-errors`.
	
	    :param environ: a WSGI environment
	    :param start_response: a callable accepting a status code,
	                           a list of headers and an optional
	                           exception context to start the response
	    """
	    # TODO: 1. 开启上下文，准备数据request、session、g
	    ctx = self.request_context(environ)
	    ctx.push()	# 将请求加入上下文
	
	    error = None
	    try:
	        try:
	            # TODO: 2. 处理请求
	            response = self.full_dispatch_request()
	        except Exception as e:
	            error = e
	            response = self.handle_exception(e)
	        except:
	            error = sys.exc_info()[1]
	            raise
	        # TODO: 3. 返回响应
	        return response(environ, start_response)
	    finally:
	        if self.should_ignore_error(error):
	            error = None
	        # TODO: 4. 关闭请求
	        ctx.auto_pop(error)
	
	def __call__(self, environ, start_response):
	    """Shortcut for :attr:`wsgi_app`."""
	    # TODO: 请求接入，开始处理
	    return self.wsgi_app(environ, start_response)
	```
11. 开启上下文管理就是实例化一个上下文管理器，详细的参阅[上下文管理](context_management.md)
	- 上下文管理是flask框架的核心和难点
12. 处理请求
	1. 执行视图之前的请求中间件
	2. 执行视图函数
	3. 处理响应
		1. 执行视图之后的响应中间件
		2. 如果有session，在这里执行session的保存(响应返回session_id,内容保存至设置的地方)

	```python
	def full_dispatch_request(self):
	    """Dispatches the request and on top of that performs request
	    pre and postprocessing as well as HTTP exception catching and
	    error handling.
	
	    .. versionadded:: 0.7
	    """
	    # TODO: 3.1. 第一个请求执行的中间件   @before_first_request
	    self.try_trigger_before_first_request_functions()
	    try:
	        # flask的信号，依赖blinker模块，否则无效
	        request_started.send(self)
	        # TODO: 3.2 视图函数之前的中间件, 返回NONE表示继续执行视图函数
	        rv = self.preprocess_request()
	        if rv is None:
	            # TODO: 3.3. 执行视图函数
	            rv = self.dispatch_request()
	    except Exception as e:
	        rv = self.handle_user_exception(e)
	    # TODO: 3.4. 对返回响应做处理
	    return self.finalize_request(rv)
	```

## 上下文管理
- 上下文原理

	```python
	# context locals
	_request_ctx_stack = LocalStack()
	_app_ctx_stack = LocalStack()
	current_app = LocalProxy(_find_app)
	request = LocalProxy(partial(_lookup_req_object, 'request'))
	session = LocalProxy(partial(_lookup_req_object, 'session'))
	g = LocalProxy(partial(_lookup_app_object, 'g'))
	```

1. 创建Local类

	```
	{
		线程或协程唯一标识：{'stack': []},
		线程或协程唯一标识：{'stack': []},
		...
	}
	```

2. 流程
	- 当请求进来之后
		- 将请求相关数据封装到RequestContext(self, environ)对象
		- 请求相关数据通过stack添加到local
	- 以后使用时，谁使用谁就通过stack读取local的数据
	- 请求完成之后，将request从列表中移除

3. 关系
	- local对象专门用于存数据
	- stack对象专门负责数据的存、取、删除

4. 数据混淆问题
	- 单线程
	- 多线程
	- 协程
	- 全部由local中实现的get_ident获取的唯一ID标识


### 源码分析
1. werkzeug.local部分源码

	```python
	# 获取唯一标识，最细支持协程
	try:
	    from greenlet import getcurrent as get_ident
	except ImportError:
	    try:
	        from thread import get_ident
	    except ImportError:
	        from _thread import get_ident

	class Local(object):
		# 定义一个本地线程，为每个线程提供一个空间，线程之间可以隔离数据
	    __slots__ = ('__storage__', '__ident_func__')
	
	    def __init__(self):
			# 创建一块存储空间
	        object.__setattr__(self, '__storage__', {})
			# 绑定获取唯一标识的方法
	        object.__setattr__(self, '__ident_func__', get_ident)
	
	    def __iter__(self):
	        return iter(self.__storage__.items())
	
	    def __call__(self, proxy):
	        """Create a proxy for a name."""
	        return LocalProxy(self, proxy)
	
	    def __release_local__(self):
	        self.__storage__.pop(self.__ident_func__(), None)
	
	    def __getattr__(self, name):
			# 通过local.name取值，实际上是
			# local.__storage__.get_ident().name
	        try:
	            return self.__storage__[self.__ident_func__()][name]
	        except KeyError:
	            raise AttributeError(name)
	
	    def __setattr__(self, name, value):
			# 本方法是本地线程实现的核心
			# 通过local.name = value，的赋值实际上执行的是
			# 给local.__storage__.get_ident().name = value	# 这里的get_ident()写法不规范，仅作为示意
			# 表面上看是给同一个local赋值，但其实，local通过这个方法为每一个不同线程、协程都维护着一个字典
	        ident = self.__ident_func__()
	        storage = self.__storage__
	        try:
	            storage[ident][name] = value
	        except KeyError:
	            storage[ident] = {name: value}
	
	    def __delattr__(self, name):
	        try:
	            del self.__storage__[self.__ident_func__()][name]
	        except KeyError:
	            raise AttributeError(name)

	class LocalStack(object):
	
	    def __init__(self):
			# 借助Local的特性
	        self._local = Local()
	
	    def __release_local__(self):
	        self._local.__release_local__()
	
	    def _get__ident_func__(self):
	        return self._local.__ident_func__
	
	    def _set__ident_func__(self, value):
	        object.__setattr__(self._local, '__ident_func__', value)
	    __ident_func__ = property(_get__ident_func__, _set__ident_func__)
	    del _get__ident_func__, _set__ident_func__
	
	    def __call__(self):
	        def _lookup():
	            rv = self.top
	            if rv is None:
	                raise RuntimeError('object unbound')
	            return rv
	        return LocalProxy(_lookup)
	
	    def push(self, obj):
	        """Pushes a new item to the stack"""
			# 在此处设置localstack._local.__storage__.get_ident().stack = []
			# 该方法为这个列表append新的元素
	        rv = getattr(self._local, 'stack', None)
	        if rv is None:
	            self._local.stack = rv = []
	        rv.append(obj)
	        return rv
	
	    def pop(self):
	        """Removes the topmost item from the stack, will return the
	        old value or `None` if the stack was already empty.
	        """
			# 利用变量存储这个线程的数据空间
	        stack = getattr(self._local, 'stack', None)
	        if stack is None:
	            return None
	        elif len(stack) == 1:
	            release_local(self._local)	# pop出这个线程的在Local中的数据空间，之后无法通过local读取到，仅能通过stack变量
	            return stack[-1]			# 返回最新的，然后方法结束，舍弃stack
	        else:
	            return stack.pop()
	
	    @property
	    def top(self):
	        """The topmost item on the stack.  If the stack is empty,
	        `None` is returned.
	        """
	        try:
	            return self._local.stack[-1]
	        except (AttributeError, IndexError):
	            return None
	```
2. flask.globals部分源码
	
	```python
	from werkzeug.local import LocalStack
	
	# 省略其他代码...
	
	_request_ctx_stack = LocalStack()
	_app_ctx_stack = LocalStack()
	```

3. 选取flask.ctx部分源码

	```python
	from flask.globals import _request_ctx_stack, _app_ctx_stack
	class RequestContext(object):
	    def __init__(self, app, environ, request=None):
	        self.app = app
	        # TODO: 2.1 处理request
	        if request is None:
	            request = app.request_class(environ)
	        self.request = request
	        self.url_adapter = app.create_url_adapter(self.request)
	        self.flashes = None
	        self.session = None
	        self._implicit_app_ctx_stack = []
	        self.preserved = False
	        self._preserved_exc = None
	        self._after_request_functions = []
	
	        self.match_request()
	
	    def push(self):
	        """Binds the request context to the current context."""
	        top = _request_ctx_stack.top
	        if top is not None and top.preserved:
	            top.pop(top._preserved_exc)
	
	        # Before we push the request context we have to ensure that there
	        # is an application context.
	        app_ctx = _app_ctx_stack.top
	        if app_ctx is None or app_ctx.app != self.app:
	            app_ctx = self.app.app_context()
	            app_ctx.push()
	            self._implicit_app_ctx_stack.append(app_ctx)
	        else:
	            self._implicit_app_ctx_stack.append(None)
	
	        if hasattr(sys, 'exc_clear'):
	            sys.exc_clear()
	
	        # TODO: 2.2 把RequestContext对象添加进stack
	        _request_ctx_stack.push(self)
	
	        # TODO: 2.3 处理session
	        self.session = self.app.open_session(self.request)
	        if self.session is None:
	            self.session = self.app.make_null_session()
	
	    def pop(self, exc=_sentinel):
	        app_ctx = self._implicit_app_ctx_stack.pop()
	
	        try:
	            clear_request = False
	            if not self._implicit_app_ctx_stack:
	                self.preserved = False
	                self._preserved_exc = None
	                if exc is _sentinel:
	                    exc = sys.exc_info()[1]
	                self.app.do_teardown_request(exc)
	
	                if hasattr(sys, 'exc_clear'):
	                    sys.exc_clear()
	
	                request_close = getattr(self.request, 'close', None)
	                if request_close is not None:
	                    request_close()
	                clear_request = True
	        finally:
	            rv = _request_ctx_stack.pop()
	
	            # get rid of circular dependencies at the end of the request
	            # so that we don't require the GC to be active.
	            if clear_request:
	                rv.request.environ['werkzeug.request'] = None
	
	            # Get rid of the app as well if necessary.
	            if app_ctx is not None:
	                app_ctx.pop(exc)
	
	            assert rv is self, 'Popped wrong request context.  ' \
	                '(%r instead of %r)' % (rv, self)
	```

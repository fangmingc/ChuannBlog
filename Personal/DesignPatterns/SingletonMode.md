## 单例模式
### 导入文件
- python会将导入文件的全局变量变成单例
- 在一个文件导入另外一个文件两次以上不会重复创建导入文件的对象

### 用类方法创建
- 定义instance类方法代替普通类构造方法
	
	```python
	class Foo:
	    """创建方式一  不支持多线程"""
	    _instance = None
	
	    def __init__(self, name):
	        self.name = name
	
	    @classmethod
	    def instance(cls, *args, **kwargs):
	        if not Foo._instance:
	            obj = cls(*args, **kwargs)
	            cls._instance = obj
	        return cls._instance
	
	class Bar:
	    """创建方式二 不支持多线程"""
	
	    def __init__(self, name):
	        self.name = name
	
	    @classmethod
	    def instance(cls, *args, **kwargs):
	        if not hasattr(cls, "_instance"):
	            obj = cls(*args, **kwargs)
	            setattr(cls, "_instance", obj)
	        return getattr(cls, "_instance")
	```
- 缺陷：无法支持多线程

	```python
	import threading
	class Bar:
	
	    def __init__(self, name):
	        self.name = name
			import time
			time.sleep(1)
	
	    @classmethod
	    def instance(cls, *args, **kwargs):
	        if not hasattr(cls, "_instance"):
	            obj = cls(*args, **kwargs)
	            setattr(cls, "_instance", obj)
	        return getattr(cls, "_instance")
	
	def task(arg):
		obj = Bar(arg)
		print(obj)
	
	for i in range(10):
		t = threading.Thread(target=task, args=[i, ])
		t.start()
	```

- 解决多线程---加锁

	```python
	from threading import Lock, Thread
	import time
	
	
	class Foo(object):
	    _instance_lock = Lock()
	
	    def __init__(self, arg):
	        time.sleep(1)
	        self.arg = arg
	
	    @classmethod
	    def instance(cls, *args, **kwargs):
	        if not hasattr(Foo, "_instance"):
	            with Foo._instance_lock:
	                if not hasattr(Foo, "_instance"):
	                    setattr(Foo, "_instance", Foo(*args, **kwargs))
	        return getattr(Foo, "_instance")
	
	def task(arg):
	    obj = Foo.instance(arg)
	    print(obj.arg, type(obj), id(obj))
	
	if __name__ == '__main__':
	    for i in range(10):
	        t = Thread(target=task, args=[i, ])
	        t.start()
	```


### 基于\_\_new__方法(推荐)
```python
import time
import threading


class Foo(object):
    _instance_lock = threading.Lock()

    def __init__(self, arg):
        self.arg = arg

    def __new__(cls, *more):
        if not hasattr(cls, "_instance"):
            with Foo._instance_lock:
                if not hasattr(cls, "_instance"):
                    time.sleep(0.01)
                    setattr(cls, "_instance", object.__new__(cls))
        return getattr(cls, "_instance")


def task(arg):
    obj = Foo(arg)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
```
- 加锁的作用
	- 在new方法一旦有稍微长一点时间的操作就会产生线程问题

### 基于metaclass
```python
import threading
import time


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    time.sleep(0.01)
                    setattr(cls, "_instance", super(SingletonType, cls).__call__(*args, **kwargs))
        return getattr(cls, "_instance")


class Foo(metaclass=SingletonType):

    def __init__(self, arg):
        self.arg = arg


def task():
    obj = Foo(threading.current_thread().ident)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()
```


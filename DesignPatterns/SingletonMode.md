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

	```
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


### 基于\_\_new__方法(推荐)


### 基于metaclass

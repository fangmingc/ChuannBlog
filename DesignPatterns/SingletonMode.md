## 单例模式
- 导入文件，python会将导入文件的全局变量变成单例
	- 在一个文件导入另外一个文件两次以上不会重复创建导入文件的对象

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


## 5 面向对象

- [5.1 类和对象的概念](5.1Concept_of_class_and_Object.md) 
- [5.2 继承](5.2Inherit)
- [5.3 封装](5.3Encapsulation)
- [5.4 多态]()
- [5.5 面向对象进阶]()
- [5.6 反射]()
- [5.7 异常]()

### 类成员
#### 字段
- 普通字段
	- 属于对象，存储在对象空间
	- 使用self.字段名操作
- 静态字段
	- 属于类，存储在类空间，如果对象有重名字段，静态字段会被覆盖
	- 使用类名.字段名访问
	- 使用对象名.字段名访问
#### 方法
- 普通方法
	- 由对象调用，至少一个self参数，
	- 执行时自动将该方法的对象赋值给self
- 类方法
	- 定义时加上@classmethod装饰器
	- 由类调用，至少一个cls参数
	- 执行时自动将该方法的类赋值给cls
- 静态方法
	- 定义时加上@staticmethod装饰器
	- 由类调用，无默认参数
#### 属性
- 普通属性
	- 普通方法的变种，定义普通方法时加上@property装饰器

## 继承
### 继承的概念
- 子类继承父类的内容，包括字段、方法、属性。  
- 将多个类共有的方法提取到父类中，子类仅需继承父类而不必一一实现每个方法。
- 基类和派生类只是与父类、子类的叫法不一样  
#### 多继承
1.Java和C#中则只能继承一个类，Python的类可以继承多个类
2.Python的类如果继承了多个类，那么其寻找方法的方式有两种，分别是：深度优先和广度优先
- python2中分经典类和新式类，经典类为深度优先，新式类为广度优先。
	- 经典类：自定义最开始的类不继承任何东西
	- 新式类：自定义最开始的类继承object类
- python3种自定义的类全部默认继承新式类，均为广度优先
### 抽象类和接口类
```python
from abc import ABCmeta, abstractmethod
class Person(classmeta=ABCmeta)
```

- 抽象类：  
	- 在Python中，默认是有的
	- 父类的方法子类必须实现
	- 抽象类不能被实例化
	- 抽象类内的方法可以被简单实现
	- 抽象类不建议多继承
- 借口类：  
	- 做出一个良好的抽象，这个抽象规定了一个兼容接口，使得外部调用者无需关心具体细节，可一视同仁的处理实现了特定接口的所有对象
	- 在python中，默认是没有的，只是一种程序设计理念
	- 接口类的方法不能被实现
	- 接口隔离原则：
		- 应该有多个独立的接口，而不是多功能的单个接口
	- 接口类推荐使用多继承
## 多态
传递参数时不需要指定参数的数据类型。  
python推崇鸭子写法：  
“会叫的鸭子，不用管是什么鸭子”  
```python
class A:
    def pay(self):
        print('from A')

class B:
    def pay(self):
        print('from B')

def mypay(obj):
    obj.pay()
a = A()
b = B()

mypay(a)
mypay(b)
```
定义一个函数专门调用对象的方法，不用管是什么类的对象，只要对象有这个方法就可以。   
 
## 相关方法
### isinstance(object,classinfo)和issubclass(class,classinfo)
- isinstance用于判断object是否是classinfo、或classinfo直接、间接的子类的实例（instance），返回值为bool类型
- classinfo可以是一个包含多个类的元组，只要object按照上面的规则符合其中一个就会返回True
- issubclass用于判断class是否是classinfo、或classinfo直接、间接的子类，返回值为布尔类型
	```python
	class A:
	    pass
	
	
	class B(A):
	    pass
	
	
	class C(B):
	    pass
	
	
	class D:
	    pass
	
	x = C()
	# x是C的直接的实例
	print(isinstance(x, C))
	# x是B的间接的实例
	print(isinstance(x, B))
	# x不是D的实例
	print(isinstance(x, D))
	
	# classinfo可以是一个元组
	print(isinstance(x, (A, D)))
	
	# C是B的直接子类
	print(issubclass(C, B))
	# C是A的间接子类
	print(issubclass(C, A))
	# C不是D的子类
	print(issubclass(C, D))
	```
### 反射
#### 常用：
- hasattr(object, name)
	- 判断name是否是object的属性，返回一个布尔值。
	- name必须是字符串，object可以是任何有方法的对象，包括：类、类的实例、模块。
- getattr(object, name[, default])
	- 调用object的name属性或者方法，失败时返回default
	- 通常和hasattr方法连用
	```python
	class Foo:
	    f = '类的静态字段'
	
	    def __init__(self, name):
	        self.name = name
	        self.common = '类的普通字段'
	
	    def say_hi(self):
	        print('hi, %s' % self.name)
	
	obj = Foo('jack')
	
	# 判断是否含有某属性
	print(hasattr(Foo, 'f'))
	print(hasattr(obj, 'name'))
	print(hasattr(obj, 'say_hi'))
	
	# 获取属性
	print(getattr(Foo, 'f'))
	print(getattr(obj, 'name'))
	getattr(obj, 'say_hi')()
	
	print(getattr(obj, 'empty', "Does't exist."))
	```
- 关于模块
	```python
	import sys
	if hasattr(sys.modules[__name__], 'Foo'):
	    getattr(getattr(sys.modules[__name__], 'Foo')('jack'), 'say_hi')()
	```
通过sys.moudules得到当前已加载的模块列表，使用\_\_name__获取本文件的对象，判断是否有Foo属性，如果有则调用Foo属性并实例化出一个对象，调用对象的say_hi方法。
#### 不常用：
- setattr(object, name, value)
	- getattr的一个变种，可以对object的name属性进行赋值操作
	```python
	setattr(obj, 'name', 'other')
	print(getattr(obj, 'name'))
	```
	- 如果name属性不存在则会为其创建一个值为value的name属性
	- value可以是函数，包括另外定义的函数或者匿名函数，但是调用的时候必须要额外进行赋值操作
- delattr(object, name)
	- 用于删除object的name属性，如不存在属性则报AttributeError


### 内置方法
- \_\_new__
	- 当类开始实例化出对象时执行该方法
	- 正常的实例化由object类的\_\_new__执行该方法，并返回一个对象
	- 通常使用该方法在实例化出对象时额外进行一些操作，然后返回object类的\_\_new__
	```python
	class A:
	    def __init__(self):
	        print('in init function')
	        self.x = 1
	
	    def __new__(cls, *args, **kwargs):
	        print('in new function')
	        return object.__new__(A, *args, **kwargs)
	```
> 单例模式：  
> 一个类仅有一个对象。

```python
class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

one = Singleton()
two = Singleton()
three = Singleton()
print(one,two,three)
```

- \_\_init__
	- 执行\_\_new__之后执行该方法
- \_\_str\_\_和\_\_repr__
	- 当打印对象时，会打印str的返回值
	- 当str方法不存在，repr会代替str
- \_\_del__
	- 当对象被del的时候执行方法
- item系列
getitem用在从对象取值的时候使用方法内的返回值，setitem用于给对象的属性赋值操作，delitem用于删除对象的属性
	- \_\_getitem__
	- \_\_setitem__
	- \_\_delitem__
```python
class Foo:
    def __init__(self):
        self.name = 'jack'
        self.age = 24
        
    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]
f = Foo()
print(f['name'])
f['name'] = 'bob'
del f['name']
```
- \_\_call__
	- 定义在将对象当做函数调用时执行的方法
- \_\_len__	
	- 定义在对对象使用len函数时执行的方法
- \_\_hash__
	- 定义在对对象使用hash函数时执行的方法
- \_\_eq__
	- 定义在对两个对象使用==运算符时执行的方法

## 异常
```python
try:
	pass
except ValueError as message:
	print('先处理个别错误，现在捕获的是ValueError')
    print(message)	# 打印异常的错误信息
except Exception:
	print('捕获所有上面的except捕获不了的ERROR')
else:
	print('try中的代码没有异常处理则执行这里')
finally:
	print('不管有没有异常都要执行的代码')
```
- 应用：with语句自动关闭文件
```python
try:
    f = open('abc', 'w')
    # f.write('123')
finally:
    f.close()
```
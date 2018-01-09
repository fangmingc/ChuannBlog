## 数据库连接池

### 本地线程
- 为什么用本地线程
	- 每次操作数据库操作都要连接数据库
		- 当在全局定义一个公用链接，多线程时会出问题
			- 加锁可以解决
			- 但是加锁后就变成串行
- 本地线程，隔离每个线程中间的数据
	
	```python
	import threading
	import time
	local_values = threading.local()
	
	
	def func(num):
	    local_values.name = num
	    time.sleep(2)
	    print(local_values.name, threading.current_thread().name)
	
	
	for i in range(10):
	    t = threading.Thread(target=func, args=[i, ])
	    t.start()
	```

- local类实例化的对象是一个类似字典的结构

	```python
	{
		'identity': {'k1': 'v1', 'k2': ''v2},
		'identity2': {'k1': 'v1', 'k2': ''v2},
		...
	}
	```

- 源码

	```python
	class _localimpl:
	    """A class managing thread-local dicts"""
	    __slots__ = 'key', 'dicts', 'localargs', 'locallock', '__weakref__'
	
	    def __init__(self):
	        # The key used in the Thread objects' attribute dicts.
	        # We keep it a string for speed but make it unlikely to clash with
	        # a "real" attribute.
	        self.key = '_threading_local._localimpl.' + str(id(self))
	        # { id(Thread) -> (ref(Thread), thread-local dict) }
	        self.dicts = {}
	
	    def get_dict(self):
	        """Return the dict for the current thread. Raises KeyError if none
	        defined."""
	        thread = current_thread()
	        return self.dicts[id(thread)][1]
	
	    def create_dict(self):
	        """Create a new dict for the current thread, and return it."""
	        localdict = {}
	        key = self.key
	        thread = current_thread()
	        idt = id(thread)
	        def local_deleted(_, key=key):
	            # When the localimpl is deleted, remove the thread attribute.
	            thread = wrthread()
	            if thread is not None:
	                del thread.__dict__[key]
	        def thread_deleted(_, idt=idt):
	            # When the thread is deleted, remove the local dict.
	            # Note that this is suboptimal if the thread object gets
	            # caught in a reference loop. We would like to be called
	            # as soon as the OS-level thread ends instead.
	            local = wrlocal()
	            if local is not None:
	                dct = local.dicts.pop(idt)
	        wrlocal = ref(self, local_deleted)
	        wrthread = ref(thread, thread_deleted)
	        thread.__dict__[key] = wrlocal
	        self.dicts[idt] = wrthread, localdict
	        return localdict
	
	
	class local:
	    # 定义类只能设置两个属性
	    __slots__ = '_local__impl', '__dict__'
	
	    def __new__(cls, *args, **kw):
	        if (args or kw) and (cls.__init__ is object.__init__):
	            raise TypeError("Initialization arguments are not supported")
	        self = object.__new__(cls)
	
	        # 设置类的_local__impl属性为一个_localimpl类的实例
	        impl = _localimpl()
	        impl.localargs = (args, kw)
	        impl.locallock = RLock()
	        object.__setattr__(self, '_local__impl', impl)
	        impl.create_dict()
	
	        return self
		
	    # 以下是一些常规的设置
	    def __getattribute__(self, name):
	        with _patch(self):
	            return object.__getattribute__(self, name)
	
	    def __setattr__(self, name, value):
	        if name == '__dict__':
	            raise AttributeError(
	                "%r object attribute '__dict__' is read-only"
	                % self.__class__.__name__)
	        with _patch(self):
	            return object.__setattr__(self, name, value)
	
	    def __delattr__(self, name):
	        if name == '__dict__':
	            raise AttributeError(
	                "%r object attribute '__dict__' is read-only"
	                % self.__class__.__name__)
	        with _patch(self):
	            return object.__delattr__(self, name)
	```

### DBUtils数据库连接池
- 连接池参数

	```python
	from DBUtils.PooledDB import PooledDB, SharedDBConnection
	POOL = PooledDB(
	    creator=pymysql,  # 使用链接数据库的模块
	    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
	    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
	    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
	    maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
	    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
	    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
	    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
	    ping=0,
	    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
	    host='127.0.0.1',
	    port=3306,
	    user='root',
	    password='123',
	    database='pooldb',
	    charset='utf8'
	)
	```
	- creator
		- 链接数据库使用的模块
	- maxconnections	
		- 连接池允许的最大连接数
		- 0和None表示不限制连接数
	- mincached
		- 初始化时，链接池中至少创建的空闲的链接，0表示不创建
	- maxcached
		- 链接池中最多闲置的链接，0和None不限制
	- maxshared
		- 链接池中最多共享的链接数量
		- 0和None表示全部共享
		- PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
	- blocking
		- 连接池中如果没有可用连接后，是否阻塞等待。
		- True，等待；
		- False，不等待然后报错
	- maxusage
		- 一个链接最多被重复使用的次数，None表示无限制
	- setsession
		- 开始会话前执行的sql命令列表
	- ping
		- ping MySQL服务端，检查是否服务可用
		- 0 = None = never, 
		- 1 = default = whenever it is requested, 
		- 2 = when a cursor is created, 
		- 4 = when a query is executed, 
		- 7 = always

- 模式一
	- 基于threding.local实现为每个线程创建一个连接，关闭非关闭，当前线程可以重复使用本线程中的链接，线程终止时链接才关闭
- 模式二
	- 连接池原理
	- 设置连接池中最大连接数
	- 启动时，连接池中默认可以创建指定数目的链接
	- 如果有三个线程来连接池获取连接
		- 1个连接时，另外两个排着队等着使用
		- 2个连接时，另外一个排着队使用
		- 3个连接时，一对一使用
	- maxshared设置的最大共享连接数是无效的
		- 除非设置pymysql中threadsafety>1

#### 模式一
```python
from DBUtils.PersistentDB import PersistentDB
import pymysql

POOL = PersistentDB(
    creator=pymysql,  
    maxusage=None,  
    setsession=[],  
    ping=0,
    cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,
    threadlocal=None,  
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)


def func():
    # conn = SteadyDBConnection()
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()
    conn.close() # 不是真的关闭，而是假的关闭。 conn = pymysql.connect()   conn.close()

    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()
    conn.close()

import threading

for i in range(10):
    t = threading.Thread(target=func)
    t.start()
```

#### 模式二
```python
import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection
POOL = PooledDB(
    creator=pymysql,  
    maxconnections=6,  
    mincached=2, 
    maxcached=5,  
    maxshared=3,  
    blocking=True,  
    maxusage=None,  
    setsession=[],  
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)

def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。

    # PooledDedicatedDBConnection
    conn = POOL.connection()

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    conn.close()

    conn = POOL.connection()

    # print(th, '链接被拿走了', conn1._con)
    # print(th, '池子里目前有', pool._idle_cache, '\r\n')

    cursor = conn.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    conn.close()

func()
```


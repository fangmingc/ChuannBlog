## multiprocessing
基本与threading相同

### Process类
#### 实例化定义传入参数
- target   
	- 指定进程的任务函数地址
- args   
	- 指定任务函数的参数，元组格式传入
- kwargs   
	- 指定任务函数的参数，字典格式传入

#### 方法
- start   
	- 向操作系统发送进程开启请求(开进程必须有的方法)
- join   
	- 主进程等待子进程结束
- terminate   
	- 终止进程(该操作不会终止该进程的子进程)

#### 属性
- daemon  
	- True时设置子进程为主进程守护进程
	- 当主进程代码执行完毕，守护进程被回收
	- 必须在start方法启用前设定
- ident   
	- 获取进程的id
- pid   
	- 获取进程的id

#### 方法
- cpu_count   
	- 查看计算机cpu数
- current_process   
	- 获取当前进程对象，返回结果同Process类实例化对象

### Pool类
- numprocess
	- 设置的最大进程数
- initializer
- initargs


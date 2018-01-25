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
- 代码演示

	```python
	import os
	from multiprocessing import Process
	import time
	
	
	def task(num, name):
	    print(os.getpid(), "开始运行", num, name)
	    time.sleep(1)
	    print(os.getpid(), "结束运行")
	
	
	if __name__ == '__main__':
	    for i in range(5):
	        p = Process(target=task, args=(i,), kwargs={"name": i**2})
	        p.start()
	```


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

### Pool类
- 进程池类
	- 指定数目的进程循环使用
- 初始化参数
	- numprocess
		- 设置的最大进程数
- 方法
	- apply
		- 同步提交任务，提交一个，等待完成，再提交下一个
	- apply_async
		- 异步提交任务，一次性提交完毕，不管结果
		- callback
			- 指定回调函数
- 示例1
	
	```python
	import os
	import time
	from multiprocessing import Pool
	
	
	def task(num):
	    print(os.getpid(), "开始运行", num)
	    time.sleep(1)
	    print(os.getpid(), "结束运行")
	
	
	if __name__ == '__main__':
	    pool = Pool(4)
	    p_list = []
	    for i in range(10):
	        p_list.append(pool.apply_async(task, args=(i,)))
	
	    for p in p_list:
	        p.wait()
	```
- 实例2：回调函数

	```python
	import os
	import time
	from multiprocessing import Pool
	
	
	def back(res):
	    print(os.getpid(), "处理来自", res, "的结果")
	
	
	def task(num):
	    print(os.getpid(), "开始运行", num)
	    time.sleep(1)
	    print(os.getpid(), "结束运行")
	    return os.getpid()
	
	
	if __name__ == '__main__':
	    pool = Pool(4)
	    p_list = []
	    for i in range(10):
	        p_list.append(pool.apply_async(task, args=(i,), callback=back))
	
	    for p in p_list:
	        p.wait()
	```

### 模块函数
- cpu_count   
	- 查看计算机cpu数
- current_process   
	- 获取当前进程对象，返回结果同Process类实例化对象



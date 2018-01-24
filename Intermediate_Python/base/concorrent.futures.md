## concorrent.futures

### Executor类
- submit
	- fn 提交的任务
	- \*args,\*\*kwargs 任务所需的参数
- shutdown
	- 集合了进程/线程池的close和join方法
	- 参数wait，设置最大等待时长
- map
	- 和内置函数map类似
- 单个进程/线程的方法
	- result

### ProcessPoolExecutor类
- 实例化参数
	- 不指定则为CPU核数
- 其余方法继承Executor抽象类

### ThreadPoolExecutor类
- 实例化参数
	- 不指定则为CPU核数乘以5
- 其余方法继承Executor抽象类
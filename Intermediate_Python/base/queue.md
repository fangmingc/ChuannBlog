## queue

### Queue类
- 就是普通队列
- put
	- 在队列末端放入数据
- get
	- 在队列最前端取走数据

### LifoQueue类
- 模拟堆栈，先进后出/后进先出
- put
	- 在堆栈最上面放入
- get
	- 从堆栈最上面取数据

### PriorityQueue类
- 优先级队列
- put
	- 参数priority
		- 数据的优先级，数字越小越高
	- 参数data
		- 存放的数据
- get
	- 按照优先级取数据
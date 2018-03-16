## 缓存

- linux 内存分配
	- 按内存页分配，page大小默认4kb
	- 进行slab allocator划分
		- 使用chain和chunk进行划分
			- centos6以后使用大叶内存方式分配
			- 4kb-8kb-16kb的chain
			- 每个chain挂载相同大小的chunk，由page组成
	- 内存清理使用buddy system
		- LRU 最近最少使用原则
	- RSS
		- 常驻内存区，内存页组成，运行程序的主体
	- page cache
		- 数据缓存区
		- 程序需要处理的数据加载于此
	- anno page
		- 程序处理完数据交给下一个程序，数据暂存区
- 缓存
	- redis,memcache，tair
	- 使用更好的chain和chunk划分
- 性能区分
	- redis，单用户多并发读写，性能高
	- memcache，多用户少读写，性能高
	- redis是单核管理机制，生产环境中一般是单机多实例架构(即一台机器装多个redis)。
	- 国内最早使用redis的是新浪，如今是直播平台使用redis更多

### redis
- 数据高速缓存

	

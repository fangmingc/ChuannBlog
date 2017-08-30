# 并发编程
进程、线程、协程
## 背景知识
进程的概念起源于操作系统，是操作系统最核心的概念。  

- 操作系统管理进程
- 进程之间的调度由操作系统的负责切换

并发实现的核心原理不是进程间的切换，而是保留下进程切换前的状态，以便切换回来时继续。

## 进程
### 概念
- 狭义定义
	- 进程是正在运行的程序的实例
	- 指的是程序的运行过程
- 广义定义
	- 计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位，是操作系统结构的基础
- 含义的变更
	- 在早期面向进程设计的计算机结构中，进程是程序的基本执行实体
	- 在当代面向线程设计的计算机结构中，进程是线程的容器
- 主要特点
	1. 进程是一个实体 每一个进程都有它自己的地址空间，包括文本区域（text region）、数据区域（data region）、堆栈（stack region）
	2. 进程是一个执行中的程序 程序是一个没有生命的实体，只有处理器赋予程序生命时（操作系统执行之），它才能成为一个活动的实体

### 特征
1. 动态性 进程的实质是程序在多道程序系统中的一次执行过程，动态产生，动态消亡
2. **并发性** 伪并行，任何进程都可以同其他进程一起并发执行
3. 独立性 进程是一个能独立运行的基本单位，同时也是系统分配资源和调度的独立单位
4. **异步性** 由于进程间的相互制约，使进程具有执行的间断性，即进程按各自独立的、不可预知的速度向前推进
5. 结构特征 进程由程序、数据和进程控制块三部分组成

### 状态

- 运行 
	1. 程序等待I/O，进入阻塞 
	2. 进程运行时间过长，调度程序选择另一个进程，该进程进入就绪
- 就绪 
	3. 调度程序选择进程，进入运行
- 阻塞
	4. I/O操作出现结果，进入就绪

### multiprocessing模块
#### Process类
```python
# 服务端
from socket import *
from multiprocessing import Process
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
s.bind(('127.0.0.1',8088))
s.listen(5)
def talk(conn,addr):
    while True: #通信循环
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
if __name__ == '__main__':
    while True:#链接循环
        conn,addr=s.accept()
        p=Process(target=talk,args=(conn,addr))
        p.start()
    s.close()

# 客户端
from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8088))

while True:
    msg=input('>>: ').strip()
    if not msg:continue
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print(data.decode('utf-8'))
c.close()

```

### 互斥锁
进程间互相排斥强制加锁，当某个进程使用某资源时，其余进程不允许使用该资源。   


如何给进程计数，开启了多少个，什么时候结束

### 数据共享
#### 文件
#### 内存
- Manager类
#### IPC
- 队列
	- Queue
	- JoinableQueue
- 管道


### 生产者消费者模型
异步并发


### 进程池（Pool类）

#### 回调函数



## 线程
轻量级进程

### 特点
- 共享进程的数据
- 创建开销小于创建进程开销

### 开线程的两种方式
- 直接实例化threading模块的Thread类，在参数指定线程任务
- 自定义一个线程类，继承Thread类，在run函数定制任务

### 数据共享





### 全局解释器锁（GIL）(Global Interpreter Lock)
### Thread



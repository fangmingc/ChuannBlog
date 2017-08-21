# Socket网络编程
- [基础知识](#1)
- [socket(套接字)模块](#2)
- 

## <span id='1'>基础知识</span>
### 客户端/服务器架构(C/S)
- 定义：C/S又称Client/Server或客户/服务器模式。服务器通常采用高性能的PC、工作站或小型机，并采用大型数据库系统，如ORACLE、SYBASE、InfORMix或 SQL Server。客户端需要安装专用的客户端软件。
- 通过它可以充分利用两端硬件环境的优势，将任务合理分配到Client端和Server端来实现，降低了系统的通讯开销。
- B/S(Browser/Server)(浏览器/服务器)是随着Internet技术的兴起，对C/S结构的一种改进。在这种结构下，软件应用的业务逻辑完全在应用服务器端实现(web应用程序)，客户端(浏览器)只需要浏览器即可进行业务处理

### OSI七层协议   
- 物理层  
	- 硬件接口，传输电信号    
- 数据链路层  
	- 主要为以太网协议，要求每台机器有一个mac地址，基于mac地址进行局域网广播通信  
- 网络层  
	- 核心为ip协议，要求每台机器有一个ip地址，基于ip通信
	- arp协议，由ip地址获取目标ip的mac地址    
- 传输层  
	- 基于tcp/udp协议通信，标识每个软件的端口
	- 0-1023为系统端口，称周知端口
	- 1024-49151分配给用户进程或应用程序，称注册端口
	- 49152-65535不固定分配某种服务，称动态端口
- 应用层  
	- 各种应用程序自定义的协议
	- HTTP(HyperText Transfer Protocol) 超文本传输协议，用于实现WWW服务
	- FTP(File Transfer Protocol) 文件传输协议，用于实现交互式文件传输功能
	- DNS(Domain Name System) 域名系统，用于实现网络设备名字到IP地址映射的网络服务
	- SMTP(Simple Mail Transfer Protocol) 简单邮件传送协议，用于实现电子邮箱传送功能
	- SNMP(Simple Network Management Protocol) 简单网络管理协议，用于管理与监视网络设备
	- Telnet 远程登录协议，用于实现远程登录功能

## <span id='1'>socket(套接字)模块</span>
>网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。

- Socket的英文原义是“孔”或“插座”。作为BSD UNIX的进程通信机制，取后一种意思。通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机之间的通信。
- 将传输层及以下的网络协议封装，提供简单使用的接口(API)给应用层的软件，专门面向C/S架构模型设计的
- 三个参数：协议，本地地址，本地端口

### 套接字的连接过程
1. 服务器监听：不指定具体的客户端套接字，处于等待连接的状态，实时监控网络状态
2. 客户端请求：指由客户端的套接字提出请求，目标是服务器端的套接字，需要指出服务器端套接字的地址和端口号
3. 连接确认：当服务器端套接字监听到客户端套接字的连接请求，就响应请求建立一个新的进程，并返回客户端服务器的套接字描述，当客户端确认描述，连接就正式建立，服务器端继续出于监听状态
![](https://baike.baidu.com/pic/socket/281150/0/d000baa1cd11728b45647b06cafcc3cec3fd2c4c?fr=lemma&ct=single)

### socket模块
```python  
import socket
socket.socket(socket_family, socket_type,protocal=0)
# socket_family 可以是 AF_UNIX 或 AF_INET。
# socket_type 可以是 SOCK_STREAM 或 SOCK_DGRAM
# protocol一般不填,默认值为 0。

# 获取tcp/ip套接字
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取udp/ip套接字
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 由于 socket 模块中有太多的属性。我们在这里破例使用了'from module import *'语句。
# 使用'from socket import *',我们就把 socket 模块里的所有属性都带到我们的命名空间里了,这样能 大幅减短我们的代码。
# 例如:
from socket import *
tcpSock = socket(AF_INET, SOCK_STREAM)
```
### 套接字(socket)函数
#### 服务端
- s.bind() 绑定(主机，端口号)到套接字
- s.listen() 开始TCP监听
- s.accept() 被动接受TCP客户的连接，(阻塞式)等待连接到来(阻塞：无响应直到接受到连接请求)

#### 客户端
- s.connect() 主动初始化TCP服务器连接
- s.connec_ex() connect()函数的扩展版本，出错时返回出错码，不抛出异常

#### 公共用途
- s.recv() 接收TCP数据
	- 不可接收'空'
- s.send() 发送TCP数据
	- 待发送数量大于己端缓存剩余区空间时，数据丢失，不会发完
- s.sendall() 发送完整的TCP数据
	- 循环调用s.send
s.recvfrom()        接收UDP数据  
s.sendto()          发送UDP数据  
s.getpeername()     连接到当前套接字的远端的地址  
s.getsockname()     当前套接字的地址  
s.getsockopt()      返回指定套接字的参数  
s.setsockopt()      设置指定套接字的参数  
- s.close() 关闭套接字

#### 面向锁的套接字方法
s.setblocking()     设置套接字的阻塞与非阻塞模式  
s.settimeout()      设置阻塞套接字操作的超时时间  
s.gettimeout()      得到阻塞套接字操作的超时时间  

#### 面向文件的套接字的函数
s.fileno()          套接字的文件描述符  
s.makefile()        创建一个与该套接字相关的文件  

### 基于TCP的套接字
#### 基础实例
- server端   

```python  
import socket

# 1.create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.Bind ip address and port to symbol the only server
# 127.*.*.* symbol local address
# in cmd, use:
#   netstat /an
#   to check the port in local machine
server.bind(('127.0.0.1', 20000))

# 3.set the limit of connect to server
server.listen(5)

# 4.start the server to begin listening the request from client
# when accept the request, the request contain information of client socket and client ip address
print('Server is listening request...')
client_connect, client_address = server.accept()
print('The information of client:\n%s\nThe client ip address:\n%s' % (client_connect, client_address))

# 5.stop the connect to client
client_connect.close()
# 6.stop the server
server.close()
```
- client端  

```python  
import socket

# 1.create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.connect to server with server's ip and port
connect = client.connect(('127.0.0.1', 20000))

# 3.stop the client
client.close()
```
#### 连接循环和通信循环
- server端  

```python   
import socket

# 1.create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.Bind ip address and port to symbol the only server
server.bind(('127.0.0.1', 20000))

# 3.set the limit of connect to server
server.listen(5)


# Link loop: server can tun long time
while True:
    # 4.start the server to begin listening the request from client
    print('Server is listening request...')
    client_connect, client_address = server.accept()
    print('The information of client:\n%s\nThe client ip address:\n%s' % (client_connect, client_address))

    # Message loop: server and client can communicate long time
    while True:
        try:
            # 5.set the limit of information received from client
            info = client_connect.recv(1024).decode('utf-8')   # bytes

            # when info is quit, just disconnect
            if info == 'quit':
                break

            # 6.send the data after operating
            client_connect.send(info[::-1].encode('utf-8'))
        # when any exception occur, just disconnect
        except Exception:
            break

    # 7.stop the connect to client
    client_connect.close()


# 8.stop the server
server.close()
```

- client端  
 
```python   
import socket

# 1.create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.connect to server with server's ip and port
client.connect(('127.0.0.1', 20000))


# Message loop: server and client can communicate long time
while True:
    info = input('>>>')

    # when info is empty, stop sending
    if not info:
        continue

    # 3.must send bytes
    client.send(info.encode('utf-8'))

    # when info is quit, just disconnect
    if info == 'quit':
        break

    # 4.receive the data from server
    data = client.recv(1024)
    print(data.decode('utf-8'))


# 5.stop the client
client.close()

```




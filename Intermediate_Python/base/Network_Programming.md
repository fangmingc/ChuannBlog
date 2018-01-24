# Socket网络编程
- [1 基础知识](#1.0)
- [2 socket(套接字)模块](#2.0)
	- [2.1 套接字的连接过程](#2.1)
	- [2.2 socket模块](#2.2)
	- [2.3 套接字(socket)函数](#2.3)
	- [2.4 基于TCP的套接字](#2.4)
	- [2.5 粘包](#2.5)
	- [2.6 基于UDP的套接字](#2.6)
	- [2.7 socketserver模块](#2.7)
- [3 练习：ftp文件上传下载](#3.0)


## <span id='1.0'>1 基础知识</span>
### 客户端/服务器架构(C/S)
- 定义：C/S又称Client/Server或客户/服务器模式。服务器通常采用高性能的PC、工作站或小型机，并采用大型数据库系统，如ORACLE、SYBASE、InfORMix或 SQL Server。客户端需要安装专用的客户端软件。
- 通过它可以充分利用两端硬件环境的优势，将任务合理分配到Client端和Server端来实现，降低了系统的通讯开销。
- B/S(Browser/Server)(浏览器/服务器)是随着Internet技术的兴起，对C/S结构的一种改进。在这种结构下，软件应用的业务逻辑完全在应用服务器端实现(web应用程序)，客户端(浏览器)只需要浏览器即可进行业务处理

### TCP/IP五层协议   
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

## <span id='2.0'>2 socket(套接字)</span>
>网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。

- Socket的英文原义是“孔”或“插座”。作为BSD UNIX的进程通信机制，取后一种意思。通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机之间的通信。
- 将传输层及以下的网络协议封装，提供简单使用的接口(API)给应用层的软件，专门面向C/S架构模型设计的
- 三个参数：协议，本地地址，本地端口

### <span id='2.1'>2.1 套接字的连接过程</span>
1. 服务器监听：不指定具体的客户端套接字，处于等待连接的状态，实时监控网络状态
2. 客户端请求：指由客户端的套接字提出请求，目标是服务器端的套接字，需要指出服务器端套接字的地址和端口号
3. 连接确认：当服务器端套接字监听到客户端套接字的连接请求，就响应请求建立一个新的进程，并返回客户端服务器的套接字描述，当客户端确认描述，连接就正式建立，服务器端继续处于监听状态
![](https://baike.baidu.com/pic/socket/281150/0/d000baa1cd11728b45647b06cafcc3cec3fd2c4c?fr=lemma&ct=single)

### <span id='2.2'>2.2socket模块</span>
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

### <span id='2.3'>2.3 套接字(socket)函数</span>
#### 服务端 
- s.bind()       
	- 绑定(主机，端口号)到套接字 
- s.listen()    
	- 开始TCP监听
	- 必须制定最大连接数（操作系统同时能够链接的最大数目）
- s.accept()      
	- 被动接受TCP客户的连接，(阻塞式)等待连接到来(阻塞：无响应直到接受到连接请求)

#### 客户端
- s.connect()     
	- 主动初始化TCP服务器连接
- s.connec_ex()    
	- connect()函数的扩展版本，出错时返回出错码，不抛出异常

#### 公共用途
- s.recv()    
	- 接收TCP数据   
	- 不可接收'空'
- s.send()     
	- 发送TCP数据   
	- 待发送数量大于己端缓存剩余区空间时，数据丢失，不会发完
- s.sendall()    
	- 发送完整的TCP数据，循环调用s.send
	- 通常给数据加上报头将数据打包更安全可靠，不常用sendall

- s.recvfrom()        
	- 接收UDP数据  
- s.sendto()          
	- 发送UDP数据  
- s.getpeername()     
	- 连接到当前套接字的远端的地址  
- s.getsockname()     
	- 当前套接字的地址  
- s.getsockopt()      
	- 返回指定套接字的参数  
- s.setsockopt()      
	- 设置指定套接字的参数  
- s.close() 
	- 关闭套接字

#### 面向锁的套接字方法
- s.setblocking()     
	- 设置套接字的阻塞与非阻塞模式  
- s.settimeout()      
	- 设置阻塞套接字操作的超时时间  
- s.gettimeout()      
	- 得到阻塞套接字操作的超时时间  

#### 面向文件的套接字的函数
- s.fileno()          
	- 套接字的文件描述符  
- s.makefile()        
	- 创建一个与该套接字相关的文件  

### <span id='2.4'>2.4 基于TCP的套接字</span>
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

#### 出现OSError: [WinError 10048]
做测试的时候有可能会出现如下错误信息：

> OSError: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。

这个是由于你的服务端仍然存在四次挥手的time_wait状态在占用地址的状态

>其中原理有可能是如下几种，请自行了解：
1. tcp三次握手，四次挥手 
2. syn洪水攻击 
3. 服务器高并发情况下会有大量的time_wait状态的优化方法

解决办法：
- 加入一条socket配置，在任务结束后重用ip和端口，需要在可以正常运行服务端的时候就使用           

	```python
	phone=socket(AF_INET,SOCK_STREAM)
	phone.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
	phone.bind(('127.0.0.1',8080))
	```

- 发现系统存在大量TIME_WAIT状态的连接，通过调整linux内核参数解决    

	```python
	vi /etc/sysctl.conf
	
	# 编辑文件，加入以下内容：
	net.ipv4.tcp_syncookies = 1
	net.ipv4.tcp_tw_reuse = 1
	net.ipv4.tcp_tw_recycle = 1
	net.ipv4.tcp_fin_timeout = 30
	 
	# 然后执行 /sbin/sysctl -p 让参数生效。
	 
	net.ipv4.tcp_syncookies = 1 
	# 表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
	
	net.ipv4.tcp_tw_reuse = 1 
	# 表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
	
	net.ipv4.tcp_tw_recycle = 1 
	# 表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭。
	
	net.ipv4.tcp_fin_timeout 
	# 修改系統默认的 TIMEOUT 时间
	```

### <span id='2.5'>2.5 粘包</span>
- 服务端    

	```python
	from socket import *
	import subprocess
	
	ip_port=('127.0.0.1',8080)
	
	server=socket(AF_INET,SOCK_STREAM)
	server.bind(ip_port)
	server.listen(5)
	
	while True:
	    conn,addr=tcp_socket_server.accept()
	    print('客户端',addr)
	
	    while True:
	        cmd=conn.recv(1024)
	        if not cmd:break
	        res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
	                         stdout=subprocess.PIPE,
	                         stdin=subprocess.PIPE,
	                         stderr=subprocess.PIPE)
	
	        stderr=act_res.stderr.read()
	        stdout=act_res.stdout.read()
	        conn.send(stderr)
	        conn.send(stdout)
	```

- 客户端    

	```python
	import socket
	ip_port=('127.0.0.1',8080)
	
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	res=s.connect_ex(ip_port)
	
	while True:
	    msg=input('>>: ').strip()
	    if not msg:continue
	    if msg == 'quit':break
	
	    s.send(msg.encode('utf-8'))
	    data=s.recv(1024)
	
	    print(data.decode('utf-8'))
	```

- 上面简单实现了一个远程cmd命令行，运行时如果使用返回较多信息的命令（如ipconfig -all）时会发生粘包：
	- 上一条命令返回的结果不完整，下一条命令返回了上一条命令未完内容

![](https://github.com/fangmingc/ChuannBlog/blob/master/Intermediate_Python/base/%E7%B2%98%E5%8C%85%E5%8E%9F%E7%90%86.png)

#### 粘包现象解释
- 粘包问题主要是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的。
- socket的命令均是对操作系统发出的请求，并不能直接建立链接、收发数据等等这些功能。
- 其中收发数据均是从系统的缓存中读取和发送。
- socket的recv和send指定的字节大小都是从操作系统中读取和写入。
- 如果缓存中保存的数据大于recv指定的字节大小，就会导致收不全数据；或者保存的数据不止一条，但recv远大于缓存的数据，就会将所有数据都接收；以上两种称之为粘包现象。

#### 关于tcp和udp协议
> TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务。收发两端（客户端和服务器端）都要有一一成对的socket，因此，发送端为了将多个发往接收端的包，更有效的发到对方，使用了优化方法（Nagle算法），将多次间隔较小且数据量小的数据，合并成一个大的数据块，然后进行封包。这样，接收端，就难于分辨出来了，必须提供科学的拆包机制。 即面向流的通信是无消息保护边界的。

> UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的，提供高效率服务。不会使用块的合并优化算法，, 由于UDP支持的是一对多的模式，所以接收端的skbuff(套接字缓冲区）采用了链式结构来记录每一个到达的UDP包，在每个UDP包中就有了消息头（消息来源地址，端口等信息），这样，对于接收端来说，就容易进行区分处理了。 即面向消息的通信是有消息保护边界的。

> tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），那也不是空消息，udp协议会帮你封装上消息头。

#### 粘包条件
- 发送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据了很小，会合到一起，产生粘包）
- 接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包） 

#### 补充
- 为何tcp是可靠传输，udp是不可靠传输      
	- tcp发送和接收消息是会进行确认的（三次握手，四次挥手）
	- tcp在数据传输时，发送端先把数据发送到自己的缓存中，然后协议控制将缓存中的数据发往对端，对端返回一个ack=1，发送端则清理缓存中的数据，对端返回ack=0，则重新发送数据，所以tcp是可靠的。而udp发送数据，对端是不会返回确认信息的，因此不可靠
- send(字节流)和recv(1024)及sendall
	- recv里指定的1024意思是从缓存里一次拿出1024个字节的数据
	- send的字节流是先放入己端缓存，然后由协议控制将缓存内容发往对端，如果待发送的字节流大小大于缓存剩余空间，那么数据丢失，用sendall就会循环调用send，数据不会丢失

#### 粘包的解决方案
- 核心原理
针对粘包因为接收方不知道消息之间的界限，在发送消息的时候事先声明消息有多长，接收时先收消息长度，再收数据即可。
- 具体实施
	- 发送端
		1. 制作报头
		报头可以包含数据长度，MD5校验值，数据类型等信息
		2. 发送报头长度
		将报头用json或其他序列化模块序列化成字符串，用struct模块将序列化后的报头长度制作成固定长度(通常4个字节足以)的bytes发送过去
		3. 发送报头
		4. 发送数据
	- 接收端
		1. 接收报头长度
		接收固定长度(与发送端约定好的长度)的数据，使用struct模块解析出报头长度
		2. 接收报头
		接收上一步解析出的报头长度的数据，使用相应的序列化模块反序列化得到报头
		3. 接收数据
		从上一步中的报头中的信息取出数据长度，按照相应长度接收
- 实例   
	- 服务端     
	
		```python
		from socket import *
		import subprocess
		import hashlib
		import json
		import struct
		
		servers = socket(AF_INET, SOCK_STREAM)
		servers.bind(('127.0.0.1', 20000))
		servers.listen(5)
		print('The server is started...')
		
		# Link loop
		while True:
		    print('Waiting for client links...')
		    connection, client_address = servers.accept()
		    print('Has been linked %s' % client_address[0])
		
		    # Communication cycle
		    while True:
		        try:
		            cmd = connection.recv(1024)
		            if not cmd:
		                break
		
		            # Execute the client's command
		            result = subprocess.Popen(cmd.decode('utf-8'), shell=True,
		                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		            stdout = result.stdout.read()
		            stderr = result.stderr.read()
		
		            md5_obj = hashlib.md5()
		            md5_obj.update(stdout + stderr)
		
		            #  Make the header
		            header_dic = {
		                'total_size': len(stdout) + len(stderr),
		                'md5': md5_obj.hexdigest()}
		            header_bytes = json.dumps(header_dic).encode('utf-8')
		
		            # Make the fixed length of header
		            header_length = struct.pack('i', len(header_bytes))
		
		            # Send the fixed length of header
		            connection.send(header_length)
		
		            # Send the header
		            connection.send(header_bytes)
		
		            # Send the result
		            connection.send(stdout)
		            connection.send(stderr)
		
		        except Exception as error_info:
		            print(error_info)
		            break
		
		    connection.close()
		
		# servers.close()
		```
	
	- 客户端   

		```python
		from socket import *
		import struct
		import json
		import hashlib
		
		client = socket(AF_INET, SOCK_STREAM)
		client.connect(('127.0.0.1', 20000))
		
		while True:
		    cmd = input('[+_+] ').strip()
		    if not cmd:
		        continue
		
		    client.send(cmd.encode('utf-8'))
		
		    # Receive the fixed length of header
		    header_length = struct.unpack('i', client.recv(4))
		
		    # Receive the header
		    header_bytes = client.recv(header_length[0])
		    header_dic = json.loads(header_bytes.decode('utf-8'))
		
		    # Receive the message
		    total_size = header_dic['total_size']
		    receive_size = 0
		    total_data = b''
		    while receive_size < total_size:
		        receive_data = client.recv(1024)
		        receive_size += len(receive_data)
		        total_data += receive_data
		
		    md5_obj = hashlib.md5()
		    md5_obj.update(total_data)
		    if md5_obj.hexdigest() == header_dic['md5']:
		        print(total_data.decode('gbk'))
		    else:
		        print('Data is not complete.')
		```

### <span id='2.6'>2.6 基于UDP的套接字</span>


### <span id='2.7'>2.7 socketserver模块</span>
- 基于tcp的套接字，关键是两个循环，一个链接循环，一个通信循环
- socketserver模块中分两大类：
	- server类（解决链接问题）
	- request类（解决通信问题）

- 类的继承关系图：       
[基于进程](https://chuann.cc/Intermediate_Python/threading.png)
[基于线程](https://chuann.cc/Intermediate_Python/forking.png)

- 服务端
	
	```python
	import socketserver
	
	
	class MyServer(socketserver.BaseRequestHandler):
	
	    def handle(self):
	        print(self.request)
	        while True:
	            try:
	                cmd = self.request.recv(1024)
	                if not cmd:
	                    break
	                self.request.send(cmd.upper())
	            except Exception as error_info:
	                print(error_info)
	                break
	        self.request.close()
	
	if __name__ == '__main__':
	    server = socketserver.ThreadingTCPServer(('192.168.20.76', 8000), MyServer)
	    server.allow_reuse_address = True
	    server.serve_forever()
	```

- 客户端
	
	```python
	import socket
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('192.168.20.76', 8000))
	
	while True:
	    msg = input('[+_+] ').strip()
	    if not msg:
	        continue
	    client.send(msg.encode('utf-8'))
	    result = client.recv(1024)
	    print(result.decode('utf-8'))
	```


## <span id='3.0'>3 练习：ftp文件上传下载</span>
[GitHub地址](https://chuann.cc/Intermediate_Python/my_ftp)


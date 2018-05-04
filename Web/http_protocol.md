## http协议
- http协议是超文本传输协议(HyperText Transfer Protocol)的简称，是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。          
- HTTP是一个**基于TCP/IP**通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。        

>HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。它于1990年提出，经过几年的使用与发展，得到不断地完善和扩展。目前在WWW中使用的是HTTP/1.0的第六版，HTTP/1.1的规范化工作正在进行之中，而且HTTP-NG(Next Generation of HTTP)的建议已经提出。

- HTTP协议工作于客户端-服务端架构为上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。Web服务器根据接收到的请求后，向客户端发送响应信息。

- http的特点：
	- 无连接-----------1.1已经更新，连接时间默认3s，可自定义
	- 无状态-----------使用cookie&session解决

- http协议格式
	- 请求协议（request）
		- 请求首行：方法，url，协议版本
			- eg：GET http://127.0.01:8080/path/blog HTTP/1.1
		- 请求头：
			- User-Agent:发出请求的设备信息，包含设备操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等
			- Accept:可以接收的文件格式
				- \*/*:任何文件
				- text/html：html文本文件
				- 其他
					- application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng....
			- Accept-Encoding:可以接受的压缩格式
			- Connection:keep-alive 持久连接，即TCP链接默认不关闭，可以被多个请求复用，不用声明
				- 客户端和服务器发现对方一段时间没有活动，就可以主动关闭连接。
				- 不过，规范的做法是，客户端在最后一个请求时，发送Connection: close，明确要求服务器关闭TCP连接。
			- Host:指定服务器的域名，可以将请求发往同一台服务器上的不同网站
			- Cookie/Session:浏览器缓存,不是http协议规定的
		- 空行：用于分割
		- 请求体
			- GET请求此处为空，其数据跟在请求首行的URL之后以键值对的形式与URL用?分割
			- POSt请求使用此种方式，格式为键值对
	- 响应协议（response）
		- 响应头
			- 响应首行：协议 状态码
				- HTTP/1.1 200 OK
			- 响应源信息
				- Content-Type: 响应正文的格式
				- Content-Encoding：说明数据的压缩方式
				- Connection:keep-alive 持久连接，即TCP链接默认不关闭
		- 空行
		- 响应正文
			- 通常为html文档
			- 也可是二进制文件，如图片，视频等







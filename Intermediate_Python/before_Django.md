## Before Django
### socket
- socket本质上传输都是字节
	- 浏览器：
	- web服务器：
	
	- MySQL客户端(pymysql)：
	- MySQL服务端(mysqld)：

### http协议
- 浏览器发送GET请求数据格式
	- socket.sendall(b'GET /index/?name=xx&age=12 http1.1\r\nAccept:text/html\r\nCookie:sdjfvhwbrhjx\r\n\r\n')
	- 以\r\n分割的字符串
	- 不具有请求体
- 浏览器发送PSOT请求数据格式
	- socket.sendall(b'POST /index/?name=xx&age=12 http1.1\r\nAccept:text/html\r\nCookie:sdjfvhwbrhjx\r\n\r\nabc=123&bbb=23&sad=12k')
	- 具有\r\n的字符串
	- 具有请求体
	- django加工POST请求后数据：abc=123&bbb=23
		- request.GET.get('name')
		- request.POST.get('bbb')
	- django加工不了非POST请求数据：{abc:123,bbb:23}
		- request.POST为空
		- request.body可以获取b'{abc:123,bbb:23}'
	- django如何判断浏览器发来的数据是否是可以向request.POST解析的？
		- 读取请求头的content-type，当格式为application/x-www-from-urlencoded时，django认为可以解析

- HTTP协议
	- 请求头和请求体分割：\r\n\r\n
	- 请求体之间：\r\n
	- GET无请求体
	- 无状态，短连接：socket请求响应断开
	- 请求头的意义，需要记住几个
		- user-agent：来源，不同的设备和操作系统不同
		- referer：防盗链，
		- content-type：请求体格式

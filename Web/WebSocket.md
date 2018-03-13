## WebSocket
- Http，单向无状态
	- 轮询
		- 客户端(浏览器)定时向服务器请求数据，服务器收到一个请求返回一个响应
	- 长轮询
		- 服务器接收到请求不立即返回响应，而是等待一个超时时间，超时返回响应，客户端根据响应再发一次请求
		- 超时时间之内，客户端可以再次发送请求，这个请求会重置超时时间并立即返回响应
- WebSocket，双工通道
	- 客户端-发起
	- 服务端-连接
	- 适用于需要实时显示数据的场景

### 流程解析
- 创建连接
	- 服务端启动，监听请求
	- 客户端向服务端发起请求，请求头中带有一串随机字符串（握手信息）
	- 服务端获取到请求，将随机字符串sha1加密，再用base64加密返回给客户端
		- 请求和响应的【握手】信息需要遵循规则：
		- 从请求【握手】信息中提取 Sec-WebSocket-Key
		- 利用magic_string 和 Sec-WebSocket-Key 进行hmac1加密，再进行base64加密
		- 将加密结果响应给客户端
			- 注：magic string为：258EAFA5-E914-47DA-95CA-C5AB0DC85B11
	- 客户端收到握手信息，建立连接成功
	- 请求的握手信息

		```
		GET /chatsocket HTTP/1.1
		Host: 127.0.0.1:8002
		Connection: Upgrade
		Pragma: no-cache
		Cache-Control: no-cache
		Upgrade: websocket
		Origin: http://localhost:63342
		Sec-WebSocket-Version: 13
		Sec-WebSocket-Key: mnwFxiOlctXFN/DeMt1Amg==
		Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits
		...
		...
		```
	- 提取Sec-WebSocket-Key值并加密

		```python
		import socket
		import base64
		import hashlib
		 
		def get_headers(data):
		    """
		    将请求头格式化成字典
		    :param data:
		    :return:
		    """
		    header_dict = {}
		    data = str(data, encoding='utf-8')
		 	
			# http协议是以\r\n分隔的
		    for i in data.split('\r\n'):
		        print(i)
			# 连续的两个\r\n\r\n代表请求头和请求体的分隔
		    header, body = data.split('\r\n\r\n', 1)
		    header_list = header.split('\r\n')
		    for i in range(0, len(header_list)):
		        if i == 0:
					# 获取请求首行中带有的请求方法，url，使用的http协议版本
		            if len(header_list[i].split(' ')) == 3:
		                header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
		        else:
					# 把其他请求头一并处理置入字典
		            k, v = header_list[i].split(':', 1)
		            header_dict[k] = v.strip()
		    return header_dict
		 
		# 启动服务端socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('127.0.0.1', 8002))
		sock.listen(5)
		 
		conn, address = sock.accept()
		data = conn.recv(1024)
		headers = get_headers(data) # 提取请求头信息

		# 对请求头中的sec-websocket-key进行加密
		magic_string = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
		value = headers['Sec-WebSocket-Key'] + magic_string
		ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())

		# 设置响应信息
		response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
		      "Upgrade:websocket\r\n" \
		      "Connection: Upgrade\r\n" \
		      "Sec-WebSocket-Accept: %s\r\n" \
		      "WebSocket-Location: ws://%s%s\r\n\r\n"
		response_str = response_tpl % (ac.decode('utf-8'), headers['Host'], headers['url'])

		# 响应【握手】信息
		conn.send(bytes(response_str, encoding='utf-8'))
		...
		...
		```

- 收发数据
	- 数据格式
		- Payload len，本身占7位，最大数字127
			- 如果小于等于125，表示无延长，头信息已结束
			- 如果等于126，表示延长16位
			- 如果等于127，表示延长64位
		- MASK，本身占一位
			- 表示是否启用mask加密，对于客户端-服务端消息通常都是启用的
			- 当启用加密，会读取Payload(有延长的话延长也算)之后的4字节(32位)，这是加密使用的key，也可以用来解密
		- Payload Data
			- 在之后的就是真实数据了，不过通常是加密后的数据
		- 详细可参考[RFC6455文档](https://tools.ietf.org/html/rfc6455#section-5.2)

	```
	 0                   1                   2                   3
	 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
	+-+-+-+-+-------+-+-------------+-------------------------------+
	|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
	|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
	|N|V|V|V|       |S|             |   (if payload len==126/127)   |
	| |1|2|3|       |K|             |                               |
	+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
	|     Extended payload length continued, if payload len == 127  |
	+ - - - - - - - - - - - - - - - +-------------------------------+
	|                               |Masking-key, if MASK set to 1  |
	+-------------------------------+-------------------------------+
	| Masking-key (continued)       |          Payload Data         |
	+-------------------------------- - - - - - - - - - - - - - - - +
	:                     Payload Data continued ...                :
	+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
	|                     Payload Data continued ...                |
	+---------------------------------------------------------------+
	```

- 示例
	- 基于Python socket实现的WebSocket服务端：

	```python
	import socket
	import base64
	import hashlib
	
	def get_headers(data):
	    """
	    将请求头格式化成字典
	    :param data:
	    :return:
	    """
	    header_dict = {}
	    data = str(data, encoding='utf-8')
		
		# 连续的两个\r\n\r\n代表请求头和请求体的分隔
	    header, body = data.split('\r\n\r\n', 1)
	    header_list = header.split('\r\n')
	    for i in range(0, len(header_list)):
	        if i == 0:
				# 获取请求首行中带有的请求方法，url，使用的http协议版本
	            if len(header_list[i].split(' ')) == 3:
	                header_dict['method'], header_dict['url'], header_dict['protocol'] = header_list[i].split(' ')
	        else:
				# 把其他请求头一并处理置入字典
	            k, v = header_list[i].split(':', 1)
	            header_dict[k] = v.strip()
	    return header_dict
	
	def send_msg(conn, msg_bytes):
	    """
	    WebSocket服务端向客户端发送消息
	    :param conn: 客户端连接到服务器端的socket对象,即： conn,address = socket.accept()
	    :param msg_bytes: 向客户端发送的字节
	    :return:
	    """
	    import struct
	
	    token = b"\x81"
	    length = len(msg_bytes)
	    if length < 126:
	        token += struct.pack("B", length)
	    elif length <= 0xFFFF:
	        token += struct.pack("!BH", 126, length)
	    else:
	        token += struct.pack("!BQ", 127, length)
	
	    msg = token + msg_bytes
	    conn.send(msg)
	    return True
	
	def run():
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    sock.bind(('127.0.0.1', 8003))
	    sock.listen(5)
	
	    conn, address = sock.accept()
	    data = conn.recv(1024)
	    headers = get_headers(data)
	    response_tpl = "HTTP/1.1 101 Switching Protocols\r\n" \
	                   "Upgrade:websocket\r\n" \
	                   "Connection:Upgrade\r\n" \
	                   "Sec-WebSocket-Accept:%s\r\n" \
	                   "WebSocket-Location:ws://%s%s\r\n\r\n"
	
	    value = headers['Sec-WebSocket-Key'] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
	    ac = base64.b64encode(hashlib.sha1(value.encode('utf-8')).digest())
	    response_str = response_tpl % (ac.decode('utf-8'), headers['Host'], headers['url'])
	    conn.send(bytes(response_str, encoding='utf-8'))
	
	    while True:
	        try:
	            info = conn.recv(8096)
	        except Exception as e:
	            info = None
	        if not info:
	            break
	        payload_len = info[1] & 127
	        if payload_len == 126:
	            extend_payload_len = info[2:4]
	            mask = info[4:8]
	            decoded = info[8:]
	        elif payload_len == 127:
	            extend_payload_len = info[2:10]
	            mask = info[10:14]
	            decoded = info[14:]
	        else:
	            extend_payload_len = None
	            mask = info[2:6]
	            decoded = info[6:]
	
	        bytes_list = bytearray()
	        for i in range(len(decoded)):
	            chunk = decoded[i] ^ mask[i % 4]
	            bytes_list.append(chunk)
	        body = str(bytes_list, encoding='utf-8')
	        print("请求数据", body)
	        body = body + "响应"
	        send_msg(conn, body.encode('utf-8'))
	
	    sock.close()
	
	if __name__ == '__main__':
	    run()
	```
	- 利用JavaScript类库实现客户端

	```html
	<!DOCTYPE html>
	<html>
	<head lang="en">
	    <meta charset="UTF-8">
	    <title></title>
	</head>
	<body>
	    <div>
	        <input type="text" id="txt"/>
	        <input type="button" id="btn" value="提交" onclick="sendMsg();"/>
	        <input type="button" id="close" value="关闭连接" onclick="closeConn();"/>
	    </div>
	    <div id="content"></div>
	 
	<script type="text/javascript">
	    var socket = new WebSocket("ws://127.0.0.1:8003/chatsocket");
	 
	    socket.onopen = function () {
	        /* 与服务器端连接成功后，自动执行 */
	 
	        var newTag = document.createElement('div');
	        newTag.innerHTML = "【连接成功】";
	        document.getElementById('content').appendChild(newTag);
	    };
	 
	    socket.onmessage = function (event) {
	        /* 服务器端向客户端发送数据时，自动执行 */
	        var response = event.data;
	        var newTag = document.createElement('div');
	        newTag.innerHTML = response;
	        document.getElementById('content').appendChild(newTag);
	    };
	 
	    socket.onclose = function (event) {
	        /* 服务器端主动断开连接时，自动执行 */
	        var newTag = document.createElement('div');
	        newTag.innerHTML = "【关闭连接】";
	        document.getElementById('content').appendChild(newTag);
	    };
	 
	    function sendMsg() {
	        var txt = document.getElementById('txt');
	        socket.send(txt.value);
	        txt.value = "";
	    }
	    function closeConn() {
	        socket.close();
	        var newTag = document.createElement('div');
	        newTag.innerHTML = "【关闭连接】";
	        document.getElementById('content').appendChild(newTag);
	    }
	 
	</script>
	</body>
	</html>
	```


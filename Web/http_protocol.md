## http协议
http协议是超文本传输协议(HyperText Transfer Protocol)的简称，是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。          
HTTP是一个**基于TCP/IP**通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。        

>HTTP是一个属于应用层的面向对象的协议，由于其简捷、快速的方式，适用于分布式超媒体信息系统。它于1990年提出，经过几年的使用与发展，得到不断地完善和扩展。目前在WWW中使用的是HTTP/1.0的第六版，HTTP/1.1的规范化工作正在进行之中，而且HTTP-NG(Next Generation of HTTP)的建议已经提出。

- HTTP协议工作于客户端-服务端架构为上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。Web服务器根据接收到的请求后，向客户端发送响应信息。

http的特点：
	- 无连接-----------1.1已经更新，连接时间默认3s，可自定义
	- 无状态-----------使用cookie&session解决

- http协议格式
	- 请求协议（request）
		- 请求首行：方法，url，协议版本
			- eg：GET http://127.0.01:8080/path/blog HTTP/1.1
		- 请求头：

			```
			Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
			Accept-Encoding:gzip, deflate, br
			Accept-Language:zh-CN,zh;q=0.8
			Cache-Control:max-age=0
			Connection:keep-alive
			Cookie:BAIDUID=7E66B164F4B2989A816152F5960C0EF0:FG=1; PSTM=1507796505; BIDUPSID=D7A0800EC577F886EC849DEE2B09675E; ispeed_lsm=2; BDUSS=5rZ3YyZ09uVkNUWGR1ZVo4a05Uc21OU2cxWjM1d1dsdnRzQ3NSQWFGRVlIQXhhSVFBQUFBJCQAAAAAAAAAAAEAAAB0XdQ01LXD8LXEvccAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABiP5FkYj-RZak; pgv_pvi=6320977920; pgv_si=s6795073536; BD_CK_SAM=1; PSINO=1; H_PS_645EC=53e3w8qMtgP3wtPKpRKgdsdslAz00prkBU%2FYqB7JlOyJyBFIkirirUcQ6CM; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1459_21118_17001; BD_UPN=12314753; sug=3; sugstore=1; ORIGIN=2; bdime=0
			Host:www.baidu.com
			Upgrade-Insecure-Requests:1
			User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36
			```
		- 空行：用于分割
		- 请求体
			- GET请求此处为空，其数据跟在请求首行的URL之后以键值对的形式与URL用?分割
			- POSt请求使用此种方式，格式为键值对

			```
			Bdpagetype:2
			Bdqid:0xecac837c0000bbcc
			Bduserid:886332788
			Cache-Control:private
			Connection:Keep-Alive
			Content-Encoding:gzip
			Content-Type:text/html;charset=utf-8
			Date:Thu, 19 Oct 2017 01:59:29 GMT
			Expires:Thu, 19 Oct 2017 01:59:29 GMT
			Server:BWS/1.1
			Set-Cookie:BDSVRTM=162; path=/
			Set-Cookie:BD_HOME=1; path=/
			Set-Cookie:H_PS_PSSID=1459_21118_17001; path=/; domain=.baidu.com
			Strict-Transport-Security:max-age=172800
			Transfer-Encoding:chunked
			X-Ua-Compatible:IE=Edge,chrome=1
			```

	- 响应协议（response）
		- 响应行
			- 协议 状态码
			- HTTP/1.1 200 OK
		- 消息报头
			- 'ALLUSERSPROFILE': 'C:\\ProgramData', 
			- 'APPDATA': 'C:\\Users\\fangm\\AppData\\Roaming', 
			- 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
			- 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
			- 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
			- 'COMPUTERNAME': 'CHUCK', 
			- 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 
			- 'CONFIGSETROOT': 'C:\\Windows\\ConfigSetRoot', 
			- 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
			- 'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
			- 'HOMEDRIVE': 'C:', 
			- 'HOMEPATH': '\\Users\\fangm', 
			- 'LOCALAPPDATA': 'C:\\Users\\fangm\\AppData\\Local', 
			- 'LOGONSERVER': '\\\\CHUCK', 
			- 'NUMBER_OF_PROCESSORS': '8', 
			- 'ONEDRIVE': 'C:\\Users\\fangm\\OneDrive', 
			- 'OS': 'Windows_NT', 
			- 'PATH': 'D:\\Python36\\Scripts\\;D:\\Python36\\;C:\\Program Files (x86)\\Intel\\iCLS Client\\;C:\\Program Files\\Intel\\iCLS Client\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\IPT;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\IPT;D:\\Python27;D:\\Python27\\Scripts;D:\\Program Files\\Git;D:\\mysql-5.7.19-winx64\\bin;D:\\Program Files (x86)\\Vim\\vim80;C:\\Users\\fangm\\AppData\\Local\\Microsoft\\WindowsApps;', 
			- 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 
			- 'PROCESSOR_ARCHITECTURE': 'AMD64', 
			- 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel', 
			- 'PROCESSOR_LEVEL': '6', 
			- 'PROCESSOR_REVISION': '9e09', 
			- 'PROGRAMDATA': 'C:\\ProgramData', 
			- 'PROGRAMFILES': 'C:\\Program Files', 
			- 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
			- 'PROGRAMW6432': 'C:\\Program Files', 
			- 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 
			- 'PUBLIC': 'C:\\Users\\Public', 
			- 'PYCHARM_HOSTED': '1', 
			- 'PYTHONIOENCODING': 'UTF-8', 
			- 'PYTHONPATH': 'E:\\Excellence\\Python', 
			- 'PYTHONUNBUFFERED': '1', 
			- 'SESSIONNAME': 'Console', 
			- 'SYSTEMDRIVE': 'C:', 
			- 'SYSTEMROOT': 'C:\\Windows', 
			- 'TEMP': 'C:\\Users\\fangm\\AppData\\Local\\Temp', 
			- 'TMP': 'C:\\Users\\fangm\\AppData\\Local\\Temp', 
			- 'USERDOMAIN': 'CHUCK', 
			- 'USERDOMAIN_ROAMINGPROFILE': 'CHUCK', 
			- 'USERNAME': 'fangm', 
			- 'USERPROFILE': 'C:\\Users\\fangm', 
			- 'WINDIR': 'C:\\Windows', 
			- 'SERVER_NAME': 'chuck', 
			- 'GATEWAY_INTERFACE': 'CGI/1.1', 
			- 'SERVER_PORT': '8080', 
			- 'REMOTE_HOST': '', 
			- 'CONTENT_LENGTH': '', 
			- 'SCRIPT_NAME': '', 
			- 'SERVER_PROTOCOL': 'HTTP/1.1', 
			- 'SERVER_SOFTWARE': 'WSGIServer/0.2', 
			- 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 
			- 'QUERY_STRING': '', 
			- 'REMOTE_ADDR': '127.0.0.1', 
			- 'CONTENT_TYPE': 'text/plain', 
			- 'HTTP_HOST': '127.0.0.1:8080', 
			- 'HTTP_CONNECTION': 'keep-alive', 
			- 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 
			- 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
			- 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
			- 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
			- 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.8', 
			- 'wsgi.input': <_io.BufferedReader name=492>, 
			- 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 
			- 'wsgi.version': (1, 0), 
			- 'wsgi.run_once': False, 
			- 'wsgi.url_scheme': 'http', 
			- 'wsgi.multithread': True, 
			- 'wsgi.multiprocess': False, 
			- 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>




		- 空行
		- 响应正文
		- 







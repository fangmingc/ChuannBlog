## reqeusts
```python
pip install requests
```

### 请求与响应
#### 基于GET请求
- url
	- URL字符串
- params
	- 字典
	- GET请求所带的参数
- headers
	- 字典
	- 请求头数据
- cookies
	- 字典
	- 请求发送的cookie
- allow_redirects
	- 布尔值
	- 当有重定向时，是否重定向

##### 高级参数
- verify
	- 布尔值
	- 是否启用SSL证书认证，但是会有警告信息
	- from requests.package import urllib3
	- urllib3.disable_warnings()
	- 禁用警告信息
- proxies
	- 字典
	- IP代理，{'http': 'http://IP:port'}
- timeout
	- 浮点数
	- 超时时间，发出请求等待响应的时间，超过时间则抛出异常
- auth
	- 字典或HTTPBasicAuth实例
	- 用于访问需要认证才可以获取内容的页面
- files
	- 文件句柄
	- 上传文件

#### 基于POST请求
- 其他与Get请求一致
- data
	- 字典
	- post提交的数据

#### 响应
- 无论是get或是post请求，都会有response，都是Response类的对象
	- status_code
		- 数字
		- 响应状态码
	- headers
		- CaseInsensitiveDict的实例
		- 响应头信息
	- content
		- 字符串
		- bytes类型的响应内容
		- iter_content(),二进制迭代器，可以一行行读取响应
	- text
		- 字符串
		- unicode类型的响应内容
	- history
		- 列表
		- 保存重定向到在本响应之前的响应(都是对象)
	- cookies
		- RequestsCookieJar的实例，具有类似字典的结构
		- 保存响应接收的cookies
	- encoding
		- 设置响应内容的编码格式，默认ISO-8859-1
	- json
		- 直接获取json格式数据

### 高级用法
####




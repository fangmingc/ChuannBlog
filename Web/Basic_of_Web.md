# Web基础

网络三要素
ip、端口、协议(应用层)

域名解析和绑定

## http协议
### URL
http://127.0.0.1:8800/blog/addBlog?username=yuan

协议：http
ip地址与端口：127.0.0.1:8800
url的路径（path）:blog/addBlog
get数据：username=yuan

### 请求协议
请求方式（从server端）：  
- get
- post


从浏览器---->服务器：
- url  
- 请求首行
- 请求头
- 换行
- 请求数据


如果这是一个get请求，将数据放入url
如果这是一个post请求，将数据放入请求数据


get请求：安全性差，数据量有限制
哪些是get请求（一般都是查询数据库操作）？
（通常默认使用get请求，非要用post也可以）
1. url访问server
2. 超链接访问即a标签



### 响应协议




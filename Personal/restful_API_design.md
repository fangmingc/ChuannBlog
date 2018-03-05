## restful API设计原则
- [原文](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
- 资源表现层状态转化
	- 资源就是URL，一个URL对应一个网络资源，这些网络资源都存在于网络上的服务器，本质上就是这些服务器上的数据
	- 资源有不同的表现形式，比如文本可以是txt,html,json等，图片可以是png，jpg等等，这些表现形式是用于客户端页面展示的
	- 状态转化指的是资源的状态可以通过显示，新增，修改，删除四个基本操作进行变化
	- 这种在客户端表现层对资源数据进行增删改查模式就称之为表现层状态转化(rest)
- 主要特点
	- 基本是按照请求方式的不同表示不同的操作类型
	- 因为是面向资源编程，URL一般都要是名词，请求的资源形式应该带上格式名
		- 如`https://example.org/api/zoos.json`
	- 过滤返回结果一般用URL传参
	- 返回结果应该带上通过状态码
	- 接口url可以设在域名的路径设置，也可以是在另外一个域名下
1. API接口路径
	- 放置在另外一个域名
		- https://api.example.com
		- 会产生跨域
	- 放置于路径
		- https://example.org/api/
2. API的版本号
	- 放置在路径
		- https://api.example.com/v1/
	- 放置在域名
		- https://v1.example.com/api
	- 放置头信息，通过增加请求头即可
		- 因为发送了额外的请求头，会产生大量复杂请求
3. 路径（Endpoint）
	- 在RESTful架构中，每个网址代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应。
	- 一般来说，数据库中的表都是同种记录的"集合"（collection），所以API中的名词也应该使用复数。
	- eg:举例来说，有一个API提供动物园（zoo）的信息，还包括各种动物和雇员的信息，则它的路径应该设计成下面这样。
		- https://api.example.com/v1/zoos
		- https://api.example.com/v1/animals
		- https://api.example.com/v1/employees
4. 对于资源的具体操作类型，由HTTP动词表示
	- GET（SELECT）：从服务器取出资源（一项或多项）。
	- POST（CREATE）：在服务器新建一个资源。
	- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
	- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
	- DELETE（DELETE）：从服务器删除资源。
		- 示例：
			- GET /zoos：列出所有动物园
			- POST /zoos：新建一个动物园
			- GET /zoos/ID：获取某个指定动物园的信息
			- PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
			- PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
			- DELETE /zoos/ID：删除某个动物园
			- GET /zoos/ID/animals：列出某个指定动物园的所有动物
			- DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
5. 如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。
	- 常见参数
		- ?limit=10：指定返回记录的数量
		- ?offset=10：指定返回记录的开始位置。
		- ?page=2&per_page=100：指定第几页，以及每页的记录数。
		- ?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
		- ?animal_type_id=1：指定筛选条件
	- 参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复
		- 比如，GET /zoo/ID/animals 与 GET /animals?zoo_id=ID 的含义是相同的。
6. 服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）
	- 2xx
		- 200 （成功）  服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页。
	- 3xx
		- 301 （永久移动）  请求的网页已永久移动到新位置。
		- 302 （临时移动）  服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。  
	- 4xx
		- 400   （错误请求） 服务器不理解请求的语法。
		- 401   （未授权） 请求要求身份验证。 对于需要登录的网页，服务器可能返回此响应。  
		- 403   （禁止） 服务器拒绝请求。  
		- 404   （未找到） 服务器找不到请求的网页。 
		- 408   （请求超时）  服务器等候请求时发生超时。  
	- 5xx
		- 500   （服务器内部错误）  服务器遇到错误，无法完成请求。  
	- [wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
7. 如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可

	```js
	{
	    error: "Invalid API key"
	}
	```

8. 针对不同操作，服务器向用户返回的结果应该符合以下规范
	- GET /collection：返回资源对象的列表（数组）
	- GET /collection/resource：返回单个资源对象
	- POST /collection：返回新生成的资源对象
	- PUT /collection/resource：返回完整的资源对象
	- PATCH /collection/resource：返回完整的资源对象
	- DELETE /collection/resource：返回一个空文档
9. Hypermedia API
	- RESTful API最好做到Hypermedia，即返回结果中提供链接，连向其他API方法，使得用户不查文档，也知道下一步应该做什么。
	- 比如，当用户向api.example.com的根目录发出请求，会得到这样一个文档。

		```js
		{"link": {
		  "rel":   "collection https://www.example.com/zoos",
		  "href":  "https://api.example.com/zoos",
		  "title": "List of zoos",
		  "type":  "application/vnd.yourformat+json"
		}}
		```
	- 文档中有一个link属性，用户读取这个属性就知道下一步该调用什么API了。rel表示这个API与当前网址的关系（collection关系，并给出该collection的网址），href表示API的路径，title表示API的标题，type表示返回类型

10. 其他
	1. API的身份认证应该使用[OAuth 2.0](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)框架。
	2. 服务器返回的数据格式，应该尽量使用JSON，避免使用XML




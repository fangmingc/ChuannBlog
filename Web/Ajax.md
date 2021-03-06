## Ajax
前后端数据交互的核心。


### json
#### 什么是json(JavaScript Object Notation)
- 是一种轻量级的数据交换格式，不同编程语言写的程序之间的数据交换
- 它基于 ECMAScript (w3c制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。
- 简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

#### json和js
- json类型是js数据类型的一个子集
- json只认双引号


### jquery实现的ajax
- 形式：$.ajax()
	- $.get()----指定type为get
	- $.post()----指定type为post

	```
	$.ajax({
		url:"",		# 请求的路径
		type:"",	# 请求的方式GET/POST
		data:{},	# 请求的数据
		contentType:"", 		# 客户端告诉服务器此次发送的数据格式，默认为application/x-www-form-urlencoded
		success: function(){}	# ajax请求正常时的回调函数
		error:{}	# 请求错误时的回调函数
	})
	```

#### contentType
- 在django框架中，服务器接收的http请求会将请求数据通过wsgi协议，所有数据都会放在request.body
	- wsgi协议自带urlencoded解析，会将符合的数据解析到request.GET，request.POST，其他类型的数据wsgi不会自动解析
	- url尾部的数据会被解析到request.GET
	- 请求体的数据如已指定POST则解析到request.POST
- 常见类型
	- application/x-www-form-urlencoded
		- 127.0.0.1:8080/getajax/?name=egon&age=12
	- application/json
	- text/html
	- text/xml



### 基于JS实现的ajax
- 浏览器兼容性解决

	```js
	function createXMLHttpRequest() {
	    var xmlHttp;
	    // 适用于大多数浏览器，以及IE7和IE更高版本
	    try{
	        xmlHttp = new XMLHttpRequest();
	    } catch (e) {
	        // 适用于IE6
	        try {
	            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
	        } catch (e) {
	            // 适用于IE5.5，以及IE更早版本
	            try{
	                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	            } catch (e){}
	        }
	    }            
	    return xmlHttp;
	}
	```

#### 使用流程

1. 打开与服务器的连接（open方法）
	1. 当得到XMLHttpRequest对象后，就可以调用该对象的open()方法打开与服务器的连接了。
	2. open()方法的参数如下：`open(method, url, async)`
		- method：请求方式，通常为GET或POST；
		- url：请求的服务器地址，例如：/ajaxdemo1/AServlet，若为GET请求，还可以在URL后追加参数；
		- async：这个参数可以不给，默认值为true，表示异步请求；

	```js
	var xmlHttp = createXMLHttpRequest();
	xmlHttp.open("GET", "/ajax_get/?a=1", true);　
	```

2. 发送请求
	- 如果需要添加头信息，则可以在此处添加
		- xmlHttp.setRequestHeader("X-CSRFTokenh",'当前表单的csrf输入框的值');
	- 当使用open打开连接后，就可以调用XMLHttpRequest对象的send()方法发送请求了。
	- send()方法的参数为POST请求参数，即对应HTTP协议的请求体内容，若是GET请求，需要在open方法中URL后连接参数。
	- 没有参数，需要给出null为参数！若不给出null为参数，可能会导致FireFox浏览器不能正常发送请求！
		- `xmlHttp.send(null);`

3. 接收服务器响应
	- XMLHttpRequest对象有一个onreadystatechange事件，它会在XMLHttpRequest对象的状态发生变化时被调用。
	- XMLHttpRequest对象的状态有五种
		0. 初始化未完成状态，只是创建了XMLHttpRequest对象，还未调用open()方法；
		1. 请求已开始，open()方法已调用，但还没调用send()方法；
		2. 请求发送完成状态，send()方法已调用；
		3. 开始读取服务器响应；
		4. 读取服务器响应结束。 
	- onreadystatechange事件会在状态1，2，3，4引发
		- 这段代码会执行四次`xmlHttp.onreadystatechange = function() {alert('hello');};`
	- 但通常我们只关心最后一种状态，即读取服务器响应结束时，客户端才会做出改变。
		- 通过XMLHttpRequest对象的readyState属性来得到XMLHttpRequest对象的状态。
		- 我们还要关心服务器响应的状态码是否为200，其服务器响应为404，或500，那么就表示请求失败了。通过XMLHttpRequest对象的status属性得到服务器的状态码。
		- 还需要获取到服务器响应的内容，可以通过XMLHttpRequest对象的responseText得到服务器响应内容。

	```js
	xmlHttp.onreadystatechange = function() {
	    if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
	        alert(xmlHttp.responseText);    
	    }
	};
	```

- POST请求需要设置请求头：
	- xmlHttp.setRequestHeader(“Content-Type”, “application/x-www-form-urlencoded”)；
	- 注意 :form表单会默认这个键值对不设定，Web服务器会忽略请求体的内容。
- 使用JS制作的ajax在django中无法通过request.is_ajax()的认证，因为缺少头信息（X-Requested-With）
	- 可以手动添加元信息xmlHttp.setRequestHeader("X-Requested-With",'XMLHttpRequest');



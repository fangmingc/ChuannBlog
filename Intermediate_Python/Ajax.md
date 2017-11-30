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


##### 常见类型
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


### jsonP
为了突破同源策略的一种方式

- 同源策略
	- 同源策略（Same origin policy）是一种约定，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，则浏览器的正常功能可能都会受到影响。可以说Web是构建在同源策略基础之上的，浏览器只是针对同源策略的一种实现。
	- RL由协议、域名、端口和路径组成，如果两个URL的协议、域名和端口相同，则表示他们同源。
	- 同源政策的目的，是为了保证用户信息的安全，防止恶意的网站窃取数据。

	>设想这样一种情况：A网站是一家银行，用户登录以后，又去浏览其他网站。如果其他网站可以读取A网站的 Cookie，会发生什么？          
	很显然，如果 Cookie 包含隐私（比如存款总额），这些信息就会泄漏。更可怕的是，Cookie 往往用来保存用户的登录状态，如果用户没有退出登录，其他网站就可以冒充用户，为所欲为。因为浏览器同时还规定，提交表单不受同源政策的限制。          
	由此可见，"同源政策"是必需的，否则 Cookie 可以共享，互联网就毫无安全可言了。
	
	- 限制范围，随着互联网的发展，"同源政策"越来越严格。目前，如果非同源，共有三种行为受到限制。
		1. Cookie、LocalStorage 和 IndexDB 无法读取。
		2. DOM 无法获得。
		3. AJAX 请求不能发送。

#### jsonP的解决方案
- 利用的原理
	- script标签可以跨域
		- `<script src="http://127.0.0.1:8022/api/"></script>`可以正常访问`http://127.0.0.1:8022/api/`，并取得返回值
	- 在开启`http://127.0.0.1:8022/api/`的服务器的该视图处返回一个js函数名的字符串，比如：`func(data)`
	- 在当前页面定义一个func的js函数，接收一个参数，则就可以实现跨域访问`http://127.0.0.1:8022/api/`，并获取返回值data用于处理
- jQuery已经将这一连串的操作封装，利用ajax的几个属性即可定制
	- url中
		- 这里的callback=list表明返回的函数名应当是list
		- _=1454376870403为特定的标识，无标识则无法通过验证
	- dataType: "jsonp"指定当前ajax为跨域请求，jQuery在处理ajax时会自动生成script标签，然后删除，即可完成跨域请求
	- jsonp: "callback"这是由服务端定制好的
	- jsonpCallback: "list"这是指定返回的函数名为list，应与url中一致，
		- 可以省略，表示函数名不重要，可以随机生成，但是url和服务器都需要与之对应
	- success
		- 这是jQuery封装的回调函数，本质上是定义一个jsonpCallback指定名称的函数，然后等跨域请求返回后，执行该函数

```js
$(".second").click(function () {
    $.ajax({
        url: "http://www.jxntv.cn/data/jmd-jxtv2.html?callback=list&_=1454376870403",
        dataType: "jsonp",
        jsonp: "callback",
        jsonpCallback: "list",
        success: function (data) {
            console.log(data.data);
            $.each(data.data, function (i, weeklist) {
                var content_str =
                    '<div id="' + i +
                    '"><h3>' + weeklist.week +
                    '</h3>'+
                    '</div>';
                $(".content").append(content_str);

                $.each(weeklist.list, function (j, item) {
                    var list_str =
                        '<p style="margin-left: 20px">' + item.time.slice(0, 2) + ':' + item.time.slice(2, 4) + '----<a href="' + item.link +
                        '">' + item.name +
                        '<p>';
                    $("#"+i).append(list_str)
                });
            })
        }
    })
})
```






## 跨域
- [同源策略](#1)
- [jsonP](#2)
- [CORS](#3)
- [简单请求和复杂请求](#4)

### <span id="1">同源策略</span>
- 为了解决同源策略
	- 同源策略是浏览器的特性，使用如requests模块就没有同源策略
		- 对ajax请求进行阻拦
		- 对href/src属性不阻拦
	- 同源策略的触发，发生在响应返回到浏览器时，浏览器会检测以下响应头
		- `Access-Control-Allow-Origin`
			- 来自于向服务器发送请求加上的域名
		- `Access-Control-Allow-Credentials`
			- 是否允许发送cookies
		- `Access-Control-Expose-Headers`
			- 允许的请求头
	- [参考阮一峰的博客](http://www.ruanyifeng.com/blog/2016/04/cors.html)

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

### <span id="2">jsonP的解决方案</span>
- 利用的原理
	- script标签的src属性可以跨域
		- `<script src="http://127.0.0.1:8022/api/"></script>`可以正常访问`http://127.0.0.1:8022/api/`，并取得返回值
	- 在开启`http://127.0.0.1:8022/api/`的服务器的该视图处返回一个js函数名的字符串，比如：`func(data)`
	- 在当前页面定义一个func的js函数，接收一个参数，则就可以实现跨域访问`http://127.0.0.1:8022/api/`，并获取返回值data用于处理

	```html
	<script src="http://127.0.0.1:8022/api/?callback=func"></script>
	<script>
		fucntion func(data){
			alert(data)
		}
	</script>
	```

- jQuery已经将这一连串的操作封装，利用ajax的几个属性即可定制
	- `url`中
		- 这里的`callback=list`表明返回的函数名应当是list
		- `_=1454376870403`为特定的标识，无标识则无法通过验证
	- `dataType: "jsonp"`指定当前ajax为跨域请求，jQuery在处理ajax时会自动生成script标签，然后删除，即可完成跨域请求
	- `jsonp: "callback"`这是由服务端定制好的
	- `jsonpCallback: "list"`这是指定返回的函数名为list，应与url中一致，
		- 可以省略，表示函数名不重要，可以随机生成，但是url和服务器都需要与之对应
	- `success:function(){}`
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


### <span id="3">CORS</span>
- 不同于jsonP只能发送GET请求，使用此方法可以发送任意请求，不过请求会被划分为简单请求和复杂请求
- 原理是利用给返回的响应加上浏览器可以识别的响应头，让浏览器对响应不进行同源策略的拦截
- 响应头有以下几种
	- `Access-Control-Allow-Origin`（必选）
		- 意思是允许来自哪些域名的请求跨域
		- 不可省略，否则请求按失败处理
		- eg:服务器域名https://api.example.com/
			- 只允许来自https://www.example.com/和https://www.example2.com/的请求跨域
			- 需要设置该请求头值为：`www.example.com www.example2.com`
			- 多个域名中间用空格分隔
		- 如果希望对来自任何域名的请求都允许跨域，可以填写"*"
	- `Access-Control-Expose-Headers` （可选）
		- 当发送请求的请求头中超过以下几个,需要填上额外的请求头，空格分隔
			- `Cache-Control`
			- `Content-Language`
			- `Content-Type`
			- `Expires`
			- `Last-Modified`
			- `Pragma`
	- `Access-Control-Allow-Credentials`（可选）
		- 是否允许请求包含cookies,设置为true 或者false
	- `Access-Control-Allow-Methods` （options请求可选）
		- 返回允许的请求方法，空格分隔

### <span id="4">简单请求和复杂请求</span>
- 简单请求
	- 请求方式只能是GET,POST,HEAD
	- 请求头不能超出以下几种

	```
	Accept
	Accept-Language
	Content-Language
	Last-Event-ID
	Content-Type，但仅能是下列之一
		application/x-www-form-urlencoded
		multipart/form-data
		text/plain
	```
- 复杂请求
	- 复杂请求必须用options请求进行预检
	- 预检返回成功才可以发送复杂请求

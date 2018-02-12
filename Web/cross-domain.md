## 解决跨域
-为了解决同源策略
	- 同源策略是浏览器的特性，使用如requests模块就没有同源策略
		- 对ajax请求进行阻拦
		- 对href/src属性不阻拦

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

### jsonP的解决方案
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


### CORS
- 跨域的一种解决方式
	- 不同于JSONP只能发GET请求
	- 可以发送各种请求
		- 运维可以通过nginx给请求加上响应头(CORS)



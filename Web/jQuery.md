# jQuery
- jQuery是一个快速、简洁的JavaScript框架，是继Prototype之后又一个优秀的JavaScript代码库（或JavaScript框架）。jQuery设计的宗旨是“Write Less，Do More”，即倡导写更少的代码，做更多的事情。它封装JavaScript常用的功能代码，提供一种简便的JavaScript设计模式，优化HTML文档操作、事件处理、动画设计和Ajax交互。
- jQuery的核心特性可以总结为：具有独特的链式语法和短小清晰的多功能接口；具有高效灵活的css选择器，并且可对CSS选择器进行扩展；拥有便捷的插件扩展机制和丰富的插件。jQuery兼容各种主流浏览器，如IE 6.0+、FF 1.5+、Safari 2.0+、Opera 9.0+等。

<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script>

## jQuery使用
- 导入jQuery文件
	- <code>\<script src="../jquery3_0_0.js">\</script></code>
	- <code>\<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js">\</script></code>


### 核心
- 当导入了jQuery库之后，就可以在script标签内使用jQuery的语法规则，
- jQuery的使用是以jQuery开头的表达式:<code>jQuery([selector,[context]])</code>，
- 为了简化书写，jQuery默认支持使用<code>$</code>代替<code>jQuery</code>:<code>$([selector,[context]])</code>

#### 第一条jQuery语句
- 可以打开任意一个支持jQuery的网页，使用浏览器的检查，在console窗口中输入<code>$("head>title").text()</code>
- 在已导入jQuery库的页面的script标签中输入<code>alert($("head>title").text());</code>
- 英文特殊字符$开头
	- jQuery.xxxxxx
	- $.xxxxxx


## jQuery的


- jQuery对象转成DOM对象
	- $("#ID").text()
	- $("#ID")[0],innerText
- DOM对象转成jQuery对象
	- var a = $("#ID")[0]
	- $(a).text()




























<script>$("code").css('color', '#D05');$("code").css('padding','0 4px');$("code").css('background','#fafafa');$("code").css('border','1px solid #ddd');</script>
# JavaScript
- [介绍](#1.0)
- [快速入门](#2.0)
	- [引入方式](#2.1)
	- [变量、常量和标识符](#2.2)
	- [数据类型](#2.3)
	- [运算符](#2.4)
	- [流程控制](#2.5)
- [对象](#3.0)
	- [String对象](#3.1)
	- [Array对象](#3.2)
	- [Date对象](#3.3)
	- [Math对象](#3.4)
	- [Function对象](#3.5)
- [BOM](#4.0)
- [DOM](#5.0)
	- [相关定义](#5.1)
	- [节点](#5.2)
	- [事件](#5.3)

## <span id="1.0">JS简介</span>
JavaScript一种直译式脚本语言，是一种动态类型、弱类型、基于原型的语言，内置支持类型。它的解释器被称为JavaScript引擎，为浏览器的一部分，广泛用于客户端的脚本语言，最早是在HTML（标准通用标记语言下的一个应用）网页上使用，用来给HTML网页增加动态功能。

>因为网景开发了JavaScript，一年后微软又模仿JavaScript开发了JScript，为了让JavaScript成为全球标准，几个公司联合ECMA（European Computer Manufacturers Association）组织定制了JavaScript语言的标准，被称为ECMAScript标准。         
所以简单说来就是，ECMAScript是一种语言标准，而JavaScript是网景公司对ECMAScript标准的一种实现。             
那为什么不直接把JavaScript定为标准呢？因为JavaScript是网景的注册商标。            
不过大多数时候，我们还是用JavaScript这个词。如果你遇到ECMAScript这个词，简单把它替换为JavaScript就行了。       

## <span id="2.0">快速入门</span>
### <span id="2.1">引入方式</span>
- 直接编写
	- 适用于需要直接对文档对象的操作

```html
<script>
    alert('hello world');
</script>
```
- 导入文件
	- 通常用来导入已经编写好的函数，在文档内操作

```html
<script src="hello.js"></script>
```

- 结束符
	- JavaScript的语法和Java语言类似，每个语句以;结束，语句块用{...}。
	- 但是，JavaScript并不强制要求在每个语句的结尾加;浏览器中负责执行JavaScript代码的引擎会自动在每个语句的结尾补上;
	- JavaScript对于缩进没有任何硬性要求，IDE提供的缩进只是有助于对代码的理解

	```javascript
	var x = 1;
	'helloworld';
	var x = 1; var y = 2;
	if (2 > 1) {
	 x = 1;
	 y = 2;
	 z = 3;
	}
	
	```

### <span id="2.2">变量、常量和标识符</span>
#### 变量
1. 声明变量时不用声明变量类型. 全都使用var关键字;
2. 一行可以声明多个变量.并且可以是不同类型;
3. 声明变量时 可以不用var. 如果不用var 那么它是全局变量;
4. 变量命名,首字符只能是字母,下划线,$美元符 三选一，余下的字符可以是下划线、美元符号或任何字母或数字字符且区分大小写，x与X是两个变量;

#### 常量和标识符
- 常量
	- 直接在程序中出现的数据值
- 标识符
	1. 由不以数字开头的字母、数字、下划线(_)、美元符号($)组成;
	2. 常用于表示函数、变量等的名称;
	3. 例如：_abc,$abc,abc,abc123是标识符，而1abc不是;
	4. JavaScript语言中代表特定含义的词称为保留字，不允许程序再定义为标识符;


### <span id="2.3">数据类型</span>
#### 数字类型(number)
#### 字符串类型(string)
#### 布尔类型(boolean)
#### Null & Undefined类型

### <span id="2.4">运算符</span>
#### 算术运算符
#### 比较运算符
#### 逻辑运算符

### <span id="2.5">流程控制</span>
#### 顺序结构
#### 分支结构
#### 循环结构
#### 异常处理

## <span id="3.0">对象</span>
### <span id="3.1">String对象</span>
### <span id="3.2">Array对象</span>
### <span id="3.3">Date对象</span>
### <span id="3.4">Math对象</span>
### <span id="3.5">Function对象</span>


## <span id="4.0">BOM</span>
### window对象


## <span id="5.0">DOM(Document Object Model)</span>
### <span id="5.1">相关定义</span>
- HTML Document Object Model（文档对象模型）
- HTML DOM 定义了访问和操作HTML文档的标准方法
- HTML DOM 把 HTML 文档呈现为带有元素、属性和文本的树结构（节点树)

#### DOM树
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Yuan</title>
</head>
<body>
    <h1>hello</h1>
    <a href="https://www.baidu.com/">点我吧</a>
</body>
</html> 
```
<img src="http://chuann.cc/Web/DOM-Tree.png" width="500px" height="auto">

### <span id="5.2">节点</span>
DOM对节点的定义：
1. 整个文档是一个文档节点 
2. 每个 HTML 标签是一个元素节点 
3. 包含在 HTML 元素中的文本是文本节点 
4. 每一个 HTML 属性是一个属性节点

#### 节点关系
节点树中的节点彼此拥有层级关系。    
父(parent),子(child)和同胞(sibling)等术语用于描述这些关系。父节点拥有子节点。同级的子节点被称为同胞（兄弟或姐妹）。    
>在节点树中，顶端节点被称为根（root）   
    每个节点都有父节点、除了根（它没有父节点）  
    一个节点可拥有任意数量的子节点   
    同胞是拥有相同父节点的节点  

<img src="http://chuann.cc/Web/DOM-Node-relative.png" width="500px" height="auto">

#### 对节点操作
##### 查找节点
- 直接查找
	- document.getElementById("idname")
	- document.getElementsByTagName("tagname")
	- document.getElementsByName("name")
	- document.getElementsByClassName("classname")
	- 可以将document换成已获得的节点对象进行局部查找
	
	```js  
	var element = document.getElementById('here');
	var element2 = document.getElementsByTagName('body');
	var element3 = document.getElementsByName('class');
	var element4 = document.getElementsByClassName('test')[0];
	var element5 = element.getElementsByTagName("li");
	```

- 导航查找
	- node.parentElement(node.parentNode)
	- node.children
	- node.firstElementChild
	- node.lastElementChild
	- node.nextElementSibling
	- node.previousElementSibling

	```js   
	var ele = document.getElementById('test');
	var ele2 = ele.parentElement;
	var ele3 = ele.children[0];
	var ele4 = ele.firstElementChild;
	var ele5 = ele.lastElementChild;
	var ele6 = ele.previousElementSibling;
	var ele7 = ele.nextElementSibling;
	```

- 注意事项
	- script标签中执行的JS代码通常是针对已经加载的HTML文档的操作，
	- 因此当执行搜索节点的JS代码的时候需要确保搜索范围的页面节点已经加载
	- 可以将script代码放置于需要操作的HTML代码之后
	- 也可以绑定在onload事件置于文档开头

- JS目前没有直接查找所有的兄弟标签的方法，通常需要自行设计函数去实现

	```js   
	function all_sibling(ele) {
	    var elements = ele.parentElement.children;
	    var arr=[];
	    for (var i = 0;i<elements.length;i++){
	        if (elements[i]!==ele){
	            arr.push(elements[i])
	        }
	    }
	    return arr
	}
	```

##### 增加节点
- 创建一个指定名称的元素
	
	```js
	var new_node = document.createElement('tagname')
	```

##### 删除节点
- 获得要删除的元素，通过父元素调用删除

	```js
	Node.removeChild()
	```


##### 替换节点
- 追加一个子节点

	```js
	node.appendChild(newnode)
	```

- 把增加的节点放到某个节点的前边

	```js
	node.insertBefore(newnode,某个节点)
	```

#### 操作节点
1. 获取节点的文本
	- node.innerText
	- node.innerHTML
2. 节点通用属性操作
	- node.setAttribute("attr_name","value")
	- node.getAttribute("attr_name")
	- node.removeAttribute("attr_name")
3. 需要使用value属性获取文本内容的节点，其他节点value属性为undefined
	- input
	- select
	- textarea

	```html
	<div id="test">点我吧</div>
	<input type="text" class="test" value="123">
	<script>
	    var ele = document.getElementById('test');
	    console.log(ele.innerText, ele.value, typeof ele.innerText);
	
	    var ele2 = document.getElementsByClassName('test')[0];
	    console.log(ele2.innerText, ele2.value, typeof ele2.innerText);
	</script>
	```
4. class属性
	- node.className
	- node.classList
	- node.classList.add
	- node.classList.remove

	```html
	<div class="c1 c2" id="test">123456789</div>
	<script>
	    var ele = document.getElementById('test');
	    console.log(ele.className, typeof ele.className);
	    console.log(ele.classList, typeof ele.classList);
	    ele.classList.add('c3');
	    ele.classList.remove('c2');
	    console.log(ele.classList, typeof ele.classList);
	</script>
	```

5. CSS样式-style属性

	```html
	<div id="test">JavaScript</div>
	<script>
	    var element = document.getElementById('test');
	    element.style.display = "inline-block";
	    element.style.width = "200px";
	    element.style.height = "100px";
	    element.style.marginTop = "100px";
	    element.style.marginLeft = "500px";
	    element.style.backgroundColor = "wheat";
	    element.style.color = "blue";
	    element.style.fontFamily = "Georgia";
	    element.style.fontSize = "30px";
	    element.style.textAlign = "center";
	    element.style.lineHeight = "100px";
	</script>
	```


6. 可以innerHTML给节点添加HTML代码（非W3C标准，但是主流浏览器支持）
	- node.innerHTML = "\<p>增加的内容\</p>"

### <span id="5.3">事件(事件句柄Event Handlers)</span>
#### 常用事件类型概览
- **onclick** 用户点击某个对象
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：button, document, checkbox, link, radio, reset, submit
- **ondbclick** 用户双击某个对象
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：document, link

- **onfoucs** 元素获得焦点（如选中输入框）
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：button, checkbox, fileUpload, layer, frame, password, radio, reset, select, submit, text, textarea, window
- **onblur** 元素失去焦点（如当用户离开某个输入框，对输入框内内容进行验证）
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：button, checkbox, fileUpload, layer, frame, password, radio, reset, submit, text, textarea, window
- **onchange** 域的内容被改变
	- 支持的HTML标签：<input type="text">, <select>, <textarea>
	- 支持的JavaScript对象：fileUpload, select, text, textarea

- **onkeydown** 某个键盘按键被按下
- **onkeypress** 某个键盘按键被按下并松开
- **onkeyup** 某个键盘按键被松开
	- 以上支持以下
	- HTML标签：绝大部分标签
	- JavaScript对象：document, image, link, textarea

- **onload** 一张页面或一幅图像完成加载
	- 支持的HTML标签：<body>, <frame>, <frameset>, <iframe>, <img>, <link>, <script>
	- 支持的JavaScript对象：image, layer, window

- **onmousedown** 鼠标按钮被按下
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：button, document, link
- **onmousemove** 鼠标被移动
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：默认不支持任何对象，因为过于频繁
- **onmouseout** 鼠标从某元素移开
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：layer, link
- **onmouseover** 鼠标移到某元素之上
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：layer, link
- **onmouseleave** 鼠标从某元素移开
	- 支持的HTML标签：绝大部分标签
	- 支持的JavaScript对象：layer, link

- **onselect** 文本框的文本被选中
	- 支持的HTML标签：<input type="text">, <textarea>
	- 支持的JavaScript对象：window
- **onsubmit** 确认按钮被点击
	- 支持的HTML标签：<form>
	- 支持的JavaScript对象：form

- [更多事件类型](http://www.w3school.com.cn/jsref/dom_obj_event.asp)

##### Event对象
Event对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。
事件通常与函数结合使用，函数不会在事件发生前被执行！event对象在事件发生时系统已经创建好了,并且会在事件函数被调用时传给事件函数.我们获得仅仅需要接收一下即可.比如onkeydown,我们想知道哪个键被按下了，需要问下event对象的属性，这里就是KeyCode.

- event.keycode 获取发生事件的键盘ASCII码
- event.target 获取发生事件的标签
	- event.target.tagname






#### 绑定事件的方式
- 方式一:

	```html
	<button id="div" onclick="foo(this)">快点这里</button>
	<script>
	    function foo(self){           // 形参不能是this
	        console.log("让你点就点，怎么这么随便？");
	        console.log(self);
	    }
	</script>
	```

- 方式二:

	```html
	<button id="abc">点我送福利！</button>
	<script>
	    var ele=document.getElementById("abc");
	    ele.onclick=function(){
	        console.log("SillyB");
	        console.log(this);    // this直接用
	    };
	</script>
	```

#### 部分事件介绍
##### onload
- 这个属性的触发**标志着**页面内容被加载完成，通常只给body加;
- 应用场景：当有些事情我们希望页面加载完立刻执行，那么可以使用该事件属性。

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <script>
	        //写法一，在body直接绑定事件给onload属性
	        function fun() {
	            alert(123)
	        }
	        //写法二，不使用body的onload属性
	//        window.onload = function () {
	//            alert(123)
	//        };
	    </script>
	</head>
	<body onload="fun()">
	<p id="ppp"></p>
	</body>
	</html>
	```

##### onsubmit
- 当表单在提交时触发，只能给form元素使用;
- 应用场景：在表单提交前验证用户输入是否正确。如果验证失败，在该方法中我们应该阻止表单的提交。

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <script>
	        window.onload = function () {
	            var ele = document.getElementById("form");
	            ele.onsubmit = function (event) {
	                alert("验证失败 表单不会提交!");
	                //阻止表单提交方式1().
	                //onsubmit 命名的事件函数,可以接受返回值. 其中返回false表示拦截表单提交.其他为放行.
	                //return false;
	                // 阻止表单提交方式2 event.preventDefault(); ==>通知浏览器不要执行与事件关联的默认动作。
	                event.preventDefault();
	            }
	        };
	    </script>
	</head>
	<body>
	<form id="form">
	    <input type="text"/>
	    <input type="submit" value="点这里！"/>
	</form>
	</body>
	</html>
	```

##### 事件传播
- 如果对某标签绑定了事件A，并且对其子标签也绑定了事件B，当子标签遭遇事件A也会执行相应的JS代码，称之为事件传播，通常我们不希望

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	<div id="abc_1" style="width:300px;height:300px;background-color: green">
	        <div id="abc_2" style="width:200px;height:200px;background-color: red">
	            INNER IDV
	        </div>
	    OUTER DIV
	</div>
	<script type="text/javascript">
	        document.getElementById("abc_1").onclick=function(){
	            alert('111');
	        };
	        document.getElementById("abc_2").onclick=function(event){
	            alert('222');
	//            event.stopPropagation(); //阻止事件向外层div传播.
	        }
	</script>
	</body>
	</html>
	```

##### onchange
- 当域内容被改变时的事件，通常用于有选项的标签

	```html
	<select name="" id="">
	    <option value="">111</option>
	    <option value="">222</option>
	    <option value="">333</option>
	</select>
	<script>
	    var ele=document.getElementsByTagName("select")[0];
	    ele.onchange=function(){
	          alert(123);
	    }
	</script>
	```

##### onkeydown
- 捕获键盘发生的事件

> Event对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。
事件通常与函数结合使用，函数不会在事件发生前被执行！event对象在事件发生时系统已经创建好了,并且会在事件函数被调用时传给事件函数.我们获得仅仅需要接收一下即可.比如onkeydown,我们想知道哪个键被按下了，需要问下event对象的属性，这里就是KeyCode.

```html
<input type="text" id="ccc">
<script>
    var key = document.getElementById('ccc');
    key.onkeydown = function (event) {
        console.log(123)
    };
    key.onkeyup = function () {
        console.log(456)
    };
</script>
```

##### onmouseout------onmouseleave
- 不论鼠标指针离开被选元素还是任何子元素，都会触发 mouseout 事件。
- 只有在鼠标指针离开被选元素时，才会触发 mouseleave 事件。

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style>
	        .container {  width: 40%;}
	        #container {  float: left;}
	        #container2 {  float: right;}
	        .title {  cursor: pointer;  background: #ccc;  height: 50px;  }
	        .list {  display: none;  background: #fff;  }
	        .list div {  line-height: 50px;  }
	        .list .item1 {  background-color: green;  }
	        .list .item2 {  background-color: rebeccapurple;  }
	        .list .item3 {  background-color: lemonchiffon;  }
	    </style>
	</head>
	<body>
	<div class="container" id="container">
	    <div class="title" id="title">使用了mouseout事件</div>
	    <div class="list" id="list">
	        <div class="item1">第一行</div>
	        <div class="item2">第二行</div>
	        <div class="item3">第三行</div>
	    </div>
	</div>
	<div class="container" id="container2">
	    <div class="title" id="title2">使用了mouseleave事件</div>
	    <div class="list" id="list2">
	        <div class="item1">第一行</div>
	        <div class="item2">第二行</div>
	        <div class="item3">第三行</div>
	    </div>
	</div>
	<script>
	    var container = document.getElementById("container");
	    var title = document.getElementById("title");
	    var list = document.getElementById("list");
	    title.onmouseover = function () {
	        list.style.display = "block";};
	    container.onmouseout = function () {
	        list.style.display = "none";};
	    var container2 = document.getElementById("container2");
	    var title2 = document.getElementById("title2");
	    var list2 = document.getElementById("list2");
	    title2.onmouseover = function () {
	        list2.style.display = "block";};
	    container2.onmouseleave = function () {
	        list2.style.display = "none";};
	</script>
	</body>
	</html>
	```

#### 事件委派
- 应用场景：原页面每一项已经绑定事件，而用户的新建项也需要绑定事件
- parentnode.addEventListener(event_type,listener,useCapture)


#### 事件实例
##### 表格全选、反选、取消
```html
<button class="select_all">全选</button>
<button class="select_reverse">反选</button>
<button class="cancel">取消</button>
<table border="1">
    <tr>
        <td><input type="checkbox" class="ck"></td>
        <td>111</td>
        <td>111</td>
        <td>111</td>
    </tr>
    <tr>
        <td><input type="checkbox" class="ck"></td>
        <td>222</td>
        <td>222</td>
        <td>222</td>
    </tr>
    <tr>
        <td><input type="checkbox" class="ck"></td>
        <td>333</td>
        <td>333</td>
        <td>333</td>
    </tr>
    <tr>
        <td><input type="checkbox" class="ck"></td>
        <td>444</td>
        <td>444</td>
        <td>444</td>
    </tr>
</table>
<script>
    var ele_select_all = document.getElementsByClassName('select_all')[0];
    var ele_select_reverse = document.getElementsByClassName('select_reverse')[0];
    var ele_cancel = document.getElementsByClassName('cancel')[0];
    var elements = document.getElementsByClassName('ck');
    ele_select_all.onclick = function () {
        for (var i=0;i<elements.length;i++){
            elements[i].checked = true;
        }
    };
    ele_cancel.onclick = function () {
        for (var i=0;i<elements.length;i++){
            elements[i].checked = false;
        }
    };
    ele_select_reverse.onclick = function () {
        for (var i=0;i<elements.length;i++){
            elements[i].checked?elements[i].checked = false:elements[i].checked = true;
        }
    }
</script>
```

##### 轮播图，tab切换

[代码链接](https://github.com/fangmingc/Python/blob/master/Web/JavaScript/0926/%E8%BD%AE%E6%92%AD%E5%9B%BE.html)







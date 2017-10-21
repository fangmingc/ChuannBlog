# CSS
- CSS(Cascading Style Sheets)：层叠样式表，对html标签的渲染和布局。

## 基础知识
- css语法：      
	- 选择器selector
	- 属性声明
		- 属性 property
		- 值 value

	```css
	selector {
	    property: value;
	    property: value;
	    property: value
	    ...
	}
	```

- CSS对于缩进没有要求
- CSS引入方式
	1. 行内式：使用html标签属性style定义，用于不经常改动的部分，或者使用JS控制生成

	```html
	<p style="background-color: rebeccapurple">hello world</p>
	```

	2. 嵌入式：在head标签内使用css语法定义，自行测试或初学练习，少部分网站会使用

	```
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style>
	        p{
	            background-color: #2b99ff;
	        }
	    </style>
	</head>
	```

	3. 链接式：在head标签内使用link标签链接到css文件(推荐使用)

	```html
	<link href="mystyle.css" rel="stylesheet" type="text/css"/>
	```

	4. 导入式：在head标签定义style，使用@import导入css文件，极少见

	```html
	<style type="text/css">
		@import"mystyle.css"
	</style>　
	```

## 选择器
### 基本选择器
#### 标签选择器
```css
p {color:green;}
div {color:red;}
```

#### id选择器
```css
#info {olor:blue;}
```

#### class选择器
```css
.info {background:#ff0;}
.info.con {background:blue;}表示同时满足两个类
```

#### 通配选择器
```css
* {margin:0; padding:0;}
```

### 组合选择器
#### 多元素选择器E,F
同时匹配所有E或F元素，E,F元素之间逗号分隔
```css
div,p {color:#f00;}
```

#### 后代选择器E F
匹配所有属于E元素后代的F元素，E和F之间空格分隔
```css
li a {font=weight:bold;}
```

#### 子代选择器E>F
匹配所有E元素的子元素F
```css
div p {color:#ff0;}
```

#### 毗邻元素选择器E+F
匹配所有紧随E元素之后的同级元素F
```css
div+p {color:#f00;}
```

#### 普通兄弟选择器E~F
匹配E元素之后的同级元素F
```css
.div1~p {font-size:300px;}
```

### 属性选择器
#### E[att]
匹配所有具有att属性的E元素，不考虑值，E可省略
```css
p[attr]{cocor:#f00;}
```

#### E[att=val]
匹配所有att属性等于val的E元素
```css
div[attr="value"]{color:red;}
```

#### E[att~=val]
匹配所有att属性具有多个空格分隔的值，其中一个值等于val的E元素
```css
td[attr~="value"]{color:red;}
```

#### E[attr^=val]
匹配属性值以指定值开头的每个元素
```css
div[attr^="value"]{color:red;}
```

#### E[attr$=val]
匹配属性值以指定值结尾的每个元素
```css
div[attr$="value"]{color:red;}
```

#### E[attr*=val]
匹配属性值中包含指定值的每个元素（模糊匹配）
```css
div[attr*="value"]{color:red;}
```

### 选择器的优先级
- 优先级排名
	1. 行内式样式
	2. id
	3. class、属性选择器
	4. element
	5. 继承父级及父级以上样式
- 注意
	- ！important声明高于一切
	- 如果!important声明冲突，则比较优先级
	- 如果都是类或属性选择器，则比较出现个数
	- 如果优先级一样，则按照在源出现的顺序决定，后来者居上

### 伪类
- 伪类指的是标签的不同状态，如超链接已访问，鼠标悬浮在标签上等
- 用法
	- 在选择器后跟“:”+伪类种类
	- 选择器加上伪类之后的属性声明仅在伪类被触发后生效
- 种类
	- link 没有被触碰的状态（通常用于超链接）
	- visited 已访问的状态（通常用于超链接）
	- hover 鼠标已放置的状态
	- active 鼠标按下的状态
	- before 元素之前插入的内容
	- after 元素之后插入的内容

## 属性声明
### 文本属性
#### 文本颜色 
- color
- 颜色指定
	- 十六进制：#FF0000
	- RGB：RGB(255,0,0)
	- 颜色的名称：red

#### 水平对齐方式 
- text-align
	- left 文本左对齐
	- right 文本右对齐
	- center 文本居中对齐
	- justify 两端对齐

#### 其他属性
- 字体大小
	- font-size: 10px;
- 文本行高，文字高度加文字上下的空白区域的高度
	- line-height: 200px;    
	- 也可指定基于字体大小的百分比
- 垂直对齐方式，只对行内元素有效，对块级元素无效
	- vertical-align:－4px;
	- vertical-align：center;
- 文本装饰，主要是用来删除链接的下划线
	- text-decoration:none;
- 字体样式
	- font-family: 'Lucida Bright';
	- font-family: 'Georgia';
- 字体加粗
	- font-weight: lighter/bold/border;
	- font-weight: 300;
- 字体类型，常规，斜体等
	- font-style: oblique;
- 首行缩进
	- text-indent: 150px;  
- 字母间距
	- letter-spacing: 10px;  
- 单词间距
	- word-spacing: 20px;  
- 文本转换，用于所有字句变成大写或小写字母，或每个单词的首字母大写
	- text-transform: capitalize/uppercase/lowercase ; 

### 背景属性
- background-color
	- 设置纯色背景色
- background-image
	- 设置北京图片
- background-repeat
	- 设置北京图片是否重复填充
- background-position
	- 设置背景图片位置
- background
	- 合写上面的属性
	- <code>background:#ffffff url('1.png') no-repeat right top;</code>

### 边框属性
- border-width
	- 设置边框宽度
- border-style
	- 设置边框样式
- border-color
	- 设置边框颜色
- border
	- 合写：<code>border: 30px rebeccapurple solid;</code>
- 可分别设置边框
	- border-top
	- border-bottom
	- border-left
	- border-right

### 列表属性
针对列表标签的属性声明
- list-style-type
	- 设置列表项标志的类型。
- list-style-image
	- 将图象设置为列表项标志。
- list-style-position
	- 设置列表中列表项标志的位置。
- list-style
	- 简写属性。用于把所有用于列表的属性设置于一个声明中

### dispaly属性
- none
	- 隐藏标签
- block
	- 设置为块级元素，可以设置width，height，独占一行
- inline
	- 设置为内联元素，不可以设置width，height，可与其他内联元素在一行
- inline-block
	- 设置为可内联的块级标签，可以设置width，height，可与其他内联元素在一行

### 外边距和内边距
- 盒子模型
	- margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
	- padding:           用于控制内容与边框之间的距离；   
	- border(边框):     围绕在内边距和内容外的边框。
	- content(内容):   盒子的内容，显示文本和图像。

<img src="https://github.com/fangmingc/ChuannBlog/blob/master/Web/box-model.png"  width=400>


### float属性
- 浮动规则
	- block元素通常被现实为独立的一块，独占一行，多个block元素会各自新起一行，默认block元素宽度自动填满其父元素宽度。block元素可以设置width、height、margin、padding属性；
	- inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。inline元素设置width、height属性无效
	- 所谓的文档流，指的是元素排版布局过程中，元素会自动从左往右，从上往下的流式排列。
	- 脱离文档流，也就是将元素从普通的布局排版中拿走，其他盒子在定位的时候，会当做脱离文档流的元素不存在而进行定位。

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style>
	        * {
	            margin: 0;
	        }
	        .r1 {
	            width: 300px;
	            height: 100px;
	            background-color: #7A77C8;
	            float: left;
	        }
	        .r2 {
	            width: 200px;
	            height: 200px;
	            background-color: wheat;
	            /*float: left;*/
	        }
	        .r3 {
	            width: 100px;
	            height: 200px;
	            background-color: darkgreen;
	            float: left;
	        }
	    </style>
	</head>
	<body>
	<div class="r1"></div>
	<div class="r2"></div>
	<div class="r3"></div>
	</body>
	</html>
	```
- 非完全脱离文档流
	- 左右结构div盒子重叠现象，一般是由于相邻两个DIV一个使用浮动一个没有使用浮动。一个使用浮动一个没有导致DIV不是在同个“平面”上，但内容不会造成覆盖现象，只有DIV形成覆盖现象。
	- 要么都不使用浮动；要么都使用float浮动；要么对没有使用float浮动的DIV设置margin样式

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style>
	        *{
	            margin: 0;
	        }
	        .r1{
	            width: 100px;
	            height: 100px;
	            background-color: #7A77C8;
	            float: left;
	        }
	        .r2{
	            width: 200px;
	            height: 200px;
	            background-color: wheat;
	        }
	    </style>
	</head>
	<body>
	<div class="r1"></div>
	<div class="r2">region2</div>
	</body>
	</html>
	```

- 父级坍塌现象

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style type="text/css">
	        * {
	            margin: 0;
	            padding: 0;
	        }
	        .container {
	            border: 1px solid red;
	            width: 300px;
	        }
	        #box1 {
	            background-color: green;
	            float: left;
	            width: 100px;
	            height: 100px;
	        }
	        #box2 {
	            background-color: deeppink;
	            float: right;
	            width: 100px;
	            height: 100px;
	        }
	        #box3 {
	            background-color: pink;
	            height: 40px;
	        }
	    </style>
	</head>
	<body>
	<div class="container">
	    <div id="box1">box1 向左浮动</div>
	    <div id="box2">box2 向右浮动</div>
	</div>
	<div id="box3">box3</div>
	</body>
	</body>
	</html>
	```
	- .container和box3的布局是上下结构，上图发现box3跑到了上面，与.container产生了重叠，但文本内容没有发生覆盖，只有div发生覆盖现象。这个原因是因为第一个大盒子里的子元素使用了浮动，脱离了文档流，导致.container没有被撑开。box3认为.container没有高度（未被撑开），因此跑上去了

#### 解决方法一：固定高度
- 给.container设置固定高度或者给.container加一个固定高度的子div
- 但一般一般情况下文字内容不确定多少就不能设置固定高度，所以一般不能设置“.container”高度
- 能确定内容多高，这种情况下“.container是可以设置一个高度即可解决覆盖问题。

	```html
	<div class="container" style="height: 100px">
	    <div id="box1">box1 向左浮动</div>
	    <div id="box2">box2 向右浮动</div>
	    <!--<div id="empty" style="height: 100px"></div>-->
	</div>
	<div id="box3">box3</div>
	```

#### 解决办法二：清除浮动（clear属性）
clear属性只会对自身起作用，而不会影响其他元素。
- clear:none  默认值。允许两边都可以有浮动对象
- clear:left  不允许左边有浮动对象
- clear:right  不允许右边有浮动对象
- clear:both  不允许有浮动对象
- 解决父级坍塌现象：
	- CSS代码

	```CSS
	.clearfix:after {             		/*在类名为“clearfix”的元素内最后面加入内容；
	    content: ".";                 	/*内容为“.”就是一个英文的句号而已。也可以不写。
	    display: block;               	/*加入的这个元素转换为块级元素。
	    clear: both;                  	/*清除左右两边浮动。
	    visibility: hidden;           	/*可见度设为隐藏。注意它和display:none;是有区别的。这里仍然占据空间，只是看不到而已；
	    line-height: 0;               	/*行高为0；
	    height: 0;                    	/*高度为0；
	    font-size:0;                  	/*字体大小为0；
	    }
	```
	- html 整段代码就相当于在浮动元素后面跟了个宽高为0的空div，然后设定它clear:both来达到清除浮动的效果。这样的操作就不必在html文件中写入大量无意义的空标签，又能清除浮动。

	```html
	<div class="container">
	    <div id="box1">box1 向左浮动</div>
	    <div id="box2">box2 向右浮动</div>
	    <div class="clearfix"></div>
	</div>
	<div id="box3">box3</div>
	```

#### 解决办法三：overflow:hidden
overflow：hidden的含义是超出的部分要裁切隐藏，float的元素虽然不在普通流中，但是他是浮动在普通流之上的，可以把普通流元素+浮动元素想象成一个立方体。如果没有明确设定包含容器高度的情况下，它要计算内容的全部高度才能确定在什么位置hidden，这样浮动元素的高度就要被计算进去。这样包含容器就会被撑开，清除浮动。

### position属性
-  static
	- 默认值，无定位，不能当作绝对定位的参照物，并且设置标签对象的left、top等值是不起作用的的。
- position: relative／absolute
	- relative: 相对定位。
		- 相对定位是相对于该元素在文档流中的原始位置，即以自己原始位置为参照物。
		- 即使设定了元素的相对定位以及偏移值，元素还占有着原来的位置，即占据文档流空间。
		- 对象遵循正常文档流，但将依据top，right，bottom，left等属性在正常文档流中偏移位置。
		- 而其层叠通过z-index属性定义。
		- 主要用法：方便绝对定位元素找到参照物。
	- absolute: 绝对定位。
		- 定义：设置为绝对定位的元素框从文档流完全删除，并相对于最近的已定位祖先元素定位，如果元素没有已定位的祖先元素，那么它的位置相对于最初的包含块（即body元素）。
		- 元素原先在正常文档流中所占的空间会关闭，就好像该元素原来不存在一样。
		- 元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。
		- 重点：如果父级设置了position属性，例如position:relative;，那么子元素就会以父级的左上角为原始点进行定位。这样能很好的解决自适应网站的标签偏离问题，即父级为自适应的，那我子元素就设置position:absolute;父元素设置position:relative;，然后Top、Right、Bottom、Left用百分比宽度表示。
		- 另外，对象脱离正常文档流，使用top，right，bottom，left等属性进行绝对定位。
		- 而其层叠通过z-index属性定义。
	
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	    <style>
	        *{
	            margin: 0;
	        }
	        .outet{
	            /*position: relative;*/
	        }
	        .item{
	            width: 200px;
	            height:200px ;
	        }
	        .r1{
	            background-color: #7A77C8;
	        }
	        .r2{
	            background-color: wheat;
	            /*position: relative;*/
	            position: absolute;
	            top: 200px;
	            left: 200px;
	        }
	        .r3{
	            background-color: darkgreen;
	        }
	    </style>
	</head>
	<body>
	<div class="item r1"></div>
	<div class="outet">
	    <div class="item r2"></div>
	    <div class="item r3"></div>
	</div>
	</body>
	</html>
	```

- position:fixed
	- 对象脱离正常文档流，使用top，right，bottom，left等属性以窗口为参考点进行定位，当出现滚动条时，对象不会随着滚动。
	- 而其层叠通过z-index属性定义。 
	- 注意： 一个元素若设置了 position:absolute | fixed; 则该元素就不能设置float。
	- 在理论上，被设置为fixed的元素会被定位于浏览器窗口的一个指定坐标，不论窗口是否滚动，它都会固定在这个位置。

















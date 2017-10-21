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



### float属性
### position属性






















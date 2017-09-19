# html

## 初识html
html是HyperTxt Makeup Language（超文本标记语言）的简称。  
HyperText is text displayed on a computer or device that provides access to 
other text through links, also known as “hyperlinks”.  

### 标签
由尖括号包围的关键词，比如 <html>。HTML 标签分为单标签和双标签    
- 双标签：HTML标签通常是成对出现的，比如 <b> 和 </b>。第一个标签是开始标签，第二个标签是结束标签；开始标签和结束标签也被称为开放标签和闭合标签
- 常见的单标签有：

```html
<img><br><hr><input>
```
- HTML标签对大小写不敏感，但通常全小写

<img src='https://s3.amazonaws.com/codecademy-content/courses/web-101/htmlcss1-diagram__htmlanatomy.svg' width=400>

### 属性
HTML标签可以拥有属性，属性提供了有关HTML元素的更多信息。       
属性以键值对(属性名=属性值)的形式出现，且总是在HTML元素的开始标签中规定。
- [常见属性]
	- class: 元素类名
	- id:元素ID
	- style:元素的行内样式
	- title:元素的额外信息，可在工具提示中显示

### 元素
从开始标签到结束标签的所有代码。HTML元素以开始标签起始，以结束标签终止，元素的内容是开始标签与结束标签之间的内容。

### 文档
HTML文档被称为网页，由嵌套的HTML元素构成。浏览器不会显示HTML标签，而是使用标签来解释页面的内容。

### 注释
注释是在HTML插入的描述性文本，用来解释该代码或提示其他信息。    
```html
<!-- This is a comment -->   
```
注释只出现在代码中，不会在页面中显示；且注释不可嵌套

### 实体
HTML中某些字符是预留的，必须被替换为字符实体

<table class="table">
<tbody>
<tr><th style="width: 20%;">显示结果</th><th style="width: 20%;">描述</th><th style="width: 30%;">实体名称</th><th style="width: 30%;">实体编号</th></tr>
<tr>
<td>&nbsp;</td>
<td>空格</td>
<td>&amp;nbsp;</td>
<td>&amp;#160;</td>
</tr>
<tr>
<td>&lt;</td>
<td>小于号</td>
<td>&amp;lt;</td>
<td>&amp;#60;</td>
</tr>
<tr>
<td>&gt;</td>
<td>大于号</td>
<td>&amp;gt;</td>
<td>&amp;#62;</td>
</tr>
<tr>
<td>&amp;</td>
<td>和号</td>
<td>&amp;amp;</td>
<td>&amp;#38;</td>
</tr>
<tr>
<td>"</td>
<td>引号</td>
<td>&amp;quot;</td>
<td>&amp;#34;</td>
</tr>
<tr>
<td>'</td>
<td>撇号&nbsp;</td>
<td>&amp;apos;&nbsp;</td>
<td>&amp;#39;</td>
</tr>
<tr>
<td>￠</td>
<td>分</td>
<td>&amp;cent;</td>
<td>&amp;#162;</td>
</tr>
<tr>
<td>£</td>
<td>镑</td>
<td>&amp;pound;</td>
<td>&amp;#163;</td>
</tr>
<tr>
<td>¥</td>
<td>日圆</td>
<td>&amp;yen;</td>
<td>&amp;#165;</td>
</tr>
<tr>
<td>€</td>
<td>欧元</td>
<td>&amp;euro;</td>
<td>&amp;#8364;</td>
</tr>
<tr>
<td>§</td>
<td>小节</td>
<td>&amp;sect;</td>
<td>&amp;#167;</td>
</tr>
<tr>
<td>©</td>
<td>版权</td>
<td>&amp;copy;</td>
<td>&amp;#169;</td>
</tr>
<tr>
<td>®</td>
<td>注册商标</td>
<td>&amp;reg;</td>
<td>&amp;#174;</td>
</tr>
<tr>
<td>™</td>
<td>商标</td>
<td>&amp;trade;</td>
<td>&amp;#8482;</td>
</tr>
<tr>
<td>×</td>
<td>乘号</td>
<td>&amp;times;</td>
<td>&amp;#215;</td>
</tr>
<tr>
<td>÷</td>
<td>除号</td>
<td>&amp;divide;</td>
<td>&amp;#247;</td>
</tr>
</tbody>
</table>

### html结构

- \<!DOCTYPE html> 告诉浏览器使用什么样的html或者xhtml来解析html文档
- \<html>\</html>是文档的开始标记和结束标记。此元素告诉浏览器其自身是一个 HTML 文档，在它们之间是文档的头部<head>和主体<body>。
- \<head>\</head>元素出现在文档的开头部分。<head>与</head>之间的内容不会在浏览器的文档窗口显示，但是其间的元素有特殊重要的意义。
- \<title>\</title>定义网页标题，在浏览器标题栏显示。 
- \<body>\</body>之间的文本是可见的网页主体内容

## 常用标签
### \<!DOCTYPE>标签
位于文档第一行，告知浏览器文档使用了哪种html或xhtml规范

- document.compatMode：
	- BackCompat：怪异模式，浏览器使用自己的怪异模式解析渲染页面。
	- CSS1Compat：标准模式，浏览器使用W3C的标准解析渲染页面。



### \<head>标签
#### \<meta>标签 
- \<meta>元素可提供有关页面的元信息（meta-information），针对搜索引擎和更新频度的描述和关键词。
- \<meta>标签位于文档的头部，不包含任何内容。
- \<meta>提供的信息是用户不可见的
- meta标签的组成：meta标签共有两个属性，它们分别是http-equiv属性和name 属性，不同的属性又有不同的参数值，这些不同的参数值就实现了不同的网页功能。 
	- name属性，主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的
		- keywords表示使用搜索引擎搜索时的关键字
		- description表示使用搜索引擎显示结果时展现的描述信息

```html
<meta name="keywords" content="meta总结,html meta,meta属性,meta跳转">
<meta name="description" content="There is nothing.">
```
	- http-equiv属性，相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。
		- Refresh表示间隔多久跳转到指定网页
		- content-Type表示用何种编码解析文档

```html
<meta http-equiv="Refresh" content="2;URL=https://www.oldboy.com"> 
<meta http-equiv="content-Type" charset=UTF8"> 
<meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" /> 
```
#### \<icon>标签
定义使用浏览器打开网页的标签页的标题左边的图标
```html
<link rel="icon" href="http://www.jd.com/favicon.ico">
```
#### \<title>标签
定义使用浏览器打开网页的标签页的标题文字
```html
<title>oldboy</title>
```
#### \<link>标签
指定CSS样式
```html
<link rel="stylesheet" href="css.css">
```
#### \<script>标签
指定JS文件
```html
<script src="hello.js"></script>　
```

### \<body>标签
#### 基本标签

- \<hn>: n的取值范围是1~6; 从大到小. 用来表示标题.

- \<p>: 段落标签. 包裹的内容被换行.并且也上下内容之间有一行空白.

- \<b> \<strong>: 加粗标签.

- \<strike>: 为文字加上一条中线.

- \<em>: 文字变成斜体.

- \<sup>和\<sub>: 上角标 和 下角表.

- \<br>:换行.

- \<hr>:水平线

- 特殊字符：
      \&lt; \&gt；\&quot；\&copy;\&reg;


#### \<div>和\<span>
\<div>\</div>：\<div>只是一个块级元素，并无实际的意义。主要通过CSS样式为其赋予不同的表现.          
\<span>\</span>： \<span>表示了内联行(行内元素),并无实际的意义,主要通过CSS样式为其赋予不同的表现.

- 块级元素与行内元素的区别
所谓块元素，是以另起一行开始渲染的元素，行内元素则不需另起一行。如果单独在网页中插入这两个元素，不会对页面产生任何的影响。

- 这两个元素是专门为定义CSS样式而生的。

#### 图形标签: \<img> 
- 属性
- src: 要显示图片的路径.
- alt: 图片没有加载成功时的提示.
- title: 鼠标悬浮时的提示信息.
- width: 图片的宽
- height:图片的高 (宽高两个属性只用一个会自动等比缩放.)

#### 超链接标签(锚标签): \<a> \</a>
```html
<a href="" target="_blank" >click</a>
```
- href属性指定目标网页地址。该地址可以有几种类型：
	- 绝对 URL - 指向另一个站点（比如 href="http://www.jd.com）
	- 相对 URL - 指当前站点中确切的路径（href="index.htm"）
	- 锚 URL - 指向页面中的锚（href="#top"）

- 什么是URL？
>URL是统一资源定位器(Uniform Resource Locator)的缩写，也被称为网页地址，是因特网上标准的资源的地址。
URL举例
http://www.sohu.com/stu/intro.html
http://222.172.123.33/stu/intro.html
URL地址由4部分组成
第1部分：为协议：http://、ftp://等 
第2部分：为站点地址：可以是域名或IP地址
第3部分：为页面在站点中的目录：stu
第4部分：为页面名称，例如 index.html
各部分之间用“/”符号隔开。

#### 列表标签
- \<ul>: 无序列表 
	- [type属性：disc(实心圆点)(默认)、circle(空心圆圈)、square(实心方块)]

- \<ol>: 有序列表
	- \<li>:列表中的每一项.

- \<dl>  定义列表
	- \<dt> 列表标题
	- \<dd> 列表项

#### 表格标签: \<table>
```html
<table>
         <tr>
                <td>标题</td>
                <th>加粗标题</th>
         </tr>
         <tr>
                <td>内容</td>
                <td>内容</td>
         </tr>
</table>
```
- 属性:
	- border: 表格边框
	- cellpadding: 内边距
	- cellspacing: 外边距
	- width: 像素 百分比.（最好通过css来设置长宽）
	- rowspan:  单元格竖跨多少行
	- colspan:  单元格横跨多少列（即合并单元格）

#### 列表标签

#### 表单标签 \<form>

- 属性：
	- name:作为发送到server端的数据的键
	- value：作为发送到server端的数据的值

### div/sapn

### 标签的嵌套
嵌套原则
块级标签可以嵌套块级标签、内联标签，内联标签只能嵌套内联标签








# CSS
- CSS(Cascading Style Sheets)：层叠样式表，对html标签的渲染和布局。

## 基础知识

css语法：
```css
selector {
    property: value;
    property: value;
    property: value
    ...
}
```

1. 查找标签
	- 选择器（selector）

2. 选择标签

- 引入方式
	1. 行内式：使用html标签属性style定义(极度不推荐)
	2. 嵌入式：在head标签内使用css语法定义(不推荐)
	3. 链接式：在head标签内使用link标签链接到css文件(推荐使用)
	4. 导入式：在head标签定义style，使用@import导入css文件(不推荐)

## CSS选择器
### 基本选择器
#### 标签选择器
```css
p {color:greem;}
```
#### id选择器
```css
#info {}
```
#### class选择器
```css
.info {background:#ff0;}
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


































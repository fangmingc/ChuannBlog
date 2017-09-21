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
常用的权重：
- id 100   
- class 10   
- element 1   
组合选择器的优先级将权重相加

优先级排名：
- 非规则
	- ！important
- 规则内
	1. 内嵌
	2. id
	3. class、属性选择器
	4. element
	5. 继承

### 伪类
在选择器后跟:使用不同样式的伪类



## CSS属性操作
### CSS text
#### 文本颜色:color
颜色的指定：
- 十六进制：#FF0000
- RGB：RGB(255,0,0)
- 颜色的名称：red


#### 水平对齐方式
text
#### 文本其他属性
### 背景属性
### 边框属性
### 外边距和内边距
### float属性






















## Vue.js
- 构建用户界面的javascrapt框架，用于自动生成html
- 轻量、灵活

- [安装](#1)
- [基本使用](#2)
- [ES6](#3)
- [node.js](#4)
- [webpack](#5)
- [axios](#6)
- [vue-router](#7)

### 安装
- CDN:
	- http://www.bootcdn.cn/vue/

### 基本使用
- 引入vue

	```html
	<script src="vue.js"></script>
	```

- 展示html

	```html
	<div id="app">
	    Vue<input type="text" v-model="msg">
	    <p>{{msg}}</p>
	</div>
	```

- 建立vue对象

	```html
	new Vue({
	        el:"#app",	# 表示在当前这个元素内开始使用Vue
	        data:{
	            msg:"",
	        }
	    })
	```

#### 指令
- v-text
	- 在元素中插入值
- v-html
	- 在元素中不仅可以插入文本，还可以插入标签
- v-if
	- 根据表达式的真假值动态插入和移除元素
- v-show
	- 根据表达式的真假值来隐藏和显示元素
- v-for
	- 根据变量的值来循环渲染元素
- v-on
	- 监听元素事件，并执行相应的操作
	- 对数组操作
		- push
		- pop
		- shift
		- unshift
		- splice
		- reverse
- v-bind
	- 绑定元素的属性来执行相应的操作
- v-model
	- 实现了数据和视图的双向绑定
		- 视图：DOM树
		- 把元素的值和数据绑定
		- 当元素的值发生变化，数据同步变化，即视图->数据的驱动
		- 当数据发生变化，元素的值同步变化，即数据->视图
- 自定义指令
	- 

### ES6


### node.js


### webpack


### axios


### vue-router




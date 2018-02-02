## Vue.js
构建用户界面的javascrapt框架，用于自动生成html       
轻量、灵活、数据驱动视图

- [基本使用](#1)
- [安装VUE项目](#2)
- [axios](#5)
- [vue-router](#6)

- 下载使用
	- http://www.bootcdn.cn/vue/

### <span id="1">基本使用</span>
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

	```js
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

### <span id="2">VUE项目</span>
- 安装VUE
	`npm install vue-cli -g`
- 创建项目
	- `vue-init webpack 项目名`
	- 会出现对项目的一些设置，可以全部默认使用默认设置（全部回车）

- 开启项目

	```cmd
	cd 项目名
	npm run dev
	```
	- 在项目的config/index.js里面，会有一个参数autoOpenBrowser,可以设置启动项目时是否自动打开浏览器
- 项目介绍
	- 项目目录结构
		- bulid
		- config
		- node_modules
		- src
			- 存放程序代码
		- static
	- 项目文件
		- .vue结尾的都是组件，编写程序都在这里
- VUE特性
	- 热重载
		- 修改VUE的代码，在浏览器无需刷新即可实现自动局部刷新


### <span id="3">axios</span>


### vue-router
- 设置文件路由流程
	1. 建立组件，.vue文件
	2. 配置路由,index.js文件中配置
	3. <router-link></router-link>
	4. <router-viem></router-viem>
	5. import 包名 from "组件路径"
	6. components进行注册


### Vue组件生命周期
1. 定义Vue对象并实例化
2. created函数
3. 编译模板
4. 把HTML元素渲染到页面当中
5. mounted函数
6. 如果有元素的更新就执行updated函数
7. 销毁实力



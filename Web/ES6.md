## ES6
EMCAScipt 6 (ES2015)
- 详细参阅[ECMAScript 6 入门](http://es6.ruanyifeng.com)
- 本文仅摘取部分内容

### 特性
#### const和let
- JS数据类型
	- 基本数据类型
		- string,int,bool,null,undefined
	- 引用数据类型
		- array,object

- const
	- 不可重复定义，定义后不可修改
- let
	- 需要先定义再使用，不存在变量提升
	- 块级作用域，类似python的局部作用域但更加细致
		- eg:for (let i=0;i<10,i++){}
		- 出了这个循环，i就不存在


#### 模板字符串
- 通过反引号使用，字符串可以使用变量
	- ${name}
- 可以当作普通字符串来处理
- 可以使用多行字符串

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>Title</title>
	</head>
	<body>
	<ul id="list_1">
	</ul>
	    <script>
	        let name = "小三";
	        console.log(`她的名字叫${name}`);
	
	        document.getElementById("list_1").innerHTML = `
	        <li>11</li>
	        <li>22</li>
	        <li>33</li>
	        <li>44</li>
	        `
	    </script>
	</body>
	</html>
	```

#### 解构变量
- 数组
	- 将数组元素的值依次赋值给变量
- 对象
	- 将对象按照键一一赋值

	```js
	let arr = [99, 22, 44, ["qwe", "asd"]];
	let [q, w, e, [r, t]] = arr;
	console.log(q);
	console.log(r);
	let obj = {
	    a:"json",
	    b:123
	};
	let {a, b} = obj;
	console.log(a)
	```

#### 对象的扩展
- 可以将外面定义的变量直接放置在对象内

	```js
	function func(){alert(888)}
	let username = "柯察金";
	let obj = {
	    username,
	    fun:function () {
	        alert(999)
	    },
	    func,
	    func2(){
	        alert(777)
	    }
	};
	console.log(obj.username);
	obj.fun();
	obj.func();
	obj.func2();
	```

#### 函数的扩展
- 可以使用默认参数
- 可以指定变量接收剩余参数

	```js
    function fun(x=123, y=213, z=435) {
        console.log(x, y+z)
    }
    fun();

    function fun2(x,...y) {
        console.log(x, y)
    }
    fun2(22, 33, 44, 55, 66);
    fun2(x=33, y=300, z=22)
	```

#### 数组的扩展
- 遍历数组
	- forEach
	- map
	- fliter
- 判断数组是否存在某个值
	- indexOf
	- includes

	```js
    let arr = [78, 89, 90, 101];
    arr.forEach(function(value, index){
        console.log(value)
    });

    let arr2 = arr.map(function (value, index) {
        return value+1
    });
    console.log(arr2);

    // 如果有，则返回下标，没有则返回-1
    console.log(arr.indexOf(90));
    console.log(arr.indexOf(900));
    // 如果有，则返回true，没有则返回false
    console.log(arr.includes(101));
    console.log(arr.includes(100));
    // 快速筛选
    let arr3 = arr.filter(function (value, index) {
        return value>89
    });
    console.log(arr3)
	```

#### 类




#### import和require
- import 
	- 必须在文件顶部
	- 相当于一个指针引用了文件，并没有把文件包含进来，需要调用文件时才引入
- require
	- 可以放在文件任何位置
	- 把文件整个包含进当前文件

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
- 关键字
	- <img src="http://chuann.cc/Web/Keywords.png" width="500px" height="auto">

### <span id="2.3">数据类型</span>
JavaScript的数据类型分为两类：
- 基本数据类型
	- Number、Null、String、Undefined、Boolean
- 引用数据类型
	- object

#### 数字类型(number)
```js
console.log(10);      //整数10
console.log(1.1);     //浮点数1.1
console.log(.1);      //浮点数0.1
console.log(10.0);    //整数10
console.log(10.);     //整数10
console.log(3.123e7); //科学计数法，31230000
```

- 不区分整型数值和浮点型数值；
- 所有数字都采用64位浮点格式存储，相当于Java和C语言中的double格式；
- 能表示的最大整数是±1.7976931348623157x10^308，可以通过Number.MAX_VALUE访问；
- 能表示的最多位小数是±5x10^-324，可以通过Number.MIN_VALUE访问；
- 能表示并进行精确算术运算的整数范围为：正负2的53次方，也即从最小值-9007199254740992到最大值+9007199254740992之间的范围；
- 对于整数的位运算（比如移位等操作），JavaScript仅支持32位整型数，也即从-2147483648到+2147483647之间的整数。

#### 字符串类型(string)
```js
console.log('hello');
console.log("hello");
console.log('你好');
console.log('\nhello');
console.log('he\'llo');
console.log('he\"llo');
console.log('he\\llo');
```

- 由Unicode字符、数字、标点符号组成的序列；
- 字符串常量首尾由单引号或双引号括起；
- JavaScript中没有字符类型；
- 常用特殊字符直接在字符串中表达；
- 字符串中部分特殊字符必须加上右划线\；
- 常用的转义字符 \n:换行 \':单引号 \":双引号 \\:右划线

#### 布尔类型(boolean)
- Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0
- 布尔值也可以看作on/off、yes/no、1/0对应true/false
- Boolean值主要用于JavaScript的控制语句，例如：

	```js
	if (x==1){
		y=y+1;
	} else {
		y=y-1;
	}
	```

#### Null & Undefined类型
- Undefined类型
	- Undefined 类型只有一个值，即 undefined。当声明的变量未初始化时，该变量的默认值是 undefined。
	- 当函数无明确返回值时，返回的也是值 "undefined";
- Null类型
	- 另一种只有一个值的类型是 Null，它只有一个专用值 null，即它的字面量。值 undefined 实际上是从值 null 派生来的，因此 ECMAScript 把它们定义为相等的;
- 尽管这两个值相等，但它们的含义不同:
	- undefined 是声明了变量但未对其初始化时赋予该变量的值;
	- null 则用于表示尚未存在的对象;
	- 如果函数或方法要返回的是对象，那么找不到该对象时，返回的通常是 null。

	```js
	var value1 = undefined;
	var value2 = null;
	if (value1==value2){
	    console.log(value1,"等于",value2)
	} else {
	    console.log(value1,"不等于",value2)
	}
	```

### <span id="2.4">运算符</span>
- 大多数与python一致，需要注意的在后面讨论
- 算术运算符：

	```js
	+   -    *    /     %       ++        -- 
	```

- 比较运算符：

	```js
	>   >=   <    <=    !=    ==    ===   !==
	```

- 逻辑运算符：

	```js
	&&   ||   ！
	```

- 赋值运算符：

	```
	js=  +=   -=  *=   /=
	```

- 字符串运算符：

	```js
	+  连接，两边操作数有一个或两个是字符串就做连接运算
	```

#### 算术运算符
##### 自加自减
- 设x=2，x++表达式执行后的值为3，x--表达式执行后的值为1
- i++相当于i=i+1，i--相当于i=i-1；
- 自增和自减运算符可以放在变量前也可以放在变量后：--i
- 多用于for循环

	```js
	var i=10;
	console.log(i++);
	console.log(i);
	console.log(++i);
	console.log(i);
	console.log(i--);
	console.log(--i);
	```

##### 单元运算符
```js
- 除了可以表示减号还可以表示负号  例如：x=-y
+ 除了可以表示加法运算还可以用于字符串的连接  例如："abc"+"def"="abcdef"
```

- 需要注意的是，JS是一门弱类型语言，在JS中，可以将字符串 '12' 和整数 3 进行连接得到字符串'123'，然后可以把它看成整数 123 ，所有这些都不需要任何的显示转换。

	```js
	var a = '12', b = 3, c = a+b;
	console.log(a, typeof a);
	console.log(b, typeof b);
	console.log(c, typeof c);
	var d = c-1;
	console.log(d, typeof d);
	```

##### NaN
```js
var d="chuck";
d=+d;
console.log(d);//NaN:属于Number类型的一个特殊值,当遇到将字符串转成数字无效时,就会得到一个NaN数据
console.log(typeof(d));//Number

//NaN特点:

var n=NaN;

console.log(n>3);
console.log(n<3);
console.log(n==3);
console.log(n==NaN);

console.log(n!=NaN);//NaN参与的所有的运算都是false,除了!=
```

#### 比较运算符
- 常用于控制语句

	```js
	if (2>1){
		console.log("条件成立!")
	}
	```

1. 全等号(===)和非全等号(!==)
	- 所做的运算与等号(==)和非等号(!=)相同
	- 但是在运算前，不执行类型转换

	```js
	console.log(2==2);
	console.log(2=="2");
	console.log(2==="2");
	console.log(2!=="2");
	```

2. 大小比较
	- 比较运算符两侧如果一个是数字类型，一个是其他类型，会将其类型转换成数字类型；
	- 比较运算符两侧如果都是字符串类型，比较的是最高位的asc码，如果最高位相等，继续取第二位比较。

	```js
	var result = "Blue" < "alpha";
	console.log(result);
	//字母B的ASCII码是66，字母a的ASCII码是97
	
	var result = "25" < "3";
	console.log(result); 
	//"2" 的ASCII码是 50，"3" 的ASCII码是 51
	
	var bResult = "25" < 3;
	console.log(result);
	//字符串 "25" 将被转换成数字 25，然后与数字 3 进行比较
	```

3. 比较运算符的类型转换规则
	1. 如果一个运算数是 Boolean 值，在检查相等性之前，把它转换成数字值。false 转换成 0，true 为 1； 
	2. 如果一个运算数是字符串，另一个是数字，在检查相等性之前，要尝试把字符串转换成数字； 
	3. 如果一个运算数是对象，另一个是字符串，在检查相等性之前，要尝试把对象转换成字符串； 
	4. 如果一个运算数是对象，另一个是数字，在检查相等性之前，要尝试把对象转换成数字。 

4. 比较运算符的其他规则
	1. 值 null 和 undefined 相等；
	2. 在检查相等性时，不能把 null 和 undefined 转换成其他值；
	3. 如果某个运算数是 NaN，等号将返回 false，非等号将返回 true； 
	4. 如果两个运算数都是对象，那么比较的是它们的引用值。如果两个运算数指向同一对象，那么等号返回 true，否则两个运算数不等。

#### 逻辑运算符
```js
if (2>1 && [1,2]){
    console.log("条件与")
}

//以下并不直接输出布尔值
console.log(1 && 3);//3
console.log(0 && 3);//0
console.log(0 || 3);//3
console.log(2 || 3);//2
```

### <span id="2.5">流程控制</span>
#### 顺序结构
- 从上到下顺序执行

	```js
	<script>
		console.log(“星期一”);
		console.log(“星期二”);
		console.log(“星期三”);
	</script>
	```

#### 分支结构
##### if-else
```js
if (表达式){
   语句１;
   ......
   } else{
   语句２;
   .....
   }
```

##### if-elif－else
```js
if (表达式1) {
    语句1;
}else if (表达式2){
    语句2;
}else if (表达式3){
    语句3;
} else{
    语句4;
}
```

##### switch-case
```js
switch (表达式) {
    case 值1:语句1;break;
    case 值2:语句2;break;
    case 值3:语句3;break;
    default:语句4;
}
```

#### 循环结构
##### for循环
- 方式一

	```js
	for(初始表达式;条件表达式;变化表达式){
		执行语句
		……
	}
	```
- 方式二

	```js
	for( 变量 in 数组或对象)
	    {
	        执行语句
	        ……
	    }
	```

##### while循环
```js
while (条件){
    语句1；
    ...
}
```


#### 异常处理
- js中较少有异常产生
	
	```js
	try {
	    //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
	}
	catch (e) {
	    // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
	    //e是一个局部变量，用来指向Error对象或者其他抛出的对象
	}
	finally {
	     //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
	}
	```

- 主动抛出异常 throw Error('xxxx')

## <span id="3.0">对象</span>
在JavaScript中除了null和undefined以外其他的数据类型都被定义成了对象，也可以用创建对象的方法定义变量，String、Math、Array、Date、RegExp都是JavaScript中重要的内置对象，在JavaScript程序大多数功能都是基于对象实现的。

```js
var aa=Number.MAX_VALUE; 
//利用数字对象获取可表示最大数
var bb=new String("hello JavaScript"); 
//创建字符串对象
var cc=new Date();
//创建日期对象
var dd=new Array("星期一","星期二","星期三","星期四"); 
//数组对象
```

<img src="http://chuann.cc/Web/Object-Classification.png" width="500px" height="auto">

### <span id="3.1">String对象</span>
#### 字符串对象的创建
- 变量 = “字符串”
- 字串对象名称 = new String (字符串)

	```js
	var str1="hello world";
	var str1= new String("hello word");
	```

#### 字符串对象的属性和方法
- x.length －－－－获取字符串的长度
- x.toLowerCase() －－－－转为小写
- x.toUpperCase()        －－－－转为大写
- x.trim()               －－－－去除字符串两边空格       

－－－－字符串查询方法

- x.charAt(index)         －－－－str1.charAt(index);－－－－获取指定位置字符，其中index为要获取的字符索引
- x.indexOf(findstr,index)－－－－查询字符串位置
- x.lastIndexOf(findstr)  

- x.match(regexp)         －－－－match返回匹配字符串的数组，如果没有匹配则返回null
- x.search(regexp)        －－－－search返回匹配字符串的首字符位置索引

	```js
	var str1="welcome to the world of JS!";
	var str2=str1.match("world");
	var str3=str1.search("world");
	console.log(str2[0]);  // 结果为"world"
	console.log(str3);     // 结果为15
	```

－－－－子字符串处理方法

- x.substr(start, length) －－－－start表示开始位置，length表示截取长度
- x.substring(start, end) －－－－end是结束位置

- x.slice(start, end)     －－－－切片操作字符串

	```js
	var str1="abcdefgh";
	var str2=str1.slice(2,4);
	var str3=str1.slice(4);
	var str4=str1.slice(2,-1);
	var str5=str1.slice(-3,-1);
	
	console.log(str2); //结果为"cd"
	
	console.log(str3); //结果为"efgh"
	
	console.log(str4); //结果为"cdefg"
	
	console.log(str5); //结果为"fg"
	```

- x.replace(findstr,tostr) －－－－    字符串替换
- x.split();                 －－－－分割字符串

	```js
	var str1="一,二,三,四,五,六,日"; 
	var strArray=str1.split(",");
	console.log(strArray[1]);//结果为"二"
	```
                           
- x.concat(addstr)         －－－－    拼接字符串


### <span id="3.2">Array对象</span>
#### 数组对象的创建
- 创建方式1:

	```js
	var arrname = [元素0,元素1,….];          
	// var arr=[1,2,3];
	```

- 创建方式2:
	
	```js
	var arrname = new Array(元素0,元素1,….); 
	// var test=new Array(100,"a",true);
	```

- 创建方式3:

	```js
	var arrname = new Array(长度); 
	//  初始化数组对象:
	var cnweek=new Array(7);
	cnweek[0]="星期日";
	cnweek[1]="星期一";
	cnweek[2]="星期二";
	cnweek[3]="星期三";
	cnweek[4]="星期四";
	cnweek[5]="星期五";
	cnweek[6]="星期六";
	```

#### 数组对象的属性和方法
- array.join()－－－－将数组元素拼接成字符串

	```js
	var arr1=[1, 2, 3, 4, 5, 6, 7];
	var str1=arr1.join("-");
	console.log(str1);  //结果为"1-2-3-4-5-6-7" 
	```
- array.concat()

	```js
	var a = [1,2,3];
	var b=a.concat(4,5) ;
	console.log(a.toString());  //返回结果为1,2,3            
	console.log(b.toString());  //返回结果为1,2,3,4,5
	```

- 数组排序reverse&sort
	- 这里自带的排序依据是按首字符的ASCII码值进行排序

	```js
	var arr1=[32, 12, 111, 444];
	//var arr1=["a","d","f","c"];
	
	arr1.reverse(); //颠倒数组元素
	console.log(arr1.toString());
	//结果为444,111,12,32
	
	arr1.sort();    //排序数组元素
	console.log(arr1.toString());
	//结果为111,12,32,444
	```
	- 如果想要按照数字大比较需要先自行定义一个函数

	```js
	arr=[1,5,2,100];
	function intSort(a,b){
	    if (a>b){
	        return 1;//-1
	    } else if(a<b){
	        return -1;//1
	    } else {
	        return 0
	    }
	}
	
	arr.sort(intSort);
	
	console.log(arr);
	//更简单的方法
	function IntSort(a,b){
	    return a-b;
	}
	```

- 数组切片操作

	```js
	//x.slice(start, end)
	var arr1=['a','b','c','d','e','f','g','h'];
	var arr2=arr1.slice(2,4);
	var arr3=arr1.slice(4);
	var arr4=arr1.slice(2,-1);
	
	console.log(arr2.toString());
	console.log(arr3.toString());
	console.log(arr4.toString());
	```

- 删除子数组

	```js
	//x. splice(start, deleteCount, value, ...)
	var a = [1,2,3,4,5,6,7,8];
	a.splice(1,2);
	console.log(a.toString());//a变为 [1,4,5,6,7,8]
	
	a.splice(1,1);
	console.log(a.toString());//a变为[1,5,6,7,8]
	
	a.splice(1,0,2,3);
	console.log(a.toString());//a变为[1,2,3,5,6,7,8]
	```

- 数组的push和pop

	```js
	//x.push(value, ...)  压栈
	//x.pop()             弹栈      
	//push是将value值添加到数组x的结尾
	//pop是将数组x的最后一个元素删除
	
	var arr1=[1,2,3];
	arr1.push(4,5);
	console.log(arr1);
	//结果为"1,2,3,4,5"
	arr1.push([6,7]);
	console.log(arr1);
	//结果为"1,2,3,4,5,6,7"
	arr1.pop();
	console.log(arr1);
	//结果为"1,2,3,4,5"
	```

- 数组的shift和unshift

	```js
	//x.unshift(value,...)
	//x.shift()
	//unshift是将value值插入到数组x的开始
	//shift是将数组x的第一个元素删除
	
	var arr1=[1,2,3];
	arr1.unshift(4,5);
	console.log(arr1);  //结果为"4,5,1,2,3"
	
	arr1. unshift([6,7]);
	console.log(arr1);  //结果为"6,7,4,5,1,2,3"
	
	arr1.shift();
	console.log(arr1);  //结果为"4,5,1,2,3"
	```

### <span id="3.3">Date对象</span>
#### 创建Date对象
- 方法1：不指定参数

	```js
	var nowd1=new Date();
	console.log(nowd1.toLocaleString( ));
	```
- 方法2：参数为日期字符串

	```js
	var nowd2=new Date("2004/3/20 11:12");
	console.log(nowd2.toLocaleString( ));
	var nowd3=new Date("04/03/20 11:12");
	console.log(nowd3.toLocaleString( ));
	```
- 方法3：参数为毫秒数

	```js
	var nowd3=new Date(5000);
	console.log(nowd3.toLocaleString( ));
	console.log(nowd3.toUTCString());
	```
- 方法4：参数为年月日小时分钟秒毫秒

	```js
	var nowd4=new Date(2004,2,20,11,12,0,300);
	console.log(nowd4.toLocaleString( ));//毫秒并不直接显示
	```

#### Date对象的方法—获取日期和时间
- getDate()                 获取日
- getDay ()                 获取星期
- getMonth ()               获取月（0-11）
- getFullYear ()            获取完整年份
- getYear ()                获取年
- getHours ()               获取小时
- getMinutes ()             获取分钟
- getSeconds ()             获取秒
- getMilliseconds ()        获取毫秒
- getTime ()                返回累计毫秒数(从1970/1/1午夜)

	```js
	function getCurrentDate(){
	    //1. 创建Date对象
	    var date = new Date();
	    //2. 获得当前年份
	    var year = date.getFullYear();
	    //3. 获得当前月份
	    var month = date.getMonth()+1;
	    //4. 获得当前日
	    var day = date.getDate();
	    //5. 获得当前小时
	    var hour = date.getHours();
	    //6. 获得当前分钟
	    var min = date.getMinutes();
	    //7. 获得当前秒
	    var sec = date.getSeconds();
	    //8. 获得当前星期
	    var week = date.getDay(); //没有getWeek
	    // 2014年06月18日 15:40:30 星期三
	    return year+"年"+changeNum(month)+"月"+day+"日 "+hour+":"+min+":"+sec+" "+parseWeek(week);
	}
	console.log(getCurrentDate());
	//自动补齐成两位数字的方法
	function changeNum(num){
		if(num < 10){
		    return "0"+num;
		}else{
		    return num;
		}
	}
	//将数字 0~6 转换成 星期日到星期六
	function parseWeek(week){
	    var arr = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"];
	    return arr[week];
	}
	```

#### Date对象的方法—设置日期和时间
- setDate(day_of_month)       设置日
- setMonth (month)                 设置月
- setFullYear (year)               设置年
- setHours (hour)         设置小时
- setMinutes (minute)     设置分钟
- setSeconds (second)     设置秒
- setMillliseconds (ms)       设置毫秒(0-999)
- setTime (allms)     设置累计毫秒(从1970/1/1午夜)

	```js
	var x=new Date();
	x.setFullYear (1997);    //设置年1997
	x.setMonth(7);        //设置月7
	x.setDate(1);        //设置日1
	x.setHours(5);        //设置小时5
	x.setMinutes(12);    //设置分钟12
	x.setSeconds(54);    //设置秒54
	x.setMilliseconds(230);        //设置毫秒230
	document.write(x.toLocaleString( )+"<br>");
	//返回1997年8月1日5点12分54秒
	
	x.setTime(870409430000); //设置累计毫秒数
	document.write(x.toLocaleString( )+"<br>");
	//返回1997年8月1日12点23分50秒
	```

#### Date对象的方法—日期和时间的转换
- getTimezoneOffset():
	- 8个时区×15度×4分/度=480;
	- 返回本地时间与GMT的时间差，以分钟为单位
- toUTCString()
	- 返回国际标准时间字符串
- toLocalString()
	- 返回本地格式时间字符串
- Date.parse(x)
	- 返回累计毫秒数(从1970/1/1午夜到本地时间)
- Date.UTC(x)
	- 返回累计毫秒数(从1970/1/1午夜到国际时间)

### <span id="3.4">Math对象</span>
属性方法：
- abs(x)    返回数的绝对值。
- exp(x)    返回 e 的指数。
- floor(x)对数进行下舍入。
- log(x)    返回数的自然对数（底为e）。
- max(x,y)    返回 x 和 y 中的最高值。
- min(x,y)    返回 x 和 y 中的最低值。
- pow(x,y)    返回 x 的 y 次幂。
- random()    返回 0 ~ 1 之间的随机数。
- round(x)    把数四舍五入为最接近的整数。
- sin(x)    返回数的正弦。
- sqrt(x)    返回数的平方根。
- tan(x)    返回角的正切。

	```js
	console.log(Math.random()); //获得随机数 0~1 不包括1.
	console.log(Math.round(1.5)); // 四舍五入
	//获取1-100的随机整数，包括1和100
	var num = Math.random();
	num = num * 10;
	num = Math.round(num);
	console.log(num);
	//============max  min=========================
	console.log(Math.max(1, 2));
	console.log(Math.min(1, 2));
	//-------------pow--------------------------------
	console.log(Math.pow(2, 4));
	```


### <span id="3.5">Function对象</span>
#### 函数的定义 
```js
function 函数名 (参数){     函数体;
    return 返回值;
}
```

- 可以使用变量、常量或表达式作为函数调用的参数
- 函数由关键字function定义
- 函数名的定义规则与标识符一致，大小写是敏感的
- 返回值必须使用return

- 用 Function 类直接创建函数的语法如下：
	- 说明函数只不过是一种引用类型，它们的行为与用 Function类明确创建的函数行为是相同的。

	```js
	var 函数名 = new Function("参数1","参数n","function_body");
	```

- js的函数加载执行与python不同，它是整体加载完才会执行，所以执行函数放在函数声明上面或下面都可以。

#### Function对象的属性与方法
- 函数属于引用类型，所以它们也有属性和方法

	```js
	function f1() {
	    var p=1;
	}
	console.log(f1.length);		//声明函数期望的参数个数
	console.log(f1.toString());	//将函数转成字符串
	```

#### Function 的调用
- 只要函数名写对即可,参数怎么填都不报错

	```js
	function func1(a,b){
	    console.log(a+b);
	}
	
	func1(1,2);  //3
	func1(1,2,3);//3
	func1(1);    //NaN
	func1();     //NaN
	```

- 函数定义不能被覆盖
	- 报错举例：

	```js
	function a(a,b){
	    alert(a+b);
	}
	
	var a=1;
	var b=2;
	a(a,b)
	```

#### 函数的内置对象arguments
- arguments的使用

	```js
	function add(a, b) {
	    console.log(a + b);//3
	    console.log(arguments.length);//2
	    console.log(arguments);//[1,2]
	}
	add(1, 2);
	```
- 场景一:多个数连加

	```js
	function func() {
	    var result = 0;
	    for (var num in arguments) {
	        result += arguments[num]
	    }
	    console.log(result)
	}
	func(1, 2, 3, 4, 5);
	```

- 场景二:手动检测参数的合法性

	```js
	function fun(a, b, c) {
	    if (arguments.length != 3) {
	        throw new Error("function f called with " + arguments.length + " arguments,but it just need 3 arguments")
	    }
	    else {
	        console.log("success!")
	    }
	}
	fun(1, 2, 3, 4, 5)
	```

#### 匿名函数
```js
var func = function(arg){
    return "tony";
}
```

- 匿名函数的应用
	- 定义后马上使用
	- 如果定义后赋给一个变量接收，是不符合匿名函数本义的

	```js
	(function(){
	    alert("tony");
	} )()
	
	(function(arg){
	    alert(arg);
	})('123')
	```


## <span id="4.0">BOM</span>
### window对象
- 所有浏览器都支持 window 对象。
- 概念上讲.一个html文档对应一个window对象.
- 功能上讲: 控制浏览器窗口的.
- 使用上讲: window对象不需要创建对象,直接使用即可.

#### Window 对象方法
- alert()            显示带有一段消息和一个确认按钮的警告框。
- confirm()          显示带有一段消息以及确认按钮和取消按钮的对话框。

	```js
	var result = confirm("您确定要删除吗?");
	alert(result);
	```

- prompt() 显示可提示用户输入的对话框。
	
	```js
	 var result = prompt("请输入一个数字!", "haha");
	 alert(result);
	```

- open() 打开一个新的浏览器窗口或查找一个已命名的窗口。
	- 打开和一个新的窗口并进入指定网址，参数1:网址.

	```js
	open("http://www.baidu.com");
	```

	- 参数1 什么都不填 就是打开一个新窗口，参数2.填入新窗口的名字(一般可以不填).参数3:新打开窗口的参数.

	```js
	open('','','width=200,resizable=no,height=100');
	```

- close() 关闭浏览器窗口。

	```js
	var result = confirm('是否关闭网页?');
    if (result == true){
        close();
    }
	```

- setInterval()      按照指定的周期（以毫秒计）来调用函数或计算表达式。
- clearInterval()    取消由 setInterval() 设置的 timeout。
- setTimeout()       在指定的毫秒数后调用函数或计算表达式。
- clearTimeout()     取消由 setTimeout() 方法设置的 timeout。

	```html
	<input id="ID1" type="text" onclick="begin()">
	<button onclick="begin()">开始</button>
	<button onclick="end()">停止</button>
	
	<script>
	    function showTime(){
	           var nowd2=new Date().toLocaleString();
	           var temp=document.getElementById("ID1");
	           temp.value=nowd2;
	    }
	    var ID;
	    function begin(){
	        if (ID==undefined){
	             showTime();
	             ID=setInterval(showTime,1000);
	        }
	    }
	    function end(){
	        clearInterval(ID);
	        ID=undefined;
	    }
	</script>
	```


- scrollTo()         把内容滚动到指定的坐标。

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







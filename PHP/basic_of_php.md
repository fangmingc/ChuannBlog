## php基础
- PHP原始为Personal Home Page的缩写，已经正式更名为 "PHP: Hypertext Preprocessor"
	- 是一种被广泛应用的开源通用脚本语言，尤其适用于 Web 开发并可嵌入 HTML 中去。
	- 它的语法利用了 C、Java 和 Perl，易于学习。
	- 该语言的主要目标是允许 web 开发人员快速编写动态生成的 web 页面，但 PHP 的用途远不只于此。
- 目录
	- [简介](#简介)
	- [php环境搭建](#php环境搭建)
	- [语法](#语法)
		- [变量、关键字、超全局变量](#变量、关键字、超全局变量)
		- [运算符](#运算符)
		- [流程控制](#流程控制)
		- [数据类型](#数据类型)
		- [函数](#函数)
		- [文件操作](#文件操作)
		- [错误与异常](#错误与异常)
		- [类和对象](#类和对象)
		- [扩展组件](#扩展组件)
		- [常用内置函数](#常用内置函数)


### 简介
- 介绍性的范例

	```html
	<html>
	    <head>
	        <title>Example</title>
	    </head>
	    <body>
	
	        <?php
	        echo "Hi, I'm a PHP script!";
	        ?>
	
	    </body>
	</html> 
	```
	- 请注意这个范例和其它用 C 或 Perl 语言写的脚本之间的区别:
		- 与用大量的命令来编写程序以输出 HTML 不同的是，PHP 页面就是 HTML，
		- 只不过在其中嵌入了一些代码来做一些事情（在本例中输出了 "Hi, I'm a PHP script!"）。
		- PHP 代码被包含在特殊的起始符和结束符 <?php 和 ?> 中，使得可以进出"PHP 模式"。 
	- 和客户端的 JavaScript 不同的是，PHP 代码是运行在服务端的。
		- 如果在服务器上建立了如上例类似的代码，则在运行该脚本后，客户端就能接收到其结果，但他们无法得知其背后的代码是如何运作的。
		- 甚至可以将 web 服务器设置成让 PHP 来处理所有的 HTML 文件，这么一来，用户就无法得知服务端到底做了什么。 
- php使用范围，主要用于以下三个领域： 
	- 服务端脚本。这是 PHP 最传统，也是最主要的目标领域。
		- 开展这项工作需要具备以下三点：PHP 解析器（CGI 或者服务器模块）、web 服务器和 web 浏览器。
		- 需要在运行 web 服务器时，安装并配置 PHP，然后，可以用 web 浏览器来访问 PHP 程序的输出，即浏览服务端的 PHP 页面。
		- 如果只是实验 PHP 编程，所有的这些都可以运行在自己家里的电脑中。请查阅安装一章以获取更多信息。 
	- 命令行脚本。
		- 可以编写一段 PHP 脚本，并且不需要任何服务器或者浏览器来运行它。
		- 通过这种方式，仅仅只需要 PHP 解析器来执行。这种用法对于依赖 cron（Unix 或者 Linux 环境）或者 Task Scheduler（Windows 环境）的日常运行的脚本来说是理想的选择。
		- 这些脚本也可以用来处理简单的文本。请参阅 PHP 的命令行模式以获取更多信息。  
	- 编写桌面应用程序。
		- 对于有着图形界面的桌面应用程序来说，PHP 或许不是一种最好的语言，但是如果用户非常精通 PHP，并且希望在客户端应用程序中使用 PHP 的一些高级特性，可以利用 PHP-GTK 来编写这些程序。
		- 用这种方法，还可以编写跨平台的应用程序。PHP-GTK 是 PHP 的一个扩展，在通常发布的 PHP 包中并不包含它。如果对 PHP-GTK 感兴趣，请访问其[网站](http://gtk.php.net/)以获取更多信息。 

### php环境搭建
- 安装apache2
	- `apt install apache2`
- 安装mysql
	- `apt install mysql-server mysql-client`
- 安装php
	- `apt install php7.0`

- 测试apache
	- 访问`http://127.0.0.1/`，展示apache相关信息则正常
- 测试php
	- 执行如下命令
		
		```linux
		cd /var/www/html
		vim hello.php
		```
	- 编写以下php脚本
	
		```php
		<?php
		  phpinfo()
		?>
		```
	- 访问`http://127.0.0.1/hello.php`，展示PHP版本及相关信息则正常
	- 可能遇到的问题：
		- 不解析php代码：
			- 原因：apache2未配置php解析
			- 解决方案：`apt install libapache2-mod-php`
			- 检查是否成功：`ls /usr/lib/apache2/modules | grep libphp`
		- 检查MySQL扩展：`php -m`查看是否有mysql或者mysqlli
			- 若无执行命令安装：`apt install php-mysql`

#### 项目相关
- 文件权限问题
	- 如果是通过`php php文件`执行php文件，操作文件的用户是root
	- 如果通过web访问的方式执行php文件，操作文件的用户是apache，apache的用户可以在配置文件中查看
		- apache2的执行用户和权限组为`www-data:www-data`
		- 通过`cat /etc/apache2/envvars`查看
	- 相关问题：
		- 在项目中自行定义了日志输出文件，如果不修改目标日志文件的读写权限给apache,会导致无法打开文件
		- `chown -R test:test test/`更改test文件夹及其子文件、文件夹的所属用户为test,所属用户组为test

## 语法
### 变量、关键字、超全局变量
#### 变量
- 命名规则
	1. 变量以`$`符号开头，其后是变量的名称
	2. 变量名称必须以字母或下划线开头
	3. 变量名称不能以数字开头
	4. 变量名称只能包含字母数字字符和下划线（`A-z`、`0-9` 以及 `_`）
	5. 变量名称对大小写敏感（`$y` 与 `$Y` 是两个不同的变量）
	6. php是弱类型语言，不需要定义时申明类型

		```php
		<?php
		$txt="Hello world!";
		$x=5;
		$y=10.5;
		?>
		```

- 作用域
	- 全局作用域
		- 函数外部申明的变量拥有全局作用域，只能在函数外部访问
		- 在函数内部使用global关键字申明的变量拥有全局作用域
	- 局部作用域
		- 函数内部申明的变量拥有局部作用域，只能在函数内部访问

			```php
			<?php
			$x=5; // 全局作用域
			
			function myTest() {
			  $y=10; // 局部作用域
			  echo "<p>测试函数内部的变量：</p>";
			  echo "变量 x 是：$x";
			  echo "<br>";
			  echo "变量 y 是：$y";
			} 
			
			myTest();
			
			echo "<p>测试函数之外的变量：</p>";
			echo "变量 x 是：$x";
			echo "<br>";
			echo "变量 y 是：$y";
			?>
			```
	- 静态作用域
		- 在函数内部使用static关键字申明的变量拥有静态作用域，不会随着函数的结束被回收

			```php
			<?php
			$x=5;
			$y=10;
			
			function myTest() {
			  global $x,$y;
			  $y=$x+$y;
			}
			
			myTest();
			echo $y; // 输出 15
			?>
			```
#### 关键字
1. `echo`
2. `if`  `elseif`  `else`
3. `for`
	1. `foreach`
4. `function`
	1. `return`
	2. `yield`
5. `class`
	1. `extension`
	2. `new`
	3. `private`
	4. `public`
	5. `abstract`
6. `aquire`
7. `include`
8. `include_once`
9. `isset`
10. `unset`
11. `array`
12. `exit`
13. `final`
14. `static`
15. `const`
16. `global`

#### 超全局变量
- 超全局变量是在全部作用域中始终可用的内置变量
1. `$_GET`
	- 关联数组，包含URL`?`后面的请求条件
2. `$_POST`
	- 关联数组，请求体的内容
3. `$_FILES`
	- HTTP 文件上传变量
4. `$_REQUEST`
	- HTTP Request 变量
5. `$_SESSION`
6. `$_COOKIE`
7. `$_SERVER`
	- 关联数组，服务器和执行环境信息
	- 常见：
		- URI：`$_SERVER["REQUEST_URI"]`
		- 请求方式：`$_SERVER['REQUEST_METHOD']`
8. `$GLOBALS`
	- 索引数组，包含所有全局变量
9. `$argv`
	- 传入php文件的参数



### 运算符
#### 算数运算符
- `+ - * / %`，加、减、乘、除、取余
- 需要注意的是
	- php中数字和字符串可以直接进行算数
	- 字符串转数字规则：
		- 如果该字符串没有包含 '.'，'e' 或 'E' 并且其数字值在整型的范围之内（由 PHP_INT_MAX 所定义），该字符串将被当成 integer 来取值。其它所有情况下都被作为 float 来取值。 
		- 该字符串的开始部分决定了它的值。如果该字符串以合法的数值开始，则使用该数值。否则其值为 0（零）。合法数值由可选的正负号，后面跟着一个或多个数字（可能有小数点），再跟着可选的指数部分。指数部分由 'e' 或 'E' 后面跟着一个或多个数字构成。 

			```php
			<?php
			$foo = 1 + "10.5";                // $foo is float (11.5)
			$foo = 1 + "-1.3e3";              // $foo is float (-1299)
			$foo = 1 + "bob-1.3e3";           // $foo is integer (1)
			$foo = 1 + "bob3";                // $foo is integer (1)
			$foo = 1 + "10 Small Pigs";       // $foo is integer (11)
			$foo = 4 + "10.2 Little Piggies"; // $foo is float (14.2)
			$foo = "10.0 pigs " + 1;          // $foo is float (11)
			$foo = "10.0 pigs " + 1.0;        // $foo is float (11)     
			?> 
			```
#### 赋值运算符 
- 普通赋值
	- `$a = 1`
	- `$b = $a`
- 组合运算
	- `$a = 3;`
	- `$a += 5; // sets $a to 8, as if we had said: $a = $a + 5;`
	- `$b = "Hello ";`
	- `$b .= "There!"; // sets $b to "Hello There!", just like $b = $b . "There!";`
- 引用赋值，表示两个变量指向同一个数据，没有拷贝任何东西
	- `$c = &$a`

### 流程控制

### 数据类型
1. 布尔值：true&false
2. 空值：null
3. 数字
4. 字符串
5. 数组


### 函数

### 文件操作

### 错误与异常

### 类和对象

### 扩展组件 

### 常用内置函数
1. `phpinfo ($what = null)`
	- 展示php解释器相关信息
2. `error_log ($message, $message_type = null, $destination = null, $extra_headers = null)`
	- 将`$message`写入php.ini中指定的日志文件
3. `var_export ($expression, $return = null)`
	- 查看php对象信息
	- `$return`为空直接echo，`$return`为true返回字符串
4. `var_dump ($expression, $_ = null)`
	- 打印php对象信息 
5. `print_r ($expression, $return = null)`
	- 打印php对象信息
6. `func_num_args()`
	- 返回函数接收的参数总数
7. `func_get_arg ($arg_num)`
	- 从函数接收的参数数组中取位于`$arg_num`的参数的值
8. `str_replace ($search, $replace, $subject, &$count = null)`
	- 字符串替换
9. `explode ($delimiter, $string, $limit = null)`
	- 将`$string`根据`$delimiter`切割成数组，类似python的字符串函数split
10. get_class ($object = null)
	- 获取`$object`所属类的类名
11. 



















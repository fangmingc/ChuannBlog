## php基础

- PHP原始为Personal Home Page的缩写，已经正式更名为 "PHP: Hypertext Preprocessor"
	- 是一种被广泛应用的开源通用脚本语言，尤其适用于 Web 开发并可嵌入 HTML 中去。
	- 它的语法利用了 C、Java 和 Perl，易于学习。
	- 该语言的主要目标是允许 web 开发人员快速编写动态生成的 web 页面，但 PHP 的用途远不只于此。


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


## 信呼oa开源项目学习
- [准备工作](#准备工作)
- [系统入口与开发调试](#系统入口与开发调试)
- [系统模块分析](#系统模块分析)
- [系统表结构分析](#系统表结构分析)

### 准备工作
- 环境搭建：apache2+php7+mysql
- 下载项目
	- `git clone git clone https://github.com/rainrocka/xinhu.git`
- 去除痕迹
	- `mv xinhu/ oa/`
	- `mv /webmain/install/ webmain/`
	- 删除install文件夹
	- 修改config/config.php下的`$config`数组为：

		```php
		$config		= array(
			'title'		=> 'OA',
			'url'		=> '',
			'urly'		=> '',	//官网域名地址，修改后就无法提供在线升级了。
			'db_host'	=> '127.0.0.1',
			'db_user'	=> 'root',
			'db_pass'	=> '',
			'db_base'	=> 'oa',
			'perfix'	=> 'oa_',
			'qom'		=> 'oa_',
			'highpass'	=> '',
			'install'	=> true,
			'version'	=> require('version.php'),
			'path'		=> 'index',
			'updir'		=> 'upload',
			'dbencrypt'	=> false,
			'sqllog'	=> true,
			'checksign'	=> false,			//列表请求是否验证
			'memory_limit'	=> '',			//运行内存大小
			'db_drive'		=> 'mysqli',	//数据库操作驱动
			'db_engine'		=> 'MyISAM',	//数据库默认引擎
			'debug'			=> true,	//默认debug模式
			'reim_show' 	=> true,	//首页是否显示REIM
			'mobile_show' 	=> true,	//首页是否显示手机版
			'accesslogs' 	=> false,	//是否记录访问日志和限制IP
			'upurl'			=> '', 		//上传文件附件地址(还不能使用)
		);
		```
	- 使用phpstorm打开远程项目
		- 全项目搜索`rockxinhu`并替换为`oa`
		- 全项目搜索`xinhu_`并替换为`oa_` **sql里面的也要改**
	- 创建数据库db： oa
		- `use oa;source /oa目录/webmain/rockxinhu.sql`

- 日志输出
	- 系统登陆日志
		- 数据库oa_log
	- 操作记录日志
		- 数据库oa_flow_log
	- 错误日志
		- 需要自行定义日志文件写入
		- 务必记得更改日志文件所属用户和权限组为www-data

- 路由系统
	- include->View.php
		
		```php
		$actpath	= $rock->strformat('?0/?1/?2?3',ROOT_PATH, $p, $d, $_m);
		define('ACTPATH', $actpath);
		$actfile	= $rock->strformat('?0/?1Action.php',$actpath, $m);
		$actfile1	= $rock->strformat('?0/?1Action.php',$actpath, $_m);
		```
		- 举例：访问webmain->home->index->indexAction.php->indexClassAction
			- url：http://localhost/index.php?m=index&d=index

### 系统入口与开发调试
1. 系统对外接口分析
	- 主页面：index.php
	- api：api.php
	- 任务：task.php
2. 配置文件：config /config.php
3. 路由系统：include/View.php
	- 匹配视图函数路径

		```php
		$actpath    = $rock->strformat('?0/?1/?2?3',ROOT_PATH, $p, $d, $_m);
		define('ACTPATH', $actpath);
		$actfile   = $rock->strformat('?0/?1Action.php',$actpath, $m);
		$actfile1  = $rock->strformat('?0/?1Action.php',$actpath, $_m);
		```
	- 执行视图函数，视图可直接终止本次请求并响应(通常为json)

		```php
		if(file_exists($actfile1))include_once($actfile1); // 导入视图
		if(file_exists($actfile)){
		   include_once($actfile);
		   $clsname   = ''.$m.'ClassAction';
		   $xhrock       = new $clsname();
		   $actname   = ''.$a.'Action';
		   if($ajaxbool == 'true')$actname    = ''.$a.'Ajax';
		    if(method_exists($xhrock, $actname)){
		      $xhrock->beforeAction();
		      $actbstr  = $xhrock->$actname(); // 执行视图
		      if(is_string($actbstr)){echo $actbstr;$xhrock->display=false;}
		      if(is_array($actbstr)){echo json_encode($actbstr);$xhrock->display=false;}
		    }else{
		      $methodbool = false;
		      if($ajaxbool == 'false')echo ''.$actname.' not found;';
		   }
		    $xhrock->afterAction();
		}else{
		   echo 'actionfile not exists;';
		   $xhrock       = new Action();
		```
4. Model表操作include/rockFun.php
	- 通过实例化m类获得指定表的操作对象，传入的name为表的后缀(除开表的前缀)
5. 日志分析方式
	- oa系统操作日志，存于数据库oa_flow_log表中
	- oa系统登陆日志，存于数据库oa_log表中
	- 系统运行日志
		- apache链接日志:`/var/log/apache2/access.log`
		- php日志，需要配置后方可使用:
			- 通过phpinfo()查明php.ini的位置，通常是: `/etc/php/7.0/apache2/php.ini`
			- 更改error_log = 日志文件路径(/var/php/error.log)
			- 修改日志文件夹的访问权限给apache: 
				- 命令: `chown -R www-data:www-data /var/php`
				- 重启apache2
	- 之后就可以通过error_log('日志消息')这个内置函数输出日志到指定日志文件


### 系统模块分析


### 系统表结构分析





## scrapy
- 基于twisted、整合其他模块的框架

### 安装
- 先装twisted
	- [详细参考](http://chuann.cc/Intermediate_Python/high-performance/twisted.md)
	- 在这里下载相应版本的twisted的whl文件：https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
	- 然后在whl文件目录使用`pip3 install whl文件`即可
- 然后
	- pip3 install scrapy

### 命令行工具
#### 查看帮助
- scrapy -h
- scrapy <command> -h

- 有两种命令
	- 其中Project-only必须切到项目文件夹下才能执行，
	- 而Global的命令则不需要
- Global commands:
	- startproject #创建项目
	- genspider    #创建爬虫程序
	- settings     #如果是在项目目录下，则得到的是该项目的配置
	- runspider    #运行一个独立的python文件，不必创建项目
	- shell        #scrapy shell url地址  在交互式调试，如选择器规则正确与否
	- fetch        #独立于程单纯地爬取一个页面，可以拿到请求头
	- view         #下载完毕后直接弹出浏览器，以此可以分辨出哪些数据是ajax请求
	- version      #scrapy version 查看scrapy的版本，scrapy version -v查看scrapy依赖库的版本
- Project-only commands:
	- crawl        #运行爬虫，必须创建项目才行，确保配置文件中ROBOTSTXT_OBEY = False
	- check        #检测项目中有无语法错误
	- list         #列出项目中所包含的爬虫名
	- edit         #编辑器，一般不用
	- parse        #scrapy parse url地址 --callback 回调函数  #以此可以验证我们的回调函数是否正确
	- bench        #scrapy bentch压力测试

#### 官网链接
[官方文档](https://docs.scrapy.org/en/latest/topics/commands.html)





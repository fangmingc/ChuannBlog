## 爬虫基础

### 爬虫原理
本质：模拟浏览器向服务器发送请求获取数据。

- 爬虫的比喻
	- 如果我们把互联网比作一张大的蜘蛛网，那一台计算机上的数据便是蜘蛛网上的一个猎物，而爬虫程序就是一只小蜘蛛，沿着蜘蛛网抓取自己想要的猎物/数据
- 爬虫的定义
	- 向网站发起请求，获取资源后分析并提取有用数据的程序 
- 爬虫的价值
	- 互联网中最有价值的便是数据，比如天猫商城的商品信息，链家网的租房信息，雪球网的证券投资信息等等，这些数据都代表了各个行业的真金白银，可以说，谁掌握了行业内的第一手数据，谁就成了整个行业的主宰，如果把整个互联网的数据比喻为一座宝藏，那我们的爬虫课程就是来教大家如何来高效地挖掘这些宝藏，掌握了爬虫技能，你就成了所有互联网信息公司幕后的老板，换言之，它们都在免费为你提供有价值的数据。

### 爬虫的基本流程
1. 分析
	- 分析是最重要的步骤
	- 首先分析目标数据或目标动作具体的位置
		- 如：分析访问拉钩网的职位信息
		- 请求URL:https://www.lagou.com/jobs/list_python
			- 可知通过更改url最后一个路径可以实现关键字搜索职位
		- 请求方式：GET
		- 请求头：
			- 清空浏览器所有缓存和cookie，访问url，众多请求中只有User-Agent是重要的，其余的不重要（通过不停测试得知）
			- User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
		- 请求体：
			- GET请求无请求体
2. 发送请求
	- response = request.get("https://www.lagou.com/jobs/list_python", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"})
3. 获取响应内容
	- 参考[requests模块](http://chuann.cc/Intermediate_Python/spider/requests.html)的响应部分内容
4. 解析内容
	- 利用re,beautifulsoup等模块解析内容
5. 保存数据
	- 利用mongodb、redis、mysql等存储数据

### 请求和响应
#### 请求request
以访问http://www.baidu.com为例
- 请求url
	- http://www.baidu.com
- 请求方法：
	- GET
- 请求头
	- 重要：
		- cookie
		- 用户代理
			- 请求者的身份
		- referer
			- 从何处跳转至本页面
	- 次要：
		- 请求的数据类型
		- 请求的数据编码
		- 请求的数据语言
		- 连接状态
		- 请求的域名
- 请求体
	- 构造form表单的数据

#### 响应
以访问http://www.baidu.com为例
- 响应的状态码
	- 200成功
	- 302重定向
- 响应体
	- html
		- 最常见的类型，通过解析库分析
	- json
		- API接口常用，直接就是大字典
	- 二进制
		- 图片
		- 视频
		- 其他格式


### 爬虫小结
1. 总结爬虫流程：
	- 爬取--->解析--->存储
2. 爬虫所需工具：
	- 请求库：requests,selenium
	- 解析库：正则，beautifulsoup，pyquery
	- 存储库：文件，MySQL，Mongodb，Redis
3. 爬虫常用框架
	- scrapy
4. 爬虫的实现其次，主要是要学会分析爬取的目标网站
	- 站点通过何种方式辨识用户?
	- 获取站点的数据需要哪些步骤？
	- 根据步骤制定爬虫方案


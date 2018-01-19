## MongoDB
一款强大、灵活、且易于扩展的通用型数据库。
- [介绍](#1)
- [MongoDB与SQL对比](#2)
- [安装与准备使用](#3)
- [基本数据类型](#4)
- [CRUD操作](#5)
	- [数据库操作](#51)
	- [集合操作](#52)
	- [文档操作](#53)
		- [增](#531)
		- [删](#532)
		- [改](#533)
		- [查](#534)

### <span id="1">介绍</span>
- 易用性
	- MongoDB是一个面向文档（document-oriented）的数据库，而不是关系型数据库。          
	- 不采用关系型主要是为了获得更好得扩展性。当然还有一些其他好处，与关系数据库相比，面向文档的数据库不再有“行“（row）的概念取而代之的是更为灵活的“文档”（document）模型。        
	- 通过在文档中嵌入文档和数组，面向文档的方法能够仅使用一条记录来表现复杂的层级关系，这与现代的面向对象语言的开发者对数据的看法一致。         
	- 另外，不再有预定义模式（predefined schema）：文档的键（key）和值（value）不再是固定的类型和大小。由于没有固定的模式，根据需要添加或删除字段变得更容易了。通常由于开发者能够进行快速迭代，所以开发进程得以加快。而且，实验更容易进行。开发者能尝试大量的数据模型，从中选一个最好的。
- 易扩展性
	- 应用程序数据集的大小正在以不可思议的速度增长。随着可用带宽的增长和存储器价格的下降，即使是一个小规模的应用程序，需要存储的数据量也可能大的惊人，甚至超出了很多数据库的处理能力。过去非常罕见的T级数据，现在已经是司空见惯了。
	- 由于需要存储的数据量不断增长，开发者面临一个问题：应该如何扩展数据库，分为纵向扩展和横向扩展，纵向扩展是最省力的做法，但缺点是大型机一般都非常贵，而且当数据量达到机器的物理极限时，花再多的钱也买不到更强的机器了，此时选择横向扩展更为合适，但横向扩展带来的另外一个问题就是需要管理的机器太多。
	- MongoDB的设计采用横向扩展。面向文档的数据模型使它能很容易地在多台服务器之间进行数据分割。MongoDB能够自动处理跨集群的数据和负载，自动重新分配文档，以及将用户的请求路由到正确的机器上。这样，开发者能够集中精力编写应用程序，而不需要考虑如何扩展的问题。如果一个集群需要更大的容量，只需要向集群添加新服务器，MongoDB就会自动将现有的数据向新服务器传送。
- 丰富的功能
	- MongoDB作为一款通用型数据库，除了能够创建、读取、更新和删除数据之外，还提供了一系列不断扩展的独特功能
	1. 索引
		- 支持通用二级索引，允许多种快速查询，且提供唯一索引、复合索引、地理空间索引、全文索引
	2. 聚合	
		- 支持聚合管道，用户能通过简单的片段创建复杂的集合，并通过数据库自动优化
	3. 特殊的集合类型
		- 支持存在时间有限的集合，适用于那些将在某个时刻过期的数据，如会话session。类似地，MongoDB也支持固定大小的集合，用于保存近期数据，如日志
	4. 文件存储
		- 支持一种非常易用的协议，用于存储大文件和文件元数据。MongoDB并不具备一些在关系型数据库中很普遍的功能，如链接join和复杂的多行事务。省略
	- 这些的功能是处于架构上的考虑，或者说为了得到更好的扩展性，因为在分布式系统中这两个功能难以高效地实现
- 卓越的性能
	- MongoDB的一个主要目标是提供卓越的性能，这很大程度上决定了MongoDB的设计。MongoDB把尽可能多的内存用作缓存cache，视图为每次查询自动选择正确的索引。总之各方面的设计都旨在保持它的高性能。
	- 虽然MongoDB非常强大并试图保留关系型数据库的很多特性，但它并不追求具备关系型数据库的所有功能。只要有可能，数据库服务器就会将处理逻辑交给客户端。这种精简方式的设计是MongoDB能够实现如此高性能的原因之一

### <span id="2">MongoDB与SQL对比</span>
<table><tr><th>SQL术语/概念</th><th>MongoDB术语/概念</th><th>解释说明</th></tr>
<tr><td>database</td><td>database</td><td>数据库</td></tr>
<tr><td>table</td><td>collection</td><td>数据库表/集合</td></tr>
<tr><td>row</td><td>document</td><td>数据记录/集合</td></tr>
<tr><td>column</td><td>field</td><td>数据字段/域</td></tr>
<tr><td>index</td><td>index</td><td>索引</td></tr>
<tr><td>table joins</td><td></td><td>表连接,MongoDB不支持</td></tr>
<tr><td>primary key</td><td>primary key</td><td>主键,MongoDB自动将_id字段设置为主键</td></tr></table>

```sql
# mysql
+----+-----------+--------------+
| id | name      | email        |
+----+-----------+--------------+
|  1 | 林海峰    | 1234@163.com |
|  2 | 武沛齐    | 1234@163.com |
+----+-----------+--------------+

# mongodb
{
        "_id" : ObjectId("5a61eca60793da2b97ba6900"),
        "name" : "林海峰",
        "eamil" : "1234@163.com"
}
{
        "_id" : ObjectId("5a61ecab0793da2b97ba6901"),
        "name" : "武沛齐",
        "eamil" : "1234@163.com"
}
```

#### 文档
- 文档是MongoDB的核心概念。文档就是键值对的一个有序集{'msg':'hello','foo':3}。类似于python中的有序字典。
- 注意：
	1. 文档中的键/值对是有序的。
	2. 文档中的值不仅可以是在双引号里面的字符串，还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
	3. MongoDB区分类型和大小写。
	4. MongoDB的文档不能有重复的键。
	5. 文档中的值可以是多种不同的数据类型，也可以是一个完整的内嵌文档。文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。
- 文档键命名规范：
	1. 键不能含有\0 (空字符)。这个字符用来表示键的结尾。
	2. 和$有特别的意义，只有在特定环境下才能使用。
	3. 以下划线"_"开头的键是保留的(不是严格要求的)。

#### 集合
- 集合就是一组文档。如果将MongoDB中的一个文档比喻为关系型数据的一行，那么一个集合就是相当于一张表。
- 集合存在于数据库中，通常情况下为了方便管理，不同格式和类型的数据应该插入到不同的集合，但其实集合没有固定的结构，这意味着我们完全可以把不同格式和类型的数据统统插入一个集合中。
- 组织子集合的方式就是使用“.”，分隔不同命名空间的子集合。
	- 比如一个具有博客功能的应用可能包含两个集合，分别是blog.posts和blog.authors，这是为了使组织结构更清晰，这里的blog集合（这个集合甚至不需要存在）跟它的两个子集合没有任何关系。
	- 在MongoDB中，使用子集合来组织数据非常高效，值得推荐
- 当第一个文档插入时，集合就会被创建。合法的集合名：
	- 集合名不能是空字符串""。
	- 集合名不能含有\0字符（空字符)，这个字符表示集合名的结尾。
	- 集合名不能以"system."开头，这是为系统集合保留的前缀。
	- 用户创建的集合名字不能含有保留字符。有些驱动程序的确支持在集合名里面包含，这是因为某些系统生成的集合中包含该字符。除非你要访问这种系统创建的集合，否则千万不要在名字里出现$。

#### 数据库
- 数据库在MongoDB中，多个文档组成集合，多个集合可以组成数据库
- 数据库也通过名字来标识。数据库名可以是满足以下条件的任意UTF-8字符串：
	1. 不能是空字符串（"")。
	2. 不得含有' '（空格)、.、$、/、\和\0 (空字符)。
	3. 应全部小写。
	4. 最多64字节。
- 有一些数据库名是保留的，可以直接访问这些有特殊作用的数据库。
	1. admin： 从身份认证的角度讲，这是“root”数据库，如果将一个用户添加到admin数据库，这个用户将自动获得所有数据库的权限。再者，一些特定的服务器端命令也只能从admin数据库运行，如列出所有数据库或关闭服务器
	2. local: 这个数据库永远都不可以复制，且一台服务器上的所有本地集合都可以存储在这个数据库中
	3. config: MongoDB用于分片设置时，分片信息会存储在config数据库中

#### 命令空间
- 把数据库名添加到集合名前，得到集合的完全限定名，即命名空间
- 如果要使用cms数据库中的blog.posts集合，这个集合的命名空间就是cmd.blog.posts。命名空间的长度不得超过121个字节，且在实际使用中应该小于100个字节

### <span id="3">安装与准备使用</span>
#### 安装
[下载](https://www.mongodb.com/download-center#community)

1. 安装路径为D:\MongoDB，将D:\MongoDB\bin目录加入环境变量
2. 新建目录与文件
	
	```dos
	D:\MongoDB\data\db
	D:\MongoDB\log\mongod.log
	```

3. 新建配置文件mongod.cfg,参考：https://docs.mongodb.com/manual/reference/configuration-options/

	```config
	systemLog:
	   destination: file
	   path: "D:\MongoDB\log\mongod.log"
	   logAppend: true
	storage:
	   journal:
	      enabled: true
	   dbPath: "D:\MongoDB\data\db"
	net:
	   bindIp: 0.0.0.0
	   port: 27017
	setParameter:
	   enableLocalhostAuthBypass: false
	```
 
4. 制作系统服务

	```dos
	mongod --config "D:\MongoDB\mongod.cfg" --bind_ip 0.0.0.0 --install
	或者直接在命令行指定配置
	mongod --bind_ip 0.0.0.0 --port 27017 --logpath D:\MongoDB\log\mongod.log --logappend --dbpath D:\MongoDB\data\db  --serviceName "MongoDB" --serviceDisplayName "MongoDB"  --install
	```

5. 启动\关闭

	```dos
	net start MongoDB
	net stop MongoDB
	```

6. 登录

	```dos
	mongo
	```

#### 账号管理
1. mongodb环境下，创建账号

	```sql
	use admin
	db.createUser(
	  {
	    user: "root",
	    pwd: "123",
	    roles: [ { role: "root", db: "admin" } ]
	  }
	)
	
	use test
	db.createUser(
	  {
	    user: "egon",
	    pwd: "123",
	    roles: [ { role: "readWrite", db: "test" },
	             { role: "read", db: "db1" } ]
	  }
	)
	```

2. 重启数据库

	```
	mongod --remove
	mongod --config "C:\mongodb\mongod.cfg" --bind_ip 0.0.0.0 --install --auth
	```

3. 登录：注意使用双引号而非单引号

	```
	mongo --port 27017 -u "root" -p "123" --authenticationDatabase "admin"
	```

	- 也可以在登录之后用db.auth("账号","密码")登录
	
	```
	mongo
	use admin
	db.auth("root","123")
	```
4. 其他
	- help查看帮助
	- mongo时一个简化的JavaScript shell，可以执行JavaScript脚本

[参考博客](https://www.cnblogs.com/zhoujinyi/p/4610050.html)

### <span id="4">基本数据类型</span>
- 概念上，MongoDB的文档与Javascript的对象相近，因而可以认为它类似于JSON。[JSON](http://www.json.org)是一种简单的数据表示方式：其规范仅用一段文字就能描述清楚（其官网证明了这点），且仅包含六种数据类型。
- 这样有很多好处：易于理解、易于解析、易于记忆。然而从另一方面说，因为只有null、布尔、数字、字符串、数字和对象这几种数据类型，所以JSON的表达能力有一定的局限。
- 虽然JSON具备的这些类型已经具有很强的表现力，但绝大数应用（尤其是在于数据库打交道时）都还需要其他一些重要的类型。例如，JSON没有日期类型，这使得原本容易日期处理变得烦人。另外，JSON只有一种数字类型，无法区分浮点数和整数，更别区分32位和64位了。再者JSON无法表示其他一些通用类型，如正则表达式或函数。
- MongoDB在保留了JSON基本键/值对特性的基础上，添加了其他一些数据类型。在不同的编程语言下，这些类型的确切表示有些许差异。

- 详细
	1. null：用于表示空或不存在的字段
		- d={'x':null}
	2. 布尔型：true和false
		- d={'x':true,'y':false}
	3. 数值
		- d={'x':3,'y':3.1415926}
	4. 字符串
		- d={'x':'egon'}
	5. 日期
		- d={'x':new Date()}
		- d.x.getHours()
	6. 正则表达式
		- d={'pattern':/^egon.*?nb$/i}
		- 正则写在／／内，后面的i代表:
			- i 忽略大小写
			- m 多行匹配模式
			- x 忽略非转义的空白字符
			- s 单行匹配模式
	7. 数组
		- d={'x':[1,'a','v']}
	8. 内嵌文档
		- user={'name':'egon','addr':{'country':'China','city':'YT'}}
		- user.addr.country
	9. 对象id:是一个12字节的ID,是文档的唯一标识，不可变
		- d={'x':ObjectId()}

- _id和ObjectId
	- MongoDB中存储的文档必须有一个"_id"键。这个键的值可以是任意类型，默认是个ObjectId对象。在一个集合里，每个文档都有唯一的“_id”,确保集合里每个文档都能被唯一标识。不同集合"_id"的值可以重复，但同一集合内"_id"的值必须唯一
	- ObjectId
		- ObjectId是"_id"的默认类型。因为设计MongoDb的初衷就是用作分布式数据库，所以能够在分片环境中生成唯一的标识符非常重要，而常规的做法：在多个服务器上同步自动增加主键既费时又费力，这就是MongoDB采用ObjectId的原因。
		- ObjectId采用12字节的存储空间，是一个由24个十六进制数字组成的字符串
	
			<table><tr><td>0|1|2|3|</td><td>4|5|6|</td><td>7|8 </td><td>9|10|11</td></tr><tr><td>时间戳</td><td>机器</td><td>PID</td><td>计数器</td></tr></table>

		- 如果快速创建多个ObjectId，会发现每次只有最后几位有变化。另外，中间的几位数字也会变化（要是在创建过程中停顿几秒）。这是ObjectId的创建方式导致的。
		1. 时间戳单位为秒，与随后5个字节组合起来，提供了秒级的唯一性。这个4个字节隐藏了文档的创建时间，绝大多数驱动程序都会提供一个方法，用于从ObjectId中获取这些信息。因为使用的是当前时间，很多用户担心要对服务器进行时钟同步。其实没必要，因为时间戳的实际值并不重要，只要它总是不停增加就好。
		2. 接下来3个字节是所在主机的唯一标识符。通常是机器主机名的散列值。这样就可以保证不同主机生成不同的ObjectId，不产生冲突
		3. 接下来连个字节确保了在同一台机器上并发的多个进程产生的ObjectId是唯一的
		4. 前9个字节确保了同一秒钟不同机器不同进程产生的ObjectId是唯一的。最后3个字节是一个自动增加的 计数器。确保相同进程的同一秒产生的ObjectId也是不一样的。
	- 自动生成_id
		- 如果插入文档时没有"_id"键，系统会自帮你创建 一个。可以由MongoDb服务器来做这件事。但通常会在客户端由驱动程序完成。这一做法非常好地体现了MongoDb的哲学：能交给客户端驱动程序来做的事情就不要交给服务器来做。
		- 这种理念背后的原因是：即便是像MongoDB这样扩展性非常好的数据库，扩展应用层也要比扩展数据库层容易的多。将工作交给客户端做就减轻了数据库扩展的负担。

### <span id="5">CRUD操作</span>
- *为空的数据不显示(空数据库/空集合)

#### <span id="51">数据库操作</span>
1. 增
	- use config #如果数据库不存在，则创建数据库，否则切换到指定数据库。
2. 查
	- show dbs #查看所有
	- 可以看到，我们刚创建的数据库config并不在数据库的列表中， 要显示它，我们需要向config数据库插入一些数据。db.table1.insert({'a':1})
3. 删
	- use config #先切换到要删的库下
	- db.dropDatabase() #删除当前库

#### <span id="52">集合操作</span>
1. 增
	- 当第一个文档插入时，集合就会被创建

	```sql
	> use database1
	switched to db database1
	> db.table1.insert({'a':1})
	WriteResult({ "nInserted" : 1 })
	> db.table2.insert({'b':2})
	WriteResult({ "nInserted" : 1 })
	```
2. 查

	```sql
	> show tables
	table1
	table2
	```

3. 删

	```sql
	> db.table1.drop()
	true
	> show tables
	table2
	```

#### <span id="53">文档操作</span>
- <span id="531">增</span>
	1. 没有指定_id则默认ObjectId,_id不能重复，且在插入后不可变
	2. 插入单条

		```sql
		user0={
		    "name":"egon",
		    "age":10,
		    'hobbies':['music','read','dancing'],
		    'addr':{
		        'country':'China',
		        'city':'BJ'
		    }
		}
		
		db.test.insert(user0)
		db.test.find()
		```
	3. 插入多条

		```sql
		user1={
		    "_id":1,
		    "name":"alex",
		    "age":10,
		    'hobbies':['music','read','dancing'],
		    'addr':{
		        'country':'China',
		        'city':'weifang'
		    }
		}
		
		user2={
		    "_id":2,
		    "name":"wupeiqi",
		    "age":20,
		    'hobbies':['music','read','run'],
		    'addr':{
		        'country':'China',
		        'city':'hebei'
		    }
		}
		
		
		user3={
		    "_id":3,
		    "name":"yuanhao",
		    "age":30,
		    'hobbies':['music','drink'],
		    'addr':{
		        'country':'China',
		        'city':'heibei'
		    }
		}
		
		user4={
		    "_id":4,
		    "name":"jingliyang",
		    "age":40,
		    'hobbies':['music','read','dancing','tea'],
		    'addr':{
		        'country':'China',
		        'city':'BJ'
		    }
		}
		
		user5={
		    "_id":5,
		    "name":"jinxin",
		    "age":50,
		    'hobbies':['music','read',],
		    'addr':{
		        'country':'China',
		        'city':'henan'
		    }
		}
		db.user.insertMany([user1,user2,user3,user4,user5])
		```
- <span id="532">删</span>
	1. 删除多个中的第一个

		```sql
		db.user.deleteOne({ 'age': 8 })
		```
	2. 删除国家为China的全部

		```
		db.user.deleteMany( {'addr.country': 'China'} ) 
		```
	3. 删除全部
		
		```
		db.user.deleteMany({}) 
		```
- <span id="533">改</span>


- <span id="534">查</span>

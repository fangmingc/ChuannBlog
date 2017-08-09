## python常用模块
<span id = "0"></span>
- [模块](4 Module and Package/4.1module.md)  
- [包](#2)
- [常用模块一](#3)
	- [collections](#3.1)
	- [time](#3.2)
	- [random](#3.3)
	- [os](#3.4)
	- [sys](#3.5)
	- [序列化](#3.6)
		- [json](#3.6.1)
		- [pickle](#3.6.2)
		- [shevle](#3.6.2)
	- [re](#3.7)
		- [re模块方法](#3.7.1)
		- [正则表达式](#3.7.2)
- [常用模块二](#4)
	- [hashlib](#4.1)
	- [configparse](#4.2)
	- [logging](#4.3)
[<p align = "right">Top</p>](#0) 
### <span id = "1">模块(module)</span>
#### 模块定义   
模块可以包含可执行的语句和函数的定义，模块内的语句目的是初始化模块，而且只在import语句第一次导入该模块时才执行。  
简单说就是把一些常用方法封装到一个文件，不需要每次编程都写一长串的方法。  
#### 模块的导入和使用  
- import ...
	- ... 为模块名
	- 使用模块内的方法：
		- module.method()
- from ... import ...
	- 第一个...为模块名，第二个...为模块内的方法
	- 直接使用方法：
		- method()
- as 启用别名
	- import moudle as my
		- my.method()
	- from module import method as my
		- my()
- from module import \*
	1. 会将模块内所有非私有变量全部导入
	2. 不建议使用这种方式导入，易产生混乱
	3. 可以在模块内使用\_\_all__进行约束
		- \_\_all__ = ['允许使用的方法名'，...]
#### 注意事项
1. 模块必须和执行文件处于同一级目录下
2. 模块内的变量名如果以一个下划线，开头表示私有变量不能被引用
3. 如果模块既被其他脚本引用，自身也在使用，应当利用__name__在自身使用和被引用时表现出不同值的特点进行控制
```python
if __name__ == '__main__'
    模块自身运行时执行的代码
```
4. 自定义的模块名不应当和系统内置或者安装的模块名重复
#### 深入理解
1. 导入模块，是新建一块名称空间，存放模块内的名字，并将里面的名字与模块名进行绑定，以便在执行文件引用
2. 模块搜索路径
	- sys.path可以查看
	- 顺序为：
		1. 当前目录下的模块
		2. 内置模块
		3. 安装的拓展模块
3. 导入当前目录下的模块时会生成编译的模块缓存文件，以便下一次更快地加载模块
	- 系统会检测文件修改时间以判断是否重新编译模块
4. dir()函数可以查看模块内定义的方法，不会列出内置函数或者变量的名字
[<p align = "right">Top</p>](#0) 
### <span id = "2">包（package）</span>
#### 定义
- 将多个模块封装到文件夹进行管理、使用
- 文件夹下应该有__init__.py文件
#### 包的导入和使用
- 使用
	- package.module.method()
- import ...
	- ... 为包或者包内模块的名字
- from ... import ...
	- 第一个...为包或者包内模块名，第二个...为包或者模块或者模块内的方法
- as 启用别名
	- import package/package.moudle as my
	- from p/p.m import p/p.m/p.m.method as my
- from p/p.m import *
	- 会将包内或者模块内所有非私有变量全部导入
	- 不建议使用这种方式导入，易产生混乱
	- 可以在__init__.py使用__all__进行约束
#### 注意事项
- python3中可以没有__init__文件，python2中必须有该文件
- __init__.py内可以为空，也可以是初始化包的代码
#### 绝对导入和相对导入
- 当包内有多级包，互相需要调用的时候
- 推荐使用相对导入
- 绝对导入
	- from p/p.m import m
	- 优点：模块可以执行
	- 缺点：如果修改了包的整体目录结构，需要手动修改文件
	- 适用于个人使用的包
- 相对导入
	- 同级目录下
		- from后面跟一个点，可以接模块名
		- from ./.m import module/method 
	- 更高级目录
		- 退几级就有几个.
		- from ..p/..p.m/..m import module/method
	- 优点：如果修改了包的整体目录结构, 不需要手动修改文件
	- 缺点：模块不能执行
	- 适用于只交给其他地方调用的包
[<p align = "right">Top</p>](#0) 
### <span id = "3">常用模块一</span>
#### <span id = "3.1">collections模块</span>
在内置数据类型（dict、list、set、tuple）的基础上，collections模块还提供了几个额外的数据类型：Counter、deque、defaultdict、namedtuple和OrderedDict等。

##### namedtuple(name,el_nm_seq)
生成可以使用名字来访问元素内容的tuple
```python
import collections

s_tuple = collections.namedtuple('chuck', ['x', 'y'])
t = s_tuple(3, 8)
print(s_tuple.__name__)
print(t.x)
```
##### deque()
双向队列，可以快速的从另外一侧追加和推出对象  
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

deque是为了高效实现插入和删除操作的双向列表（链表实现），适合用于队列和栈：
```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```
##### OrderedDict()
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。  
如果要保持Key的顺序，可以用OrderedDict：  
```python
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```
##### defaultdict()
带有默认值的字典

##### Counter()
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
[<p align = "right">Top</p>](#0) 
#### <span id="3.2">时间模块</span>
- 模块内函数一览：
>time（） - 从Epoch以浮点数返回当前时间（以秒为单位）  
clock（） - 返回CPU进程作为浮点开始时间  
sleep（） - 作为浮点数给定的秒数延迟  
gmtime（） - 将Epoch的秒数转换为UTC元组  
localtime（） - 将Epoch的秒数转换为本地时间元组  
asctime（） - 将时间元组转换为字符串  
ctime（） - 将时间转换为字符串  
mktime（） - 将本地时间元组转换为自Epoch以来的秒  
strftime（） - 根据格式规范将时间元组转换为字符串  
strptime（） - 根据格式规范解析时间元组的字符串  
tzset（） - 更改本地时区    
##### 时间元组（struct_time）
使用九位整数组成一个元组表示本地时间。

	year (including century, e.g. 1998)  
	month (1-12)  
	day (1-31)  
	hours (0-23)  
	minutes (0-59)  
	seconds (0-59)  
	weekday (0-6, Monday is 0)  
	Julian day (day in the year, 1-366)  
	DST (Daylight Savings Time) flag (-1, 0 or 1)  

###### 时间元组属性
0	tm_year	2008  
1	tm_mon	1 到 12  
2	tm_mday	1 到 31  
3	tm_hour	0 到 23  
4	tm_min	0 到 59  
5	tm_sec	0 到 61 (60或61 是闰秒)  
6	tm_wday	0到6 (0是周一)  
7	tm_yday	1 到 366(儒略历)  
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜  
##### time.time()
返回自1970年1月1日午夜（历元）开始到当前时间的时间戳，经过运算可以得到当前的具体时间.  
```python
import time

print(time.time())
```
>时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。 
##### time.localtime([seconds])
接收一个秒为单位的时间戳，转成时间元组输出。  
不传入参数则返回当前本地时间戳的时间元组。
```python
import time

local_time = time.localtime(time.time())

print(local_time)
```
e.g.:
>time.struct_time(tm_year=2017, tm_mon=8, tm_mday=4, tm_hour=16, tm_min=13, tm_sec=5, tm_wday=4, tm_yday=216, tm_isdst=0)
##### time.asctime(p_tuple=None) 
接收一个时间元组，转换为时间的字符串。  
不传入参数则返回当前本地时间的字符串。
```python
import time

print(time.asctime(time.localtime()))
```
e.g.
>Fri Aug  4 16:19:38 2017
##### time.strftime(format, p_tuple=None)
fromat指定时间输出格式和位置，格式和位置参考下文；  
p_tuple指定时间元组进行转换，不指定则使用当前时间。  

>%Y  Year with century as a decimal number.  
    %m  Month as a decimal number [01,12].  
    %d  Day of the month as a decimal number [01,31].  
    %H  Hour (24-hour clock) as a decimal number [00,23].  
    %M  Minute as a decimal number [00,59].  
    %S  Second as a decimal number [00,61].  
    %z  Time zone offset from UTC.  
    %a  Locale's abbreviated weekday name.  
    %A  Locale's full weekday name.  
    %b  Locale's abbreviated month name.  
    %B  Locale's full month name.  
    %c  Locale's appropriate date and time representation.  
    %I  Hour (12-hour clock) as a decimal number [01,12].  
    %p  Locale's equivalent of either AM or PM.  
```python
import time

print(time.strftime('%Y %m %d'))
```
e.g.:
>2017 08 04
##### time.sleep(sceonds)
接收一个秒数的浮点数，延迟程序的运行，时长为给定的秒数。
[<p align = "right">Top</p>](#0) 
#### <span id = "3.3">random模块</span>
```python
import random
```
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：   
1. choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。  
2. randrange ([start,] stop [,step]) 	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1  
3. random() 	随机生成下一个实数，它在[0,1)范围内。  
4. seed([x]) 	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。  
5. shuffle(lst) 	将序列的所有元素随机排序  
6. uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。  
[<p align = "right">Top</p>](#0) 
#### <span id = "3.4">os模块</span>
- os.walk()
walk()方法语法格式如下：  
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])  
	- top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
	- topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
	- onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
	- followlinks -- 设置为 true，则通过软链接访问目录。

os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径  
os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd  
os.makedirs('dirname1/dirname2')    可生成多层递归目录  
os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推  
os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname  
os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname  
os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印  
os.remove()  删除一个文件  
os.rename("oldname","newname")  重命名文件/目录  
os.stat('path/filename')  获取文件/目录信息  
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"  
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"  
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:  
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'  
os.system("bash command")  运行shell命令，直接显示  
os.popen("bash command)  运行shell命令，获取执行结果  
os.environ  获取系统环境变量  


os.path  
os.path.abspath(path) 返回path规范化的绝对路径   
os.path.split(path) 将path分割成目录和文件名二元组返回   
os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素   
os.path.basename(path) 返回path最后的文件名。如果path以／或\结尾，那么就会返回空值。  
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False  
os.path.isabs(path)  如果path是绝对路径，返回True  
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False  
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False  
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略  
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间  
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间  
os.path.getsize(path) 返回path的大小  

#### <span id = "3.5">sys模块</span>
- sys.argv           
	- 命令行参数List，第一个元素是程序本身路径
- sys.exit(n)        
	- 退出程序，正常退出时exit(0)
- sys.version        
	- 获取Python解释程序的版本信息
- sys.maxsize         
	- 单个位的最大整数
- sys.path           
	- 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
- sys.platform       
	- 返回操作系统平台名称
[<p align = "right">Top</p>](#0) 
#### <span id = "3.6">序列化模块</span>
将原本的字典、列表等内容转换成一个字符串的过程就叫做序列化。  
- 序列化的目的
	1. 以某种存储形式使自定义对象持久化；
	2. 将对象从一个地方传递到另一个地方。
	3. 使程序更具维护性。
##### <span id = "3.6.1">json</span>
用于字符串 和 python数据类型间进行转换，编程界通用的转换，只能转化字典和列表
- dumps(obj)
	- 将obj转换成字符串
- loads(str)
	- 将json格式的字符串转换成相应的数据类型
- dump(obj, fp)
	- 将obj写入文件fp
- load(fp)
	- 读取文件fp的内容，转成相应的数据类型，文件内只能有一个数据类型（数据类型内的嵌套不算）
##### <span id = "3.6.1">pickle</span>
用于python特有的类型 和 python的数据类型间进行转换, 不仅可以序列化字典，列表, 还可以把python中任意的数据类型序列化  
- dump(object, file)
- dumps(object) -> string
- load(file) -> object
- loads(string) -> object
##### <span id = "3.6.2">shelve</span>
python新出的序列化工具，比pickle用起来更简单一些。  
只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。 
- open(filename)
```python
import shelve
d = shelve.open(filename) # open, with (g)dbm filename -- no suffix

d[key] = data   # store data at key (overwrites old data if
           	 	# using an existing key)
data = d[key]   # retrieve a COPY of the data at key (raise
            	# KeyError if no such key) -- NOTE that this
            	# access returns a *copy* of the entry!
del d[key]      # delete data stored at key (raises KeyError
            	# if no such key)
flag = key in d # true if the key exists
list = d.keys() # a list of all existing keys (slow!)

d.close()       # close it
```
[<p align = "right">Top</p>](#0) 
#### <span id = "3.7">re</span>
- re模块vs正则表达式  
	- 正则表达式 
		独立的一个东西和python是两个系统
	- re 
		python的一个模块
##### <span id = "3.7.1">re模块方法</span>
##### <span id = "3.7.2">正则表达式</span>
做字符串匹配的一个规则，在编程界占据很重要的地位，尤其在python，因python擅长爬虫，爬虫需要对大量字符串数据进行处理。  
- 关于等价   
. [] ^ $四个字符是所有语言都支持的正则表达式，所以这四个是基础的正则表达式。  
正则难理解因为里面有一个等价的概念，这个概念大大增加了理解难度，让很多初学者看起来会懵，如果把等价都恢复成原始写法，自己书写正则就超级简单了，就像说话一样去写你的正则了
###### 通用基础字符
- 基本用法示例  
	[0135] 匹配单个0-3的数字  
	[0135][0135][0135] 匹配三个0-3的数字  
	[0-9] 匹配单个0-9的数字  
	[a-z] 匹配单个小写字母  
	[A-Z] 匹配单个大写字母  
	[0-9a-zA-Z] 匹配单个数字、小写字母、大写字母  
- .  
匹配除\r\n之外的任意字符
- []  
	- [字符组范围]  匹配符合字符组范围的单个字符
	- 字符组  同一个位置上可以出现的字符的范围
- ^  
	- 放在表达式开头表示匹配字符串的开头
		- ^[0-9]表示数字开头
	- 放在字符组内开头表示匹配不符合字符组范围的字符
		- [^8]表示除了匹配8以外的字符
- $  
	- 放在表达式末表示匹配字符串的结尾
###### 元字符
- \  
	- 转义符，与后面的字符组成固定、有特殊意义的匹配格式(\\\\匹配自身)
- \w  等价[A-Za-z_0-9]  
	- 匹配字母或数字或下划线（word）
- \W  等价[^A-Za-z_0-9]  
	- 匹配\w无法匹配的
- \s  等价[ ]  
	- 匹配空格（space）
- \S  等价[^ ]  
	- 匹配非空白符
- \d  等价[0-9]  
	- 匹配数字（digit）
- \D  等价[^0-9]  
	- 匹配非数字
- \n    
	- 匹配换行符
- \t    
	- 匹配制表符
- \b  等价\s+  
	- 匹配一个单词的结尾
- a|b    
	- 匹配字符a或字符b
- ()    
	- 将(  ) 之间的表达式定义为“组”（group）,最多9个，它们可以用 \1 到\9 的符号来引用
###### 量词
- {n}
	- 匹配n次
- {n,m}
	- 最少匹配n次，最多匹配m次，n<=m
- {n,}  
	- 最少匹配n次，最多不限
- \*  等价{0, }  
	- 匹配零次或无限次
- \+  等价{1，}
	- 匹配一次或无限次
- ?	 等价{0,1}
	- 匹配零次或一次
- 贪婪匹配
	- 尽可能多的匹配
	- 正则默认贪婪匹配
- 非贪婪匹配
	- 仅在在量词之后使用 ? 表示非贪婪匹配
[<p align = "right">Top</p>](#0) 
### <span id = "4">常用模块二</span>
#### <span id = "4.1">hashlib</span>

#### <span id = "4.2">configparse</span>

#### <span id = "4.2">logging</span>

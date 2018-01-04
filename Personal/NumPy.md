## NumPy

### ndarry--多维数组
- 创建
	- np.array()
	- 数组大小不可修改
	- 数组对象类型都必须是一样的
- 方法
	- T 转置
	- dtype 查看类型
	- size 最外层有多长
		- 二维数组arr,有多少行len(arr)，有多少列len(arr[0])
	- shape 返回维度大小（元组形式）
	- ndim 数组的维数
- 数据类型dtype
	- 布尔型 bool
	- 整型 int_ int8 int16 int32 int 64
	- 无符号整型 uint8 uint16 uint32 uint64
	- 浮点型 float_ float16 float32 float64
	- 复数型 complex_ complex
- 创建ndarray
	- array() 将列表转换为数组，可选择显式指定dtype
	- arange() range的numpy版，支持浮点数
	- linspace() 类似arange()，第三个参数为数组长度，返回线性空间
	- zeros(shape,dtype) 根据指定形状和dtype创建全0数组
		- np.zeros((2,3), dtype='int')
	- ones(shape,dtype) 据指定形状和dtype创建全1数组
		- np.ones((3,4),dtype='int')
	- empty(shape,dtype) 据指定形状和dtype创建空数组（残留值），比zeros快一点
		- np.empty((3,4))
	- eye(shape, dtype) 据指定形状和dtype创建单位矩阵
		- np.eye(4, dtype='int')
- 索引和切片
	- 数组和标量之间的运算
		- 任何运算
	- 同样大小数组之间的运算 (对应位的数运算)
		- 加减乘除
	- 数组的索引
		- 一维数组 a[3]
		- 多维数组
			- a[2][3]
			- a[2,3] (推荐)
	- 数组的切片
		- 一维数组：a[5:8] a[4:]
		- 多位数组：a[1:2, 3:4] a[:.3:5]
	- 与列表不同，数组切片时并不会自动复制，在切片数组上的修改会影响原数组
		- 解决方法copy()
- 布尔型索引
	- a = [2,4,5]
	- b = [True, False, True]
	- a[b] = [2,5]
	- arr[arr>5]
- 花式索引

### 通用函数
- 能同时对数组中所有元素进行运算的函数
- 常见通用函数
	- 一元函数
		- abs 取绝对值
		- sqrt  
			- np.abs(arr) ** 0.5
			- np.sqrt(np.abs(arr))
		- 对浮点数取整
			- ceil:向上取整
			    - 3.6->4 
			    - 3.1->4
			    - -3.6->-3
			    - -3.1->-3
			- floor:向下取整
			    - 3.6->3
			    - 3.1->3
			    - -3.6->-4
			    - -3.1->-4
			- rint(round):四舍五入
			    - 3.6->4
			    - 3.1->3
			    - -3.6->-4
			    - -3.1->-3
			- trunc(int):向零取整（舍去小数点）
			    - 3.6->3
			    - 3.1->3
			    - -3.6->-3
			    - -3.1->-3
	    - modf 整数小数分离
		    - 返回元组，一个小数数组，一个整数数组
	    - isnan
	    - isinf
    - 二元函数
	    - 加、减、乘、除、取余。。。。
	    - maxinum 取最小值
	    - mininum 取最大值

- 特殊浮点数
	- nan(Not a Number) 不等于任何浮点数(nan != nan)
	- inf(infinity) 比任何浮点数都大
- 创建特殊值
	- np.nan
	- np.inf
- 数据分析中，nan常被用作表示数据缺失值


### 数学和统计方法
- sum 求和
- mean 求平均数
- cumsum 求前缀和
	- 用于快速求一维数组一段值的和
- var 求方差
	- 方差表示这组数的离散程度
- std 求标准差
	- 方差开根号

### 随机数生成
- numpy.random
	- rand([shape])
	- randint(start, end, [shape]) 随机整数
	- choices(数组或列表) 随机选一个
	- shuffle(数组或列表) 随机打乱
	- uniform(strat, end, [shape])  随机小数





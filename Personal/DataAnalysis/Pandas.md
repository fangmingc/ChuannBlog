## pandas
- 强大的python数据分析工具包
- 基于numpy构建

### 主要功能
- 具备DataFrame、Series

### Series
- 类似一维数组，由一组数据和一组与之对应的标签数组
	- 普通创建
		- sr = pd.Series([-4,2,5,6])
			- sr[0]
	- 标签创建
		- sr = pd.Series([-4,2,5,6], index=['a', 'b', 'c', 'd']) 
			- sr[0]
			- sr['a']
		- sr = pd.Series(0, index=['a', 'b', 'c', 'd'])
		- sr = pd.Series({'a':1, 'b':2})
	- 像列表和字典的结合体
- 特性
	- 可以通过数组创建
	- 可以和标量进行计算
	- 两个Series运算
	- 下标切片、标签切片(包括最后一个)
	- 具备通用函数
	- 布尔值索引
	- 统计函数
	- 支持in操作
		- 使用for循环时，获取的是值不是键(标签)
	- 支持.get(‘标签’)
- 注意
	- 当pandas对象的标签为整数的时候，在用索引取值时，整数不再被解读为下标而是标签
	- sr = pd.Series(np.arange(1,6), index[1,2,3,4,5])
		- sr[0] 不存在
		- sr[1] 表示1
		- sr[-1] 不存在
	- sr = pd.Series(np.arange(1,6), index['a','b','c','d','e'])
		- sr[0] 表示1
		- sr[1] 表示2
		- sr[-1] 表示6
- 数据对齐
	- 按照标签对齐

- 处理NaN
	- dropna() 删除nan
	- fillna() nan填充指定值
	- isnull() 
	- notnull() 

- 方法
	- sr.isin(list)
		- list,循环sr中每一个值，判断是否在list中，返回布尔值sr


### DataFrame
- 表格型数据结构，含有一组有序的列
	- 看作由Series组成的二维结构
	- index
	- columns
- 创建
	- DaraFrame(data=None, index=None, columns=None, dtype=None, copy=False)
		- data，可以是字典、二维数组、列表、迭代器等
		- index，指定行索引

- 索引切片
	- 基本索引
		- df\[列标签\]\[行标签或下标\]
		- df\[行下标:行下标]
	- 标签索引
		- df.loc\[行标签(,列标签)]
		- df.at\[行标签,列标签]
	- 位置索引
		- df.iloc\[行下标(,列下标)]
		- df.iat\[行下标,列下标]
	- 条件索引
		- df\[条件]
			- eg:`df[df>0]`

- 方法
	- df.dtypes
		- 查看每列的数据类型
	- df.head(n=5)
		- n，展示前n条数据
	- df.tail(n=5)
		- n，展示后n条数据
	- df.index
		- 查看索引
	- df.columns
		- 查看列名
	- df.values
		- 查看数据体
	- df.describe()
		- 查看对数据的简短描述
		- count，列计数
		- mean，平均值
		- std，标准差
		- min，列最小值
		- 25%
		- 50%
		- 75%
		- max，列最大值
	- df.T/df.transpose()
		- 矩阵的逆置
		- 将行列以及相应数据互换
	- df.copy()
		- 浅拷贝
	- df.sort_index(axis=1,ascending=False)
		- 通过axis排序，0为按行索引，1为列标签
			- axis："轴"，即坐标轴，dataframe有两个坐标轴，纵轴为0，横轴为1，这是沿用numpy的概念，numpy支持多维数据结构通过axis区分
	- df.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)
		- excel_writer是写模式的文件句柄
		- 将df写入excel_writer，
	- df.to_dict()
		- 将df转为字典
	











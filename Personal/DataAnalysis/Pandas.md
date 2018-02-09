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
	- df\[列标签\]\[行标签或下标\]
	- df.loc[行标签,列标签]
	- df.iloc[行下标,列下标]

- 方法
	- df.T/df.transpose()
		- 矩阵的逆置
		- 将行列以及相应数据互换
	- df.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)
		- excel_writer是写模式的文件句柄
		- 将df写入excel_writer，
	- df.to_dict()
		- 将df转为字典

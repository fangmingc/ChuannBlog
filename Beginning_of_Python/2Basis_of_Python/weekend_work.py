# coding=utf-8
#    颜川广
# 2017年7月21日


"""
1、执行 Python 脚本的两种方式
    1.1 在cmd中使用“python” + “文件名”可以执行文件名以.py结尾的python脚本
    1.2 在pycharm和其他集成开发环境（IDE）中直接解释运行
"""


# 5、Python 单行注释和多行注释分别用什么？
#     5.1 单行注释以“#”作为注释开头
#     5.2 多行注释用“'''”或者“"""”作为注释开头和结尾，同一段注释必须在前后使用两个“'''”或者“"""”


"""
6、声明变量注意事项有那些？
    注意：
        1）不得和python内置的关键字重名
        2）不得使用纯数字作为变量名
        3）必须是字母、数字、下划线的有限组合
        4）尽量将变量名命名得有意义
        5）当变量名全部大写的时候，默认为常量名
"""


# # 8、如何查看变量在内存中的地址?
# n = 7
# print('n = 7\n变量n的内存地址是：', id(7))


"""
9、执行 Python 程序时，自动生成的.pyc文件的作用是什么？
    .pyc文件是由.py文件经过编译后生成的字节码文件，比.py文件加载更快，还可以隐藏源码
"""


# # 10、写代码
# # a.实现用户输入用户名和密码，当用户名为seven且密码为123时，显示登陆成功，否则登陆失败！
# user = {'seven': '123'}
# name = input('Please input username:').strip()
# password = input('Please input password:').strip()
# if name in user and password == user[name]:
#     print('Login successful!')
# else:
#     print('Login failure!')
#
# # b.实现用户输入用户名和密码，当用户名为seven且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次
# user = {'seven': '123'}
# cnt = 0
# while cnt < 3:
#     name = input('Please input username:').strip()
#     password = input('Please input password:').strip()
#     if name in user and password == user[name]:
#         print('Login successful!')
#         break
#     else:
#         print('Login failure! You only have %d chance!' % (2-cnt))
#         cnt += 1
#
# # c.实现用户输入用户名和密码，当用户名为seven或alex且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次
# user = {
#     'seven': '123',
#     'alex': '123'
# }
# cnt = 0
# while cnt < 3:
#     name = input('Please input username:').strip()
#     password = input('Please input password:').strip()
#     if name in user and password == user[name]:
#         print('Login successful!')
#         break
#     else:
#         print('Login failure! You only have %d chance!' % (2-cnt))
#         cnt += 1


# # 11、写代码
# # a.	 使用 while 循环实现输出 2	- 3	+	4	- 5	+	6	...	+	100	 的和
# cnt = 2
# s = 0
# while cnt < 101:
#     s += cnt * ((-1) ** cnt)
#     cnt += 1
# print(s)
#
# # b.	 使用 for 循环和 range 实现输出 1	- 2	+	3	- 4	+	5	- 6	...	+	99	 的和
# s = 0
# for cnt in range(1, 100):
#     s += cnt * ((-1) ** (cnt - 1))
# print(s)
#
# # c.	 使用 while 循环实现输出 1，2，3，4，5，  7，8，9，  11，12
# cnt = 1
# while cnt < 13:
#     if cnt == 6:
#         print(end=' ')
#     elif cnt == 10:
#         print(end='  ')
#     elif cnt == 12:
#         print(cnt)
#     else:
#         print(cnt, end=', ')
#     cnt += 1
#
# # d.	 使用 while 循环实现输出 1-100	 内的所有奇数
# cnt = 1
# while cnt < 100:
#     if cnt % 2 != 0:
#         print('%2d' % cnt, end=' ')
#     if cnt % 20 == 0:
#         print('')
#     cnt += 1
#
# # e.	 使用 while 循环实现输出 1-100	 内的所有偶数
# cnt = 1
# while cnt < 100:
#     if cnt % 2 == 0:
#         print('%2d' % cnt, end=' ')
#     if cnt % 20 == 0:
#         print('')
#     cnt += 1


# 12、分别书写数字 5，10，32，7 的二进制表示
# num = [5, 10, 32, 7]
# for i in range(len(num)):
#     print('{:2d}的二进制表示：{:8}'.format(num[i], bin(num[i])))


# 14、现有如下两个变量，请简述 n1和 n2是什么关系？
# n1 = 123
# n2 = 123
# print(id(n1), type(n1), n1)
# print(id(n1), type(n1), n1)
# print(n1 is n2)
# 通过上面的代码可以看出n1和n2的id、type、值完全一样，除了变量名不一样，其余的特征完全一样，说明n1,n2指向的是同一块内存空间


# 15、现有如下两个变量，请简述 n1	 和 n2	 是什么关系？
#   15.1 pycharm中，通过下面这段代码可以看出n1,n2完全一样，指向同一块内存空间
# n1 = 123456
# n2 = 123456
# print(id(n1), type(n1), n1)
# print(id(n1), type(n1), n1)
# print(n1 is n2)
#   15.2 cmd中的python解释器下，下面的代码显示n1,n2的id是不同的，说明指向的不是同一块内存
"""
>>>n1 = 123456
>>>n2 = 123456
>>> print(id(n1), type(n1), n1)
626003253200 <class 'int'> 123456
>>> print(id(n2), type(n2), n2)
626003253168 <class 'int'> 123456
>>> print(n1 is n2)
False
"""


# 16、现有如下两个变量，请简述 n1	 和 n2	 是什么关系？
# n1 = 123456
# n2 = n1
#       因n2由n1赋值，n1,n2必然完全相同，指向同一块内存空间


# # 17、如有一下变量 n1	=	5，请使用 int 的提供的方法，得到该变量最少可以用多少个二进制位表示？
# n1 = 5
# print(n1.bit_length())
# # 通过int.bit_length()可以得出n1可以由3个二进制位表示


# 18、布尔值分别有什么？
#     布尔值分别有True和False两个值
#       通常情况下，当一个变量不为空的时候表示True,标量为空的时候为False
#       通常，数字0表示False，数字不为0表示True


"""
19、阅读代码，请写出执行结果
a = "alex"
b = a.capitalize()
print(a)
print(b)
请写出输出结果：
Alex
alex
"""


# # # 20、写代码，有如下变量，请按照要求实现每个功能
# name = " aleX"
# # a.	移除 name 变量对应的值两边的空格，并输入移除有的内容
# name = name.strip()
# print('a.', name)
#
# # b.	 判断 name 变量对应的值是否以 "al"	 开头，并输出结果
# print('b.{}是否以"al"开头：{}'.format(name, name.startswith('al')))
#
# # c.	 判断 name 变量对应的值是否以 "X"	 结尾，并输出结果
# print('c.{}是否以"X结尾：{}'.format(name, name.endswith('X')))
#
# # d.	 将 name 变量对应的值中的 “l” 替换为 “p”，并输出结果
# print('d.{}中的 “l” 替换为 “p”：{}'.format(name, name.replace('l', 'p')))
#
# # e.	 将 name 变量对应的值根据 “l” 分割，并输出结果。
# print('e.{}根据 “l” 分割：{}'.format(name, name.split('l')))
#
# # f.	 请问，上一题 e	 分割之后得到值是什么类型？
# # 分割后得到的值是列表类型
# print('f.{}的类型是：{}'.format(name.split('l'), type(name.split('l'))))
#
# # g.	 将 name 变量对应的值变大写，并输出结果
# print('g.{}全部变大写：{}'.format(name, name.upper()))
#
# # h.	 将 name 变量对应的值变小写，并输出结果
# print('h.{}全部变小写：{}'.format(name, name.lower()))
#
# # i.	 请输出 name 变量对应的值的第 2 个字符？
# print('i.{}的第 2 个字符是:{}'.format(name, name[1]))
#
# # j.	 请输出 name 变量对应的值的前 3 个字符？
# print('j.{}的前3 个字符是:{}'.format(name, name[:3]))
#
# # k.	 请输出 name 变量对应的值的后 2 个字符？
# print('k.{}的后2 个字符是:{}'.format(name, name[-2:]))
#
# # l.	 请输出 name 变量对应的值中 “e” 所在索引位置？
# print('l.{}中的"e"的索引是：{}'.format(name, name.index('e')))


# # 21、字符串是否可迭代？如可以请使用 for 循环每一个元素？
# # 字符串可以迭代
# string = 'abcdefghijklmopq'
# print(string)
# for i in range(len(string)):
#     print(string[i])


# # 22、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li	 ＝ ['alex',	'eric',	'rain']
# li = ['alex', 'eric', 'rain']
# string = '_'.join(li)
# print(string)


# # 22、写代码，有如下列表，按照要求实现每一个功能
# li = ['alex', 'eric', 'rain']
# print("li = ['alex', 'eric', 'rain']")
# # a.	计算列表长度并输出
# print('a.列表li的长度是：{}'.format(len(li)))
#
# # b.	 列表中追加元素 “seven”，并输出添加后的列表
# li.append('seven')
# print('b.列表li追加“seven”：{}'.format(li))
#
# # c.	 请在列表的第 1	 个位置插入元素 “Tony”，并输出添加后的列表
# li.insert(0, 'Tony')
# print('c.列表li第1个位置插入元素 “Tony”：{}'.format(li))
#
# # d.	 请修改列表第 2	 个位置的元素为 “Kelly”，并输出修改后的列表
# li[1] = 'Kelly'
# print('d.修改列表li第2个位置元素为 “Kelly”：{}'.format(li))
#
# # e.	 请删除列表中的元素 “eric”，并输出修改后的列表
# li.remove('eric')
# print('e.删除列表li中的元素 “eric”：{}'.format(li))
#
# # f.	 请删除列表中的第 2	 个元素，并输出删除的元素的值和删除元素后的列表
# li2 = ['alex', 'rain', 'apple', 'mac', 'tesla', 'home', 'car', 'eric']
# print('f.删除列表li2中的第2个元素{}'.format(li2.pop(1)))
# print('  删除列表li2中的第2个元素后：{}'.format(li2))
#
# # g.	 请删除列表中的第 3	 个元素，并输出删除元素后的列表
# li2.pop(2)
# print('g.删除列表li2中的第3个元素后：{}'.format(li2))
#
# # h.	 请删除列表中的第 2 至 4 个元素，并输出删除元素后的列表
# for i in range(3, 0, -1):
#     li2.pop(i)
# print('h.删除列表li2中的第2至4个元素后：{}'.format(li2))
#
# # i.	 请将列表所有的元素反转，并输出反转后的列表
# li3 = ['alex', 'rain', 'apple', 'mac', 'tesla', 'home', 'car', 'eric']
# print('i.当前列表li3:{}'.format(li3))
# li3.reverse()
# print('  将列表li3所有元素反转：{}'.format(li3))
#
# # j.	 请使用 for、len、range 输出列表的索引
# print('j.列表li3的索引：')
# for i in range(len(li3)):
#     print(i, end=' ')
# print()
#
# # k.	 请使用 enumerate 输出列表元素和序号（序号从 100 开始）
# for o, e in enumerate(li3, 100):
#     print(o, e)
#
# # l.	 请使用 for 循环输出列表的所有元素
# for i in range(len(li3)):
#     print(li3[i])


# # 23、写代码，有如下列表，请按照功能要求实现每一个功能
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'],	123, 446]
# # a.	 请输出 “Kelly”
# print(li[2][1][1])
#
# # b.	 请使用索引找到 'all'	 元素并将其修改为 “ALL”
# print(li)
# li[2][2] = 'ALL'
# print(li)


# # 24、写代码，有如下元组，按照要求实现每一个功能
# tu = ('alex', 'eric', 'rain')
# print("tu = ('alex', 'eric', 'rain')")
# # a.	 计算元组长度并输出
# print('a.元组tu的长度是：{}'.format(len(tu)))
#
# # b.	 获取元组的第 2	 个元素，并输出
# print('b.元组tu的第2个元素是：{}'.format(tu[1]))
#
# # c.	 获取元组的第 1-2	 个元素，并输出
# print('b.元组tu的第1-2个元素是：{},{}'.format(*tu[:2]))
#
# # d.	请使用 for 输出元组的元素
# for i in range(len(tu)):
#     print(tu[i])
#
# # e.	 请使用 for、len、range 输出元组的索引
# for i in range(len(tu)):
#     print(i, end=' ')
# print()
#
# # f.	请使用 enumerate 输出元祖元素和序号（序号从 10 开始）
# for o, e in enumerate(tu, 10):
#     print(o, e)

#
# # 25、有如下变量，请实现要求的功能
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# # a.讲述元祖的特性
# #    1）元组内部元素不可改变，创建元组的时候就固定了元素，如果要改变元组内部元素需要重新创建元组
# #    2）由于特性1），元组少了很多操作，比起列表，内存占用更省空间
#
# # b.请问 tu 变量中的第一个元素 “alex” 是否可被修改？
# #    不可修改
#
# # c.请问 tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
# #     tu变量中的"k2"对应的值是列表类型，可以被修改
# print(tu)
# tu[1][2]['k2'].append('Seven')
# print(tu)
#
# # d.请问 tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
# #     tu变量中的"k3"对应的值是元组类型，不可以被修改


# # 26、字典
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# # a.	 请循环输出所有的 key
# for key in dic:
#     print(key)
# for key in dic.keys():
#     print(key)
# for k, v in dic.items():
#     print(k)
#
# # b.	 请循环输出所有的 value
# for val in dic.values():
#     print(val)
# for key in dic:
#     print(dic[key])
# for key in dic.keys():
#     print(dic[key])
# for k, v in dic.items():
#     print(v)
#
#  # c.	 请循环输出所有的 key 和 value
# for k, v in dic.items():
#     print(k, ':', v)
#
#  # d.	 请在字典中添加一个键值对，"k4":	"v4"，输出添加后的字典
# dic['k4'] = 'v4'
# dic.setdefault('k4', 'v4')
# print(dic)
#
#  # e.	 请在修改字典中 “k1” 对应的值为 “alex”，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
#
#  # f.	 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
#
#  # g.	 请在 k3 对应的值的第 1	 个位置插入个元素 18，输出修改后的字典
# dic['k3'].insert(0, 18)
# print(dic)


# # 28、求 1-100 内的所有数的和
# summ = 0
# for i in range(1, 100):
#     summ += i
# print(summ)
# print(sum(range(100)))


# # 29、元素分类
# # 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66的值保存至字典的第一个 key 中，将小于 66	 的值保存至第二个 key 的值中。
# # 即： {'k1': 大于 66 的所有值,'k2':小于 66 的所有值}
# l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# dic = {
#     'k1': [],
#     'k2': []
# }
# for i in range(len(l)):
#     if l[i] > 66:
#         dic['k1'].append(l[i])
#     elif l[i] < 66:
#         dic['k2'].append(l[i])
# print(dic)

#
# # 30、购物车
# # 功能要求：
# # 要求用户输入总资产，例如：2000
# # 显示商品列表，让用户根据序号选择商品，加入购物车
# # 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# goods = [
#         {"name": "电脑", "price": 1998},
#         {"name": "鼠标", "price": 38},
#         {"name": "游艇", "price": 888},
#         {"name": "美女", "price": 998},
#         {"name": "水果", "price": 88},
#         {"name": "奔驰", "price": 99998},
#     ]
# cart = []
# balance = 0
# while True:
#     balance2 = input('请输入资产(q退出)：').strip()
#     if balance2 and balance2.isdigit():
#         balance += int(balance2)
#         # 购物环节
#         while True:
#             # 打印商品信息
#             for i in range(len(goods)):
#                 print("{} {name} {price:5}".format(i + 1, **goods[i]))
#             # 根据指令执行相关功能
#             cmd = input('请用序号选择商品！(q退出，c购物车)').strip()
#             # 输入数字表示购物
#             if cmd and cmd.isdigit():
#                 # 当所选商品存在
#                 if cmd in (str(i) for i in range(1, len(goods)+1)):
#                     # 确保商品数量正确
#                     while True:
#                         num = input('请输入购买数量：').strip()
#                         if num and num.isdigit() and (int(num) < 100):
#                             # 检测所选商品在购物车是否已经存在
#                             for ck in range(len(cart)):
#                                 # 当所选商品在购物车已经存在，改变购物车该商品数量
#                                 if goods[int(cmd) - 1]['name'] == cart[ck][0]:
#                                     cart[ck] = (cart[ck][0], cart[ck][1], int(cart[ck][2]) + int(num))
#                                     break
#                             else:
#                                 # 当所选商品在购物车中不存在，添加进购物车
#                                 cart.append((goods[int(cmd) - 1]['name'], goods[int(cmd) - 1]['price'], int(num)))
#                             print('已加入购物车！')
#                             break
#                         else:
#                             print('请输入有效数量(1-99)！')
#                 else:
#                     print('商品未上架！')
#             # 输入c查看购物车
#             elif cmd == 'c' or cmd == 'cart':
#                 while True:
#                     # 打印购物车并计算商品总价
#                     total = 0
#                     for i in range(len(cart)):
#                         print('{}{:6}{:3}'.format(*cart[i]))
#                         total += cart[i][1] * cart[i][2]
#                     print('商品总计：{:6}\n账户余额：{:6}'.format(total, balance))
#                     cmd2 = input('(b确认购买，q退出)').strip()
#                     if cmd2 and cmd2 == 'b':
#                         if total == 0:
#                             print('购物车是空的！')
#                         # 当余额大于总价显示购买成功并清空购物车
#                         elif balance > total:
#                             balance -= total
#                             cart.clear()
#                             print('购买成功！')
#                             break
#                         # 当余额不足，显示余额不足，不清空购物车
#                         else:
#                             print('余额不足！')
#                     elif cmd2 == 'quit' or cmd2 == 'q':
#                         break
#                     else:
#                         print('请输入有效指令')
#             elif cmd == 'quit' or cmd == 'q':
#                 break
#             else:
#                 print('请输入有效指令！')
#     elif balance2 == 'quit' or balance2 == 'q':
#         break
#     else:
#         print('请输入有效数字！')

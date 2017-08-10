# 实现员工信息表
# 文件存储格式如下：
# 	id，name，age，phone，job
# 	1,Alex,22,13651054608,IT
# 	2,Egon,23,13304320533,Tearcher
# 	3,nezha,25,1333235322,IT
#
# 现在需要对这个员工信息文件进行增删改查。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。
# 示例：
# select name,age where age>22
# select * where job=IT
# select * where phone like 133
#
# 进阶选做：
# b.可创建新员工记录，id要顺序增加
# c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值”  where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
#      其他需求尽量用函数实现


import os
import functools
inspect = {
    'status': False,
    'permission': 10,
}


# 打印列表
def show(data):
    if not data:
        pass
    else:
        for i in range(len(data)):
            for j in range(len(data[i])):
                print(data[i][j], end=', ')
            print()


# 判断从读取文件的一行字符串是否为空或者注释
def judge_line(line):
    """Function to judge the blank line or comment.

    Receive a string from a line of file and judge whether this line is blank line or comment.
    :param line: Receive a string.
    :return:
    """
    if len(line) < 4:
        return True
    elif line[0] == '#':
        return True
    else:
        return False


# 从指定文件名加载数据
def load_data(filename):
    """Function to load data.

    :return: Return a list which element is single information.
    """
    data = []
    with open(filename, 'r') as rf:
        for line in rf:
            if judge_line(line):
                continue
            # 文件一行有四个逗号，为员工信息文件
            elif line.count(',') == 4:
                temp = line.strip('\n').split(',')
                data.append([int(temp[0]), temp[1], int(temp[2]), temp[3], temp[4]])
            # 文件一行有三个逗号，为用户信息文件
            elif line.count(',') == 2:
                temp = line.strip('\n').split(',')
                data.append([temp[0], temp[1], int(temp[2])])
    return data


# 登录函数，成功返回True，失败返回False
def sign_in():
    """Function to sign in.

    :return: True for signing in successfully, False for failure.
    """
    data = load_data('Account')
    while True:
        username = input("'quit' or 'q' to quit\nPlease input \033[1;34musername\033[0m:").strip()
        if username in ('quit', 'q'):
            return False
        elif username:
            for i in range(len(data)):
                if username == data[i][0]:
                    while True:
                        password = input("'quit' or 'q' to quit\nPlease input \033[1;34mpassword\033[0m:")
                        if not password:
                            print('Password can not be empty!')
                        elif password == data[i][1]:
                            inspect['permission'] = data[i][2]
                            print('Login successful!')
                            return True
                        elif password in ('quit', 'q'):
                            return False
                        else:
                            print('Password is incorrect!')
            else:
                print('Username is incorrect!')


# Decorator to judge the permission to execute the function.
def permission(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if inspect['permission'] <= 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('You do not have permission to use this feature.')
    return inner


# Decorator to check the login status of user.
def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if inspect['status']:
            ret = func(*args, **kwargs)
            return ret
        else:
            print("Continue after login!")
            if sign_in():
                inspect['status'] = True
                ret = func(*args, **kwargs)
                return ret
    return inner


# 根据给定的条件从员工信息文件筛选，返回结果
def search(column_index, i, logic, cmd):
    """"""
    be_data = load_data('Employee_info_table')
    af_data = []
    for j in range(len(be_data)):
        if logic == '>=' and int(be_data[j][i]) >= int(cmd):
            af_data.append(be_data[j])
        elif logic == '<=' and int(be_data[j][i]) <= int(cmd):
            af_data.append(be_data[j])
        elif logic == '!='and be_data[j][i] != cmd:
            af_data.append(be_data[j])
        elif logic == '<>' and be_data[j][i] != cmd:
            af_data.append(be_data[j])
        elif logic == '>' and int(be_data[j][i]) > int(cmd):
            af_data.append(be_data[j])
        elif logic == '<' and int(be_data[j][i]) < int(cmd):
            af_data.append(be_data[j])
        elif logic == '=' and str(be_data[j][i]) == str(cmd):
            af_data.append(be_data[j])
        elif logic == 'like' and str(be_data[j][i]).count(cmd) > 0:
            af_data.append(be_data[j])
    if len(column_index) == 5:
        data = af_data
    else:
        data = []
        for k in range(len(af_data)):
            temp = list(af_data[k][column_index[n]] for n in range(len(column_index)))
            data.append(temp)
    return data


# 将select语句的范围和条件进一步拆分
@auth
def command_select(c_n1, cmd):
    """"""
    column_name = ['id', 'name', 'age', 'phone', 'job']
    logics = ['>=', '<=', '!=', '<>', '>', '<', '=', 'like']
    # 把列名对应的索引储存进c_n2
    if c_n1.count('*') > 0:
        c_n2 = range(len(column_name))
    else:
        c_n2 = tuple(i1 for i1 in range(len(column_name)) if c_n1.count(column_name[i1]) > 0)
    if not c_n2:
        print('Please specify the effective range!')
        return
    for i2 in range(len(logics)):
        if cmd.count(logics[i2]) > 0:
            logic = tuple(cmd.split(logics[i2])[j].strip() for j in range(len(cmd.split(logics[i2]))))
            if logic[0] in column_name:
                return search(c_n2, column_name.index(logic[0]), logics[i2], logic[1])
    else:
        print('Please specify the effective logic!')


# 将add语句的的添加信息进行鉴别，写入文件
@auth
def command_add(info, filename='Employee_info_table'):
    """"""
    if len(info) != 4:
        print('Please input valid information!\nlike:\nadd jack,18,1234568911,student')
        return False
    data = load_data(filename)
    name = (data[i][1] for i in range(len(data)))
    job = ('Teacher', 'IT', 'Student', 'Employee')
    job_lower = tuple(job[i].lower() for i in range(len(job)))
    item = list(info[i].strip() for i in range(len(info)))
    # 如果信息为空则初始化信息
    for j in range(4):
        if j == 0 and not item[j]:
            print('name can not be empty!')
            return False
        elif j == 1 and not item[j]:
            item[j] = str(16)
        elif j == 2 and not item[j]:
            item[j] = '***********'
        elif j == 3 and not item[j]:
            item[j] = 'Employee'
    # 给信息添加id，追加进文件
    if item[0].isalpha():
        if item[0] not in name:
            if int(item[1]) in range(16, 100):
                if len(item[2]) in (6, 11):
                    if item[3].lower() in job_lower:
                        with open(filename, 'a', encoding='utf-8')as wf:
                            ind = job_lower.index(item[3].lower())
                            wf.write(','.join((str(data[-1][0]+1), *item[:-1], job[ind]))+'\n')
                            print('Add successfully!')
                            return True
                    else:
                        print('This job can not be added!\nYou can add these:\n{}'.format(job))
                else:
                    print('Invalid phone number!(6/11 phone number is valid)')
            else:
                print('Invalid age!(16-99 is valid)')
        else:
            print('This name has existed.')
    else:
        print('Name is invalid!')
    return False


# 从delete语句给定的id或者name确定唯一员工，从文件删除
@auth
@permission
def command_delete(obj, filename='Employee_info_table'):
    """
    sadadssadfdsag
    """
    if obj.isdigit() or obj.isalpha():
        with open(filename, encoding='utf-8') as rf, \
                open(filename + '_swap', 'w', encoding='utf-8') as wf:
            for line in rf:
                if judge_line(line):
                    wf.write(line)
                elif obj == line.split(',')[0] or obj == line.split(',')[1]:
                    print('Delete successfully!')
                    continue
                else:
                    wf.write(line)
        os.remove(filename)
        os.rename(filename + '_swap', filename)
        return True
    else:
        print('Please input valid command!')
        return False


# 将set语句的范围和条件给select函数得到筛选好的结果，对结果进行修改
@auth
@permission
def command_set(change, condition):
    """"""
    column_name = ('name', 'age', 'phone', 'job')
    cha = tuple(change.split('=')[i].strip().strip('"') for i in range(len(change.split('='))))
    if len(cha) == 2 and cha[0] in column_name:
        select_data = command_select('*', condition)
        data = load_data('Employee_info_table')
        if select_data:
            for i in range(len(select_data)):
                select_data[i][column_name.index(cha[0])] = cha[1]
                for j in range(len(data)):
                    if select_data[i][0] == data[j][0]:
                        data[j] = select_data[i]
            with open('Employee_info_table', 'r', encoding='utf-8') as rf, \
                    open('Employee_info_table_swap2', 'w', encoding='utf-8') as wf:
                for line in rf:
                    if judge_line(line):
                        wf.write(line)
                    else:
                        for k in range(len(data)):
                            item = (str(data[k][0]), data[k][1], str(data[k][2]))
                            wf.write(','.join((*item, *data[k][3:]))+'\n')
                        else:
                            break
            os.remove('Employee_info_table')
            os.rename('Employee_info_table_swap2', 'Employee_info_table')
            print('Successfully modified！')
            return True
    else:
        print('Please input valid command!')
        return False


# 主页面
@auth
def index():
    """"""
    print("Welcome to \033[1;33mEmployee Information Management System\033[0m!\n\
    'help' or 'help <command>'to check command")
    flag = True
    while flag:
        cmd = input('@EIMS $ ').strip()
        # select语句，去掉select，以where分割开列名和条件传入select函数，打印返回值
        if cmd.startswith('select') and 'where' in cmd:
            temp = cmd.lstrip('select').split('where')
            show(command_select(temp[0].strip(), temp[1].strip()))
        # set语句，去掉set，以where分隔开修改内容和条件，传入set函数
        elif cmd.startswith('set') and 'where' in cmd:
            temp = cmd.lstrip('set').split('where')
            command_set(temp[0].strip(), temp[1].strip())
        # add语句，去掉add，传入增加信息
        elif cmd.startswith('add'):
            command_add(cmd.lstrip('add').split(','))
        # delete语句，去掉delete，传入修改目标
        elif cmd.startswith('delete'):
            command_delete(cmd.lstrip('delete').strip())
        # help语句，去掉help，传入help目标
        elif cmd.startswith('help'):
            command_help(cmd.lstrip('help').strip())
        elif cmd in ('quit', 'q'):
            return
        else:
            print('Command is incorrect!')


# 帮助函数
def command_help(cmd):
    """"""
    select = ''' \
    1.select <范围> where <条件>
        <范围>
            支持列名：
                'id', 'name', 'age', 'phone', 'job'， '*'
        <条件>
            支持逻辑（按优先级排列）：
                '>=', '<=', '!=', '<>', >', '<', '=', 'like'
        指令示范：
            select name,age where id>=3 \
    '''
    add = '''\
    2.add <信息>
        <信息>
            支持信息格式：
                姓名,年龄,电话,职位
        指令示范：
            add jack,22,13340578393,student\
    '''
    delete = '''\
    3.delete <id>/<name>
        <id>/<name>
            支持格式：
                id号码或者员工姓名
        指令示范：
            delete 4 \
    '''
    _set = '''\
    4.set <列名>=<修改值> where <条件>
        <列名>=<修改值>
            支持格式：
                列名：'id', 'name', 'age', 'phone', 'job'
                修改值：不限
        <条件>
            支持逻辑：
                '>=', '<=', '!=', '<>', >', '<', '=', 'like'
        指令示范：
            set name=alex where name=Alex\
    '''
    # _help = '''\
    # 查看指定命令：
    #     help <指令>
    # '''
    if not cmd:
        print('{}\n{}\n{}\n{}'.format(select, add, delete, _set))
    elif cmd == 'select':
        print(select)
    elif cmd == 'add':
        print(add)
    elif cmd == 'delete':
        print(delete)
    elif cmd == 'set':
        print(set)
    return True
index()
# print(command_delete.__doc__)

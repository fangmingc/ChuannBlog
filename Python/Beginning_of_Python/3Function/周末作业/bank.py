"""atm（选做）——实现信用卡程序
    基础需求：
    信用卡为用户提供功能：
        查询余额
        查询账单
        提现取款  提现手续费5% 额度 10000或自定义
        转账
        充值
        查看本月消费 消费和日常操作等内容以字符串的形式记录到文件中
        *以上所有功能均需做用户认证，请用装饰器完成

    扩展需求：
        实现购物商城，买东西加入 购物车，调用信用卡接口结账
"""

# 需要的模块
import os
import time
import functools
import random


# ##### 常量信息 ######
# 资金变动种类 Types of changes in funds
TCF = ['cost', 'borrow', 'transfer', 'receive', 'charge', 'repayment']
# 文件名 File Name
FN = ['users', 'balance', 'logs', 'goods']
# 指示输入符Indicates the input character
IDIC = '[\033[32mC\033[34m_\033[31m+\033[0m]$ '

# ##### 模拟cookie #####
# 当前用户状态 Current user status
CUS = {
    'status': False,
    'card_num': '',
    'username': 'visitor',
}


# 装饰器：登录认证
def auth(func):
    # 获取被装饰函数的元信息
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if CUS['status']:
            ret = func(*args, **kwargs)
        else:
            print('Please sign in!')
            ret = sign_in()
            if ret:
                ret = func(*args, **kwargs)
        return ret
    return inner


# 读取数据模块
def read_data(filename, flag=False):
    with open(filename, 'r', encoding='utf-8') as rf:
        data = {}
        for line in rf:
            temp = line.strip('\n').split(',')
            # 根据不同文件名使用不同方式读取和处理数据
            # users文件
            if filename == FN[0]:
                data.setdefault(temp[1], [temp[0], temp[2], temp[3]])
            # balance文件
            elif filename == FN[1]:
                # 读取全部用户balance
                if flag:
                    data[temp[0]] = [float(temp[1]), float(temp[2])]
                # 读取当前用户balance
                elif CUS['card_num'] == temp[0]:
                    data[temp[0]] = [float(temp[1]), float(temp[2])]
            # logs文件
            elif filename == FN[2]:
                # 读取全部用户logs
                if flag:
                    data.setdefault(temp[0], []).append(temp[1:])
                # 读取当前用户logs
                elif CUS['card_num'] == temp[0]:
                    data.setdefault(temp[0], []).append(temp[1:])
            # goods文件
            elif filename == FN[3]:
                data.setdefault(temp[0], temp[1:])
    return data


# 登录
def sign_in():
    user_data = read_data(FN[0])
    cnt = 0
    while True:
        username = input('Please input username:').strip()
        if username in user_data:
            while cnt < 3:
                password = input('PLease input password:').strip()
                if password == user_data[username][1]:
                    # 更新cookie
                    CUS['card_num'] = user_data[username][0]
                    CUS['username'] = username
                    CUS['status'] = True
                    print('Login successful!')
                    return True
                elif cnt < 2:
                    print('Password is incorrect! You only have %d chance.' % (2 - cnt))
                    cnt += 1
                elif cnt == 2:
                    print('Password is incorrect! You have no chance.')
                    return False
        else:
            print("Username doesn't exist!")


# 卡号生成
def random_card_num():
    data = read_data(FN[1], True)
    while True:
        # 生成一个五位数数字，检测是否在和已有卡号重复
        card_num = random.choice(range(100000))
        if card_num not in data:
            return str(card_num).zfill(5)


# 注册
def sign_up():
    data = read_data(FN[0])
    # 注册主循环
    while True:
        username = input('Register username:').strip()
        if not username:
            print('Name can not be empty!')
            continue
        elif username in data:
            print('This name have existed!')
            continue
        elif username in ['q', 'quit']:
            return True
        elif len(username) < 3:
            print('Name is too short!(>2)')
            continue
        else:
            while True:
                password = input('Please input password:').strip()
                if not password:
                    print('Password can not be empty!')
                    continue
                elif len(password) < 3:
                    print('Password is too short!(>2)')
                    continue
                else:
                    password2 = input('Please input password again:').strip()
                    if password == password2:
                        # 将注册成功的卡号，用户名，密码，额度写入用户信息文件
                        card_num = random_card_num()
                        with open(FN[0], 'a') as wf:
                            wf.write(','.join((card_num, username, password, '5000')) + '\n')
                        with open(FN[1], 'a') as wf:
                            wf.write(','.join((card_num, '0', '5000'))+'\n')
                        # 初始化账户余额
                        add_money(float('0'), TCF[4], 'balance', card_num)
                        print('Register successful!')
                        return True
                    else:
                        print('The twice password is not same!')
                        continue


# 页面打印
def print_page(symbol=''):
    print('-' * 50)
    if symbol == 'bank':
        print('Bank of [\033[32mC\033[34m_\033[31m+\033[0m]'.center(60, ' '))
        print('''\
            \033[1m1. C_+ Store
            2. Balance
            3. Bill
            4. Withdraw money  
            5. Transfer
            6. Charge
            7. View consumption\033[0m\
        ''')
    elif symbol == 'bill':
        print('''\
            1. check all bills
            2. check cost bills
            3. check transfer bills
            4. check receive bills
            5. check charge bills
            6. check repayment bills
            'q' to quit\
        ''')
    elif symbol == 'store':
        print('''\
            Welcome to \033[32mC\033[34m_\033[31m+\033[0m store!
            "\033[32min\033[0m" to sign in,
            "\033[34mup\033[0m" to sign up, 
            "visit" to check goods,
            "\033[31mexit\033[0m" to exit\
        ''')
    elif symbol == 'menu':
        print('''\033[1m\
            1. goods
            2. cart
            3. bank
            4. recharge
            5. balance\033[0m\
        ''')
    elif symbol == 'consumption':
        print('''\033[1m\
            1. check today
            2. check today
            3. check a week
            4. check a month
            5. check a year
            'q' to quit\033[0m\
        ''')


# 追加logs文件
def add_log(card_num, p_time, tcf, num):
    # 卡号，时间，资金变动种类，变动数目
    with open(FN[2], 'a') as af:
        af.write(','.join((card_num, p_time, tcf, num))+'\n')


# 更新balance文件
def update(filename, card_num, symbol, num):
    with open(filename, encoding='utf-8') as rf, \
            open(filename+'_swap', 'w', encoding='utf-8') as wf:
        for line in rf:
            # 查找操作目标账户
            if card_num == line[:5]:
                temp = line.strip('\n').split(',')
                # 检测对哪一项操作
                if symbol == FN[1]:
                    # 对余额操作
                    wf.write(','.join((temp[0], str(float(temp[1])+float(num)), temp[2]))+'\n')
                else:
                    # 对可用额度操作
                    wf.write(','.join((temp[0], temp[1], str(float(temp[2]) + float(num))))+'\n')
            else:
                wf.write(line)
    os.remove(filename)
    os.replace(filename+'_swap', filename)


# 查看余额功能 #########################################################
@auth
def ck_balance():
    data = read_data(FN[1])
    while True:
        print_page()
        print('''\
            Card Number : \033[34m%s\033[0m
              Username  : \033[1m%s\033[0m
              Balance   : \033[31m%s\033[0m 
            Credit line : \033[33m%s\033[0m\
            ''' % (CUS['card_num'], CUS['username'], data[CUS['card_num']][0], data[CUS['card_num']][1]))
        cmd = input('\t\033[32m"q" to quit\t"b" to C_+ Store\033[0m\n%s' % IDIC).strip()
        if cmd in ('q', 'quit'):
            return True
        elif cmd == 'b':
            menu()


# 打印账单
def print_bill(data):
    cnt = 0
    # 从最后一条日志开始打印
    for i in range(len(data)-1, -1, -1):
        # 打印单条账目
        print('''\
                -----------\033[1;34m%s\033[0m-----------
                Types of change fund:  \033[33m%s\033[0m
                        amount      :  \033[1;31m%s\033[0m\
                ''' % (time.strftime('%Y/%m/%d %H:%M', time.localtime(float(data[i][0]))),
                       data[i][1], data[i][2]))
        # 一次最多打印五条账单
        cnt += 1
        if cnt % 5 == 0:
            cmd2 = input("\033[32m'c' to continue 'q' to quit\033[0m >>>")
            if cmd2 == 'c':
                continue
            elif cmd2 == 'q':
                return


# 按照需求过滤账单
def filter_bill(data, symbol):
    temp = []
    for i in data:
        if symbol == i[1]:
            temp.append(i)
    return temp


# 查看账单功能 #########################################################
@auth
def ck_bill():
    data = read_data(FN[2])[CUS['card_num']]
    while True:
        print_page('bill')
        cmd = input('%s' % IDIC).strip()
        if cmd == '1':
            print_bill(data)
        elif cmd == '2':
            print_bill(filter_bill(data, TCF[0]))
        elif cmd == '3':
            print_bill(filter_bill(data, TCF[2]))
        elif cmd == '4':
            print_bill(filter_bill(data, TCF[3]))
        elif cmd == '5':
            print_bill(filter_bill(data, TCF[4]))
        elif cmd == '6':
            print_bill(filter_bill(data, TCF[5]))
        elif cmd == 'q':
            return


# 余额减少
def deduct(num, tcf, obj):
    data = read_data(FN[1])
    if num <= data[obj][0]:
        data[obj][0] -= num
        add_log(obj, str(time.time()), tcf, str(-num))
        update(FN[1], obj, 'balance', str(-num))
        return True
    else:
        print('Your balance is not enough!\nYou have %s credit line to use.' % data[obj][1])
        cmd2 = input('Do you want to use a credit line?(yes or no)\n%s' % IDIC).strip()
        if cmd2 == 'no':
            return False
        elif cmd2 == 'yes':
            num = num - data[obj][0]
            if num <= data[obj][1]:
                data[obj][1] -= num
                add_log(obj, str(time.time()), TCF[0], str(-data[obj][0]))
                add_log(obj, str(time.time()), TCF[1], str(-num))
                update(FN[1], obj, 'balance', str(-data[obj][0]))
                update(FN[1], obj, 'credit', str(-num))
                return True
            else:
                print('Your credit is not enough!')
                return False


# 提现取款功能 #########################################################
@auth
def withdraw():
    while True:
        print_page()
        cmd = input("'q' to quit\nHow much you want to take?\n%s" % IDIC).strip()
        if cmd.isdigit():
            num = float(cmd)
            if num > 200:
                rate = 1.05
            else:
                rate = 1
            if deduct(num*rate, TCF[0], CUS['card_num']):
                print('Withdraw successfully! Deduct the fee of %s yuan' % (round(num*rate-num, 2)))
        elif cmd in ('q', 'quit'):
            return


# 转账功能 ############################################################
@auth
def transfer():
    data = read_data(FN[1], True)
    obj = CUS['card_num']
    while True:
        print_page()
        print("'q' to quit\nWho do you want to transfer?\nPlease enter the card number：")
        aim_card = input('%s' % IDIC).strip()
        if aim_card in data:
            if aim_card == obj:
                print('You can not transfer to yourself!')
                continue
            tr_num = input('Please enter the transfer amount：\n%s' % IDIC).strip()
            if tr_num.isdigit():
                num = float(tr_num)
                if num <= data[obj][0]:
                    data[obj][0] -= num*1.05
                    deduct(num*1.05, TCF[2], obj)
                    add_money(num, TCF[3], 'balance', aim_card)
                    print('Transfer successfully! Deduct the fee of %s yuan' % (round(num*1.05-num, 2)))
                else:
                    print('Your balance is insufficient!')
        elif aim_card in ('q', 'quit'):
            return
        else:
            print('Please enter a valid card number')


# 余额增加
def add_money(num, tcf, symbol, obj):
    add_log(obj, str(time.time()), tcf, str(+num))
    update(FN[1], obj, symbol, str(+num))


# 充值功能 ############################################################
@auth
def charge(obj):
    data = read_data(FN[1])
    data2 = read_data(FN[0])
    while True:
        print_page()
        ch_num = input("'q' to quit\nPlease enter the amount charged:\n%s" % IDIC).strip()
        if ch_num.isdigit():
            num = float(ch_num)
            # 如果有欠款（使用了可用额度），优先还额度
            if data[obj][1] < float(data2[CUS['username']][2]):
                cre = num + data[obj][1]
                if cre > float(data2[CUS['username']][2]):
                    # 如果欠款还清，充值余额
                    num2 = float(data2[CUS['username']][2]) - data[obj][1]
                    add_money(num2, TCF[5], 'credit', obj)
                    print('Pay off the arrears %s Yuan!' % num2)
                    add_money(num - num2, TCF[4], 'balance', obj)
                    print('Recharge %s Yuan successfully!' % (num - num2))
                else:
                    # 如果欠款未还清，不充值余额
                    add_money(num, TCF[5], 'credit', obj)
                    print('Pay off the arrears %s Yuan!' % num)
            else:
                # 没有欠款则充值
                add_money(num, TCF[4], 'balance', obj)
                print('Recharge %s Yuan successfully!' % num)
        elif ch_num in ('q', 'quit'):
            return
        else:
            print('Please input valid number!')


# 计算条件时间
def calc_time(symbol):
    _time = 0
    if symbol == 'today':
        # 获取今天的日期
        today = time.localtime(time.time())[:3]
        # 换算成今日零点的时间戳
        zero_day = (str(today[0]), str(today[1]), str(today[2]), '8')
        _time = time.mktime(time.strptime('.'.join(zero_day), '%Y.%m.%d.%H'))
    elif symbol == 'day':
        _time = time.time() - 86400.0
    elif symbol == 'week':
        _time = time.time() - 86400.0*7
    elif symbol == 'month':
        _time = time.time() - 86400.0*30
    elif symbol == 'year':
        _time = time.time() - 86400.0*365
    return _time


# 计算消费
def calc_consume(record, t_time):
    total_get = 0
    total_give = 0
    for i in record:
        if float(i[0]) > t_time:
            if float(i[2]) >= 0:
                total_get += float(i[2])
            else:
                total_give += float(i[2])
    return total_get, total_give


# 打印消费记录
def print_consume(data, symbol):
    print('''\
         %s get    : %s
    %s consumption : %s
            total     : %s''' % (symbol, data[0], symbol, data[1], data[0]+data[1]))


# 查看消费功能 ########################################################
@auth
def mon_consumption():
    data = read_data(FN[2])[CUS['card_num']]
    while True:
        print_page('consumption')
        cmd = input('%s' % IDIC).strip()
        if cmd == '1':
            print_consume(calc_consume(data, calc_time('today')), 'Today')
        elif cmd == '2':
            print_consume(calc_consume(data, calc_time('day')), 'A day')
        elif cmd == '3':
            print_consume(calc_consume(data, calc_time('week')), 'A week')
        elif cmd == '4':
            print_consume(calc_consume(data, calc_time('month')), 'A month')
        elif cmd == '5':
            print_consume(calc_consume(data, calc_time('year')), 'A Year')
        elif cmd == 'q':
            return


# 更新goods文件
def update_data(data, cart):
    # 将数据写入文件
    with open(FN[3]+'_swap', 'w') as wf:
        for i in data:
            info = ','.join((i, *data[i]))+'\n'
            wf.write(info)
    os.remove(FN[3])
    os.rename(FN[3]+'_swap', FN[3])

    cart.clear()
    return True


# 打印商品信息
def print_goods(data):
    print("""\
        序号  商品名     单价    库存\
    """)
    for i in range(1, len(data)+1):
        print("""\
        {}    {:8}  {:6}  {}\
        """.format(i, data[str(i)][0], data[str(i)][1], data[str(i)][2]))
    return data


# 购物车功能 ###########################################################
def shopping_cart(cart, storehouse):
    print_page()
    # 打印购物车
    total = 0
    for i in cart:
        print('{:8} {:9} {}'.format(i, cart[i][0], cart[i][1]))
        total += int(cart[i][0]) * int(cart[i][1])
    print('Total:  {:10}'.format(total))
    if not total:
        print('shopping cart is empty!')
        return cart
    # 当购物车不为空则继续
    while True:
        cmd = input("\033[32m'1' to buy '2' to clear cart 'q' to quit\033[0m \n%s" % IDIC).strip()
        if not cmd:
            print('Please input valid command!')
        elif cmd in ('b', 'B', 'buy'):
            if purchase(total, storehouse, cart):
                print('Purchase successful!')
                return cart
            else:
                print('Purchase failure!')
        elif cmd in ('q', 'quit'):
            return cart
        elif cmd in ('2', 'clear'):
            cart.clear()
            print('Shopping cart has been cleared!')
            return cart


# 结账
@auth
def purchase(total, storehouse, cart):
    if deduct(total, TCF[0], CUS['card_num']):
        # 结账成功更新数据
        update_data(storehouse, cart)
        cart.clear()
        return True
    else:
        return False


# 购物/选择商品  ########################################################
def choose_goods(data, cart):
    while True:
        print_page()
        cmd = input("'q' to quit\nPlease choose goods:\n%s" % IDIC).strip()
        if not cmd:
            print('Goods is empty!')
        elif cmd in data:
            num = input("Please input number of goods:\n%s " % IDIC).strip()
            if num and num.isdigit():
                if int(num) <= int(data[cmd][2]):
                    # 检查已选商品是否已在购物车
                    if data[cmd][0] in cart:
                        cart[data[cmd][0]][1] += int(num)
                        print('{} have added into cart!'.format(data[cmd][0]))
                    else:
                        cart.setdefault(data[cmd][0], [data[cmd][1], int(num)])
                        print('\033[33m{}\033[0m have added into cart!'.format(data[cmd][0]))
                    data[cmd][2] = str(int(data[cmd][2]) - int(num))
                else:
                    print('Stock is not enough!')
            else:
                print('Please input valid number!')
        elif cmd in ('q', 'quit'):
            return cart
        else:
            print("Goods doesn't exist!")


# 信用卡界面 ############################################################
@auth
def credit_index():
    while True:
        print_page('bank')
        cmd = input('%s' % IDIC).strip()
        if cmd == '1':
            return
        elif cmd == '2':
            ck_balance()
        elif cmd == '3':
            ck_bill()
        elif cmd == '4':
            withdraw()
        elif cmd == '5':
            transfer()
        elif cmd == '6':
            charge(CUS['card_num'])
        elif cmd == '7':
            mon_consumption()
        elif cmd == 'q':
            return


# 商店界面 ##############################################################
def menu():
    # load data
    storehouse = read_data(FN[3])
    cart = {}
    while True:
        print_page('menu')
        cmd = input('%s' % IDIC).strip()
        if cmd in ('1', 'goods'):
            storehouse = print_goods(storehouse)
            cart = choose_goods(storehouse, cart)
        elif cmd in ('2', 'cart'):
            cart = shopping_cart(cart, storehouse)
        elif cmd == '3':
            credit_index()
        elif cmd in ('4', 'charge'):
            charge(CUS['card_num'])
        elif cmd == '5':
            ck_balance()
        elif cmd in ('q', 'quit'):
            break


# 起始页面 ##############################################################
def index():
    while True:
        print_page('store')
        cmd = input('%s' % IDIC).strip()
        if cmd:
            if cmd == 'in':
                sign_in()
                menu()
            elif cmd == 'up':
                sign_up()
            elif cmd == 'visit':
                menu()
            elif cmd == 'exit' or cmd == 'e':
                return

if __name__ == '__main__':
    index()

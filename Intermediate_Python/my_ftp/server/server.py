from socket import *
from multiprocessing import Process
import os
import json
from hashlib import md5, sha256
import struct


SERVER_ADDRESS = ('192.168.20.6', 20000)
MAX_CONNECTION = 5
MAX_PACKAGE_SIZE = 1024
HEADER_LENGTH = 4

MESSAGE = 'MESSAGE'
FILE = 'FILE'
OTHER = 'OTHER'
PUT = 'PUT'

COMMAND_ERROR = 'Error: The command is incorrect.'.encode('utf-8')
COMMAND_SHOW = '----------------'.encode('utf-8')


def put(connection, cmd, path):
    """接收上传文件"""
    # 告诉客户端准备发送
    data = PUT.encode('utf-8')
    # md5_obj = md5()
    # md5_obj.update(data)
    # first_header = make_header(PUT, len(data), data, cmd[1].encode('utf-8'), md5_obj.hexdigest())
    send_message(connection, cmd[1].encode('utf-8'), PUT)

    # 接收报头
    header_length = struct.unpack('i', connection.recv(HEADER_LENGTH))[0]
    header = json.loads(connection.recv(header_length).decode('utf-8'))

    _path = os.sep.join((path, header['filename']))

    total_size = header['total_size']
    md5_obj = md5()
    recv_size = 0

    with open(_path + '_temp', 'wb') as wf:
        while recv_size < total_size:
            recv_data = connection.recv(MAX_PACKAGE_SIZE)
            md5_obj.update(recv_data)
            recv_size += len(recv_data)
            wf.write(recv_data)

    if md5_obj.hexdigest() == header['md5']:
        if os.path.isfile(_path):
            os.remove(_path)
        os.rename(_path + '_temp', _path)
        send_message(connection, '\nUpload successful!'.encode('utf-8'))
    else:
        os.remove(_path + '_temp')
        send_message(connection, '\nUpload failed!'.encode('utf-8'))


def get(connection, cmd, path):
    """下载命令"""
    _path = path + os.sep + cmd[1]
    if os.path.isfile(_path):
        send_file(connection, _path)
    else:
        send_message(connection, COMMAND_ERROR)


def show(connection, cmd, path):
    """查看当前目录下文件"""
    if cmd[1] == 'local':
        send_message(connection, COMMAND_SHOW, OTHER)
    elif cmd[1] == 'origin':
        if not os.path.isdir(path):
            os.makedirs(path)
        result = os.walk(path)
        res = COMMAND_SHOW.decode('utf-8') + '\n' + '\n'.join(next(result)[2])

        send_message(connection, res.encode('utf-8'))
    else:
        send_message(connection, COMMAND_ERROR)


def make_header(data_type, data_length, data_bytes=None, filename=None, _md5=None):
    """制作报头"""
    if not _md5:
        md5_obj = md5()
        md5_obj.update(data_bytes)
        _md5 = md5_obj.hexdigest()

    header = {
        'data_type': data_type,
        'filename': filename,
        'total_size': data_length,
        'md5': _md5
    }

    header_bytes = json.dumps(header).encode('utf-8')
    return header_bytes


def send_message(connection, data_bytes, data_type=MESSAGE):
    """发送对象为消息"""
    # make header
    data_length = len(data_bytes)
    header_bytes = make_header(data_type, data_length, data_bytes=data_bytes)
    header_length = struct.pack('i', len(header_bytes))

    # send the length of header
    connection.send(header_length)

    # send header
    connection.send(header_bytes)

    # send the data
    if data_length > MAX_PACKAGE_SIZE:
        times, remainder = divmod(data_length, MAX_PACKAGE_SIZE)
        for _times in range(times):
            connection.send(data_bytes[_times*MAX_PACKAGE_SIZE: (_times+1)*MAX_PACKAGE_SIZE])
        if remainder:
            connection.send(data_bytes[times*MAX_PACKAGE_SIZE:])
    else:
        connection.send(data_bytes)


def file_md5(filename):
    """文件MD5计算"""
    with open(filename, 'rb') as rf:
        md5_obj = md5()
        send_size = 0
        file_size = os.path.getsize(filename)
        while send_size < file_size:
            send_data = rf.read(MAX_PACKAGE_SIZE)
            send_size += len(send_data)
            md5_obj.update(send_data)
    return md5_obj.hexdigest()


def send_file(connection, path):
    """发送对象为文件"""
    # make header
    file_size = os.path.getsize(path)
    filename = os.path.basename(path)
    header_bytes = make_header(FILE, file_size, filename=filename, _md5=file_md5(path))
    header_length = struct.pack('i', len(header_bytes))

    # send length of header
    connection.send(header_length)

    # send header
    connection.send(header_bytes)

    # send file
    with open(path, 'rb') as rf:
        if file_size > MAX_PACKAGE_SIZE:
            send_size = 0
            while send_size < file_size:
                send_data = rf.read(MAX_PACKAGE_SIZE)
                connection.send(send_data)
                send_size += len(send_data)
        else:
            connection.send(rf.read())


def sign_in(connection):
    """登录"""
    with open('users') as rf:
        user_data = json.load(rf)
        while True:
            sha256_obj = sha256()
            connection.send('请输入用户名：'.encode('utf-8'))
            username = connection.recv(1024).decode('utf-8')
            if username in user_data:
                connection.send('请输入密码：'.encode('utf-8'))
                password = connection.recv(1024).decode('utf-8')
                sha256_obj.update(str(username+password+username).encode('utf-8'))
                if sha256_obj.hexdigest() == user_data[username]:
                    connection.send('Login success!'.encode('utf-8'))
                    os.getpid()
                    return username
                # else:
                #     connection.send('密码错误！'.encode('utf-8'))
            # else:
            #     connection.send('用户名不存在！'.encode('utf-8'))


def talk(connection):
    """会话函数"""
    username = sign_in(connection)
    path = os.sep.join((os.getcwd(), 'user', username))
    # communication loop
    while True:
        try:
            cmd = connection.recv(1024).decode('utf-8').split(' ', 1)
            if not cmd:
                break
            if len(cmd) > 1 and cmd[0] in cmd_dic:
                cmd_dic[cmd[0]](connection, cmd, path)
            else:
                send_message(connection, COMMAND_ERROR)
        except Exception as error_info:
            print(error_info)
            break
    connection.close()


def start():
    """服务端启动主程序"""
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(SERVER_ADDRESS)
    server.listen(MAX_CONNECTION)

    print('The server is starting ...')

    # connection loop
    while True:
        print('The server is waiting connection ...')
        conn, client_addr = server.accept()
        print('Have connected ', client_addr)

        process = Process(target=talk, args=(conn,))
        process.start()

cmd_dic = {
    'put': put,
    'get': get,
    'show': show, }

if __name__ == '__main__':
    start()

# with open('users') as rf, open('users_swap', 'w') as wf:
#     # user = json.load(rf)
#     # print(user)
#     user = {
#         'egon': 'ef11044ec57541b1de187ed3b7d6d8427133dbbece29194c4a51287ab3300cd2',
#         'alex': '04d57652e8c6ba71e771a947121fc662bb818a62ceba8628b85f1b12fefba2da',
#         'chuck': 'ca6fe1c0820aed5dc370e453119cc294cd56be1b196a4829eed34c72262b4c6b',
#     }
#     json.dump(user, wf)
# os.remove('users')
# os.rename('users_swap', 'users')


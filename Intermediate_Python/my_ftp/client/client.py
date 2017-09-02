from socket import *
import struct
import json
from hashlib import md5
import os
import time
import sys


SERVER_ADDRESS = ('192.168.20.6', 20000)
MAX_PACKAGE_SIZE = 8
HEADER_LENGTH = 4

FILE = 'FILE'

FILENAME_ERROR = 'Error: The filename is incorrect.'


def receive_header(connection):
    """接收报头"""
    header_length = struct.unpack('i', connection.recv(HEADER_LENGTH))[0]
    header = json.loads(connection.recv(header_length).decode('utf-8'))

    return header


def operate_message(connection, header):
    """接收对象为信息"""
    total_size = header['total_size']
    md5_obj = md5()
    recv_size = 0
    total_data = ''.encode('utf-8')
    while recv_size < total_size:
        recv_data = connection.recv(MAX_PACKAGE_SIZE)
        md5_obj.update(recv_data)
        recv_size += len(recv_data)
        total_data += recv_data

    if md5_obj.hexdigest() == header['md5']:
        print(total_data.decode('utf-8'))
    else:
        print('传输数据有误！')
        print(total_data.decode('utf-8'))


def operate_file(connection, header):
    """接收对象为文件"""
    total_size = header['total_size']
    md5_obj = md5()
    recv_size = 0

    with open(header['filename'] + '_temp', 'wb') as wf:
        while recv_size < total_size:
            recv_data = connection.recv(MAX_PACKAGE_SIZE)
            md5_obj.update(recv_data)
            recv_size += len(recv_data)
            wf.write(recv_data)

            # 进度条
            num = int((recv_size / total_size) * 100)
            char_num = num // 4  # 打印多少个
            per_str = '\r%3d%% : %s%s' % (num, '-' * char_num, '|' * (25-char_num))
            print(per_str, end='', file=sys.stdout, flush=True)

    if md5_obj.hexdigest() == header['md5']:
        if os.path.isfile(header['filename']):
            os.remove(header['filename'])
        os.rename(header['filename'] + '_temp', header['filename'])
        print('\nDownload successful!')
    else:
        os.remove(header['filename'] + '_temp')
        print('\nDownload failed!')


def operate_other(connection, header):
    operate_message(connection, header)
    my_dir = os.walk(os.getcwd())
    for filename in next(my_dir)[2]:
        print(filename)


def operate_put(connection, header):
    """上传文件"""
    def make_header(data_type, data_length, _filename, _md5):
        """制作报头"""

        _header = {
            'data_type': data_type,
            'filename': _filename,
            'total_size': data_length,
            'md5': _md5
        }

        header_bytes = json.dumps(_header).encode('utf-8')
        return header_bytes

    def file_md5(_path):
        """文件MD5计算"""
        with open(_path, 'rb') as rf:
            md5_obj = md5()
            send_size = 0
            file_size = os.path.getsize(_path)
            while send_size < file_size:
                send_data = rf.read(MAX_PACKAGE_SIZE)
                send_size += len(send_data)
                md5_obj.update(send_data)
        return md5_obj.hexdigest()

    def send_file(_connection, _path):
        """发送对象为文件"""
        # make header
        file_size = os.path.getsize(_path)
        _filename = os.path.basename(_path)
        header_bytes = make_header(FILE, file_size, _filename=_filename, _md5=file_md5(_path))
        header_length = struct.pack('i', len(header_bytes))

        # send length of header
        _connection.send(header_length)

        # send header
        _connection.send(header_bytes)

        # send file
        with open(_path, 'rb') as rf:
            if file_size > MAX_PACKAGE_SIZE:
                send_size = 0
                while send_size < file_size:
                    send_data = rf.read(MAX_PACKAGE_SIZE)
                    _connection.send(send_data)
                    send_size += len(send_data)

                    # 进度条
                    num = int((send_size / file_size) * 100)
                    char_num = num // 4  # 打印多少个
                    per_str = '\r%3d%% : %s%s' % (num, '-' * char_num, '|' * (25 - char_num))
                    print(per_str, end='', file=sys.stdout, flush=True)

            else:
                _connection.send(rf.read())
                per_str = '\r%3d%% : %s%s' % (100, '-' * 25, '|' * 0)
                print(per_str, end='', file=sys.stdout, flush=True)

    filename = connection.recv(header['total_size']).decode('utf-8')
    path = os.getcwd() + os.sep + filename
    if os.path.isfile(path):
        send_file(connection, path)
        operate_message(connection, receive_header(connection))
    else:
        print(FILENAME_ERROR)


def sign_in(connection):
    """登录"""
    while True:
        data = connection.recv(1024).decode('utf-8')
        print(data)
        if 'success' in data:
            return True
        while True:
            cmd = input('[+_+] ').strip()
            if cmd:
                break
        connection.send(cmd.encode('utf-8'))


operate_dic = {
    'MESSAGE': operate_message,
    'FILE': operate_file,
    'OTHER': operate_other,
    'PUT': operate_put
}


def main():
    """客户端启动主程序"""
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(SERVER_ADDRESS)
    if sign_in(client):
        while True:
            cmd = input('>> ').strip()
            if not cmd:
                continue
            client.send(cmd.encode('utf-8'))
            print('The server is preparing ...')
            time.sleep(0.5)
            header = receive_header(client)
            if header['data_type'] in operate_dic:
                operate_dic[header['data_type']](client, header)

if __name__ == '__main__':
    main()


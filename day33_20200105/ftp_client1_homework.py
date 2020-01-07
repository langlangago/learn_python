#! encoding:utf-8
import socket
import struct
import hashlib
import os
import struct
import json
import sys
import time

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))


# 密码加密后传输
def encrypt(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode('utf-8'))
    return md5.hexdigest()

def processBar(remain, total):
    rate = (total - remain) / total
    rate_num = int(rate*100)
    if rate_num == 100:
        r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num)
    else:
        r = '\r%s>%d%%' % ('=' * rate_num, rate_num)
    sys.stdout.write(r)
    # sys.stdout.flush()

# 接收指令，登录or注册
msg = sk.recv(37).decode('utf-8')
msg = input(msg).strip()
sk.send(msg.encode('utf-8'))

# 第一次输入，一切正常，成功登陆or注册
name = sk.recv(30).decode('utf-8')
name = input(name).strip()
name_len = struct.pack('i', len(name))
sk.send(name_len)
sk.send(name.encode('utf-8'))

passwd = sk.recv(27).decode('utf-8')
passwd = input(passwd).strip()
passwd = encrypt(passwd)
passwd_len = struct.pack('i', len(passwd))
sk.send(passwd_len)
sk.send(passwd.encode('utf-8'))
print(sk.recv(30).decode('utf-8'))

# 非正常情况，登陆or注册
ret = int(sk.recv(1).decode('utf-8'))
if ret == 1 or ret == 3:
    name = sk.recv(30).decode('utf-8')
    name = input(name).strip()
    name_len = struct.pack('i', len(name))
    sk.send(name_len)
    sk.send(name.encode('utf-8'))

    passwd = sk.recv(27).decode('utf-8')
    passwd = input(passwd).strip()
    passwd = encrypt(passwd)
    passwd_len = struct.pack('i', len(passwd))
    sk.send(passwd_len)
    sk.send(passwd.encode('utf-8'))

# 文件上传操作
head_dict = {'filename': None, 'filepath': None, 'filesize': None}
file = sk.recv(30).decode('utf-8')
file = input(file).strip()
# 组装报头
(filepath, filename) = os.path.split(file)
filesize = os.path.getsize(file)
head_dict['filename'] = filename
head_dict['filepath'] = filepath
head_dict['filesize'] = filesize

# 发送报头, 先发送报头长度，固定4个字节
# 先转成str，再用struct计算长度
# 再发送报头内容
head_str = json.dumps(head_dict)
head_len = len(head_str)
num = struct.pack('i', head_len)
sk.send(num)
sk.send(head_str.encode('utf-8'))

ret = sk.recv(15)
print(ret.decode('utf-8'))
status = int(sk.recv(1).decode('utf-8'))
if status == 1:
    # 计算md5值，并传送到服务端对比
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            md5.update(line)
    sk.send(md5.hexdigest().encode('utf-8'))

    ret2 = sk.recv(60)
    print(ret2.decode('utf-8'))
    status2 = int(sk.recv(1).decode('utf-8'))
    if status2 == 2:
        print('我是状态2，我没事做，要退出了')
    elif status2 == 3:
        # 断点续传，接收到断点的位置
        num = sk.recv(4)
        position_len = struct.unpack('i', num)[0]
        position = int(sk.recv(position_len).decode('utf-8'))
        with open(file, 'rb') as f:
            buffer = 4096
            f.seek(position)
            total = filesize
            filesize -= position
            while True:
                if filesize >= buffer:
                    content = f.read(buffer)
                    sk.send(content)
                    filesize -= buffer
                    processBar(filesize, total)
                else:
                    content = f.read(filesize)
                    sk.send(content)
                    processBar(filesize, total)
                    break
            processBar(0, 100)
        sk.send(md5.hexdigest().encode('utf-8'))
        print(sk.recv(42).decode('utf-8'))
else:
    # 发送文件，一遍读，一遍计算md5，一遍发送
    print('开始上传文件')
    buffer = 4096
    md5 = hashlib.md5()
    total = filesize
    with open(file, 'rb') as f:
        while True:
            if filesize >= buffer:
                content = f.read(buffer)
                sk.send(content)
                md5.update(content)
                filesize -= buffer
                processBar(filesize, total)
            else:
                content = f.read(filesize)
                sk.send(content)
                md5.update(content)
                processBar(filesize, total)
                break
        processBar(0, 100)

    sk.send(md5.hexdigest().encode('utf-8'))
    print(sk.recv(42).decode('utf-8'))

sk.close()

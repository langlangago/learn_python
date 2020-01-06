#! encoding:utf-8
import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

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
    passwd_len = struct.pack('i', len(passwd))
    sk.send(passwd_len)
    sk.send(passwd.encode('utf-8'))

sk.close()

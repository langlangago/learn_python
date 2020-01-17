#! encoding:utf-8

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

ret = sk.recv(1024)
print(ret)

cmd = input('>>>>')
sk.send(cmd.encode('utf-8'))
ret2 = sk.recv(1024)
print(ret2)

sk.close()



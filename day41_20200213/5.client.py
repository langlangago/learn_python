#! encoding:utf-7

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
print(sk.recv(1024).decode('utf-8'))
msg = input('>>>')
sk.send(msg.encode('utf-8'))
sk.close()
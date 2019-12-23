#! encoding:utf-8
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

sk.send(b'Hello, I am from client.')
message = sk.recv(1024)
print(message)

sk.close()

#! encoding:utf-8
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))

while True:
    ret = input('>>>')
    sk.send(bytes(ret, encoding='utf-8'))
    if ret == 'bye': break
    msg = sk.recv(1024)
    print(msg.decode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        break

sk.close()

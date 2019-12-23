#! encoding:utf-8
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

while True:
    ret, addr = sk.recvfrom(1024)
    print(ret.decode('utf-8'))
    msg = input('>>>')
    sk.sendto(msg.encode('utf-8'), addr)

sk.close()

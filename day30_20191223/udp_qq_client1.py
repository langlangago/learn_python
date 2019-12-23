# coding=utf-8
import  socket

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

while True:
    msg = input('二哥说：')
    msg = msg + 'From 二哥'
    sk.sendto(msg.encode('utf-8'), ip_port)
    ret, addr = sk.recvfrom(1024)
    print(ret.decode('utf-8'))

sk.close()
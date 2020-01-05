# coding=utf-8
# 为了解决黏包问题，使用struct模块
# struct模块可以将某个数据类型转换成固定长度的bytes类型
# 比如，把int类型转成4个字节长度的bytes类型，这样接收端固定接收4个字节即可。
# 之后可以再次接收数据，保证不会黏包
import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('>>>>')
    if cmd == 'q':
        break
    conn.send(cmd.encode('gbk'))
    num = conn.recv(4)   # 接收到对方要传输的数据大小,因为使用了struct这里固定使用4个字节
    num = struct.unpack('i', num)
    print(num[0])
    ret = conn.recv(num[0])   # 确定了要接收的数据大小，即可解决黏包问题
    print(ret.decode('gbk'))

conn.close()
sk.close()
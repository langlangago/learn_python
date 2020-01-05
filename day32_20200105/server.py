# coding=utf-8
# 为了解决黏包问题，多走一次交互
# 黏包现象的本质是，不知道要接收多少个字节
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()

while True:
    cmd = input('>>>>')
    if cmd == 'q':
        break
    conn.send(cmd.encode('gbk'))
    num = conn.recv(1024)   # 接收到对方要传输的数据大小，在下面填写正确的receive大小
    print(num.decode('gbk'))
    conn.send(b'ok')
    ret = conn.recv(int(num))   # 确定了要接收的数据大小，即可解决黏包问题
    print(ret.decode('gbk'))

conn.close()
sk.close()
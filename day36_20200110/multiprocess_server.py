#! encoding:utf-8

import socket
from multiprocessing import Process


# 使用多进程实现tcp server端的多进程并发连接
# 将conn操作写在子进程的函数中
def server(conn):
    conn.send(b'Hello!')
    ret = conn.recv(1024)
    print(ret)
    conn.send(b'ByeBye')
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()

    while True:
        conn, addr = sk.accept()
        p = Process(target=server, args=(conn, ))
        p.start()

    sk.close()
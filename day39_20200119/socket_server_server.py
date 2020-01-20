#! encoding:utf-8
import socket
from multiprocessing import Pool


# 用进程池异步的方式实现socketserver
def func(conn):
    conn.send(b'Hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8080))
    sk.listen()
    p = Pool(5)
    while True:
        conn, addr = sk.accept()
        p.apply_async(func, args=(conn, ))
    sk.close()
#! encoding:utf-8
from gevent import monkey;monkey.patch_all()
import socket
import gevent

def talk(conn):
    conn.send(b'Hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

while True:
    conn, addr = sk.accept()
    gevent.spawn(talk, conn)
sk.close()
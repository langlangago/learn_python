# coding=utf-8
# 利用hmac实现校验客户端的合法性
# 服务端和客户端拥有同样的secret_key, 服务端发送
# 到客户端一个数据，两边同时加密后，回传到server端进行比较验证。

import socket
import hmac
import os

SECRET_KEY = b'alex'

def valid_conn(conn):
    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(SECRET_KEY, msg)
    key1 = h.digest()
    key2 = conn.recv(1024)
    return hmac.compare_digest(key1, key2)

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()
ret = valid_conn(conn)
if ret:
    print('合法的客户端')
    conn.close()
else:
    print('不合法的客户端')
    conn.close()

sk.close()
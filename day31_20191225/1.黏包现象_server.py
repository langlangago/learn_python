# coding=utf-8

# 黏包现象是tcp特有的现象，tcp会根据情况把发送数据进行拆分和合并。
# 发送数据过小，会合并一起发送，对方可能一次recv到全部数据。
# 发送数据过大，会拆分发送，对方一次只能接收到一部分数据，下一次收另一部分。
# 是tcp的优化算法决定的。另一方面是因为tcp不会丢包
# udp 绝对没有黏包现象，如果发送数据过大，udp会直接丢掉。不会继续发送剩余数据。

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
while True:
    cmd = input('Please input cmd >>>')
    conn.send(cmd.encode('utf-8'))
    ret = conn.recv(1024)
    print(ret.decode('utf-8'))

conn.close()
sk.close()


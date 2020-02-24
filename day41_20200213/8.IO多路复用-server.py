#! encoding:utf-8
# 使用IO多路复用技术实现socket-server
# IO多路复用，即操作系统提供了代理select，来帮助监听连接操作
# 比如:accept,recv;一旦有连接建立，就发信号给socket，让socket去操作
# select列表中，可以有多个accept和recv，谁收到建立连接请求，谁就激活了并被显示和使用
# 空的，没有接收到请求的，没有被激活的，默认隐藏了。

import select
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)
sk.listen()

read_list = [sk]
while True:
    r_list, w_list, x_list = select.select(read_list, [], [])    # 建立代理，传入accept、conn列表,帮我监听连接操作
    # print('*****', r_list)
    for i in r_list:
        if i is sk:
            conn, addr = i.accept()
            read_list.append(conn)
        else:
            msg = i.recv(1024)
            if msg == b'':
                i.close()
                read_list.remove(i)
                continue
            print(msg)
            i.send(b'ByeBye')

# conn, addr = sk.accept()

sk.close()
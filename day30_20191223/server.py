#! encoding:utf-8
import socket

sk = socket.socket() #买手机
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8080)) #装手机卡
sk.listen() # 监听,等着别人打电话

conn, addr = sk.accept()    # 接受别人的电话，conn连接，addr地址
message = conn.recv(1024)   # 听别人说话
print(message)
conn.send(b'HI, I am from server.') # 和别人说话，必须传一个bytes类型

conn.close()    # 挂电话
sk.close()  #关机



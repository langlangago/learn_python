#! encoding:utf-8

# 前端 学三个东西
# HTML 内容
# CSS 样式
# JS 动作
# 前端的本质：服务端、浏览器、文件

# 服务端，用网页做客户端来访问
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
conn.recv(1024)
conn.send(b'HTTP/1.1 200 OK \r\n\r\n')      # 按照Http协议，先发送一段数据
#conn.send(b'<h1>Hello World!</h1>')
# 从文件里读取数据，并返回给客户端
with open('data.txt', 'rb') as f:
    msg = f.read()
conn.send(msg)

conn.close()
sk.close()
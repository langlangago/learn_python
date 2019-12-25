#! encoding:utf-8
# ftp client端，读取本地文件，并传送给server端。
import socket

sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)
filename = input('Please input the filename which to upload >>>')
sk.send(filename.encode('utf-8'))

with open(filename, 'rb') as f:
    for line in f:
        print(line.decode('utf-8'))
        sk.send(line)
#sk.send(b'bye')

sk.close()

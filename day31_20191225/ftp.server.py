#! encoding:utf-8
# ftp server端，接受client传送来的文件数据，重命名后保存起来
import socket
import os

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn,addr = sk.accept()

ret = conn.recv(1024)
filename = ret.decode('utf-8')
new_file = filename + '.bak'
f = open(new_file, 'w', encoding='utf-8')
f.close()

sum = ''
while True:
    content = conn.recv(1024)
    #print(content.decode('utf-8'))
    if content:
       # print(content.decode('utf-8'))
        sum += content.decode('utf-8')
    else:
        break
print(sum)

with open(new_file, 'wb') as f:
    print(content.decode('utf-8'))
    f.write(sum.encode('utf-8'))


conn.close()
sk.close()



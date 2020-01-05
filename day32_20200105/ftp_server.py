#! encoding:utf-8
# 大文件传输，使用定制报头

import socket
import struct
import json

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()

conn, addr = sk.accept()
ret = conn.recv(4)    # 接收报头长度，使用了struct模块固定地4个字节
head_len = struct.unpack('i', ret)[0]
head_bytes = conn.recv(head_len)    # 接收报头
head_json = head_bytes.decode('utf-8')
head_dict = json.loads(head_json)

# 接收文件，一边接收，一边写入
buffer = 4096
filesize = 0
with open(head_dict['filename'], 'wb') as f:
    while True:
        if filesize < head_dict['filesize']:
            content = conn.recv(buffer)
            f.write(content)
            filesize += len(content)
            print(filesize, head_dict['filesize'])
        else:
            break

conn.close()
sk.close()












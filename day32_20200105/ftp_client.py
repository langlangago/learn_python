#! encoding:utf-8

import socket
import struct
import json
import os
import  hashlib

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

# 先定制报头
head_dict = {'filename':'闪电侠.The.Flash.S05E14.中英字幕.HDTVrip.720P-人人影视.mp4',
             'filepath':'F:\迅雷下载',
             'filesize':None}
filesize = os.path.getsize(os.path.join(head_dict['filepath'], head_dict['filename']))
head_dict['filesize'] = filesize

# 发送报头大小，发送报头
# 数据网络传输必须用bytes类型传输，故dict-->str-->bytes
# 用json.dumps操作内存数据，即可把字典转成str，然后str.encode把str转成bytes
# 先转换str，再计算大小，再传输大小（用struct转换后，固定传4个字节bytes数据），在发送报头
head_str = json.dumps(head_dict)
head_len = len(head_str)
num = struct.pack('i', head_len)
sk.send(num)
sk.send(head_str.encode('utf-8'))

# 发送文件，一边读一边发,读一次发一次
buffer = 4096
file = os.path.join(head_dict['filepath'], head_dict['filename'])
with open(file, 'rb') as f:
    while True:
        if filesize >= buffer:
            content = f.read(buffer)
            sk.send(content)
            filesize -= buffer
        else:
            content = f.read(filesize)
            sk.send(content)
            break

sk.close()


























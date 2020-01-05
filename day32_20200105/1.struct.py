#! encoding:utf-8

import struct

ret = struct.pack('i',5)
print(ret)
ret2 = struct.unpack('i', ret)
print(ret2[0])
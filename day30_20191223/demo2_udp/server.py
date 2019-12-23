#! encoding:utf-8

# udp socket
import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8080))

ret, addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))
sk.sendto(b'bye', addr)

sk.close()
import socket, sys
print(sys.path)
sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

sk.sendto(b'bye', ip_port)
ret, addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()
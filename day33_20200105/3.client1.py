import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>>')
    if msg == 'q':
        break
    else:
        sk.send(('Client1: '+msg).encode('utf-8'))
        ret = sk.recv(1024)
        print(ret.decode('utf-8'))

sk.close()
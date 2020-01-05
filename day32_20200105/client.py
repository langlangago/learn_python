# coding=utf-8
import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while True:
    cmd = sk.recv(1024)
    if cmd.decode('gbk') == 'q':
        break
    ret = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out = ret.stdout.read()
    std_err = ret.stderr.read()
    num = len(std_out) + len(std_err)
    sk.send(str(num).encode('gbk')) # 先传大小过来，让接收端做好准备
    sk.recv(1024)
    sk.send(std_out)
    sk.send(std_err)

sk.close()
#! encoding:utf-8
import socket
import subprocess

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

sk.sendto(b'Hello', ip_port)
while True:
    cmd, addr = sk.recvfrom(1024)
    ret = subprocess.Popen(cmd.decode('gbk'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = 'Stdout:' + ret.stdout.read().decode('gbk')
    stderr = 'Stderr:' + ret.stderr.read().decode('gbk')
    sk.sendto(stdout.encode('utf-8'), addr)
    sk.sendto(stderr.encode('utf-8'), addr)

sk.close()

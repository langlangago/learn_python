#! encoding:utf-8
import socket
import subprocess

sk = socket.socket()
ip_port = ('127.0.0.1', 8080)
sk.connect(ip_port)
while True:
    cmd = sk.recv(1024)
    ret = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout = 'Stdout:' + ret.stdout.read().decode('gbk')
    stderr = 'Stderr:' + ret.stderr.read().decode('gbk')
    sk.send(stdout.encode('utf-8'))
    sk.send(stderr.encode('utf-8'))

sk.close()



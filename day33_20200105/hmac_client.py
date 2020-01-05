# coding=utf-8
import socket
import hmac

SECRET_KEY = b'alex'

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
msg = sk.recv(1024)
h = hmac.new(SECRET_KEY, msg)
sk.send(h.digest())

sk.close()


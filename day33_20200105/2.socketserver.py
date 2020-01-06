#! encoding:utf-8

import socketserver

class MyClass(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            ret = self.request.recv(1024)   # == conn
            print(ret.decode('utf-8'))
            msg = input('>>>')
            if msg == 'q':
                self.request.close()
                break
            else:
                self.request.send(msg.encode('utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyClass)
    # thread 线程
    server.serve_forever()

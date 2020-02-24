#! encoding:utf-8
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.setblocking(False)       # 把socket中所有阻塞的方法变为非阻塞 recv recvfrom accept
sk.listen()

conn_l = []
conn_del = []
while True:
    try:
        conn, addr = sk.accept()
        print('建立连接了', addr)
        conn_l.append(conn)
    except BlockingIOError:
        for conn in conn_l:
            try:
                msg = conn.recv(1024)
                if msg == b'':
                    conn_del.append(conn)
                    continue
                print(msg)
                conn.send(b'Byebye')
            except BlockingIOError:
                pass
        for conn in conn_del:
            conn_del.remove(conn)
        conn_del.clear()
sk.close()
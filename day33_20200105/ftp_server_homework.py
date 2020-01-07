#! encoding:utf-8
# 登录注册，用户认证
# 多用户同时登录，加密认证，客户端和服务端同时加密
import socketserver
import struct
import hashlib
import struct
import json
import os

method_dict = {'登录':'sign_in', '注册':'sign_up'}

class Person:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    # 登录加密，客户端传密码的md5值过来，服务端用salt再次md5存文件
    # 保证1、加密在服务端，2、传输过程中不是明文
    def encrypt(self):
        md5 = hashlib.md5(b'ftp')
        md5.update(self.passwd.encode('utf-8'))
        return md5.hexdigest()

    # 登录函数，读取文件中的用户名和密码，如果相同就返回True
    def sign_in(self):
        with open('user.txt', 'a+') as f:
            f.seek(0)
            for line in f:
                user = line.split('|')
                if self.name == user[0]:
                    if self.encrypt() == user[1].strip('\n'):
                        print('登录成功，请选择操作')
                        msg = '登录成功，请选择操作'
                        return 0, msg
                    else:
                        print('登录失败，密码错误，请重新输入用户名密码')
                        msg = '登录失败，密码错误，请重新输入用户名密码'
                        return 1, msg
            print('登录失败，用户名不存在，现在进行自动注册')
            msg = '登录失败，用户名不存在，现在进行自动注册'
            return 2, msg

    # 注册函数，将用户名和密码写入文件
    def sign_up(self):
        with open('user.txt', 'a+') as f:
            f.seek(0)
            for line in f:
                user = line.split('|')
                if self.name == user[0]:
                    print('用户名已存在，请登录')
                    return 3
            f.write(self.name+'|'+self.encrypt()+'\n')
            print('注册成功，请选择操作')
            msg = '注册成功，请选择操作'
        return 0, msg    # 不知道返回啥，先占位

# 反射，让用户选择登录或者注册 sign_in or sign_up
# 注册成功，即认证成功。注册失败，跳到登录。登录成功即认证成功
# method = input('请选择登录or注册(eg:登录)>>>')
# name = input(method+'：请输入用户名:>>>')
# passwd = input(method+'：请输入密码:>>>')
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        msg = '请选择登or注册(eg:登录)>>>'
        self.request.send(msg.encode('utf-8'))
        method = self.request.recv(6).decode('utf-8')

        self.request.send((method+'：请输入用户名>>>').encode('utf-8'))
        name_len = self.request.recv(4)
        name_len = struct.unpack('i', name_len)[0]
        name = self.request.recv(name_len).decode('utf-8')

        self.request.send((method+'：请输入密码>>>').encode('utf-8'))
        passwd_len = self.request.recv(4)
        passwd_len = struct.unpack('i', passwd_len)[0]
        passwd = self.request.recv(passwd_len).decode('utf-8')

        p = Person(name, passwd)
        ret = getattr(p, method_dict[method])()
        self.request.send(ret[1].encode('utf-8'))
        self.request.send(str(ret[0]).encode('utf-8'))
        # 1 登录类型，密码错误，重新输入用户名密码，登录
        # 2 登录类型，用户名不存在，注册
        # 3 注册类型，用户名已存在，登录
        if ret[0] == 1 or ret[0] == 3:
            self.request.send(('登陆：请输入用户名>>>').encode('utf-8'))
            name_len = self.request.recv(4)
            name_len = struct.unpack('i', name_len)[0]
            name = self.request.recv(name_len).decode('utf-8')
            self.request.send(('登陆：请输入密码>>>').encode('utf-8'))
            passwd_len = self.request.recv(4)
            passwd_len = struct.unpack('i', passwd_len)[0]
            passwd = self.request.recv(passwd_len).decode('utf-8')
            p = Person(name, passwd)

            # name = input('登录：请输入用户名:>>>')
            # passwd = input('登录：请输入密码:>>>')
            # p = Person(name, passwd)
            p.sign_in()
        elif ret[0] == 2:
            p.sign_up()

        # 请选择操作
        print('开始上传文件')
        self.request.send('请选择要上传的文件>>>'.encode('utf-8'))
        ret = self.request.recv(4)
        head_len = struct.unpack('i', ret)[0]
        head_bytes = self.request.recv(head_len)
        head_str = head_bytes.decode('utf-8')
        head_dict = json.loads(head_str)

        # 判断服务端是否有此文件，有 --> 计算md5值，并对比
        # 相同，break；不同，断点续传。
        # 没有 --> 传输文件并保存。
        ret = os.path.exists(os.path.join(os.getcwd(), head_dict['filename']))
        if ret:
            print('文件已存在')
            msg = '文件已存在'
            self.request.send(msg.encode('utf-8'))
            self.request.send('1'.encode('utf-8'))
            # 计算md5值，并在服务端比较，得出决定是结束，还是让客户端断点续传
            md5 = hashlib.md5()
            with open(head_dict['filename'], 'rb') as f:
                for line in f:
                    md5.update(line)
            print(md5.hexdigest())

        else:
            print('文件不存在')
            msg = '文件不存在'
            self.request.send(msg.encode('utf-8'))
            self.request.send('0'.encode('utf-8'))
            # 接收文件，一边接收，一遍计算md5，一边写入
            buffer = 4096
            filesize = 0
            md5 = hashlib.md5()
            with open(head_dict['filename'], 'wb') as f:
                while True:
                    if filesize < head_dict['filesize']:
                        content = self.request.recv(buffer)
                        md5.update(content)
                        f.write(content)
                        filesize += len(content)
                    else:
                        break
            md5_server = md5.hexdigest()
            md5_client = self.request.recv(32).decode('utf-8')
            if md5_server == md5_client:
                msg = '文件一致性校验正确，上传成功'
                self.request.send(msg.encode('utf-8'))
            else:
                msg = '文件一致性校验错误，上传失败'
                self.request.send(msg.encode('utf-8'))



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyServer)
    server.serve_forever()

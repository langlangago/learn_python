#! encoding:utf-8
# 登录注册，用户认证
# 多用户同时登录，加密认证，客户端和服务端同时加密

class Person:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    # 登录函数，读取文件中的用户名和密码，如果相同就返回True
    def sign_in(self):
        with open('user.txt', 'a+') as f:
            f.seek(0)
            for line in f:
                user = line.split('|')
                if self.name == user[0]:
                    if self.passwd == user[1].strip('\n'):
                        print('登录成功，请选择操作')
                        return 0
                    else:
                        print('登录失败，密码错误，请重新输入用户名密码')
                        return 1
            print('登录失败，用户名不存在，现在进行自动注册')
            return 2

    # 注册函数，将用户名和密码写入文件
    def sign_up(self):
        with open('user.txt', 'a+') as f:
            f.seek(0)
            for line in f:
                user = line.split('|')
                if self.name == user[0]:
                    print('用户名已存在，请登录')
                    return 3
            f.write(self.name+'|'+self.passwd+'\n')
            print('注册成功，请选择操作')
        return 0 # 不知道返回啥，先占位

# 反射，让用户选择登录或者注册 sign_in or sign_up
# 注册成功，即认证成功。注册失败，跳到登录。登录成功即认证成功
method_dict = {'登录':'sign_in', '注册':'sign_up'}
method = input('请选择登录or注册(eg:登录)>>>')
name = input(method+'：请输入用户名:>>>')
passwd = input(method+'：请输入密码:>>>')
p = Person(name, passwd)
ret = getattr(p, method_dict[method])()
# 1 登录类型，密码错误，重新输入用户名密码，登录
# 2 登录类型，用户名不存在，注册
# 3 注册类型，用户名已存在，登录
if ret == 1 or ret == 3:
    name = input('登录：请输入用户名:>>>')
    passwd = input('登录：请输入密码:>>>')
    p = Person(name, passwd)
    p.sign_in()
elif ret == 2:
    p.sign_up()

# 请选择操作
print('Continue......')


#! encoding:utf-8

# hashlib是一个摘要算法模块
# 主要有md5,SHA1,SHA256等算法
# 普通md5值计算
# import hashlib
# md5 = hashlib.md5()
# md5.update(b'123456')
# print(md5.hexdigest())
#
# # md5 加盐
# import hashlib
# md5 = hashlib.md5(bytes('salt', encoding='utf-8'))
# md5.update(b'123456')
# print(md5.hexdigest())
#
# # md5 动态加盐
# import hashlib
# md5 = hashlib.md5(b'salt' + b'123')
# md5.update(b'123456')
# print(md5.hexdigest())
#
# # md5 可以update多次，和一次update结果一样
# # 比如求一个文件的md5值，分拆一个文件为多行，多次update
# import hashlib
# md5 = hashlib.md5()
# md5.update(b'123')
# md5.update(b'456')
# print(md5.hexdigest())

# 联系，注册登录，密码加密存储
import hashlib
def register():
    user = input('请输入用户名:').strip()
    passwd = input('请输入密码:').strip()
    if user and passwd:
        md5 = hashlib.md5()
        md5.update(bytes(passwd, encoding='utf-8'))
        passwd = md5.hexdigest()
        with open('userinfo', 'w') as f:
            f.write(user+'|'+passwd)
        print('注册成功，请登录--->')
    else:
        print('用户名和密码不能为空。')

def login():
    user = input('请输入用户名:').strip()
    passwd = input('请输入密码:').strip()
    if user and passwd:
        with open('userinfo', 'r') as f:
            line = f.readline().strip('\n')
            user_f, passwd_f = line.split('|')
        md5 = hashlib.md5()
        md5.update(bytes(passwd, encoding='utf-8'))
        passwd = md5.hexdigest()
        if user == user_f and passwd == passwd_f:
            print('登录成功。')
        else:
            print('用户名或者密码错误。')
    else:
        print('用户名和密码不能为空。')

register()
login()
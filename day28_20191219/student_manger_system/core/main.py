#! encoding:utf-8
import sys
from conf.config import *
from core.Manager import  Manager

# 登录函数，从userinfo文件读取用户名密码验证后，
# 返回用户名和角色，返回角色方便操作对应视图
def login():
    usr = input('username:')
    pwd = input('password:')
    with open(userinfo) as f:
        for line in f:
            username, passwd, role = line.split('|')
            if username == usr and passwd == pwd:
                print('\033[1;32mLogin success!\033[0m')
                return {'username':username, 'role':role}
            else:
                print('Wrong username or password.')
                return None


# 主函数，登录成功后，根据返回的角色操作对应的视图
#  打印菜单（某个类可以做什么事）,输入序号，调用对应的类的方法
def main():
    print('\033[1;42m欢迎登陆选课系统\033[0m')
    ret = login()
    if ret:
        # 反射，获取角色类
        role_class = getattr(sys.modules[__name__], ret['role'].strip('\n'))
        # 实例化类，创建对象
        obj = role_class(ret['username'])
        # 打印菜单，并附上序号
        for i in list(enumerate(role_class.menu, 1)):
            print(i[0], i[1][0])


        num = int(input('请输入编号：'))
        # 通过反射调用相应的方法
        getattr(obj, role_class.menu[num-1][1])()
        #except ValueError:
        #    print('请输入正确的数字编号。')
#! encoding:utf-8

# 通过反射 hasattr,getattr,delattr
# 对象名 获取对象属性 和 普通方法
# 类名  获取 静态属性，静态方法，类方法

class Manager:
    key = 123
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
    def hello(self):
        print('Hello Login.')
    @classmethod
    def create_user(cls):
        print('Already Create User.')
    @staticmethod
    def del_user():
        print('Del User.')

tom = Manager('tom', '123')
cmd1 = 'user'
cmd2 = 'hello'
print(getattr(tom, cmd1))
getattr(tom, cmd2)()

cmd3 = 'key'
cmd4 = 'create_user'
cmd5 = 'del_user'
print(getattr(Manager, cmd3))
getattr(Manager, cmd4)()
getattr(Manager, cmd5)()
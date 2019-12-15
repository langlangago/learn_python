#! encoding:utf-8

# 封装，就是把自己的属性和方法隐藏起来。
# 用双下方法，外部不能直接调用。
class Person:
    __key = 123 # 私有静态属性
    def __init__(self, name, password):
        self.name = name
        self.__password = password # 私有属性

    def __get_passwd(self): # 私有方法
        return self.__password

    def login(self): # 正常方法，调用私有方法
        return self.__get_passwd()

alex = Person('alex', 'alex123')
print(alex.__dict__)
print(alex._Person__password) #_类名_属性名
print(alex.login())

# 所有的私有 都是在变量的左边加上双下划綫
    # 对象的私有属性
    # 类中的私有方法
    # 类中的静态私有属性
# 所有的私有的 都不能在类的外部使用

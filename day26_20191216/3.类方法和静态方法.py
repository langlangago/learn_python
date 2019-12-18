#! encoding:utf-8

# classmethod 类的方法
# staticmethod 静态方法
# 类的操作行为

# classmethod 类的方法，把外部的一个函数，变成类中的一个方法，这个方法就可以直接被类调用，不需要依托任何对象
# 当这个方法的操作只涉及到类的静态属性的时候，就可以使用classmethod来装饰这个方法
# class Goods:
#     discount = 0.8
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.discount
#
#     @classmethod
#     def change_discount(cls, new_discount):
#         cls.discount = new_discount
#
# apple = Goods('apple', 5)
# print(apple.price)
# Goods.change_discount(0.6)
# print(apple.price)

# staticmethod  java
class Login:
    def __init__(self, username, passwd):
        self.__username = username
        self.__passwd = passwd

    def login(self):pass
    @staticmethod     # 强制把和类没关系的函数变成类的一个静态方法，以便都是面向对象
    def get_user_pwd():
        user = input('用户名：')
        pwd = input('密码：')
        Login(user, pwd)
Login.get_user_pwd()
# 面向对象的程序中
# 如果一个方法，既和类没关系，又和对象没关系，那么用staticmethod装饰器就可以把这个函数变成类的一个静态方法

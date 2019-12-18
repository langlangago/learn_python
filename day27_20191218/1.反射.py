#! encoding:utf-8

# isinstance, issubclass
# class A:pass
# class B(A):pass
# a = A()
# print(isinstance(a, A))
# print(issubclass(B, A))
# print(issubclass(A,B))

# 反射是用输入的字符串来调用属性和方法
# 用字符串类型的的名字去调用变量
# getattr,hasattr,delattr,setattr
# 对象.属性，对象.方法，类.属性，类.方法， 模块的方法(import)
# 内置模块，自己模块，都可以用反射

# class A:
#     def func(self):
#         print('in func.')
# a = A()
# a.name = 'alxe'
# a.age = 18
# 反射对象的属性
# print(getattr(a, 'name'))   # 通过变量名的字符串形式取到值
# print(a.__dict__)
# 变量名 = input('>>>>')
# print(getattr(a, 变量名))
# print(a.__dict__[变量名])
# 反射对象的方法
# a.func()
# ret = getattr(a, 'func')
# ret()

# 反射类的属性和方法
# class A:
#     price = 20
#     @classmethod
#     def func(cls):
#         print('in func.')
#
# print(A.price)
# print(getattr(A, 'price'))
# A.func()
# getattr(A, 'func')()

# 反射模块的方法和属性
# import my
# print(my.day)
# print(getattr(my, 'day'))
# my.wahaha()
# getattr(my, 'wahaha')()

# 内置模块
# import time
# print(time.time())
# print(time.asctime())
# print(getattr(time, 'time')())
# print(getattr(time, 'asctime')())

# 反射自己模块的方法和函数，要找到模块名字
# import sys
# year = 2019
# def qqxing():
#     print('QQxing')
# print(sys.modules['__main__'].year)
# print(getattr(sys.modules['__main__'], 'year'))
# sys.modules['__main__'].qqxing()
# getattr(sys.modules['__main__'], 'qqxing')()
# 变量名 = input('>>>>')
# print(getattr(sys.modules[__name__], 变量名))

# # 要反射的函数有参数怎么办?
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(getattr(time, 'strftime')('%Y-%m-%d %H:%M:%S'))
#
# # 一个模块中的类能不能反射得到，用hasattr ,和getattr夫妻档
# import my
# print(getattr(my, 'C'))
# if hasattr(my, 'day'):
#     print(getattr(my, 'day'))

# setattr , delattr ，不重要，一般不用
# setattr
class A:pass
a = A()
setattr(a, 'name', 'alex')
setattr(A, 'name', 'tom')
print(a.name)
print(A.name)

# delattr
delattr(a, 'name')
print(a.name)
delattr(A, 'name')
print(a.name)

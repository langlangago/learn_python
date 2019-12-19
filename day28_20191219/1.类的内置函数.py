#! encoding:utf-8

# item系列，__new__, __eq__, __hash__

# item系列，实现字典的调用方式dict[]=''和操作
# __getitem__, __setitem__, __delitem__
# class Foo:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __getitem__(self, item):
#         if hasattr(self, item):
#             return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#     def __delitem__(self, key):
#         del self.__dict__[key]
# f = Foo('alex', 35)
# print(f['name'])
# f['sex'] = 'male'
# print(f.__dict__)
# del f['sex']
# print(f.__dict__)

# __new__构造函数，创建一个对象。
# __init__ 初始化一个对象，系统自动调用object.__new__创建了一个self对象
# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init function.')
#     def __new__(cls, *args, **kwargs):
#         print('in __new__ function.')
#         return object.__new__(A, *args, **kwargs)
#
# # 先执行__new__方法创建了一个self对象，后执行__init__方法初始化self对象的属性
# # 等于自己实现了object的__new__方法,用于替代。
# a = A()
# a1 = A()
# print(id(a))
# print(id(a1))
# print(a.x)

# example: 设计模式--单例模式，用__new__自己实现
# 单例模式，一个类始终只实例化一个对象，后面再实例化拿到的还是同一个对象
# 后面实例化之后的操作，是在第一次实例化对象的基础上进行。
# class A:
#     __instance = False
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance:
#             return cls.__instance
#         cls.__instance =  object.__new__(cls)
#         return cls.__instance
#
# alex = A('alex', 35)
# alex.cloth = '小花袄'
# print(alex.__dict__)
# tom = A('tom', 28)
# print(tom.__dict__)

# # __eq__ ,自己定义 == 判断的依据，默认是比较内存地址
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
# a = A('alex', 22)
# b = A('alex', 22)
# print(a == b)
# 如果自己未实现__eq__方法，这里会默认调用object.__eq__
# 比较内存地址，结果为False；自己实现了__eq__,结果就为True

# __hash__，hash()的调用实现，计算对象的hash值
# 默认有一些数据类型不可hash，但你可以自己实现__hash__让他可hash

class A:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
    def __hash__(self):
       # 调用父类object的hash方法实现hash值，计算可hash类型的hash值
        return hash(self.name + self.sex)

a = A('alex', 'male', 22)
b = A('alex', 'male', 25)
print(hash(a))  # 使用自定义的hash方法（__hash__）
print(hash(b))  # a。b两个属性不同的对象，hash值一样





















#! encoding:utf-8

# property 内置装饰器函数，作用是将方法转换成属性，常用在面向对象中
# 某些方法看起来更像是属性，比如面积，BMI值,所以我们就用property装饰器
# 让这些方法看起来是属性，按照属性的调用方法使用

# #example: circle's area
# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     @property
#     def area(self):
#         return pi * self.r ** 2
#     @property
#     def perimeter(self):
#         return 2 * pi * self.r
#
# c = Circle(5)
# # print(c.area()) # 加上property装饰器后调用失败
# # print(c.perimeter())
# print(c.area, c.perimeter) # 加上property装饰器后，调用方法可以像属性一样调用

# example2: person's bmi
# class Person:
#     def __init__(self, name, high, weight):
#         self.name = name
#         self.high = high
#         self.weight = weight
#     @property
#     def bmi(self):
#         return self.weight / self.high **2
#
# alex = Person('alex', 1.8, 90)
# print(alex.bmi)

# example2: apple discount，price方法变属性后，给出打折的价格
# class Goods:
#     discount = 0.8
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.discount
# apple = Goods('apple', 5)
# print(apple.price)

# example3: setter,修改私有属性

# class Person:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name + 'sb'
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
# alex = Person('金老板')
# print(alex.name)
# alex.name = '全班'
# print(alex.name)

# deleter,setter 属性的查看、修改、删除
class Person:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    @name.deleter
    def name(self):
        del self.__name
alex = Person('金老板')
print(alex.name)
alex.name = 'Tom'
print(alex.name)
del alex.name
print(alex.name)














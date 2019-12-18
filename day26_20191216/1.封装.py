#! encoding:utf-8

# 属性封装私有化后，想要查看或者改变属性值，要借助方法,get_name,set_name
# class Room:
#     def __init__(self, name, length, width):
#         self.__name = name
#         self.__length = length
#         self.__width = width
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, new_name):
#         if type(new_name) is str and new_name.isdigit() == False:
#             self.__name = new_name
#         else:
#             print('输入的姓名不合法')
#
#     def area(self):
#         return self.__length * self.__width
#
# jin = Room('金老板', 2, 1)
# print(jin.area())
# jin.set_name('alex')
# print(jin.get_name())

# 父类的私有属性，不能被子类调用

class Foo:
    __key = 123      # _Foo__key

class Son(Foo):
    print(Foo.__key) # _Son_key
    # AttributeError: type object 'Foo' has no attribute '_Son__key'

















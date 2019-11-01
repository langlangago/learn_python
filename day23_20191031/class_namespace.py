#! encoding:utf8
# 类里可以定义两种属性
# 静态属性 （变量），动态属性（函数，方法）

# 类指针对象
# 类有自己的命名空间，对象通过类指针对象来关联到类。
# 类的静态属性和动态属性，类和对象都可以调用
# 对象先在自己的namespace里找，找不到就是类的namespace里找
# 对象不能修改类的静态属性，强制修改等于给自己namespace添加一个值，和类无关。
# class Course:
#     language = 'Chinese'
#     def __init__(self, teacher, course_name, period, price):
#         self.teacher = teacher
#         self.name = course_name
#         self.period = period
#         self.price = price
#
# python = Course('alex', 'Python', '6 months', 20000)
# linux = Course('lilei', 'linux', '6 months', 20000)
# python.language = 'English' #赋值给对象自己，和类无关。等于给自己字典加一个key、value，认内存地址的。
# print(python.language)
# print(python.__dict__)
# print(Course.language)
# print(Course.__dict__)
# print(linux.language)
# print(linux.__dict__)

# 对于不可变数据类型的静态属性，最好用类名去调用。
# 对于可变数据类型，修改是共享的，重新赋值是独立的。

# 创建一个类，每实例化一个对象就计数，个数加一，所有对象共享这个数据。
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
#
# f1 = Foo()
# f2 = Foo()
# print(f1.count, f2.count)

# 绑定方法
# 当对象调用类的一个方法时，这个方法就和这个对象绑定了。
# 对象就当做self传给了方法，对象的参数传给了方法。

# class Foo:
#     def func(self):
#         pass
#
# f1 = Foo()
# print(f1)
# print(f1.func)
# print(Foo.func)

# 包，__init__, 导入包的时候会执行__initi__文件。
# import package , 类似于类的实例化
# import time
# time.time()












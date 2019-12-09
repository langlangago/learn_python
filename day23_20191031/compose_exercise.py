# from  math import pi
#
# # 求圆环的面积和周长,用到组合
# # 组合，一个类的对象做另一个类的属性
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return self.r**2 * pi
#
#     def perimeter(self):
#         return self.r * pi * 2
#
#
# class Ring:
#     def __init__(self, outside_r, inside_r):
#         self.outside_c = Circle(outside_r)
#         self.inside_c = Circle(inside_r)
#
#     def area(self): return self.outside_c.area() - self.inside_c.area()
#     def perimeter(self):return self.outside_c.perimeter() - self.inside_c.perimeter()
#
#
# ring = Ring(20, 10)
# print(ring.area(), ring.perimeter())

# 一个生日类，一个老师类，老师有生日属性

# class Birthday:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Teacher:
#     def __init__(self, name, age, birthday):
#         self.name = name
#         self.age = age,
#         self.birthday = birthday
#
# birthday = Birthday(1987, 11, 6)
# alex = Teacher('Alex', 31, birthday)
# print(alex.birthday.year)


# 创建一个类，每实例化一个对象就计数，所有对象共享这个值
# 静态变量，用类名操作的时候，是共享的
class Foo():
    count = 0
    def __init__(self):
        Foo.count += 1

f1 = Foo()
f2 = Foo()
print(f1.count)
print(f2.count)
f3 = Foo()
print(f3.count)

















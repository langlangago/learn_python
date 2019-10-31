#! encoding:utf8

# 类，实例化，实例。
# 实例的属性和方法。

# 人狗大战
# class Person:
#     def __init__(self, name, blood, aggr, sex):
#         self.name = name
#         self.blood = blood
#         self.aggr = aggr
#         self.sex = sex
#
#     def attack(self, dog):
#         dog.blood -= self.aggr
#         print('%s被攻击了,剩余血量%s' %(dog.name, dog.blood))
#
# class Dog:
#     def __init__(self, name, blood, aggr, kind):
#         self.name = name
#         self.blood = blood
#         self.aggr = aggr
#         self.kind = kind
#
#     def bite(self, person):
#         person.blood -= self.aggr
#         print('%s被咬了,剩余血量%s' %(person.name, person.blood))
#
#
# alex = Person('alex', 100, 20, 'male')
# wangcai = Dog('wangcai', 200, 10, 'taddy')
# alex.attack(wangcai)
# wangcai.bite(alex)

# 上上去砍柴，开车去东北，最爱大保健
# class Person():
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
#
#     def shangshan(self):
#         print('%s,%s岁,上山去砍柴.' % (self.name, self.age))
#
#     def kaiche(self):
#         print('%s,%s岁,开车去东北.' % (self.name, self.age))
#
#     def favor(self):
#         print('%s,%s岁,最爱大保健.' % (self.name, self.age))
#
# zhangsan = Person('张三', 18)
# lisi = Person('李四', 22)
# wangwu = Person('王五', 30)
# zhangsan.shangshan()
# lisi.kaiche()
# wangwu.favor()

# 圆形的周长和面积
from math import  pi
class Cir:
    def __init__(self, r):
        self.r = r

    def zhouchang(self):
        return 2*pi*self.r

    def area(self):
        return pi*(self.r**2)

c1 = Cir(5)
print(c1.area())
print(c1.zhouchang())

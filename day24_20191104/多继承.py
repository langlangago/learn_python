#! encoding:utf-8
# 多继承只有Python有，几个景点场景如下：
# 钻石集成 D->B->A, D->C->A
# python3 新式类，默认继承object，广度优先
# 多继承中，子类的对象调用一个方法，默认就近原则，找的顺序是
# python3是广度优先,python2是深度优先，python2.7分经典类和新式类。
# 新式类的mro()方法，查看广度优先的继承顺序
# 继承，什么是什么
# 组合，什么有什么

# class A:
#     def func(self):
#         print('A')
#
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
#
# class C(A):
#     def func(self):
#         super().func()
#         print('C')
#
# class D(B,C):
#     def func(self):
#         super().func()
#         print('D')
#
# d = D()
# d.func()
# print(D.mro()) # 查看新式类的继承顺序

# 两分支集成
# D->B->A, D->C->E
# class A:
#     def func(self):
#         print('A')
#
# class E:
#     def func(self):
#         print('E')
#
# class B(A):
#     def func(self):
#         super().func()
#         print('B')
#
# class C(E):
#     def func(self):
#         super().func()
#         print('C')
#
# class D(B,C):
#     def func(self):
#         super().func()
#         print('D')
#
# d = D()
# d.func()
# print(D.mro())

# 小乌龟问题，能找到先找到，不然后面就找不到了（B）
class A:
    def func(self):
        print('A')

class B(A):
    def func(self):
        super().func()
        print('B')

class C(A):
    def func(self):
        super().func()
        print('C')

class D(B):
    def func(self):
        super().func()
        print('D')
class E(C):
    def func(self):
        super().func()
        print('E')

class F(D, E):
    def func(self):
        super().func()
        print('F')
f = F()
f.func()
print(F.mro())





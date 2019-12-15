#! encoding:utf-8

# 接口类和抽象类都是一种规范，开发规范，
# 规范子类必须实现特定的方法，不实现就报错。
# Python原生支持抽象类，不支持接口类（可以模拟实现）
# 抽象类，从类中提取出共同处形成抽象类，单继承，可以在类中写代码实现
# 接口类，多继承，必须不能在类中写接口实现代码，要在子类中写。
# 接口类的代表，动物；抽象类的代表，os中一切皆文件，都要有读写功能。

# 接口类， 多继承
# example1, pay class
# from abc import abstractclassmethod, ABCMeta
#
# class Payment(metaclass=ABCMeta): # 接口类，不能实例化
#     @abstractclassmethod
#     def pay(self):
#         pass
#
# class WeChatPay(Payment):
#     def pay(self):
#         print('WeChatPay.')
#
# class AliPay(Payment):
#     # def fuqian(self):
#     # 报错，TypeError: Can't instantiate abstract class AliPay with abstract methods pay
#     def pay(self):
#         print('AliPay ')
#
# w = WeChatPay()
# a = AliPay()
# a.pay()

# 接口类的多继承，动物园里的动物
# tiger walk，swim
# eagle walk, fly
# swan walk, swim, fly

# from abc import abstractclassmethod, ABCMeta
# class WalkAnimal(metaclass=ABCMeta):
    # @abstractclassmethod
    # def walk(self):pass

# class SwimAnimal(metaclass=ABCMeta):
    # @abstractclassmethod
    # def swim(self):pass

# class FlyAnimal(metaclass=ABCMeta):
    # @abstractclassmethod
    # def fly(self): pass

# class Tiger(WalkAnimal, SwimAnimal):
    # def walk(self):print('Tiger can walk.')
    # def swim(self):print('Tiger can swim.')

# class Eagle(WalkAnimal, FlyAnimal):
    # def walk(self):print('Eagle can walk.')
    # def fly(self):print('Eagle can fly')

# class Swan(WalkAnimal, SwimAnimal, FlyAnimal):
    # def walk(self):print('Swan can walk.')
    # def swim(self):print('Swan can swim')
    # def fly(self):print('Swan can fly')

# t = Tiger()
# e = Eagle()
# s = Swan()
# t.swim()
# e.walk()
# s.fly()

# 抽象类， 单继承，可以在类中写代码实现。
# example,对操作系统而言，一切皆对象
# 文件，进程，磁盘，都是文件，都可以读写。

from abc import abstractclassmethod, ABCMeta

class AllFile(metaclass=ABCMeta):
    all_type = 'file'
    @abstractclassmethod
    def read(self):
        print('子类必须定义读功能.')
        with open('filename') as f :pass

    @abstractclassmethod
    def write(self):
        print('子类必须定义写功能.')
        pass

class TXT(AllFile):
    def read(self):
        print('文本数据的读方法.')
    def write(self):
        print('文本数据的写方法.')

class STAT(AllFile):
    def read(self):
        print('磁盘数据的读方法.')
    def write(self):
        print('磁盘数据的写方法.')

class Process(AllFile):
    def read(self):
        print('进程数据的读方法.')
    def write(self):
        print('进程数据的写方法.')

# 这样大家被归一化了，实现的都是类似的功能（读，写），也就是一切皆文件的思想
wenbenwenjian = TXT()
cipanwenjian = STAT()
jinchnegwenjian = Process()
wenbenwenjian.read()
cipanwenjian.read()
jinchnegwenjian.read()

# 抽象类 ： 规范
# 一般情况下 单继承 能实现的功能都是一样的，所以在父类中可以有一些简单的基础实现
# 多继承的情况 由于功能比较复杂，所以不容易抽象出相同的功能的具体实现写在父类中


# 抽象类还是接口类 ： 面向对象的开发规范 所有的接口类和抽象类都不能实例化
# java ：
# java里的所有类的继承都是单继承,所以抽象类完美的解决了单继承需求中的规范问题
# 但对于多继承的需求，由于java本身语法的不支持，所以创建了接口Interface这个概念来解决多继承的规范问题

# python
# python中没有接口类  ：
#  python中自带多继承 所以我们直接用class来实现了接口类
# python中支持抽象类  ： 一般情况下 单继承  不能实例化
#  且可以实现python代码
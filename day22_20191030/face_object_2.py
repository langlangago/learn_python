#! encoding:utf8
# class lei:
#     shuxing = 'a'
#
# print(lei.shuxing)

class Person():
    country = 'China'           # 类属性，静态属性
    def __init__(self, *args):
        # print(self.__dict__)  # self 是一个空字典，赋值方法有所不同,最后会返回
        self.name = args[0]
        self.blood = args[1]
        self.aggr = args[2]
        self.sex = args[3]
        # print(self.__dict__)
        # print(id(self))

    def walk(self, n):
        print('%s gogogo %s steps.' % (self.name, n))


alex = Person('alex', 100, 10, 'male') # alex = 返回的self ，一模一样，内存地址都一样
#print(id(alex))
#print(alex.__dict__)
#print(alex.name)
# 对象 = 类名(参数)
# 类名首先会创建一个对象，创建了一个self变量
# 然后调用init方法，类名括号里的参数会被self接收，传参
# 执行 init方法，赋值
# 返回 self

# print(Person.__dict__)
# Person.walk(alex) # 类名.方法名(对象) 方法调用
alex.walk(5) # 上面调用方法的简写

print(Person.country)
print(Person.__dict__['country'])
print(alex.__dict__['name'])
print(alex.name)

alex.name = 'haha'
# Person.country ='India'  # 静态属性，可以这样修改
Person.__dict__['country'] = 'India'  # 不可这样修改
print(Person.country)
print(Person.__dict__['country'])
print(alex.name)

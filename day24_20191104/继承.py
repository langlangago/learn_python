#! encoding:utf-8
#人狗大战

#继承，派生, 派生属性，派生方法
class Animal:
    def __init__(self, name, blood, aggr):
        self.name = name
        self.blood = blood
        self.aggr = aggr

    def eat(self):
        print('吃药回血')
        self.blood += 100

class Person(Animal):
    def __init__(self, name, blood, aggr, sex):
        #Animal.__init__(self, name, blood, aggr)
        super().__init__(name, blood, aggr) #super()使用，替代类名和self
        self.sex = sex  #派生属性

    def attack(self, dog):  #派生方法
        dog.blood -= self.aggr
        print('%s被攻击了,剩余血量%s' %(dog.name, dog.blood))

class Dog(Animal):
    def __init__(self, name, blood, aggr, kind, teeth):
        #Animal.__init__(self, name, blood, aggr)
        super().__init__(name, blood, aggr)
        self.kind = kind
        self.teeth = teeth

    def bite(self, person):
        person.blood -= self.aggr
        print('%s被咬了,剩余血量%s' %(person.name, person.blood))

    def eat(self): # 派生方法，既有自己的方法，也想使用父类的方法。
        Animal.eat(self)
        self.teeth += 2

alex = Person('alex', 100, 20, 'male')
wangcai = Dog('wangcai', 200, 10, 'taddy', 10)
alex.attack(wangcai)
wangcai.bite(alex)
alex.eat()
wangcai.eat()
print(alex.blood)
print(wangcai.blood)
print(wangcai.teeth)

# super使用方法2,直接使用父类的方法
# super(Dog, wangcai).eat
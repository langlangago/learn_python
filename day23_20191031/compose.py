#! encoding:utf8

# 人狗大战，人装备武器
class Person:
    def __init__(self, name, blood, aggr, sex):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.sex = sex

    def attack(self, dog):
        dog.blood -= self.aggr
        print('%s被攻击了，剩余血量%s' % (dog.name, dog.blood))

    def get_weapon(self, weapon):
        self.weapon = weapon
        self.aggr += weapon.aggr

class Dog:
    def __init__(self, name, blood , aggr, kind):
        self.name = name
        self.blood = blood
        self.aggr = aggr
        self.kind = kind

    def bite(self, person):
        person.blood -= dog.aggr
        print('%s被咬了，剩余血量%s' %(person.name, person.blood))

class Weapon:
    def __init__(self, name, aggr):
        self.name = name
        self.aggr = aggr

    def hand18(self, person):
        person.blood -= self.aggr *2


alex = Person('Alex', 100, 2, 'male')
wangcai = Dog('Wangcai', 200, 5, 'taddy')
dagoubang = Weapon('Dagoubang', 10)
alex.get_weapon(dagoubang)
alex.attack(wangcai)
alex.weapon.hand18(wangcai)
print(wangcai.blood)

# 组合，一个对象的属性值是另一个类的对象
# alex.weapon 是 Weapon的对象


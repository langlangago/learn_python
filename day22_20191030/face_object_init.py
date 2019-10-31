# 人狗大战的游戏
# 有一大堆人和一大堆狗，所以要定义模板

def Person(name, blood, aggr, sex):
    person = {
        'name': name,
        'blood': blood,
        'aggr': aggr,
        'sex': sex
    }
    def attack(dog):
        dog['blood'] -= person['aggr']
        print('%s被攻击了，掉了%s血' % (dog['name'], person['aggr']))
    person['attack'] = attack
    return person
# 闭包，内层函数调用外层的变量

def Dog(name, blood, aggr, kind):
    dog = {
        'name': name,
        'blood': blood,
        'aggr': aggr,
        'kind': kind
    }
    def bite(person):
        person['blood'] -= dog['aggr']
        print('%s被咬了，掉了%s血' % (person['name'], dog['aggr']))
    dog['bite'] = bite
    return  dog

alex = Person('alex', 100, 10, 'male')
lilei = Person('lilei',100, 15, 'male')
wangcai = Dog('wangcai', 200, 20, 'taddy')

# attack(alex, wangcai)
# bite(wangcai, lilei)
# bite(lilei, wangcai)

alex['attack'](wangcai)
wangcai['bite'](lilei)
wangcai['bite'](alex)

# 类，抽象的，比如一类人
# 对象，类的具体化，实例化。比如张三李四
# 面向对象编程，就是抽象后实例化成对象，然后操作对象。
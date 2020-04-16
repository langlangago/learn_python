#! encoding:utf-8


class Foo():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def wang(self):
        print('旺旺~')
        # 返回self对象，就可以继续调用其他方法了
        return self

    def run(self):
        print('哒哒~哒哒~')

f = Foo('Wangcai', 500)
# 链式操作
f.wang().run()

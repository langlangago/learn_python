import os
from multiprocessing import Process

# 多进程第二种启动方式:1、自定义类，必须继承Process
# 2、在自定义类中实现run函数，写子进程要实现的功能代码
# 3、要传参需自己实现__init__方法，并继承父类的__init__方法
class MyProcess(Process):
    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(self.pid)
        print(os.getpid())
        print(self.arg1)
        print(self.arg2)

if __name__ == '__main__':
    p = MyProcess('1111', '22222')
    p.start()
    p = MyProcess('1111', '22222')
    p.start()
    print('父进程：', os.getpid())
#! encoding:utf-8

import os
from multiprocessing import Process

# 主进程和子进程之间数据隔离，n值互不影响
def func():
    global n
    n = 0
    print('子进程pid:%s' % os.getpid(), n)


if __name__ == '__main__':
    n = 100
    p = Process(target=func)
    p.start()
    p.join()
    print('主进程pid:%s' % os.getpid(), n)

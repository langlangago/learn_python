#! encoding:utf-8

# 协程更适用于网络操作

# gvent用来产生协程并调度
# 通过greenlet来实现
# 进程和线程的切换由操作系统完成，时间片到了就切换
# 协程的切换由程序代码完成，遇见能识别的IO才切换，实现并发效果
# 如果没有遇到能识别的IO操作，则同步执行（time.sleep）

# 打补丁，补充gevent认识的IO操作，比如time.sleep
# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
# import threading
#
# def eat():
#     print('Start eat.')
#     print(threading.current_thread().getName())
#     time.sleep(1)       # 配合monkey使用，才有效。
#     # gevent.sleep(1)   # 产生IO现象 1s
#     print('End eat.')
#
# def play():
#     print('Start play.')
#     print(threading.current_thread().getName())
#     time.sleep(1)
#     # gevent.sleep(1)
#     print('End play.')
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# g1.join()
# g2.join()

# example: 同步和异步
from gevent import monkey;monkey.patch_all()
import gevent
import time

def func1():
    time.sleep(1)
    print(123)

def sync():
    for i in range(10):
        func1()

def async1():
    g_list = []
    for i in range(10):
        g = gevent.spawn(func1)
        g_list.append(g)
    # for g in g_list:g.join()
    gevent.joinall(g_list)

sync()
async1()


















import time
from threading import Thread
import os

# 多线程并发
# def func(n):
#     time.sleep(1)
#     print(n)
#
# for i in range(10):
#     t = Thread(target=func, args=(i, ))
#     t.start()


# 线程拿到的PID只主进程（主线程）的
# 线程间共享数据，用global
def func(a, b):
    global g
    g = 0
    time.sleep(1)
    print(os.getpid(), a+b, g)

g = 100
print('主进程:', os.getpid())
t_list = []
for i in range(10):
    t = Thread(target=func, args=(i, 5))
    t.start()
    t_list.append(t)
for t in t_list: t.join()
print(g)



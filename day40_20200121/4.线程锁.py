#! encoding:utf-8

# GIL是锁线程的，保证同一时间只能有一个线程访问CPU，从而解决资源征用的问题
# 但是，即使有GIL，也不能完全保证数据的安全，因为CPU时间片的切换，会强制线程释放锁。
# 别的被CPU调度到的线程，会拿到锁继续修改数据。一旦，CPU时间片又回到原来的线程，因为
# 它已经拿过一次数据，已经有记录，不会在重新拿第二次，只会重新获取GIL锁。
# 实际上原始数据可能已经被别的线程修改了，但原来的线程不知道，所以产生了数据不一致。
# 所以即使有GIL锁，线程也要再次加锁。

# Lock 是互斥锁， RLock 递归锁
# from threading import Thread, Lock
# import time
#
# def func1(lock):
#     global n
#     lock.acquire()
#     temp = n - 1
#     time.sleep(0.2)     # 为了迫使CPU时间片切换的操作，从而造成资源不安全
#     lock.release()
#     n = temp
#
#
# n = 10
# t_list = []
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         t = Thread(target=func1, args=(lock,))
#         t.start()
#         t_list.append(t)
#     for t in t_list: t.join()
#     print(n)

# 科学家吃面问题，模拟死锁
# 同时拿到叉子和面条才能吃面
# 两个人，一个拿到叉子，一个拿到面条，就无法再进行下去
# 都在等对方释放另外一把锁。
# from threading import Thread, Lock
# import time
#
# noodle_lock = Lock()
# fork_lock = Lock()
#
# def func1(name):
#     noodle_lock.acquire()
#     print(name, '拿到面条了')
#     fork_lock.acquire()
#     print(name, '拿到叉子了')
#     print(name, '开始吃面')
#     fork_lock.release()
#     noodle_lock.release()
#
# def func2(name):
#     fork_lock.acquire()
#     print(name, '拿到叉子了')
#     time.sleep(2)       # 确保死锁百分之百发生
#     noodle_lock.acquire()
#     print(name, '拿到面条了')
#     print(name, '开始吃面')
#     noodle_lock.release()
#    fork_lock.release()

# if __name__ == '__main__':
#     Thread(target=func1, args=('Alex', )).start()
#     Thread(target=func2, args=('Lilei', )).start()
#     Thread(target=func1, args=('Tom', )).start()
#     Thread(target=func2, args=('Hanmeimei', )).start()

# RLock递归锁，只能有一个人拿到递归锁。
# 顾名思义，多层锁，一直深入进去accquire
# 再一层层释放realease
# from threading import RLock
# rlock = RLock()
# rlock.acquire()
# rlock.acquire()
# rlock.acquire()
# print(123)
# rlock.release()
# rlock.release()
# rlock.release()
#
# # Lock 互斥锁，就必须等待别人释放这把锁，才能进行下去
# from threading import Lock
# lock = Lock()
# lock.acquire()
# lock.acquire()
# print(456)

# 如果把科学家吃面问题，互斥锁改为递归锁，那么面条和叉子都是递归锁的一层锁，子锁
# 就解决了死锁的问题，必须且只能有一个人拿到递归锁（子锁是两个，但也是独占）。
# （互斥锁是两把不一样的锁，会有资源等待）
from threading import Thread, RLock
import time

noodle_lock = fork_lock = RLock()

def func1(name):
    noodle_lock.acquire()
    print(name, '拿到面条了')
    fork_lock.acquire()
    print(name, '拿到叉子了')
    print(name, '开始吃面')
    fork_lock.release()
    noodle_lock.release()

def func2(name):
    fork_lock.acquire()
    print(name, '拿到叉子了')
    time.sleep(2)       # 确保死锁百分之百发生
    noodle_lock.acquire()
    print(name, '拿到面条了')
    print(name, '开始吃面')
    noodle_lock.release()
    fork_lock.release()

if __name__ == '__main__':
    Thread(target=func1, args=('Alex', )).start()
    Thread(target=func2, args=('Lilei', )).start()
    Thread(target=func1, args=('Tom', )).start()
    Thread(target=func2, args=('Hanmeimei', )).start()


















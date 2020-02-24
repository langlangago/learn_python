#! encoding:utf-8

# 信号量，控制同时有几个线程执行锁之间的代码
# 控制锁的并发个数
from threading import Semaphore, Thread
import time

def func1(sem,a):
    sem.acquire()
    print(a*2)
    time.sleep(2)
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(10):
        t = Thread(target=func1, args=(sem, i))
        t.start()

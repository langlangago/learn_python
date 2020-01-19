#! encoding:utf-8

from multiprocessing import Process, Semaphore
import random
import time

# 信号量说明
# sem = Semaphore(3)
# sem.acquire()
# print('1拿钥匙进去了')
# sem.acquire()
# print('2拿钥匙进去了')
# sem.acquire()
# print('3拿钥匙进去了')
# sem.acquire()
# print('4拿钥匙进去了')

# 信号量 类似于1个Lock有多把钥匙，可以多个人进入房间。
# 一旦钥匙没有了，其他人必须等有人退出才能进入房间。
def func(i, sem):
    sem.acquire()
    print('%i走进KTV' % i)
    time.sleep(random.randint(10, 30))
    print('%i走出KTV' % i)
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(4)
    for i in range(10):
        p = Process(target=func, args=(i, sem))
        p.start()
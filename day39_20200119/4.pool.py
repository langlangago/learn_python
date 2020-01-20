#! encoding:utf-8

from multiprocessing import Pool, Process
import time

def func(n):
    for i in range(10):
        print(n+1)

if __name__ == '__main__':
    start = time.time()
    p = Pool(5)             # 5个进程
    p.map(func, range(100)) # 100个任务
    t1 = time.time() - start

    start = time.time()
    p_list = []
    for i in range(100):
        p = Process(target=func, args=(i, ))
        p.start()
        p_list.append(p)
    for p in p_list:
            p.join()
    t2 = time.time() - start
    print(t1, t2)

# 从结果可以看出，使用进程池的执行时间要比多进程快5s钟，效率更高。
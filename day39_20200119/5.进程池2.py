#! encoding:utf-8
from multiprocessing import Pool
import time
import os

# apply 同步执行, 先start后end，复用5个进程
# def func(n):
#     print('start func %s' % n, os.getpid())
#     time.sleep(1)
#     print('end func %s' % n, os.getpid())
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     for i in range(10):
#         pool.apply(func, args=(i, ))

# apply_async，真正的异步执行
def func(n):
    print('start func %s' % n, os.getpid())
    time.sleep(1)
    print('end func %s' % n, os.getpid())

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func, args=(i, ))
    pool.close()   # 结束进程池接受任务
    pool.join()    # 等待进程池中任务执行结束

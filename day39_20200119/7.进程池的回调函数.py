#! encoding:utf-8
from multiprocessing import Pool
import os

# 回调函数，第一个子函数的返回值作为回调函数的参数
# 回调函数在主函数中执行
def func1(n):
    print('in func1', os.getpid())
    return n*n

def func2(n):
    print('in func2', os.getpid())
    print(n)

if __name__ == '__main__':
    p = Pool()
    p.apply_async(func1, args=(10, ), callback=func2)
    p.close()
    p.join()
    print('主进程:', os.getpid())
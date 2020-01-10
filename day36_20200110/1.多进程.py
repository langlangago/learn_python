#! encoding:utf-8
from multiprocessing import Process
import os
import time

# 使用Process类创建子进程
def func(args):
    print(123456)
    time.sleep(1)
    print(args)
    print('我是子进程的PID:', os.getpid())
    print('子进程的父进程PID是:', os.getppid())


if __name__ == '__main__':
    p = Process(target=func, args=('参数',))  # 进程注册，并没有启动

    p.start()   # 启动一个子进程
    print('我是主进程')  # 和子进程并行实行，不确定谁快谁慢。
    print('我是主进程的PID：', os.getpid())
    print('主进程的父进程PID是：', os.getppid())

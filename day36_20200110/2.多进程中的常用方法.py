#! encoding:utf-8
import time
from multiprocessing import Process
import os

# join方法，等待子进程结束后才继续执行主进程剩余的代码
# 捕捉子进程的结束
# 类似强行将异步变成同步

# def func(args1, args2):
#     print('*' * args1)
#     time.sleep(5)
#     print('*' * args2)
#
# if __name__ == '__main__':
#     p = Process(target=func, args=(10, 20))
#     p.start()
#     p.join()
#     print('========：结束了')

# 多子进程，混乱异步，
# 主进程的代码会等待最后一个子进程join（执行完毕），然后
# def func(args1, args2):
#     print('*' * args1)
#     time.sleep(5)
#     print('*' * args2)
#
# if __name__ == '__main__':
#     for i in range(1,10):
#         p = Process(target=func, args=(10*i, 20*i))
#         p.start()
#     p.join()
#     print('========：结束了')


# 多子进程， 正常子进程异步结束后，再执行主进程代码
# def func(args1, args2):
#     print('*' * args1)
#     time.sleep(5)
#     print('=' * args2)
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(1,10):
#         p = Process(target=func, args=(10*i, 20*i))
#         p_list.append(p)
#         p.start()
#     [p.join() for p in p_list]
#     print('**********==========：结束了')

# 例子：10个子进程同时写10个文件，待全部写完后，主进程说ByeBye
# 之后用os.walk查看写的文件名字
def func(filename, num):
    with open(filename, 'w') as f:
        f.write(str(num))

if __name__ == '__main__':
    p_list = []
    for i in range(1, 10):
        p = Process(target=func, args=('test'+str(i), i))
        p_list.append(p)
        p.start()
    [p.join() for p in p_list]
    print([files for root, dirs, files in os.walk(r'D:\my_python\learn_python\day36_20200110')])
    print('**********==========：结束了')

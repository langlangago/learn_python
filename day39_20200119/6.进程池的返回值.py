#! encoding:utf-8

# 进程池有三种方法
# 1、map(func, iterable) 默认异步的执行任务，自带join和close方法
# 2、apply 同步调用
# 3、apply_async 异步调用，和主进程完全异步，需要手动join和close
from multiprocessing import Pool
import time

# apply 同步,一个结果一个结果返回
# def func(i):
#     time.sleep(0.5)
#     return i*i
#
# if __name__ =='__main__':
#     p = Pool(5)
#     for i in range(10):
#         res = p.apply(func, args=(i, ))
#         print(res)

# apply_async 完全异步执行
# def func(i):
#     time.sleep(0.5)
#     return i*i
#
# if __name__ =='__main__':
#     p = Pool(5)
#     res_list = []
#     for i in range(10):
#         res = p.apply_async(func, args=(i, ))
#         # get()方法，阻塞在这里，等待子进程的执行后的结果，硬生生变成了同步。
#         # print(res.get())
#         # 将返回值对象放入list,后面循环调用get()获取返回值,这里不调用get不会阻塞，还是异步
#         res_list.append(res)
#     # 循环从进程池返回值的对象中取值，一次取5个
#     for res in res_list:
#         print(res.get())

# map，返回值是包含所有值的一个列表
def func(i):
    time.sleep(0.5)
    return i*i

if __name__ =='__main__':
    p = Pool(5)
    res = p.map(func, range(10))
    print(res)
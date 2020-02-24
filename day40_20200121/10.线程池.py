#! encoding:utf-8
from concurrent.futures import ThreadPoolExecutor
import time

# def func(n):
#     time.sleep(2)
#     print(n)
#     return n*n
# t_list = []
# tpool = ThreadPoolExecutor(max_workers=5)  # 推荐线程池中线程数为CPU*5
# for i in range(20):
#     t = tpool.submit(func, i)       # 异步提交
#     t_list.append(t)
# tpool.shutdown()                # 等待线程池结束，才继续执行主线程的代码，close + join
# for t in t_list:print('****', t.result())   # 等全部线程shutdown后，才能一次性拿到结果。如果注释掉shutdown，既可以分批次拿到结果
# print('主线程结束')
# tpool.map(func, range(20))      # 使用map效果等同于for，但是拿不到返回值

# 回调函数用法
def func(n):
    time.sleep(2)
    print(n)
    return n*n

def call_back(m):
    print('结果是%s' % m.result())
tpool = ThreadPoolExecutor(max_workers=5)  # 推荐线程池中线程数为CPU*5
for i in range(20):
    tpool.submit(func, i).add_done_callback(call_back)












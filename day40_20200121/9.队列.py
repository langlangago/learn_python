#! encoding:utf-8

# queue 队列
# 是线程安全的，内置了锁，可以保证数据安全

# import queue
# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put_nowait(3)         # 如果队列满了，put会阻塞等待，put_nowait就是不等待直接报错
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get_nowait())   # 如果队列空了,get会阻塞等待，get_nowait就是不等待直接报错

# 堆栈，先进后出
# from queue import LifoQueue
# lq = LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# print(lq.get())
# print(lq.get())
# print(lq.get())

# 优先级队列，put的时候传入优先级，get按照优先级取数据
# 数字越小，优先级越高。如果优先级一样，按照ASCII码大小比较
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((10, 'a'))
pq.put((1, 'b'))
pq.put((30, 'c'))
pq.put((1, 'e'))
print(pq.get())
















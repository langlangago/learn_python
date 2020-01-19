#! encoding:utf-8
from multiprocessing import Queue, Process

# 进程间通讯（IPC）通过队列完成
# q = Queue(4)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print(q.full())
# # q.put(5) # 定义队列长度是5，超过队列长度会阻塞
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# # print(q.get()) # 取多了，依然会阻塞
# try:
#     q.get_nowait()  # 取数据的时候不阻塞，如果没数据了会报错queue.Empty
# except:
#     print('没有数据了')

# 简单的生产者消费者模型 进程间通讯例子
def product(q):
    q.put('Hello')

def consumer(q):
    print(q.get())

if __name__ == '__main__':
    q = Queue()
    p = Process(target=product, args=(q, ))
    p.start()
    c = Process(target=consumer, args=(q, ))
    c.start()















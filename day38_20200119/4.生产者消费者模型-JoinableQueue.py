#! encoding:utf-8

# 2个生产者2个消费者
# 要确保：1、生产者先生产完 2、消费者消费完要退出
from multiprocessing import Process, JoinableQueue
import time
import random


def producer(name, food, q):
    for i in range(5):
        time.sleep(random.randint(1, 3))
        f = ('%s生产了%s%s' % (name, food, i))
        print(f)
        q.put(f)
    q.join()    # 阻塞，直到一个队列中的所有数据被取完

def consumer(name, q):
    while True:
        food = q.get()
        print('\033[31m%s消费了%s\033[0m' % (name, food))
        time.sleep(random.randint(1, 3))
        q.task_done()   # count - 1

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer, args=('李磊', '包子', q))
    p2 = Process(target=producer, args=('韩梅梅', '饺子', q))
    c1 = Process(target=consumer, args=('Alex', q))
    c2 = Process(target=consumer, args=('Rose', q))
    p1.start()
    p2.start()
    c1.daemon = True    # 消费者等待主进程代码执行完后，自行结束。不用手动退出while循环了
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()           # p1、p2进程执行完后，主进程代码结束，消费者子进程代码也自行结束

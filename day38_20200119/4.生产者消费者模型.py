#! encoding:utf-8

# 2个生产者2个消费者
# 要确保：1、生产者先生产完 2、消费者消费完要退出
from multiprocessing import Process, Queue
import time
import random


def producer(name, food, q):
    for i in range(5):
        time.sleep(random.randint(1, 3))
        f = ('%s生产了%s%s' % (name, food, i))
        print(f)
        q.put(f)


def consumer(name, q):
    while True:
        food = q.get()
        if food is None:
            print('获取到了一个空')
            break
        print('\033[31m%s消费了%s\033[0m' % (name, food))
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=('李磊', '包子', q))
    p2 = Process(target=producer, args=('韩梅梅', '饺子', q))
    c1 = Process(target=consumer, args=('Alex', q))
    c2 = Process(target=consumer, args=('Rose', q))
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    q.put(None)     # None作为队列的最后一个值，消费者取到就认为没有了，即刻结束
    q.put(None)
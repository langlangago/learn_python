#! encoding:utf-8

# 管道会有资源竞争的缺点，不安全，可以加锁解决
from multiprocessing import Process, Pipe, Lock
import time
import random


def producer(pro, con, name, food):
    con.close()
    for i in range(5):
        time.sleep(random.randint(1, 3))
        f = ('%s生产了%s%s' % (name, food, i))
        print(f)
        pro.send(f)
    pro.close()


def consumer(pro, con, name, lock):
    pro.close()
    while True:
        try:
            #lock.acquire()
            f = con.recv()
            #lock.release()
            print('\033[31m%s消费了%s\033[0m' % (name, f))
            time.sleep(random.randint(1,2))
        except EOFError:
            con.close()
            break

if __name__ == '__main__':
    lock = Lock()
    pro, con = Pipe()
    p = Process(target=producer, args=(pro, con, '李雷', '包子'))
    c1 = Process(target=consumer, args=(pro, con, '韩梅梅', lock))
    c2 = Process(target=consumer, args=(pro, con, '张三', lock))
    c1.start()
    c2.start()
    p.start()
    pro.close()
    con.close()





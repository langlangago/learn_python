#! encoding:utf-8
from multiprocessing import Process, Lock
import json
import time

# 这里使用并发买火车票的事情，来讲解锁
# 查看火车票数量
def show(i):
    with open('ticket.txt') as f:
        dic = json.load(f)
    print('%d看了票，余票：%d' % (i, dic['ticket']))

def buy_ticket(i, lock):
    lock.acquire()
    with open('ticket.txt') as f:
        dic = json.load(f)
    time.sleep(0.1)
    if dic['ticket'] > 0:
        dic['ticket'] -= 1
        print('\033[32m%s买到票了\033[0m' % i)
    else:
        print('\033[31m%s没买到票\033[0m' % i)
    time.sleep(0.1)
    with open('ticket.txt', 'w') as f:
        json.dump(dic, f)
    lock.release()

if __name__ == '__main__':
#    for i in range(10):
#        p = Process(target=show, args=(i,))
#        p.start()
    lock = Lock()
    for i in range(10):
        p = Process(target=buy_ticket, args=(i, lock))
        p.start()

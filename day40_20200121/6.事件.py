#! encoding:utf-8

# Event事件，默认带一个状态False
# 状态False，wait()会阻塞；状态True,wait()就放通
# wait(1)，设置超时时间为1s，1s后结束阻塞状态，放行。
# set，设置事件状态为True，clear设置事件状态为False

# 数据库连接的例子，两个线程公用一个事件
# 线程1：检测网络是否畅通，通的话，通知时间2 可以连接数据库（设置事件状态为True）。
# 线程2：连接数据库的操作，根据线程1的通知，决定连接成功还是失败。
# 2个线程共享一个事件的状态。

from threading import Thread, Event
import time
import random

def check_network(e):
    time.sleep(random.randint(0, 3))
    e.set()

def connect_db(e):
    count = 0
    e.wait(1)
    while count < 3:
        if e.is_set():
            print('连接上数据库了.....')
            break
        else:
            count += 1
            print('连接失败，第%s次' % count)
    else:
        raise TimeoutError('连接超时')

e = Event()
t1 = Thread(target=check_network, args=(e, ))
t2 = Thread(target=connect_db, args=(e, ))
t1.start()
t2.start()















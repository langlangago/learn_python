#! encoding:utf-8
from multiprocessing import Process, Manager, Lock

# Manager 使用字典来完成进程间数据共享
# 使用字典完成进程间数据共享有数据抢占风险，不安全，要使用锁

def func(dic, lock):
    lock.acquire()
    dic['count'] -= 1
    lock.release()

if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'count': 100})
    lock = Lock()
    p_list = []
    for i in range(50):
        p = Process(target=func, args=(dic, lock))
        p.start()
        p_list.append(p)
    for i in p_list: i.join()
    print('主进程：%s' % dic)
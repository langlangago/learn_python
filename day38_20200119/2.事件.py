#! encoding：utf-8
from multiprocessing import Event, Process
import time,random

# 事件Event，通过一个信号控制事件进入阻塞或者放行状态
# 一个事件被撞见后，默认是阻塞状态

# e = Event()
# print(e.is_set())   # 查看事件状态
# # e.wait()            # 根据事件状态，决定是否执行阻塞操作
# e.set()             # 设置事件状态为非阻塞，True
# print(e.is_set())
# e.wait()
# print('123456')
# e.clear()           # 清除事件的状态，还原为默认的False
# print(e.is_set())
# e.wait()
# print('*******')


# 红绿灯事件
# 车和红绿灯共享主进程的事件状态，通过主进程的事件状态来决定
# 红绿灯是否通行，比如:True 绿灯 通行；False 红灯 等待
# 等待即是阻塞状态;
# 事件的状态是全局共享的，全局一样的
def cars(e, i):
    if not e.is_set():
        print('\033[31m%i在等待\033[0m' % i)
        e.wait()
    print('\033[32m%i通过了\033[0m' % i)

def light(e):
    while True:
        if e.is_set():
            e.clear()
            print('\033[31m红灯亮了\033[0m')
        else:
            e.set()
            print('\033[32m绿灯亮了\033[0m')
        time.sleep(2)

if __name__ == '__main__':
    e = Event()
    traffic = Process(target=light, args=(e, ))
    traffic.start()
    time.sleep(1)
    for i in range(10):
        car = Process(target=cars, args=(e, i))
        car.start()
        time.sleep(random.random())

# 所有子进程都是并行的，红绿灯子进程在2S后会改变状态。
# car子进程，0点几秒启动一个，结果是通过或者等待。
# 2s之内，事件的状态是不变的，如果是True，车辆通过，子进程完结。
# 如果是False，car子进程会wait阻塞在那里等待，直到2s后状态变化，继续执行通过的代码。




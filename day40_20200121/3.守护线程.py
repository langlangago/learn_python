#! encoding:utf-8
from threading import Thread
import time

# 默认情况下，主线程会等待子线程代码执行结束，才结束
# 如果设置了子线程为守护线程Deamon=True, 主线程就不会再等待守护子线程的代码执行完毕，
# 会在其他非守护线程执行完毕后，结束掉自己。
def func1():
    # print('6666666\n')
    # time.sleep(5)
    # print('Code after sleep.')
    while True:
        print('*' * 5)
        time.sleep(1)

def func2():
    time.sleep(5)
    print('In func2\n')

if __name__ == '__main__':
    t1 = Thread(target=func1, )
    t1.daemon = True  # 设置子线程为守护线程，主线程就不会再管他的死活。
    t1.start()
    t2 = Thread(target=func2, )     # 主线程会等待非守护线程执行完毕，主线程才会结束。
    t2.start()
    t2.join()       # 等在这里，捕捉t2线程的结束
    print('主线程代码结束')

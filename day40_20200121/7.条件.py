#! encoding:utf-8

# 线程的条件，类似于锁
# acquire，release, wait, notify
# 1、acquire和release 类似锁的用法，拿钥匙还钥匙，同时给wait和notify做保镖。
# 2、wait，条件默认自带状态为False，会阻塞等待，直到notify的通知它可以放行了。
# 3、notify(int n)，通知n个wait可以通行了
# 4、wait和notify成对组合使用，wait阻塞，等待notify通知可以放行了，wait就会解除阻塞。

from threading import Thread, Condition

# 制造10个线程，10个线程默认都在阻塞等待，根据notify决定是否继续执行
def func1(conn, i):
    print('制造第%s个线程' % i)
    conn.acquire()
    conn.wait()
    print('执行第%s个线程' % i)
    conn.release()

conn = Condition()
for i in range(10):
    Thread(target=func1, args=(conn, i)).start()

# 输入数字，决定一次放行几个线程
while True:
    num = int(input('>>>'))
    conn.acquire()
    conn.notify(num)
    conn.release()





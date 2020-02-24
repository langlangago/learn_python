#! encoding:utf-8

# 协程，存在于线程之中，本质上是一个线程
# 协程在不同任务间进行切换，在发生IO操作、等待IO操作的时候后进行切换，
# 切换后执行其他任务的非IO操作，从而节省等待IO的时间，整体上节省更多的时间。
# 协程间任务切换也需要消耗时间，但是开销要远小于进程线程之间的切换开销。

from greenlet import greenlet

# 一边吃一边玩的例子，在吃和玩两个任务间切换
def eat():
    print('开始吃啦')
    g2.switch()
    print('吃完了')
    g2.switch()

def play():
    print('开始玩啦')
    g1.switch()
    print('玩完了')

g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
#! encoding:utf-8

# 定时器，Timer
# 就是定时开启一个线程，类似于crontab

from threading import Timer
import time

def func():
    print('开始时间同步')

while True:
    Timer(3, func).start()  # 创建一个线程3s后再执行，异步的
    time.sleep(3)           # 延时3s再启动下一个线程
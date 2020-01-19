#! encoding:utf-8

from multiprocessing import Pipe, Process
# conn1, conn2 = Pipe()
# conn1.send('123456')
# print(conn2.recv())


# 管道，在两个进程之间传递消息
# 管道读到最后，有一个EOFError
def func(conn1, conn2):
    conn2.close()
    while True:
        try:
            msg = conn1.recv()
            print(msg)
        except EOFError:
            conn1.close()
            break


if __name__ == '__main__':
    conn1, conn2 = Pipe()
    Process(target=func, args=(conn1, conn2)).start()
    conn1.close()
    for i in range(10):
        conn2.send('吃了吗')
    conn2.close()
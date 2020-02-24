#! encoding:utf-8

# 协程在名义上实现了线程里的并发操作
# 协程只用在有IO操作产生的地方，比如sleep，socket，爬虫

# 爬虫的使用协程的例子

# from gevent import monkey;monkey.patch_all()
# import gevent
# from urllib.request import  urlopen
# import time
#
# # 两种访问url的方式
# # urllib.request 的urlopen()， 然后read()
# # requests.get() 然后content()
# def get_content(url):
#     res = urlopen(url)
#     content = res.read().decode('utf-8')
#     return len(content)
#
# time_start = time.time()
# g1 = gevent.spawn(get_content, 'http://www.baidu.com')
# g2 = gevent.spawn(get_content, 'http://www.sohu.com')
# g3 = gevent.spawn(get_content, 'http://www.taobao.com')
# g4 = gevent.spawn(get_content, 'http://www.sina.com')
# g5 = gevent.spawn(get_content, 'http://www.cnblogs.com')
# gevent.joinall([g1, g2, g3, g4, g5])
# print(g1.value)
# print(g2.value)
# print(g3.value)
# print(g4.value)
# print(g5.value)
# time_end = time.time()
# print(time_end - time_start)

# 对比，同步读取，时间1.2s
# 上面用协程的异步读取，时间0.6s，节省了一般时间
from urllib.request import urlopen
import time
def get_content(url):
    res = urlopen(url)
    content = res.read().decode('utf-8')
    return len(content)
time_start = time.time()
url_list = ['http://www.baidu.com',
            'http://www.sohu.com',
            'http://www.taobao.com',
            'http://www.sina.com',
            'http://www.cnblogs.com']

for url in url_list:
    print(get_content(url))
time_end = time.time()
print(time_end - time_start)

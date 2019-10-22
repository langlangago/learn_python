#collections 模块，是python的扩展模块

#命名元组
# from collections import namedtuple
# Point = namedtuple('point',['x', 'y'])
# p = Point(0,2)
# print(p.x)
# print(p.y)
# print(p)

#花色和数字，描述一张扑克牌
# Card = namedtuple('card', ['suits', 'number'])
# c0 = Card('red', 3)
# print(c0)
# print(c0.suits)
# print(c0.number)

# queue, FIFO
# import queue
# q = queue.Queue()
# q.put(0)
# q.put(1)
# q.put(9)
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.qsize())

#双端队列deque
# from collections import deque
# dq = deque([1,2])
# dq.append('a')
# dq.appendleft('b') # [b,1,2,a]
# dq.insert(1, 'x')
# dq.pop()
# dq.popleft()
# print(dq)

# 有序字典
# from collections import OrderedDict
# od = OrderedDict([('a',1), ('b', 2), ('c', 3)])
# for i in od:
#     print(od[i])
#
# #默认值字典,给字典一个默认的value
# from collections import defaultdict
# dic = defaultdict(lambda : 5)
# rint(dic['k1'])



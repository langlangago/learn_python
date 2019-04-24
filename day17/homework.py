# 3.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=['alex','wupeiqi','yuanhao','nezha']
#
# def func(x):
#     return x + '_sb'
#
# # ret = map(func, name)
# ret = map(lambda x: x+'_sb',name)
# print(list(ret))

# 4.用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num = [1,3,5,6,7,8]
#
# def func(x):
#     return x % 2 == 0
#
# ret = filter(func, num)
# print(list(ret))

# 5.随意写一个20行以上的文件
# 运行程序，先将内容读到内存中，用列表存储。
# 接收用户输入页码，每页5条，仅输出当页的内容

# lines_per_page = 5
#
# with open('file', encoding='utf-8') as f:
#     long_list = f.readlines()
#
# all_lines = len(long_list)
#
# t = divmod(all_lines, lines_per_page)
# if t[1] == 0:
#     pages = t[0]
# else:
#     pages = t[0] + 1
#
# page_num = int(input('请输入页码：').strip())
#
# page_list = long_list[(page_num-1)*5:page_num*5]
#
# for i in page_list:
#     print(i.strip())


# 6.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 6.1.计算购买每支股票的总价

#ret = map(func,portfolio)
ret = map(lambda dic: {dic['name'] : dic['shares'] * dic['price']}, portfolio)
print(list(ret))


# 6.2.用filter过滤出，单价大于100的股票有哪些

ret = filter(lambda dic: True if dic['price'] > 100 else False, portfolio)
print(list(ret))
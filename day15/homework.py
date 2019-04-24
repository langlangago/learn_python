# 3.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕

# def generate(file, word):
#     with open(file, encoding='utf-8') as f:
#         for line in f.readlines():
#             if word in line:
#                 yield line
#
# g = generate('file', 'python')
# for i in g:
#     print(i.strip())





# 4.写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。

# def generate(file):
#     with open(file, encoding='utf-8') as f:
#         for line in f.readlines():
#             yield '***' + line
#
# g = generate('file')
# for i in g:
#     print(i.strip())



# 面试题1
# def demo():
#     for i in range(4):
#         print('I am g')
#         yield i
#
# g=demo()

# 生成器嵌套，都没开始干活，生成器只能取一次
# g1=(i for i in g)
# g2=(i for i in g1)


# print(list(g1))
# print(list(g2))

# 面试题2
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()

for n in [1,10]:
    g=(add(n,i) for i in g)
# # n=1
# g = add(n,i) for i in test
# # n=10
# g = add(n,i) for i in (add(n,i) for i in test)
#
# g = add(10, i) for i in (add(10, i) for i in [0,1,2,3])
#                          [10, 11, 12, 13]
print(list(g))

# def func(f):
#     f = open(f, encoding='utf-8')
#
#     while True:
#         line = f.readline()
#         if line:
#             print(line.strip())
#
# func('file')

def func(f):
    f = open(f, encoding='utf-8')

    while True:
        line = f.readline()
        if line:
            yield line.strip()

g = func('file')
for i in g:
    if 'python' in i:
        print(i)
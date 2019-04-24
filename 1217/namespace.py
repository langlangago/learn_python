# a = 1
#
# def func():
#     # global a
#     a += 1
#     print(a)
#
# func()

a = 1

def func():
    b = 'xxx'
    print(locals())

func()
print(globals())

#namespace: inner namespace, global namespace, zone namespace
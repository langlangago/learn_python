# def my_sum(a, b):
#     res = a +b
#     return res
#
# data = my_sum(3, 5)
# print(data)

# dymatic arguments
# def my_sum(**args):
#     n = 0
#     print(args)
#     for i in args:
#         n += i
#     return  n
#
# # print(my_sum(1, 2))
# # print(my_sum(1, 2, 3))
# # print(my_sum(1, 2, 3, 4))
# print(my_sum([1,2,3]))

#参数
#位置参数    默认参数
#*args      **kwargs
#tuple()    dict{}
#顺序：位置参数，*args，默认参数，**kwargs

# def func(a,*args,defalut=1,**kwargs):
#     print(a,args,defalut,kwargs)
#
# func('a','b','c','d', defalut=3, name='alex', age=16, sex='male')



# def func(*args):
#     print(args)
#
# func(1, 2, 3, 4)
# l = [1, 2, 3, 4]
# func(*l)



def func(**kwargs):
    print(kwargs)

func(a=1, b=2)
dic = {'a':1, 'b':2}
func(**dic)

str.split()












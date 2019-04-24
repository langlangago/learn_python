#python函数默认参数陷阱
#Default values are computed once, then re-used.
#Default parameter values are evaluated when the function definition is executed. This means that the expression is evaluated once, when the function is defined, and that the same “pre-computed” value is used for each call.
#Python中一切皆对象，调用传的是地址，而不是数值。对于可变类型，List 和Dict ，在函数定义初始化的时候，参数list地址已经确定，如果不改变默认参数，
#那么，函数体中对于默认参数的修改，都在同一内存地址中修改。而对于不可变类型来说，传地址相当于多了一个指针，不会改变地址中的值的。

# def fun(l=[]):
#     l.append(1)
#     print(l)
#
# fun()
# fun([2])
# fun()

def func(a, d = {}):
    d[a] = 'v'
    print(d)

func(1)
func(2)
func(3)

# 如果默认参数的值是一个可变数据类型，
# 那么每一次调用函数的时候，
# 如果不传值就公用这个数据类型的资源

#三元运算
a = 2
b = 3
c = a if a > b else b
print(c)
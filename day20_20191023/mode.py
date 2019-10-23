import demo

# demo.read()

# import sys
# print(sys.modules.keys())
# print(sys.path)
# 导入模块的原理：
# 先从sys.modules里寻找模块是否已经被导入，找到就结束
# 否则，继续从sys.path中寻找要导入的模块，找不到就报错
# 找到了，就导入
# 创建这个模块独立的命名空间
# 执行文件，把文件中的字都放入命名空间（读入内存）。

# as 别名，方便通用性操作
# import time as t

# import规则
# 先import内置的，再import 第三方的，再import自己定义的模块。

# 包，一大推模块的集合

# 在模块中有一个特殊变量__name__,如果单独执行这个模块，他的值就是__main__,
# 如果被调用import后，他的值就是模块名
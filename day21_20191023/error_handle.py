# 异常处理，处理程序运行中产生的逻辑错误

try:
    ret = int(input('Number:'))
    print(ret*'*')
except ValueError:
    print('请输入一个数字')
except Exception as error:
    print('老铁，你错了.',error)
else:
    print('没有报错的时候执行else中的代码')
finally:
    print('==========')
# 先写特定异常ValueError、IndexError，最后写万能异常Exception
# try中如果有异常，就执行except，没有异常就执行else,可以做一些通知工作
# finally不管有咩有异常，都会执行; finally和return相遇的时候，依然会执行。
# finally 一般在函数里做异常处理用,不管持否异常去做一些收尾工作，比如关闭文件，关闭数据库连接。
# 一般在小段代码加异常处理


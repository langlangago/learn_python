# homework1, 计算时间差
# 计算今天上班了几天几小时几分钟
import time

t1 = '2019-10-23 9:00:00'
t2 = time.time()

t1 = time.mktime(time.strptime(t1, '%Y-%m-%d %H:%M:%S'))
has_gone = time.gmtime(t2 - t1)
print('已经上班了%d小时，%d分钟，%d秒' % (has_gone.tm_hour, has_gone.tm_min, has_gone.tm_sec))

# homework2, 验证码
# 65-90大写字母，97-122,小写字母，chr()转化
import random

d_list = []
for i in range(0, 10):
    d_list.append(i)
for i in range(65, 91):
    d_list.append(i)
for i in range(97, 123):
    d_list.append(i)

captcha = ''
for i in range(1, 5):
    num = random.choice(d_list)
    if num >=0 and num < 10:
        captcha += str(num)
    else:
        captcha += chr(num)

print('验证码为：',captcha)

# homework3  利用sys.argv验证用户名和密码
import sys
username = 'langxiaowei'
passwd = '123123'

if sys.argv[1] == username and sys.argv[2] == passwd:
    print('登录成功')
else :
    print('用户名密码错误，登录失败。')
    sys.exit(1)
print('你现在可以使用我的计算器了。')

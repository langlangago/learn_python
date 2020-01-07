# import sys
# import time
#
# def processBar(num, total):
#     rate = num / total
#     rate_num = int(rate * 100)
#     if rate_num == 100:
#         r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
#     else:
#         r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
# for i in range(1, 101):
#     processBar(i, 100)
#     time.sleep(0.1)

# md5.hexdigest 是取数据，显示当前md5值
import hashlib

md5 = hashlib.md5()
#md5.update(b'123456')
#print(md5.hexdigest())
md5.update(b'123')
print(md5.hexdigest())
md5.update(b'456')
print(md5.hexdigest())

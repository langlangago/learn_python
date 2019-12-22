#! encoding:utf-8
# logging 模块

# 日志级别5个 : debug--info--warning--error--critical
# 默认打印info以上的三个级别日志
# 日志格式化,logging.basicConfig 或者 log对象
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H %M %S',
#                     filename='test.log',
#                     filemode='w')
# logging.debug('Debug message.')
# logging.info('Info message.')
# logging.warning('Warning message.')
# logging.error('Error message.')
# logging.critical('Critical message.')
#
# try:
#     int(input('请输入一个数字:'))
# except ValueError:
#     logging.error('输入的不是数字.')
#
# basicConfig的两个缺点：
# 1.日志中文乱码的问题 2.日志不能同时输出在屏幕和文件中。

# log对象
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(filename)s-%(levelname)s-%(message)s')

fh = logging.FileHandler('log.log', encoding='utf-8')
sh = logging.StreamHandler()

fh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

logging.debug('Debug message.')
logging.info('Info message.')
logging.warning('Warning message.')
logging.error('错误信息.')
logging.critical('Critical message.')

# log对象优点：高度解耦，可定制化高
# coding=utf-8

# hmac类似hashlib的rsa加密操作
import hmac

h = hmac.new(b'1', b'2')
print(h.digest())
# 比较两个加密后的bytes类型数据
# hmac.compare_digest()
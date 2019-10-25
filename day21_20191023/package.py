# 把解决一类问题的模块放在同一个文件夹里--包
import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py', 'w'))
# l.append(open('glance/api/__init__.py', 'w'))
# l.append(open('glance/api/policy.py', 'w'))
# l.append(open('glance/api/versions.py', 'w'))
# l.append(open('glance/cmd/__init__.py', 'w'))
# l.append(open('glance/cmd/manage.py', 'w'))
# l.append(open('glance/db/__init__.py', 'w'))
# l.append(open('glance/db/manage.py', 'w'))
# map(lambda f:f.close(), l)

# import
# import glance.api.policy as policy
# policy.get()

# from ... import ...
# from glance.api import policy
# policy.get()
#
# import sys
# print(sys.path)

import glance
#glance.api.policy.get()
glance.cmd.manage.main()
glance.db.models.registter_models('MySQL')
# 引用文件名是直接导入模块，引用文件夹名字是运行包下面的__init__.py文件
# 绝对导入，相对导入(from . import * 对应 __all__方法)
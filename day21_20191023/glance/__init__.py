print('I am __init__.py')
import sys
print(sys.path)
from glance import api
from glance import cmd
from glance import db

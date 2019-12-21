import os, sys
dirname = os.path.dirname(os.getcwd())
sys.path.insert(0, dirname)

from core import main
if __name__ == '__main__':
    main.main()

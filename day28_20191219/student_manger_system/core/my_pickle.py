import pickle
import os

class MyPickle:
    def __init__(self, filename):
        self.filename = filename

    def dump(self, obj):
        with open(self.filename, 'ab') as f:
            pickle.dump(obj, f)

    def loaditer(self):
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield  obj
                except EOFError:
                    break

    def edit(self, obj):
        new_file = MyPickle(self.filename + '.bak')
        for item in self.loaditer():
            if item.name == obj.name:
                new_file.dump(obj)
            else:
                new_file.dump(item)

        os.remove(self.filename)
        os.rename(self.filename+'.bak', self.filename)

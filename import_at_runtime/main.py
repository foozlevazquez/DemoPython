

import sys

import importlib

def import_class(cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = importlib.__import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)

class Foo:
    pass

if __name__ == '__main__':
    print(import_class(sys.argv[1]))

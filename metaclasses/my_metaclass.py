"""Classes that use this metaclass will have an additional class attribute added called specvar.
"""
from pprint import pprint as pp

class MyMetaClass(type):
    ## __new__ is run BEFORE the class actually exists, that is, it is what is
    ## called to CREATE the class itself.
    def __new__(cls, clsname, bases, dct):
        dct['specvar'] = cls
        pp( dct )
        # WTF super?
        return super(MyMetaClass, cls).__new__(cls, clsname, bases, dct)

    ## __init__ is called AFTER the class has been instantiated (the ``self''
    ## that is passed to __init__ is the already instantiated class).
    #def __init__(self, name, bases, dct):
        #super().__init__(self, name, bases, dct)
        #print(self.__dict__ == dct)



class MyClass(metaclass=MyMetaClass):
    class_var = 100

    def __init__(self):
        self.var = 99

    @classmethod
    def print_it(cls):
        print(cls.specvar)


MyClass.print_it()

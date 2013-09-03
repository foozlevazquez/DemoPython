from abc import ABCMeta, abstractmethod

class MyClass(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def will_do_something(x):
        raise NotImplementedError

    def does_something(x):
        return (x+1)



class MyBrokenSubClass(MyClass):
    # nothing!
    pass

class MyWorkingSubClass(MyClass):
    def will_do_something(x):
        return (x+100)

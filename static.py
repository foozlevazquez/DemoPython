
class MyClass():
    x_factor = 8

    @staticmethod
    def do_thing(x):
        return x+1


    @staticmethod
    def do_other_thing(y):
        return MyClass.do_thing(y + 1)

    @classmethod
    def ya_thing(cls, x):
        return x + 10 + cls.x_factor



class SubClass(MyClass):
    x_factor = 1000

    @classmethod
    def ya_thing(cls, x):
        ox = super().ya_thing(x)
        return ox + 100 + cls.x_factor

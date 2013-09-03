
class MyClass():
    @staticmethod
    def do_thing(x):
        return x+1


    @staticmethod
    def do_other_thing(y):
        return MyClass.do_thing(y + 1)

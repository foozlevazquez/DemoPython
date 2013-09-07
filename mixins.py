

class MyClass():
    the_x = None
    x_factor = ' MyClass.x_factor'

    @classmethod
    def init(cls, x):
        cls.the_x = ' MyClass.init({}) '.format(x) + cls.x_factor


class MyMixin():
    x_factor = ' MyMixin.x_factor'

    @classmethod
    def init(cls, x):
        super().init('MyMixin.init({})'.format(x))


class Right(MyMixin, MyClass):
    pass

class Wrong(MyClass, MyMixin):
    pass

Right.init('Right')
Wrong.init('Wrong')

#assert Right.the_x == 1016
#assert Wrong.the_x == 26

print('\n', Right.the_x, '\n', Wrong.the_x)

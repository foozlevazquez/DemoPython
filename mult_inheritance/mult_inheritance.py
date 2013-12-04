
class Foo1:
    def __init__(self):
        print("Foo init")

class Bar1:
    def __init__(self):
        print("Bar init")

class Baz1(Foo, Bar):
    def __init__(self):
        Foo1.__init__(self)
        Bar1.__init__(self)
        print("Baz init")

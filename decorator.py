import functools


class DaClass():

    def __init__(self, got_thing):
        self.got_thing = got_thing

    def has_thing(func):
        def check_for_thing(self, *args, **kw):
            if not self.got_thing:
                raise Exception('Sessionid unset - session not started.')
            return func(self, *args, **kw)
        return functools.update_wrapper(check_for_thing, func)



    @has_thing
    def must_have_thing(self):
        return True

    def dont_care_bout_things(self):
        return True


def wrap_func(func=None, other="yes"):
    if func:
        def wrapper(cls, *args, **kwargs):
            print("cls = {}, func= {}, other={}".format(cls, func, other))
            func(cls, *args, **kwargs)
    else:
        def wrapper(func):
            return wrap_func(func=func, other=other)

    return wrapper


class SubClass(DaClass):
    @classmethod
    @wrap_func()
    def foo(cls):
        print("In foo")

class YaClass():
        @classmethod
        @wrap_func(other="no")
        def bar(cls):
            print("In bar")

if __name__ == '__main__':

    SubClass.foo()
    YaClass.bar()

    yes = DaClass(True)
    no = DaClass(False)

    assert yes.must_have_thing()
    assert yes.dont_care_bout_things()
    assert no.dont_care_bout_things()

    try:
        no.must_have_thing()
    except Exception:
        pass
    print("Success.")

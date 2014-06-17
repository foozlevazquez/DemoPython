def c_inc():
    c=0
    def fn():
        nonlocal c
        c=c+1
        return c
    return fn


def foo():
    fn = c_inc()
    dct = {}
    for i in range(5):
        dct.setdefault('thing', fn())
    print('final fn value = ', fn())

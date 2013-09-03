def takes_kwargs(**kwargs):
    uses_kwargs(**kwargs)

def takes_both(*args, **kwargs):
    uses_both(*args, **kwargs)

def uses_both(*args, foo=None, bar=None):
    print(sum(args) + foo + bar)

def uses_kwargs(foo=None, bar=None):
    print(foo + bar)

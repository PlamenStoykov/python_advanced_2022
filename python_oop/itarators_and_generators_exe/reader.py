def read_next(*args):
    for iterable in args:
        for i in iterable:
            yield i


def even_odd(*args):
    command = args[-1]
    parity = 0 if command == 'even' else  1
    return list(filter(lambda x: x if x % 2 == parity else False, args[:-1]))




def even_odd_filter(**kwargs):
    for i in kwargs:
        parity = 0 if i == 'even' else 1
        value = list(filter(lambda x: x if x % 2 == parity else False, kwargs[i]))
        kwargs[i] = value
    c = sorted(kwargs.items(), key=lambda kvpt: -len(kvpt[1]))
    return dict(c)


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

def concatenate(*args, **kwargs):
    result = ''
    for i in args:
        result += i
    for k in kwargs:
        if k in result:
            result = result.replace(k, kwargs[k])
    return result


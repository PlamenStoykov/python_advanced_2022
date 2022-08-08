def multiply(times):

    def decorator(function):
        def wrapper(num):
            number = function(num)
            return number * times
        return wrapper
    return decorator



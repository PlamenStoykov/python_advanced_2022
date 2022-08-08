def even_numbers(function):
    def wrapper(numbers):
        result = [i for i in numbers if i % 2 == 0]
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

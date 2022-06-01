
def func_executor(*args):
    result = ''
    for func_ref, func_arg in args:
        result += f"{func_ref.__name__} - {func_ref(*func_arg)}" + '\n'
    return result




def operate(sign, *args):
    return eval(f'{sign}'.join([str(i) for i in args]))



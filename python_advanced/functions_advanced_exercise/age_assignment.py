def age_assignment(*args, **kwargs):
    res = ''
    my_dict = {}
    for i in args:
        my_dict[i] = kwargs[i[0]]
    using = dict(sorted(my_dict.items(), key=lambda x: x[0]))
    for i in using:
        res += f"{i} is {using[i]} years old." + '\n'
    return res




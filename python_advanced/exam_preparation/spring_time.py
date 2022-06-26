def start_spring(**kwargs):
    my_dict = {}

    for k, v in kwargs.items():
        if v not in my_dict:
            my_dict[v] = []
        my_dict[v].append(k)
    length = set([len(my_dict[i]) for i in my_dict])
    if len(length) == len(my_dict):
        sorted_dict = sorted(my_dict.items(), key=lambda kvpt: -len(kvpt[1]))
    else:
        sorted_dict = sorted(my_dict.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ''
    for key, value in sorted_dict:
        sorted_value = sorted(value)
        result += f'{key}:\n'
        for i in sorted_value:
            result += f'-{i}\n'
    return result


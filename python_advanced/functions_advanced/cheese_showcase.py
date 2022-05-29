def sorting_cheeses(**kwargs):
    result = ''
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    for key, value in sorted_cheeses:
        value = sorted(value, reverse=True)
        result += key + '\n' + '\n'.join([str(i) for i in value]) + '\n'

    return result



def naughty_or_nice_list(santa_kids_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    numbers = []
    names = []
    for num, name in santa_kids_list:
        numbers.append(num)
        names.append(name)
    if args:
        for i in args:
            n, behavior = i.split('-')
            n = int(n)
            if numbers.count(n) == 1:
                idx = numbers.index(n)
                if behavior == 'Naughty':
                    naughty_list.append(names[idx])
                    names.pop(idx)
                    numbers.pop(idx)
                else:
                    nice_list.append(names[idx])
                    names.pop(idx)
                    numbers.pop(idx)
    if kwargs:
        for name in kwargs:
            if names.count(name) == 1:
                if kwargs[name] == 'Naughty':
                    naughty_list.append(name)
                    idx = names.index(name)
                    names.remove(name)
                    numbers.pop(idx)

                else:
                    nice_list.append(name)
                    idx = names.index(name)
                    names.remove(name)
                    numbers.pop(idx)
    result = ''
    if nice_list:
        nice = f"Nice: {', '.join(nice_list)}\n"
        result += nice
    if naughty_list:
        naughty = f"Naughty: {', '.join(naughty_list)}\n"
        result += naughty
    if names:
        n = f"Not found: {', '.join(names)}\n"
        result += n

    return result


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

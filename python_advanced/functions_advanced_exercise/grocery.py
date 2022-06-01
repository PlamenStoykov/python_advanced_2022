def grocery_store(**kwargs):
    res = ''
    sorted_receipt = sorted(kwargs.items(), key=lambda kvpt: (-kvpt[1], -len(kvpt[0]), kvpt[0]))
    c = dict(sorted_receipt)
    for i in c:
        res += f"{i}: {c[i]}" + '\n'
    return res

def get_primes(a):
    for i in a:
        is_it = False
        if i == 1 or i == 0:
            continue
        for n in range(2, i):
            if (i % n) == 0:
                is_it = True
                continue
        if not is_it:
            yield i


from itertools import permutations

def possible_permutations(a):
    for i in list(permutations(a)):
        yield list(i)
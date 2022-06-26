def print_space(num, index):
    for space in range(num - index-1):
        print(' ', end='')


def print_star(num, index):
    for star in range(index):
        print('*', end=' ')
    print('*')


n = int(input())
for i in range(n):
    print_space(n, i)
    print_star(n, i)
for j in range(n - 2, -1, -1):
    print_space(n, j)
    print_star(n, j)

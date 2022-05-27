a = [[int(y) for y in i.split()] for i in input().split('|')]
for i in range(len(a) - 1, -1, -1):
    if a[i]:
        print(*a[i], sep=' ', end=' ')

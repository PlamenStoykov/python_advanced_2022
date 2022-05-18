def generator(a):
    one, two = list(map(int, a.split(',')))
    s = set(range(one, two + 1))
    return s


biggest = set()
n = int(input())
for i in range(n):
    expression = input().split('-')
    first = generator(expression[0])
    second = generator(expression[1])
    current = first.intersection(second)
    if len(current) > len(biggest):
        biggest = current
print(f'Longest intersection is [{", ".join([str(i) for i in biggest])}] with length {len(biggest)}')
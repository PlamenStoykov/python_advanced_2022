first = set([int(i) for i in input().split()])
second = set([int(i) for i in input().split()])
n = int(input())
for i in range(n):
    command = input().split()
    direction = command[0]
    position = command[1]
    if position == 'First':
        nums = command[2:]
        nums = set([int(i) for i in nums])
        if direction == 'Add':
            first = first.union(nums)
        else:
            first = first.difference(nums)
    elif position == 'Second':
        nums = command[2:]
        nums = set([int(i) for i in nums])
        if direction == 'Add':
            second = second.union(nums)
        else:
            second = second.difference(nums)
    else:
        print(True if first.issubset(second) or second.issubset(first)else False)
print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')

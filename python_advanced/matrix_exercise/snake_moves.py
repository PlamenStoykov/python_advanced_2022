rows, cols = [int(i) for i in input().split()]
string = input()
index = 0
for i in range(rows):
    current = []
    for j in range(cols):
        current.append(string[index % len(string)])
        index += 1
    if i % 2 == 0:
        print(*current, sep='')
    else:
        print(*reversed(current), sep='')

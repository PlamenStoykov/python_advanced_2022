rows, cols = [int(i) for i in input().split()]
for i in range(rows):
    for j in range(cols):
        print(chr(97 + i), chr(97 + i + j), chr(97 + i), sep='', end=" ")
    print()

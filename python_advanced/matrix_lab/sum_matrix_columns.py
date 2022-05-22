
result = 0
rows, cols = list(map(int, input().split(', ')))
matrix = [[int(j) for j in input().split()]for i in range(rows)]
for i in range(cols):
    current = 0
    for j in range(rows):
        current += matrix[j][i]
    print(current)
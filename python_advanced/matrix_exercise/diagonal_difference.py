rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]
primary = [matrix[o][o] for o in range(rows)]
secondary = [matrix[y][j]for y in range(rows) for j in range(rows) if j + y == rows - 1]
print(abs(sum(primary)-sum(secondary)))

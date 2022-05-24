rows, cols = [int(i) for i in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(rows)]
final = -99999999
position = None
for i in range(rows - 2):
    for j in range(cols - 2):
        res = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j] + matrix[i + 1][j + 1] + \
              matrix[i + 1][j + 2] + matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if res > final:
            final = res
            position = (i, j)
i, j = position
print(f"Sum = {final}")
print(matrix[i][j], matrix[i][j + 1], matrix[i][j + 2])
print(matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2])
print(matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2])

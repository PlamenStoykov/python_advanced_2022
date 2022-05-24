rows, cols = [int(i) for i in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
num = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            num += 1

print(num)
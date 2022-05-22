rows, cols = [int(i)for i in input().split(', ')]
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
res = 0
square = []
position = None
for row in range(rows - 1, 0, -1):
    for col in range(cols - 1, 0, -1):
        if matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1] >= res:
            res = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
            position = (row, col)
row, col = position
print(matrix[row - 1][col - 1], matrix[row - 1][col])
print(matrix[row][col - 1], matrix[row][col])
print(res)
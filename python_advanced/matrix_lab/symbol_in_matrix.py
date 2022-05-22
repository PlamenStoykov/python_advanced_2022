n = int(input())
matrix = [[j for j in list(input())] for _ in range(n)]
searched = input()

position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched and not position:
            position = (row, col)
if position:
    print(position)
else:
    print(f"{searched} does not occur in the matrix")


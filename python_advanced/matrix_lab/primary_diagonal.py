n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]
r = 0
for i in range(n):
    for j in range(n):
        if i == j:
            r += matrix[i][j]
print(r)

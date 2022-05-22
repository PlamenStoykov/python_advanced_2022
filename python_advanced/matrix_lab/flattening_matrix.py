matrix = []
result = 0
n = int(input())
for i in range(n):
    data = list(map(int, input().split(', ')))
    matrix.extend(data)
print(matrix)
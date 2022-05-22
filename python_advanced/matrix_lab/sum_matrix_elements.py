matrix = []
result = 0
rows ,cols = list(map(int, input().split(', ')))
for i in range(rows):
    data = list(map(int, input().split(', ')))
    matrix.append(data)
    result += sum(data)
print(result)
print(matrix)
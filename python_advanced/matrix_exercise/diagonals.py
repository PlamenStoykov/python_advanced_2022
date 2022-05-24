rows = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
primary = [matrix[o][o] for o in range(rows)]
secondary = [matrix[y][j]for y in range(rows) for j in range(rows) if j + y == rows - 1]
print(f"Primary diagonal: {', '.join([str(c)for c in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(c)for c in secondary])}. Sum: {sum(secondary)}")

n = int(input())
matrix = []
for i in range(n):
    data = [int(i) for i in input().split()]
    matrix.append(data)
bomb_input = input().split()
for v in bomb_input:
    row, col = [int(i) for i in v.split(',')]
    bomb_value = matrix[row][col]
    if bomb_value > 0:
        for current_row in range(row - 1, row + 2):
            if 0 <= current_row < n:
                if 0 <= col - 1 < n:
                    if matrix[current_row][col - 1] > 0:
                        matrix[current_row][col - 1] -= bomb_value
                if 0 <= col < n:
                    if matrix[current_row][col] > 0:
                        matrix[current_row][col] -= bomb_value
                if 0 <= col + 1 < n:
                    if matrix[current_row][col + 1] > 0:
                        matrix[current_row][col + 1] -= bomb_value
alive = [f for g in matrix for f in g if f > 0]
print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")
for i in matrix:
    print(*i)

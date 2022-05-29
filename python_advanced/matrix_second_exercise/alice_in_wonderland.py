def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False
    else:
        return True


def pos_left(row, col):
    return row, col - 1


def pos_right(row, col):
    return row, col + 1


def pos_up(row, col):
    return row - 1, col


def pos_down(row, col):
    return row + 1, col


position_functions = {'left': pos_left, 'right': pos_right, 'up': pos_up, 'down': pos_down}
n = int(input())
matrix = []
bags = 0
alice_row = None
alice_col = None

for i in range(n):
    data = [int(g) if g != '.' and g != 'R' and g != 'A' else g for g in input().split()]
    matrix.append(data)
    for f in data:
        if f == 'A':
            alice_col = data.index(f)
            alice_row = i

command = input()
while command:
    matrix[alice_row][alice_col] = '*'

    next_row, next_col = position_functions[command](alice_row, alice_col)
    if is_outside(next_row, next_col, n):
        matrix[alice_row][alice_col] = '*'
        break
    alice_row, alice_col = next_row, next_col
    if matrix[alice_row][alice_col] == 'R':
        matrix[alice_row][alice_col] = '*'
        break
    if matrix[alice_row][alice_col] != '.' and matrix[alice_row][alice_col] != '*':
        bags += matrix[alice_row][alice_col]
    if bags >= 10:
        matrix[alice_row][alice_col] = '*'
        break
    command = input()
if bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
for i in matrix:
    print(*i)

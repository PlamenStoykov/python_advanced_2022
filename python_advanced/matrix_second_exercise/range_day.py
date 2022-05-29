def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def pos_left(row, col, num):
    return row, col - num


def pos_right(row, col, num):
    return row, col + num


def pos_up(row, col, num):
    return row - num, col


def pos_down(row, col, num):
    return row + num, col


position_functions = {'left': pos_left, 'right': pos_right, 'up': pos_up, 'down': pos_down}
starter_row = None
starter_col = None
targets = 0
matrix = []
shot_pos = []
for i in range(5):
    data = input().split()
    matrix.append(data)
    for j in data:
        if j == 'x':
            targets += 1
        elif j == 'A':
            starter_row = i
            starter_col = data.index('A')
matrix[starter_row][starter_col] = '.'
n = int(input())
shot_targets = 0
for i in range(n):
    command = input()
    tokens = command.split()
    if tokens[0] == 'shoot':
        direction = tokens[1]
        next_row, next_col = position_functions[direction](starter_row, starter_col, 1)
        while True:
            if is_outside(next_row, next_col, 5):
                break
            if matrix[next_row][next_col] == 'x':
                shot_targets += 1
                matrix[next_row][next_col] = '.'
                shot_pos.append([next_row, next_col])
                break
            next_row, next_col = position_functions[direction](next_row, next_col, 1)
        if targets == shot_targets:
            break
        continue
    direction = tokens[1]
    steps = int(tokens[2])
    matrix[starter_row][starter_col] = '.'
    next_row, next_col = position_functions[direction](starter_row, starter_col, steps)
    if not is_outside(next_row, next_col, 5):
        if matrix[next_row][next_col] == '.':
            starter_row, starter_col = next_row, next_col
    matrix[starter_row][starter_col] = 'A'
if targets == shot_targets:
    print(f"Training completed! All {targets} targets hit.")
if targets != shot_targets:
    print(f"Training not completed! {targets - shot_targets} targets left.")
for c in shot_pos:
    print(c)

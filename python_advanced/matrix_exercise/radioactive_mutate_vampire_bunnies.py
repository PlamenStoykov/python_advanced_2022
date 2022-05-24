def get_next_pos(row, col, direction):
    if direction == 'U':
        return row - 1, col
    if direction == 'L':
        return row, col - 1
    if direction == 'R':
        return row, col + 1
    if direction == 'D':
        return row + 1, col


def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(i) for i in input().split()]

player_row = None
player_col = None
matrix = []
bunnies = set()
for i in range(rows):
    data = list(input())
    matrix.append(data)
    for j in range(cols):
        if data[j] == 'B':
            bunnies.add(f'{i} {j}')
        elif data[j] == 'P':
            player_row = i
            player_col = j
commands = input()
won = False
lost = False
matrix[player_row][player_col] = '.'
for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        lost = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col
    new_bunnies = set()
    for bunny in bunnies:
        bunny_row, bunny_col = [int(y) for y in bunny.split()]
        if not is_outside(bunny_row + 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row + 1} {bunny_col}')
            matrix[bunny_row + 1][bunny_col] = 'B'
        if not is_outside(bunny_row - 1, bunny_col, rows, cols):
            new_bunnies.add(f'{bunny_row - 1} {bunny_col}')
            matrix[bunny_row - 1][bunny_col] = 'B'
        if not is_outside(bunny_row, bunny_col - 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col - 1}')
            matrix[bunny_row][bunny_col - 1] = 'B'
        if not is_outside(bunny_row, bunny_col + 1, rows, cols):
            new_bunnies.add(f'{bunny_row} {bunny_col + 1}')
            matrix[bunny_row][bunny_col + 1] = 'B'
    bunnies = bunnies.union(new_bunnies)
    if matrix[player_row][player_col] == 'B':
        lost = True
    if lost or won:
        break

for i in matrix:
    print(*i, sep='')
if won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")

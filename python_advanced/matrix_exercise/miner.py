def miner_mover(direction, r, c, mdl, size):
    position = False
    if direction == 'up':
        if 0 <= r - 1 < size:
            position = (r - 1, c)
    elif direction == 'down':
        if 0 <= r + 1 < size:
            position = (r + 1, c)
    elif direction == 'right':
        if 0 <= c + 1 < size:
            position = (r, c + 1)
    else:  # left
        if 0 <= c - 1 < size:
            position = (r, c - 1)
    return position


n = int(input())
all_coal = 0
starting_row = None
starting_col = None
matrix = []
condition = False
commands = input().split()
for i in range(n):
    data = input().split()
    for j in data:
        if j == 'c':
            all_coal += 1
        elif j == 's':
            starting_row = i
            starting_col = data.index('s')
    matrix.append(data)
current_coal = 0
# Finished with entering the matrix
for command in commands:  # if miner steps on e or current_coal == all_coal we should break
    if all_coal == current_coal:
        break
    if miner_mover(command, starting_row, starting_col, matrix, n):
        matrix[starting_row][starting_col] = '*'
        starting_row, starting_col = miner_mover(command, starting_row, starting_col, matrix, n)
        if matrix[starting_row][starting_col] == 'c':
            current_coal += 1
        elif matrix[starting_row][starting_col] == 'e':
            condition = True
            break
        matrix[starting_row][starting_col] = 's'
    else:
        continue
if all_coal == current_coal:
    print(f"You collected all coal! ({starting_row}, {starting_col})")
if condition:
    print(f"Game over! ({starting_row}, {starting_col})")
if not condition and all_coal != current_coal:
    print(f"{all_coal - current_coal} pieces of coal left. ({starting_row}, {starting_col})")

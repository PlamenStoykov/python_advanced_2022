from collections import deque

starting_row = None
starting_col = None
matrix = []
for i in range(6):
    data = input().split()
    matrix.append(data)
    for j in data:
        if j == 'E':
            starting_row = i
            starting_col = data.index('E')
commands = deque(input().split(', '))
found = set()


def move_position(m, r, c, direction, f):
    if direction == 'down':
        if r == 5:
            r = 0
        else:
            r += 1
    elif direction == 'up':
        if r == 0:
            r = 5
        else:
            r -= 1
    elif direction == 'left':
        if c == 0:
            c = 5
        else:
            c -= 1
    elif direction == 'right':
        if c == 5:
            c = 0
        else:
            c += 1
    if m[r][c] != '-':
        f.add(m[r][c])
    return r, c, f


while commands:
    current_command = commands.popleft()
    starting_row, starting_col, found = move_position(matrix, starting_row, starting_col, current_command, found)
    if matrix[starting_row][starting_col] == 'R':
        print(f"Rover got broken at ({starting_row}, {starting_col})")
        break
    elif matrix[starting_row][starting_col] == 'W':
        print(f"Water deposit found at ({starting_row}, {starting_col})")
    elif matrix[starting_row][starting_col] == 'C':
        print(f"Concrete deposit found at ({starting_row}, {starting_col})")
    elif matrix[starting_row][starting_col] == 'M':
        print(f"Metal deposit found at ({starting_row}, {starting_col})")
if 'W' in found and 'M' in found and 'C' in found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
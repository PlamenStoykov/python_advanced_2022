def doer(direction, mdl, row, col, n, ):
    eggs = 0
    positions = []
    moved = False
    if direction == 'right':
        for y in range(col + 1, n):
            if mdl[row][y] == 'X':
                break
            else:
                eggs += mdl[row][y]
                moved = True
                positions.append(f'[{row}, {y}]')
    elif direction == 'left':
        for y in range(col - 1, -1, -1):
            if mdl[row][y] == 'X':
                break
            else:
                moved = True
                eggs += mdl[row][y]
                positions.append(f'[{row}, {y}]')
    elif direction == 'up':
        for y in range(row - 1, -1, -1):
            if mdl[y][col] == 'X':
                break
            else:
                moved = True
                eggs += mdl[y][col]
                positions.append(f'[{y}, {col}]')
    elif direction == 'down':
        for y in range(row + 1, n):
            if mdl[y][col] == 'X':
                break
            else:
                moved = True
                eggs += mdl[y][col]
                positions.append(f'[{y}, {col}]')
    if not moved:
        eggs = -999999999999
    return eggs, positions, direction


biggest_path = None
my_dict = {}
size = int(input())
starter_row = 0
starter_col = 0
matrix = []
for i in range(size):
    data = [int(c) if c != 'B' and c != 'X' else c for c in input().split()]
    matrix.append(data)
    for c in data:
        if 'B' == c:
            starter_row = i
            starter_col = data.index(c)
d = ('right', 'left', 'up', 'down')
biggest = -999999999999
using = []
for position in d:
    eggs, containment, direct = doer(position, matrix, starter_row, starter_col, size)
    if eggs > biggest:
        using = containment
        biggest_path = direct
        biggest = eggs

if biggest_path:
    print(biggest_path)
if using:
    for i in using:
        print(i)
print(biggest)

def next_move(s, r, c, m, direction, size_col, size_row):
    if direction == 'up':
        for row in range(steps+1):

            if r == -1:
                r = size_row - 1
            m[r][c] = 'x'
            r = r - 1
    elif direction == 'down':
        for row in range(steps+1):
            if r == size_row - 1:
                r = 0
            m[r][c] = 'x'
            r = r + 1
    elif direction == 'right':
        for col in range(steps+1):
            if r == size_col - 1:
                c = 0
            m[r][c] = 'x'
            c = c + 1
    elif direction == 'left':
        for col in range(steps+1):

            if r == -1:
                c = size_col - 1
            m[r][c] = 'x'
            c = c - 1
    return r, c, m


unique_items = set()
matrix = []
start_row = None
start_col = None
my_dict = {'D': 'Christmas decorations', 'G': 'Gifts', 'C': 'Cookies'}
collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
rows, cols = list(map(int, input().split(', ')))
for i in range(rows):
    data = input().split()
    matrix.append(data)
    for j in data:
        if j == 'Y':
            start_row = i
            start_col = data.index('Y')
command = input()
matrix[start_row][start_col] = 'x'
while command != 'End':
    way, steps = command.split('-')
    steps = int(steps)
    start_row, start_col, matrix = next_move(steps, start_row, start_col, matrix, way, cols, rows)
    if matrix[start_row][start_col] != '.' and matrix[start_row][start_col] != 'x':
        key = my_dict[matrix[start_row][start_col]]
        collected_items[key] += 1
        unique_items.add(matrix[start_row][start_col])

    command = input()
matrix[start_row][start_col] = 'Y'
if len(unique_items) == 3:
    print("Merry Christmas!")
print(f"You've collected:")
for k, v in collected_items.items():
    print(f'- {v} {k}')
for i in matrix:
    print(*i)

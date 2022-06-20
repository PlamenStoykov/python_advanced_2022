matrix = []
white_row = None
white_col = None
black_row = None
black_col = None
winner = None
queen = False
captured = False
my_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
second_dict = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
for i in range(8):
    data = input().split()
    matrix.append(data)
    for j in data:
        if j == 'w':
            white_row = i
            white_col = data.index('w')
        elif j == 'b':
            black_row = i
            black_col = data.index('b')


def check_capture(r, c, color, m):
    if color == 'w':
        possible_white = [(r - 1, c - 1), (r - 1, c + 1)]
        for row, col in possible_white:
            if 0 <= row < 8 and 0 <= col < 8:
                if m[row][col] == 'b':
                    return row, col
    else:
        possible_black = [(r + 1, c - 1), (r + 1, c + 1)]
        for row, col in possible_black:
            if 0 <= row < 8 and 0 <= col < 8:
                if m[row][col] == 'w':
                    return row, col
    return False


def next_move(r, c, color, m):
    if color == 'w':
        t = check_capture(r, c, 'w', m)
        if not t:
            r = r-1
            return r, c
        else:

            return t[0], t[1]
    else:
        t = check_capture(r, c, 'b', m)
        if not t:
            return r + 1, c
        else:
            return t[0], t[1]


while True:
    matrix[white_row][white_col] = '-'
    white_row, white_col = next_move(white_row, white_col, 'w', matrix)
    matrix[white_row][white_col] = 'w'
    if white_row == -1:
        winner = 'White'
        queen = True
        white_row += 1
        coords = f'{my_dict[white_col]}{second_dict[white_row]}'
        break
    if matrix[black_row][black_col] == 'w':
        captured = True

        winner = "White"
        coords = f'{my_dict[white_col]}{second_dict[white_row]}'
        break
    matrix[black_row][black_col] = '-'
    black_row, black_col = next_move(black_row, black_col, 'b', matrix)
    matrix[black_row][black_col] = 'b'
    if black_row == 7:
        winner = 'Black'
        queen = True
        coords = f'{my_dict[black_col]}{second_dict[black_row]}'
        break
    if matrix[white_row][white_col] == 'b':

        captured = True
        winner = "Black"
        coords = f'{my_dict[black_col]}{second_dict[black_row]}'
        break
if captured:
    print(f"Game over! {winner} win, capture on {coords}.")
if queen:
    print(f"Game over! {winner} pawn is promoted to a queen at {coords}.")

def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False
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
presents = int(input())
n = int(input())
matrix = []
nice_kids = 0
santa_col = None
santa_row = None
for i in range(n):
    data = [g for g in input().split()]
    matrix.append(data)
    for f in data:
        if f == 'S':
            santa_col = data.index(f)
            santa_row = i
        if f == 'V':
            nice_kids += 1
received_gifts_nice_kids = 0
matrix[santa_row][santa_col] = '-'
command = input()
while command != "Christmas morning":
    matrix[santa_row][santa_col] = '-'
    condition = False
    santa_row, santa_col = position_functions[command](santa_row, santa_col)
    if matrix[santa_row][santa_col] == 'V' and presents:
        presents -= 1
        received_gifts_nice_kids += 1
    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col - 1] == 'V' and presents:  # left
            matrix[santa_row][santa_col - 1] = '-'
            received_gifts_nice_kids += 1
            presents -= 1
        elif matrix[santa_row][santa_col - 1] == 'X' and presents:
            matrix[santa_row][santa_col - 1] = '-'
            presents -= 1
        if matrix[santa_row][santa_col + 1] == 'V' and presents:  # right
            matrix[santa_row][santa_col + 1] = '-'
            received_gifts_nice_kids += 1
            presents -= 1
        elif matrix[santa_row][santa_col + 1] == 'X' and presents:
            matrix[santa_row][santa_col + 1] = '-'
            presents -= 1
        if matrix[santa_row - 1][santa_col] == 'V' and presents:  # up
            matrix[santa_row - 1][santa_col] = '-'
            received_gifts_nice_kids += 1
            presents -= 1
        elif matrix[santa_row - 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if matrix[santa_row + 1][santa_col] == 'V' and presents:  # down
            matrix[santa_row + 1][santa_col] = '-'
            received_gifts_nice_kids += 1
            presents -= 1
        elif matrix[santa_row + 1][santa_col] == 'X' and presents:
            matrix[santa_row + 1][santa_col] = '-'
            presents -= 1
    matrix[santa_row][santa_col] = 'S'
    if presents <= 0 or received_gifts_nice_kids == nice_kids:
        break
    command = input()
if presents <= 0 and received_gifts_nice_kids < nice_kids:
    print("Santa ran out of presents!")
for i in matrix:
    print(*i)
if nice_kids == received_gifts_nice_kids:
    print(f"Good job, Santa! {received_gifts_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - received_gifts_nice_kids} nice kid/s.")

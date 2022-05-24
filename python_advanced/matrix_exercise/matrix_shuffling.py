rows, cols = [int(i) for i in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
command = input()
while command != 'END':
    tokens = command.split()
    order = tokens[0]
    if order == 'swap':
        if len(tokens) == 5:
            row_one = int(tokens[1])
            col_one = int(tokens[2])
            row_two = int(tokens[3])
            col_two = int(tokens[4])
            if min(row_two, row_one) >= 0 and max(row_two, row_one) < rows and min(col_two, col_one) >= 0 and max(
                    col_two, col_one) < cols:
                matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
                for c in matrix:
                    print(*c)
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()

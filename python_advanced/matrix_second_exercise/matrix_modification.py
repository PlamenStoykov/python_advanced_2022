n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]
command = input()
while command != 'END':
    tokens = command.split()
    row = int(tokens[1])
    col = int(tokens[2])
    value = int(tokens[3])

    if col in range(0, len(matrix)) and row in range(0, len(matrix)):

        if tokens[0] == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input()
for i in matrix:
    print(*i)
first, second = input().split(', ')
matrix = []
for i in range(6):
    data = input().split()
    matrix.append(data)
current_player = first
waiting_player = second
resting_players = []
while True:
    tokens = input().strip('()')
    current_row, current_col = list(map(int, tokens.split(', ')))
    if current_player in resting_players:
        resting_players.remove(current_player)
        current_player, waiting_player = waiting_player, current_player
        continue

    if matrix[current_row][current_col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    if matrix[current_row][current_col] == 'T':
        print(f"{current_player} is out of the game! The winner is {waiting_player}.")
        break

    if matrix[current_row][current_col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        resting_players.append(current_player)
    current_player, waiting_player = waiting_player, current_player

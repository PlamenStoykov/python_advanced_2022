def sequence_generator(num):
    sequence = [0, 1]
    num_one = 0
    num_two = 1
    while len(sequence) != num:
        num_one = num_one + num_two
        num_two = num_one + num_two
        sequence.append(num_one)
        sequence.append(num_two)
    return sequence


def locater(searching_num, a):
    index = False
    counter = 0
    for i in a:
        if i == searching_num:
            index = counter
            break
        counter += 1
    if index:

        print(f'The number - {searching_num} is at index {index}')
    else:
        print(f'The number {searching_num} is not in the sequence')


command = input()
while command != 'Stop':
    tokens = command.split()
    order = tokens[0]
    if 'Create' == order:
        using = sequence_generator(int(tokens[2]))
        print(*using)
    else:
        num = int(tokens[1])
        locater(num, using)
    command = input()

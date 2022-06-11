import os
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')
    order = tokens[0]
    file_name = tokens[1]
    if order == 'Create':
        with open(f'{file_name}', 'w') as file:
            pass
    elif order == 'Add':
        if os.path.exists(f'{file_name}'):
            with open(f'{file_name}', 'a') as file:
                file.write(tokens[2])
            continue
        with open(f'{file_name}', 'w') as file:
            file.write(tokens[2])
    elif order == 'Replace':
        if os.path.exists(f'{file_name}'):
            with open(f'{file_name}', 'r+') as file:
                old_string = tokens[2]
                new_string = tokens[3]
                content = file.read()
                while old_string in content:
                    content = content.replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print('An error has occurred')
    elif order == 'Delete':
        if os.path.exists(f'{file_name}'):
            os.remove(f'{file_name}')
            continue
        print('An error has occurred')


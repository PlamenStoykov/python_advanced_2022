import re

my_dict = {}
with open('words.txt') as file:
    searched_words = file.read().split()
with open('input.txt') as file:
    text = file.read()
    for i in searched_words:
        pattern = fr"\b{i}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))
        my_dict[i] = count
    s = sorted(my_dict.items(), key=lambda x: -x[1])
with open('new_file', 'w') as a:
    a.write(f'{s}')

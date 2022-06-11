import re
with open('second_text.txt', 'r') as file, open('output.txt', 'w') as output_file:
    x = []
    for row, line in enumerate(file):
        stripped_line = line.strip()
        for c in stripped_line:
            letters = re.findall(r'[a-zA-z]', stripped_line)
            marks = re.findall(r'[,.\-\'":?!]',stripped_line)

        x.append(f'Line {row}: {stripped_line} ({len(letters)}) ({len(marks)})')
    output_file.write('\n'.join(x))

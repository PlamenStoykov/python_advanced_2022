marks = {"-", ",", ".", "!", "?"}
with open('text.txt', 'r') as text_file:
    whole = []
    for row, line in enumerate(text_file):
        if row % 2 == 0:
            for c in marks:
                while c in line:
                    line = line.replace(c, '@')
            whole.append(' '.join(reversed(line.strip().split())))

    print('\n'.join(whole))

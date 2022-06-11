from os import listdir, path

extensions_dict = {}


def traverse_dir(current_path):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element))
        else:
            ext = element.split('.')[-1]
            if ext not in extensions_dict:
                extensions_dict[ext] = []
            extensions_dict[ext].append(element)


traverse_dir('.')
for k, v in sorted(extensions_dict.items()):
    print(f'.{k}')
    for j in sorted(v):
        print(f'- - - {j}')


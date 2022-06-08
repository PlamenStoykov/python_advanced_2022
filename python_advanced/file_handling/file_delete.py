import os
try:
    file = input()
    os.remove(file)
except FileNotFoundError:
    print('File already deleted')

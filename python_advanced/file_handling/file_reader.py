import os
with open('numbers.txt', 'r') as file:
    a = 0
    for line in file:
        a += int(line)
print(a)
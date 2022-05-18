line = input()
collection = {}
for letter in line:
    if letter not in collection:
        collection[letter] = 0
    collection[letter] += 1
sorted_dict = sorted(collection.items(), key= lambda kvp: kvp[0])

for i in sorted_dict:
    print(f'{i[0]}: {i[1]} time/s')

from collections import deque

main = {"red", "yellow", "blue"}
secondary = {"orange", "purple", "green"}
main_dict = {"orange": ["red", "yellow"], "purple": ["blue", "red"], "green": ["yellow", "blue"]}
subs = deque(input().split())
found = []
while subs:
    first = subs.popleft()
    last = subs.pop() if subs else ''
    result = first + last
    if result in main or result in secondary:
        found.append(result)
        continue
    result = last + first
    if result in main or result in secondary:
        found.append(result)
        continue
    first = first[:-1]
    last = last[:-1]
    if first:
        subs.insert(len(subs) // 2, first)
    if last:
        subs.insert(len(subs) // 2, last)
for color in found:
    if color not in main:
        for i in main_dict[color]:
            if i not in found:
                found.remove(color)
print(found)
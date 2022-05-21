from collections import deque

materials = deque(map(int, input().split()))
magic_values = deque(map(int, input().split()))

dolls = 0
trains = 0
bears = 0
bicycles = 0
one = False
two = False
toys = {150: [0, 'Doll'], 250: [0, 'Wooden train'], 300: [0, 'Teddy bear'], 400: [0, 'Bicycle']}
while magic_values and materials:
    condition = False
    box_material = materials.pop()
    current_magic = magic_values.popleft()
    res = box_material * current_magic
    if res < 0:
        materials.append(box_material + current_magic)
    elif res == 0:
        if box_material == 0 and current_magic == 0:
            continue
        if box_material == 0:
            magic_values.appendleft(current_magic)
        if current_magic == 0:
            materials.append(box_material)

    elif res > 0:
        for i in toys:
            if res == i:
                toys[i][0] += 1
                condition = True
                break
        if not condition:
            materials.append(box_material + 15)
if toys[300][0] > 0 and toys[400][0] > 0 or toys[150][0] > 0 and toys[250][0] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(i) for i in reversed(materials)])}")
if magic_values:
    print(f"Magic left: {', '.join([str(i) for i in magic_values])}")
sorted_dict = sorted(toys.items(), key=lambda kvpt: kvpt[1])
r = dict(sorted_dict)
for k, v in r.items():
    if v[0] > 0:
        print(f"{v[1]}: {v[0]}")

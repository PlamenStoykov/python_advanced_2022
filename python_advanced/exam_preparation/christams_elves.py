from collections import deque

elf_energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))
made_toys = 0
used_energy = 0
counter = 1
while True:
    if not elf_energy:
        break
    if not materials:
        break
    current_elf_energy = elf_energy.popleft()
    current_material = materials.pop()
    if current_elf_energy < 5:
        materials.append(current_material)
        continue
    if counter % 3 == 0 and current_elf_energy >= current_material * 2:
        made_toys += 2
        current_elf_energy -= 2 * current_material
        current_elf_energy += 1
        used_energy += 2 * current_material
        elf_energy.append(current_elf_energy)

    elif counter % 5 == 0 and current_elf_energy >= current_material:
        current_elf_energy -= current_material
        used_energy += current_material
        elf_energy.append(current_elf_energy)

    elif current_elf_energy >= current_material and counter % 3 != 0 and counter % 5 != 0:
        current_elf_energy -= current_material
        current_elf_energy += 1
        made_toys += 1
        used_energy += current_material
        elf_energy.append(current_elf_energy)

    else:
        materials.append(current_material)
        elf_energy.append(2 * current_elf_energy)
    counter += 1

print(f"Toys: {made_toys}")
print(f"Energy: {used_energy}")
if elf_energy:
    print(f"Elves left: {', '.join([str(i) for i in elf_energy])}")
if materials:
    print(f"Boxes left: {', '.join([str(i) for i in materials])}")

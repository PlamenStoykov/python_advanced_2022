unique = set()
other = list()
iterations = 0
numbers = list(map(int, input().split()))
target = int(input())
counter = 0
for i in numbers:

    for k in range(counter+1, len(numbers)):
        if i + numbers[k] == target:
            print(f"{i} + {numbers[k]} = {target}")
            var = f'({i}, {numbers[k]})'
            unique.add(var)
        iterations += 1

    counter += 1
print(f"Iterations done: {iterations}")
for i in unique:
    print(i)

from collections import deque

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
symbols = deque(input().split())

honey = 0
while bees and nectar:
    bee = bees.popleft()
    current_nectar = nectar.pop()
    if bee <= current_nectar:
        symbol = symbols.popleft()
        if symbol == '+':
            honey += abs(bee + current_nectar)
        elif symbol == '-':
            honey += abs(bee - current_nectar)
        elif symbol == '*':
            honey += abs(bee * current_nectar)
        else:
            if current_nectar != 0:
                honey += abs(bee / current_nectar)
    else:
        bees.appendleft(bee)
print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(i) for i in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")

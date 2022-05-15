from collections import deque

stations = deque()
n = int(input())
winning = None
for _ in range(n):
    using = list(map(int, input().split()))
    stations.append(using)
for attempt in range(n):
    tank = 0
    failed = False
    for petrol, distance in stations:
        tank += petrol
        if tank < distance:
            failed = True

            break
        else:
            tank -= distance
    if not failed:
        winning = attempt
        break
    else:
        stations.rotate(-1)

print(winning)

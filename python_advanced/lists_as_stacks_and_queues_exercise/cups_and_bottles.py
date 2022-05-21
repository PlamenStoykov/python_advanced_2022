from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted = 0
while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle >= cup:
        wasted += bottle - cup
    else:
        cups.appendleft(cup - bottle)
if cups:
    print(f"Cups: {' '.join([str(i)for i in cups])}")
else:
    print(f"Bottles: {' '.join([str(i)for i in bottles])}")
print(f"Wasted litters of water: {wasted}")

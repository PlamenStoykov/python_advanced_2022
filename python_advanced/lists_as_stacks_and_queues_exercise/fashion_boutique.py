from collections import deque

sequence = deque(map(int, input().split()))
size = int(input())
used = 1
current_size = size
while sequence:
    current = sequence.pop()
    if current_size - current >= 0:
        current_size -= current
    else:
        used += 1
        current_size = size - current
print(used)

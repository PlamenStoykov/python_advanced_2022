from collections import deque

quantity = int(input())
sequence = deque(map(int, input().split()))
print(max(sequence))
while sequence:
    current = sequence.popleft()
    if quantity - current >= 0:
        quantity -= current
    else:
        sequence.appendleft(current)
        break
new = [str(i)for i in sequence]

if sequence:
    print(f"Orders left: {' '.join(new)}")
else:
    print('Orders complete')

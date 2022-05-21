from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence_value = int(input())
cost = 0
current_size = size_gun_barrel
while locks and bullets:
    bullet = bullets.pop()
    lock = locks.popleft()
    cost += price_bullet
    current_size -= 1
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)
    if current_size == 0 and bullets:
        print('Reloading!')
        current_size = size_gun_barrel
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - cost}")
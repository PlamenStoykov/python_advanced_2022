from collections import deque

bowls_of_ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))

while customers and bowls_of_ramen:
    current_customer = customers.popleft()
    current_bowl = bowls_of_ramen.pop()
    if current_bowl > current_customer:
        bowls_of_ramen.append(current_bowl - current_customer)
    elif current_customer > current_bowl:
        customers.appendleft(current_customer - current_bowl)
if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(i)for i in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join([str(i)for i in customers])}")

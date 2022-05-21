from collections import deque

condition = False
chocolates = deque(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
shakes = 0

while chocolates and cups_of_milk and shakes < 5:
    chocolate = chocolates.pop()
    cup = cups_of_milk.popleft()
    if chocolate > 0 and cup > 0:
        if chocolate == cup:
            shakes += 1
        else:
            chocolates.append(chocolate - 5)
            cups_of_milk.append(cup)
    if chocolate <= 0:
        if cup > 0:
            cups_of_milk.appendleft(cup)
    if cup <= 0:
        if chocolate > 0:
            chocolates.append(chocolate)

if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(i) for i in chocolates])}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}")
else:
    print("Milk: empty")

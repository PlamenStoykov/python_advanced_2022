from collections import deque
quantity = int(input())
command = input()
queue = deque()
while not command == 'Start':
    queue.append(command)
    command = input()
command = input()
while not command =="End":
    if command.isdigit():
        liters = int(command)
        if quantity >= liters:
            print(f"{queue.popleft()} got water")
            quantity -= liters
        else:
            print(f"{queue.popleft()} must wait" )
    else:
        using, liters = command.split()
        liters = int(liters)
        quantity += liters

    command = input()
print(f"{quantity} liters left")
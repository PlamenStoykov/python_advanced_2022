from collections import deque

green_light_duration = int(input())
free_window = int(input())
command = input()
cars_passed = 0
light = True
current_time = free_window + green_light_duration
time = free_window + green_light_duration
condition = False
letter = None
while command != 'END':
    if command == 'green':
        current_time = free_window + green_light_duration
        time = free_window + green_light_duration
        command = input()
        light = True
        continue
    if light:
        if len(command) <= time:
            time -= len(command)
            cars_passed += 1

        car = deque(command)
        while car:
            letter = car.popleft()
            current_time -= 1
            if current_time <= free_window:
                light = False
            if current_time < 0:
                condition = True
                break
    if condition:
        print("A crash happened!")
        print(f"{command} was hit at {letter}.")
        break

    command = input()
if not condition:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
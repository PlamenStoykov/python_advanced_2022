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
cars = deque()
current_green = green_light_duration
while command != 'END':
    if command == 'green':
        current_time = free_window + green_light_duration
        time = free_window + green_light_duration
        command = input()
        current_green = green_light_duration
        light = True
        continue
    else:
        cars.append(command)
        current_car = cars.popleft()
        if light:
            if len(current_car) > current_time:
                letter = current_car[free_window + current_green]
                condition = True
                break
            else:
                current_time -= len(current_car)
                cars_passed += 1
                current_green -= len(current_car)
                if current_time <= free_window:
                    light = False

    command = input()
if not condition:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{command} was hit at {letter}.")

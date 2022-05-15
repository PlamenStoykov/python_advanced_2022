from collections import deque


def seconds_to_time(num):
    num %= 24 * 60 * 60
    hours = num // (60 * 60)
    num %= (60 * 60)
    minutes = num // 60
    num %= 60
    c = f"{hours:02d}:{minutes:02d}:{num:02d}"
    return c


def str_to_seconds(string):
    h, m, s = string.split(':')
    return int(h) * 60 * 60 + int(m) * 60 + int(s)


items = deque()
robots_line = input().split(';')
time = input()
robots_process_time = {}
busy_until_robot = {}
for i in robots_line:
    name, seconds = i.split('-')
    robots_process_time[name] = int(seconds)
    busy_until_robot[name] = 0
item = input()
while item != 'End':
    items.append(item)
    item = input()
time = str_to_seconds(time)
while items:
    time += 1
    current_item = items.popleft()
    for name, busy_until in busy_until_robot.items():
        if time >= busy_until:
            busy_until_robot[name] = time + robots_process_time[name]
            print(f"{name} - {current_item} [{seconds_to_time(time)}]")
            break
    else:
        items.append(current_item)

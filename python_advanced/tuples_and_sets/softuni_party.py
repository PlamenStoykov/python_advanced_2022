n = int(input())
command = input()
guests = set()
condition = True
while command != 'END':
    if len(guests) < n and condition:
        guests.add(command)
    else:
        condition = False
        guests.remove(command)
    command = input()
sorted_guests = sorted(guests)
print(len(guests))
for i in sorted_guests:
    print(i)

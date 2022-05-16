parking_lot = {}
n = int(input())
t= set()

for i in range(n):
    way, number = input().split(', ')
    if way == "IN":
        if number not in t:
            t.add(number)
    elif way == "OUT":
        if number in t:
            t.remove(number)
if t:
    for i in t:
        print(i)
else:
    print("Parking Lot is Empty")
from collections import deque

numbers = deque()
expression = input().split()
for i in expression:

    if i in '+-*/':
        while len(numbers) > 1:
            one = numbers.popleft()
            two = numbers.popleft()
            if i == '+':
                res = one + two
            elif i == '-':
                res = one - two
            elif i == '*':
                res = one * two
            else:
                res = one // two
            numbers.appendleft(res)
    else:
        numbers.append(int(i))
print(numbers[0])

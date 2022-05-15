from collections import deque

stack = deque()
expression = input()
balanced = True
for char in expression:
    if char in '({[':
        stack.append(char)
    else:
        if stack:
            last_open = stack.pop()
            using = f'{last_open}{char}'
            if using not in '(){}[]':
                balanced = False
        else:
            balanced = False
            break
if balanced and not stack:
    print('YES')
else:
    print('NO')

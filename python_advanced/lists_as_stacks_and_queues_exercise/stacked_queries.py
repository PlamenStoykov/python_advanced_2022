n = int(input())
stack = list()
for _ in range(n):
    query = input()
    if query.startswith('1'):
        first, second = query.split()
        second = int(second)
        stack.append(second)
    elif stack:
        if query.startswith('2'):
            if stack:
                stack.pop()
        elif query.startswith('3'):
            print(max(stack))
        elif query.startswith('4'):
            print(min(stack))
new = []
while stack:
    new.append(str(stack.pop()))

print(', '.join(new))


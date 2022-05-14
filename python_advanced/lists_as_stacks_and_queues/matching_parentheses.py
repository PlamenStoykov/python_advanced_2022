expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':

        open_bracket = stack.pop()
        print(expression[open_bracket:i+1])
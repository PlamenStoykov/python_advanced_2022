from math import pow


def operation(num_one, sign, num_two):
    if sign == '+':
        print(num_one + num_two)
    elif sign == '-':
        print(num_one - num_two)
    elif sign == '*':
        print(num_one * num_two)
    elif sign == '/':
        try:
            print(num_one / num_two)
        except ZeroDivisionError:
            num_two = float(input('Cannot divide by zero. Give me other divider: '))
    elif sign == '^':
        print(pow(num_one, num_two))


input_line = input().split()
operation(float(input_line[0]), input_line[1], float(input_line[2]))


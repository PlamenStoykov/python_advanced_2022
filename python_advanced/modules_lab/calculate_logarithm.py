from math import log

n = int(input())
second_line = input()
result = log(n) if second_line == 'natural' else log(n, int(second_line))
print(f"{result:.2f}")

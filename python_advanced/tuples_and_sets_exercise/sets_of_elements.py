n, m = list(map(int, input().split()))
f = set()
s = set()
for _ in range(n):
    num = input()
    f.add(num)
for _ in range(m):
    num = input()
    s.add(num)
g = f.intersection(s)


for i in g:
    print(i)
n = int(input())
el = set()
for i in range(n):
    elements = input().split()
    el = el.union(elements)
for e in el:
    print(e)

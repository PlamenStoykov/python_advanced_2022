n = int(input())
even = set()
odd = set()
even_sum = 0
odd_sum = 0
for i in range(1, n +1):
    name = input()
    using = sum(ord(ch) for ch in name) // i
    if using % 2 == 0:
        even.add(using)
        even_sum += using
    else:
        odd.add(using)
        odd_sum += using
if even_sum == odd_sum:
    res = even.union(odd)
elif even_sum > odd_sum:
    res = even.symmetric_difference(odd)
else:
    res = odd - even
print(*res, sep=', ')
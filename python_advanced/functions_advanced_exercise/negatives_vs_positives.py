one = [int(x) for x in input().split()]
a = ([int(x) for x in one if x > 0])
b = (list(filter(lambda x: x if x < 0 else False, one)))
print(sum(a))
print(sum(b))
if sum(a) > abs(sum(b)):
    print("The positives are stronger than the negatives")

else:
    print("The negatives are stronger than the positives")

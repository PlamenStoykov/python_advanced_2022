nums = tuple(map(float, input().split()))

dict = {}
for i in nums:
    dict[i] = nums.count(i)
for i in dict:
    print(f"{i:.1f} - {dict[i]} times")

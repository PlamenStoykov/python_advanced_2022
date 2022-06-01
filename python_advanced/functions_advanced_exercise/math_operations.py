from collections import deque


def math_operations(*args, **kwargs):
    nums = deque(args)
    while nums:
        kwargs['a'] += nums.popleft()
        if not nums:
            break
        kwargs['s'] -= nums.popleft()
        if not nums:
            break
        current = nums.popleft()
        if current != 0:
            kwargs['d'] /= current
        if not nums:
            break
        kwargs['m'] *= nums.popleft()
    sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))
    res = ''
    for i in sorted_dict:
        res += f"{i}: {sorted_dict[i]:.1f}" + '\n'
    return res


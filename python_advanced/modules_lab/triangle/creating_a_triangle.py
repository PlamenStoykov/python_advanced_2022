def triangle_maker(num):
    for i in range(1, num + 1):
        print_line(i)
    for i in range(num - 1, -1, -1):
        print_line(i)


def print_line(num):
    for i in range(1, num + 1):
        print(i, end=" ")
    print()


n = int(input())
triangle_maker(n)

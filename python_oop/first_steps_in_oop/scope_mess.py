x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"
    def change_outer():
        nonlocal x
        x = "nonlocal"

    print("outer:", x)
    inner()
    change_outer()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

def rectangle(length, width):
    if type(length) == int and type(width) == int:
        def area(l, w):
            return f"Rectangle area: {l * w}"

        def perimeter(l, w):
            return f"Rectangle perimeter: {2 * l + 2 * w}"
        return area(length,width) + '\n' + perimeter(length, width)
    return "Enter valid values!"

def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    using = args[3:]
    size = height * length * width
    res = []
    for i in using:
        if i == 'Finish':
            break
        else:
            res.append(i)
    if sum(res) < size:
        return f"There is free space in the box. You could put {size - sum(res)} more cubes."
    else:
        return f"No more free space! You have {sum(res) - size} more cubes."


def fibonacci():
    num_one = 0
    num_two = 1
    while True:
        yield num_one
        num_one = num_one + num_two
        yield num_two
        num_two = num_two + num_one


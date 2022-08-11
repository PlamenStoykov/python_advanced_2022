class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > -1:
            current = self.i
            self.i -= 1
            return current
        raise StopIteration


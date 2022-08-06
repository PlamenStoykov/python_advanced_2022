class custom_range:
    def __init__(self, start, end):

        self.end = end
        self.i = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= self.end:
            current = self.i
            self.i += 1
            return current
        raise StopIteration


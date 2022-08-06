class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.i = len(obj) -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            current = self.i
            self.i -= 1
            return self.obj[current]
        raise StopIteration



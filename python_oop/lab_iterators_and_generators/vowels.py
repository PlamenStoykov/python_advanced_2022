class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= len(self.string) - 1:
            current = self.i
            self.i += 1
            if self.string[current] in 'AIOEUYaioeuy':
                return self.string[current]
        else:
            raise StopIteration


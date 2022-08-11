class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            idx = self.counter
            if idx >= len(self.sequence):
                times = idx // len(self.sequence)
                idx -= len(self.sequence) * times
            self.counter += 1
            return self.sequence[idx]
        raise StopIteration


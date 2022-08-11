class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.dict_obj):
            values = list(self.dict_obj.values())
            keys = list(self.dict_obj.keys())
            current = self.counter
            self.counter += 1
            return (keys[current], values[current])
        raise StopIteration



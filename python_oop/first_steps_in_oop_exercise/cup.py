class Cup:

    def __init__(self, size, quantity):
        self.quantity = quantity
        self.size = size

    def fill(self, quantity):
        if self.size - self.quantity > quantity:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity


class Hero:
    def __init__(self, name, health):
        self.health = health
        self.name = name

    def defend(self, damage):
        self.health -= damage
        if self.health < 1:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount



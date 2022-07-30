from project.animals.animal import Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    @property
    def weight_incremental(self):
        return 0.10

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Fruit']


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    @property
    def weight_incremental(self):
        return 0.40

    @property
    def allowed_foods(self):
        return ['Meat']


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    @property
    def weight_incremental(self):
        return 0.30

    @property
    def allowed_foods(self):
        return ['Meat', "Vegetable"]


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    @property
    def weight_incremental(self):
        return 1

    @property
    def allowed_foods(self):
        return ['Meat']



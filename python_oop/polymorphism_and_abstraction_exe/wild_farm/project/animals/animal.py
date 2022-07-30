from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight):
        self.weight = weight
        self.food_eaten = 0
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def weight_incremental(self):
        pass

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    def feed(self, food):
        if food.__class__.__name__ not in self.allowed_foods:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_incremental


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

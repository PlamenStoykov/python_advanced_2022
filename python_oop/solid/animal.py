from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return 'Meow'


class Dog(Animal):

    def make_sound(self):
        return 'Woof'


class Chicken(Animal):

    def make_sound(self):
        return 'Cluck'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals_group = [Dog(), Cat(), Chicken()]
animal_sound(animals_group)
big_g = Dog()
print(big_g.make_sound())
## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни

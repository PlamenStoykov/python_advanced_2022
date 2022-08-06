import copy
from abc import ABC, abstractmethod


class Slave:
    def __init__(self, position):
        self.position = position

    def walk_north(self):
        self.position[1] += 0

    def walk_east(self):
        self.position[0] += 0


class FreePerson(ABC):
    @abstractmethod
    def walk_north(self, dist):
        pass

    @abstractmethod
    def walk_east(self, dist):
        pass


class Person(FreePerson):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Slave):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

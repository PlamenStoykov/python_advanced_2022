from project.animals.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: float):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        searching = None
        for worker in self.workers:
            if worker.name == worker_name:
                searching = worker
        if searching is not None:
            self.workers.remove(searching)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        whole_sum = 0
        for worker in self.workers:
            whole_sum += worker.salary
        if self.__budget >= whole_sum:
            self.__budget -= whole_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        whole_sum = 0
        for animal in self.animals:
            whole_sum += animal.money_for_care
        if whole_sum <= self.__budget:
            self.__budget -= whole_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(lions)} Lions:\n"
        result += '\n'.join(lions)
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += '\n'.join(tigers)
        cheetahs = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheetahs)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        result += f"----- {len(keepers)} Keepers:\n"
        result += '\n'.join(keepers)
        caretakers = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += '\n'.join(caretakers)
        vets = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += f"\n----- {len(vets)} Vets:\n"
        result += '\n'.join(vets)
        return result


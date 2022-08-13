class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase,main


class WorkerTests(TestCase):
    def test_if_worker_is_initialised_correctly(self):
        worker = Worker('Kiko', 100, 10)
        self.assertEqual('Kiko', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)

    def test_if_energy_chenges_after_rest_method(self):
        worker = Worker('Kiko', 100, 10)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_if_raises_after_working_without_energy(self):
        with self.assertRaises(Exception) as ex:
            worker = Worker('Kiko', 100, 0)
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_if_money_increases_after_work_method(self):
        worker = Worker('Kiko', 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)
    def  test_if_energy_decreases_after_work_method(self):
        worker = Worker('Kiko', 100, 10)
        worker.work()
        self.assertEqual(9, worker.energy)
    def testing_the_get_info_methods_return(self):
        worker = Worker('Kiko',100,10)
        self.assertEqual(f'{worker.name} has saved {worker.money} money.',worker.get_info())

if __name__ == '__main__':
    main()
from abc import ABC, abstractmethod
import time


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self,worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")

    def eat(self):
        print("I don't need to eat....")




class WorkManager(Manager):

    def manage(self):
        assert isinstance(self.worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker.work()


work_manager = WorkManager()


class BreakManager(Manager):

    def lunch_break(self):
        assert isinstance(self.worker, Eatable), "`worker` must be of type {}".format(Eatable)

        self.worker.eat()


break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass




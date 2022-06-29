class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.salary = salary
        self.last_name = last_name
        self.first_name = first_name
        self.id = id

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

    def get_annual_salary(self):
        return self.salary * 12


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def search_customer(self, customer_id):
        searched_customer = None
        for customer in self.customers:
            if customer.id == customer_id:
                searched_customer = customer
        return searched_customer

    def search_dvd(self, dvd_id):
        searched_dvd = None
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                searched_dvd = dvd
        return searched_dvd

    def rent_dvd(self, customer_id, dvd_id):
        searched_dvd = self.search_dvd(dvd_id)
        searched_customer = self.search_customer(customer_id)

        if searched_dvd in searched_customer.rented_dvds:
            return f"{searched_customer.name} has already rented {searched_dvd.name}"
        if searched_dvd.is_rented:
            return "DVD is already rented"
        if searched_customer.age < searched_dvd.age_restriction:
            return f"{searched_customer.name} should be at least {searched_dvd.age_restriction} to rent this movie"
        searched_customer.rented_dvds.append(searched_dvd)
        searched_dvd.is_rented = True
        return f"{searched_customer.name} has successfully rented {searched_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        searched_dvd = self.search_dvd(dvd_id)
        searched_customer = self.search_customer(customer_id)
        if searched_dvd in searched_customer.rented_dvds:
            searched_customer.rented_dvds.remove(searched_dvd)
            searched_dvd.is_rented = False
            return f"{searched_customer.name} has successfully returned {searched_dvd.name}"
        return f"{searched_customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for client in self.customers:
            result += f'{repr(client)}\n'
        for movie in self.dvds:
            result += f'{repr(movie)}\n'
        return result


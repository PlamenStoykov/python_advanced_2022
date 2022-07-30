from project.animals.animal import Bird


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def weight_incremental(self):
        return 0.25

    @property
    def allowed_foods(self):
        return ['Meat']


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    @property
    def weight_incremental(self):
        return 0.35

    @property
    def allowed_foods(self):
        return ['Meat', 'Vegetable', 'Fruit','Seed']

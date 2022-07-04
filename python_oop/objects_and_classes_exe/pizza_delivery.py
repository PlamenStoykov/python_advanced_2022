class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.ingredients = ingredients
        self.price = price
        self.name = name
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity *quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity *quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{i}: {self.ingredients[i]}' for i in self.ingredients])} and the price will be {self.price}lv."


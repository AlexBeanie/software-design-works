from meal import Meal

class Order(Meal):
    def __init__(self, id):
        self.meals: list[Meal] = []
        self.id = id
        
    def __str__(self):
        order_str = f"Order #{self.id}\n"
        for meal in self.meals:
            order_str += str(meal) + "\n"
        return order_str
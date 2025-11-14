from enum import Enum

class MealType(Enum):
    FOOD = 0
    DRINK = 1

class Meal():
    def __init__(self, name, type: MealType):
        self.name = name
        self.ingredients: list[Meal] = []
        self.type = type
        
    def __str__(self):
        return f"{self.name} con {', '.join(ing for ing in self.ingredients)}"
        
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self.ingredients
      
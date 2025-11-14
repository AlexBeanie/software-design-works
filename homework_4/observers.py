from meal import Meal

class IMealObserver:
    def update(self, meal: Meal):
        pass
    
class FoodObserver(IMealObserver):
    def update(self, meal: Meal):
        print(f"[Chef] Cooking food: {str(meal)}")

class DrinkObserver(IMealObserver):
    def update(self, meal: Meal):
        print(f"[Barista] Preparing drink: {str(meal)}")

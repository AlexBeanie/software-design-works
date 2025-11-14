from baseChainHandler import BaseChainHandler
from order import Order
from meal import Meal, MealType
from observers import IMealObserver, FoodObserver, DrinkObserver
import time

class PrepHandler(BaseChainHandler):  
    def __init__(self):
        super().__init__()
        self._food_observer = FoodObserver()
        self._drink_observer = DrinkObserver()
         
    def _notify(self, meal: Meal):
        if meal.type == MealType.FOOD:
            self._food_observer.update(meal)
        elif meal.type == MealType.DRINK:
            self._drink_observer.update(meal)
        time.sleep(0.2)

    def _try(self, order: Order):
        print(f"[Kitchen]: Preparing order #{order.id}")
        for meal in order.meals:
            self._notify(meal)
        

class NotifHandler(BaseChainHandler):    
    def _try(self, order: Order):
        print(f"Order {order.id} is Ready!")